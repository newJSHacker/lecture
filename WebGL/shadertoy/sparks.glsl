// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Sparks / embers rising from the bottom.

float hash12(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * 0.1031);
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.x + p3.y) * p3.z);
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 col = vec3(0.03, 0.02, 0.02);
  for (int i = 0; i < 40; i++) {
    float fi = float(i);
    float rnd = hash12(vec2(fi, 3.1));
    float t = fract(iTime * (0.15 + rnd * 0.25) + rnd);
    float x = (hash12(vec2(fi, 8.8)) - 0.5) * 1.2 + 0.08 * sin(iTime * 2.0 + fi);
    float y = mix(-0.55, 0.7, t);
    float size = 0.006 + 0.01 * (1.0 - t);
    float d = length(p - vec2(x, y));
    float spark = exp(-d * d / (size * size));
    vec3 c = mix(vec3(1.0, 0.3, 0.05), vec3(1.0, 0.9, 0.4), rnd);
    col += c * spark * (1.0 - t);
  }
  fragColor = vec4(col, 1.0);
}
