// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Aurora: vertical curtains, slow phase drift.

float hash12(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * 0.1031);
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.x + p3.y) * p3.z);
}
float noise(vec2 p) {
  vec2 i = floor(p), f = fract(p);
  vec2 u = f * f * (3.0 - 2.0 * f);
  return mix(mix(hash12(i), hash12(i + vec2(1,0)), u.x),
             mix(hash12(i + vec2(0,1)), hash12(i + vec2(1,1)), u.x), u.y);
}
float fbm(vec2 p) {
  float v = 0.0, a = 0.5;
  for (int i = 0; i < 5; i++) { v += a * noise(p); p *= 2.03; a *= 0.5; }
  return v;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 col = mix(vec3(0.01, 0.02, 0.06), vec3(0.0, 0.0, 0.02), p.y * 0.5 + 0.5);
  float y = p.y + 0.15;
  float curtain = fbm(vec2(p.x * 1.4 + iTime * 0.08, 0.3));
  float band = exp(-3.5 * abs(y - 0.15 - 0.25 * curtain));
  float detail = fbm(vec2(p.x * 3.0 - iTime * 0.12, y * 2.0));
  vec3 g = vec3(0.1, 0.85, 0.45);
  vec3 ppl = vec3(0.55, 0.15, 0.75);
  vec3 aur = mix(g, ppl, clamp(p.x * 0.5 + 0.5 + 0.2 * detail, 0.0, 1.0));
  col += aur * band * (0.35 + 0.65 * detail) * smoothstep(-0.6, 0.1, y);
  float stars = step(0.992, hash12(floor(fragCoord.xy)));
  col += stars * 0.7;
  fragColor = vec4(col, 1.0);
}
