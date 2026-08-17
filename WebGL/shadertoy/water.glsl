// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Top-down pond: layered sines, sparkle, dark depth.

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
  for (int i = 0; i < 5; i++) { v += a * noise(p); p = m * p; a *= 0.5; }
  return v;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  float h = 0.0;
  h += 0.045 * sin(dot(p, vec2(8.0, 2.0)) + iTime * 1.6);
  h += 0.03 * sin(dot(p, vec2(-3.0, 9.0)) + iTime * 2.1);
  h += 0.02 * fbm(p * 6.0 + iTime * 0.25);
  vec2 e = vec2(0.01, 0.0);
  float hx = (0.045 * sin(dot(p + e.xy, vec2(8.0, 2.0)) + iTime * 1.6)) - h;
  float hy = (0.045 * sin(dot(p + e.yx, vec2(8.0, 2.0)) + iTime * 1.6)) - h;
  vec3 N = normalize(vec3(-hx, 0.12, -hy));
  vec3 L = normalize(vec3(0.4, 0.8, 0.3));
  float nd = max(dot(N, L), 0.0);
  float spec = pow(max(dot(N, normalize(L + vec3(0.0, 1.0, 0.0))), 0.0), 80.0);
  vec3 deep = vec3(0.02, 0.12, 0.18);
  vec3 shallow = vec3(0.12, 0.45, 0.48);
  float depth = 0.45 + 0.55 * fbm(p * 2.0);
  vec3 col = mix(deep, shallow, depth) * (0.35 + 0.65 * nd);
  col += vec3(0.85, 0.95, 1.0) * spec * 0.7;
  float spark = smoothstep(0.82, 0.95, fbm(p * 18.0 + iTime));
  col += spark * 0.25;
  fragColor = vec4(pow(col, vec3(0.9)), 1.0);
}
