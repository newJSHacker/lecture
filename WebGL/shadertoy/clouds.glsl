// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Clouds: fBm density, sky gradient, sun rim.

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
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 sky = mix(vec3(0.55, 0.7, 0.9), vec3(0.2, 0.4, 0.75), p.y * 0.5 + 0.3);
  vec2 q = vec2(fbm(p * 1.5 + iTime * 0.03), fbm(p * 1.5 + 4.0));
  float c = fbm(p * 2.2 + 2.5 * q + vec2(iTime * 0.04, 0.0));
  c = smoothstep(0.45, 0.78, c);
  c *= smoothstep(-0.85, -0.1, p.y);
  vec3 cloud = mix(vec3(0.75, 0.8, 0.88), vec3(1.0), c);
  float rim = pow(c, 3.0) * (0.5 + 0.5 * p.x);
  cloud += vec3(1.0, 0.9, 0.7) * rim * 0.2;
  vec3 col = mix(sky, cloud, c);
  fragColor = vec4(col, 1.0);
}
