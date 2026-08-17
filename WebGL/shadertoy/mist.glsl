// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Ground mist + dark tree cards.

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
  for (int i = 0; i < 5; i++) { v += a * noise(p); p *= 2.02; a *= 0.5; }
  return v;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 col = mix(vec3(0.35, 0.4, 0.42), vec3(0.55, 0.6, 0.65), p.y + 0.4);
  for (int i = 0; i < 5; i++) {
    float fi = float(i);
    float x = -0.7 + fi * 0.32 + 0.05 * sin(fi);
    float trunk = smoothstep(0.012, 0.0, abs(p.x - x)) * smoothstep(-0.45, -0.1, p.y);
    float crown = smoothstep(0.22, 0.0, length(p - vec2(x, 0.12)) - 0.02 * fbm(p * 8.0));
    col = mix(col, vec3(0.08, 0.09, 0.08), max(trunk, crown) * 0.85);
  }
  float mist = fbm(vec2(p.x * 1.5 + iTime * 0.05, p.y * 2.0));
  mist *= smoothstep(0.25, -0.5, p.y);
  col = mix(col, vec3(0.75, 0.78, 0.8), mist * 0.65);
  fragColor = vec4(col, 1.0);
}
