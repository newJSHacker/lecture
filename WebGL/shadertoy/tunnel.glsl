// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Polar tunnel: 1/r depth, stripes, fog. Demo-scene staple.

float hash12(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * 0.1031);
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.x + p3.y) * p3.z);
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  float r = length(p);
  float a = atan(p.y, p.x);
  vec2 uv = vec2(a / 3.14159265, 0.35 / max(r, 0.02) + iTime * 0.55);
  float stripes = 0.5 + 0.5 * sin(uv.x * 18.0 + uv.y * 4.0);
  float tiles = step(0.5, fract(uv.x * 8.0)) * step(0.5, fract(uv.y * 3.0));
  vec3 col = mix(vec3(0.05, 0.06, 0.1), vec3(0.9, 0.35, 0.15), stripes);
  col = mix(col, vec3(0.15, 0.45, 0.85), tiles * 0.65);
  col += 0.12 * hash12(floor(uv * vec2(32.0, 12.0)));
  col *= smoothstep(0.0, 0.18, r);
  col *= exp(-0.15 / max(r, 0.04));
  vec3 fog = vec3(0.02, 0.02, 0.04);
  col = mix(fog, col, smoothstep(0.0, 0.22, r));
  fragColor = vec4(col, 1.0);
}
