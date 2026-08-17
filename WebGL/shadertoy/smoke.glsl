// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Smoke: large-scale fBm, slow rise, soft contrast.

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
  mat2 m = mat2(1.6, 1.2, -1.2, 1.6);
  for (int i = 0; i < 6; i++) { v += a * noise(p); p = m * p; a *= 0.52; }
  return v;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec2 q = vec2(fbm(p * 1.4 + iTime * 0.05), fbm(p * 1.4 + 5.1));
  float n = fbm(p * 2.0 + 3.0 * q + vec2(0.0, -iTime * 0.12));
  float dens = smoothstep(0.35, 0.85, n);
  dens *= smoothstep(1.1, 0.1, length(p * vec2(0.7, 0.9)));
  vec3 bg = vec3(0.06, 0.07, 0.09);
  vec3 sm = mix(vec3(0.15, 0.16, 0.18), vec3(0.45, 0.48, 0.52), dens);
  vec3 col = mix(bg, sm, dens);
  fragColor = vec4(col, 1.0);
}
