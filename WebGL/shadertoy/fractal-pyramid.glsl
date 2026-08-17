// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Fractal pyramid: recursive box fold, glow along a ray.
// Genre made famous on Shadertoy; this implementation is original.

mat2 rot(float a) {
  float c = cos(a), s = sin(a);
  return mat2(c, -s, s, c);
}

float fold(vec3 p) {
  float s = 1.0;
  for (int i = 0; i < 6; i++) {
    p = abs(p);
    if (p.x < p.z) p.xz = p.zx;
    if (p.y < p.z) p.yz = p.zy;
    if (p.x < p.y) p.xy = p.yx;
    p = p * 1.85 - vec3(0.55, 0.55, 0.85);
    s *= 1.85;
  }
  return length(max(p, vec3(0.0))) / s;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 rd = normalize(vec3(uv, 1.35));
  rd.yz = rot(0.45) * rd.yz;
  rd.xz = rot(iTime * 0.15) * rd.xz;
  vec3 ro = vec3(0.0, 0.15, -2.6);
  vec3 acc = vec3(0.0);
  float t = 0.0;
  for (int i = 0; i < 70; i++) {
    vec3 p = ro + rd * t;
    float d = fold(p);
    vec3 g = mix(vec3(0.25, 0.55, 1.1), vec3(1.0, 0.45, 0.85), fract(t * 0.35));
    acc += g * (0.018 / (d + 0.008));
    t += d * 0.55 + 0.012;
    if (t > 8.0) break;
  }
  acc = 1.0 - exp(-acc * 0.55);
  fragColor = vec4(pow(acc, vec3(0.9)), 1.0);
}
