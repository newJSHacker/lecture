// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Lava: dark crust, glowing cracks, slow domain warp.

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
  for (int i = 0; i < 6; i++) { v += a * noise(p); p = m * p; a *= 0.5; }
  return v;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = fragCoord / iResolution.xy;
  vec2 p = uv * vec2(iResolution.x / iResolution.y, 1.0) * 3.0;
  p += 0.35 * vec2(fbm(p + iTime * 0.08), fbm(p + 4.2 - iTime * 0.06));
  float n = fbm(p);
  float ridge = 1.0 - abs(n * 2.0 - 1.0);
  float crack = smoothstep(0.55, 0.92, ridge);
  vec3 crust = mix(vec3(0.04, 0.03, 0.03), vec3(0.12, 0.06, 0.04), n);
  vec3 glow = mix(vec3(0.6, 0.05, 0.0), vec3(1.0, 0.7, 0.15), pow(crack, 2.0));
  vec3 col = mix(crust, glow, crack);
  col += glow * 0.25 * crack;
  fragColor = vec4(col, 1.0);
}
