// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Fountain: basin, vertical jet, falling spray.

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
  for (int i = 0; i < 4; i++) { v += a * noise(p); p *= 2.02; a *= 0.5; }
  return v;
}
float sdCircle(vec2 p, float r) { return length(p) - r; }

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 col = mix(vec3(0.15, 0.18, 0.22), vec3(0.45, 0.55, 0.6), p.y * 0.5 + 0.5);

  float basin = sdCircle(p - vec2(0.0, -0.38), 0.32);
  col = mix(col, vec3(0.35, 0.32, 0.28), 1.0 - smoothstep(0.0, 0.01, abs(basin) - 0.02) * step(basin, 0.03));
  float water = 1.0 - smoothstep(0.0, 0.01, sdCircle(p - vec2(0.0, -0.38), 0.26));
  col = mix(col, vec3(0.15, 0.35, 0.42), water * 0.8);

  float jet = abs(p.x) - 0.018 - 0.01 * sin(p.y * 30.0 + iTime * 12.0);
  jet = 1.0 - smoothstep(0.0, 0.012, jet);
  jet *= smoothstep(-0.35, -0.1, p.y) * smoothstep(0.42, 0.15, p.y);
  vec3 jetC = mix(vec3(0.4, 0.65, 0.75), vec3(0.9, 0.95, 1.0), fbm(vec2(p.x * 20.0, p.y * 12.0 - iTime * 6.0)));
  col = mix(col, jetC, jet);

  float spray = 0.0;
  for (int i = 0; i < 12; i++) {
    float fi = float(i);
    float ph = fract(iTime * 0.55 + fi * 0.08);
    float x = (hash12(vec2(fi, 1.0)) - 0.5) * 0.55 * ph;
    float y = 0.28 - 1.1 * ph * ph;
    spray += smoothstep(0.03, 0.0, length(p - vec2(x, y)));
  }
  col = mix(col, vec3(0.85, 0.92, 0.98), clamp(spray, 0.0, 1.0));
  fragColor = vec4(col, 1.0);
}
