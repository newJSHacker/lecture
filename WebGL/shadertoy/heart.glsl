// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// 2D heart SDF with a beat and a soft glow. Beginner favorite.

float heart(vec2 p) {
  p.x = abs(p.x);
  if (p.x + p.y > 1.0) return length(p - vec2(0.25, 0.75)) - 0.35355339;
  return sqrt(min(dot(p, p), dot(p - vec2(0.0, 1.0), p - vec2(0.0, 1.0)))) * sign(p.x - p.y);
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  float beat = 1.0 + 0.08 * sin(iTime * 6.0) + 0.04 * sin(iTime * 12.0);
  p.y += 0.12;
  p /= 0.55 * beat;
  float d = heart(p);
  float fill = 1.0 - smoothstep(0.0, 0.01, d);
  float glow = exp(-3.5 * max(d, 0.0));
  vec3 bg = mix(vec3(0.08, 0.04, 0.08), vec3(0.18, 0.06, 0.1), 0.5 + 0.5 * p.y);
  vec3 red = mix(vec3(0.55, 0.05, 0.12), vec3(0.95, 0.2, 0.28), fill * (0.6 + 0.4 * (0.5 - p.y)));
  vec3 col = mix(bg, red, fill);
  col += vec3(0.8, 0.15, 0.25) * glow * 0.45 * (1.0 - fill);
  float spec = smoothstep(0.12, 0.0, length(p - vec2(-0.18, 0.22))) * fill;
  col += spec * 0.35;
  fragColor = vec4(col, 1.0);
}
