// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Domain-warped cosine palette. Can flicker — warn the room.
// Technique popularized on Shadertoy; this implementation is original.

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

vec3 pal(float t) {
  return 0.5 + 0.5 * cos(6.2831853 * (t + vec3(0.0, 0.33, 0.67)));
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec2 q = p;
  q += 0.35 * vec2(fbm(q * 2.0 + iTime * 0.12), fbm(q * 2.0 + 4.2));
  q += 0.2 * vec2(fbm(q * 3.5 - iTime * 0.08), fbm(q * 3.5 + 7.1));
  float n = fbm(q * 2.4);
  vec3 col = pal(n + iTime * 0.06 + length(p) * 0.15);
  col *= 0.75 + 0.25 * n;
  fragColor = vec4(col, 1.0);
}
