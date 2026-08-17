// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Volumetric star field: walk a ray, fold/invert, accumulate glow.
// Genre made famous on Shadertoy; this implementation is original.

mat2 rot(float a) {
  float c = cos(a), s = sin(a);
  return mat2(c, -s, s, c);
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 rd = normalize(vec3(uv, 1.25));
  rd.xz = rot(iTime * 0.07) * rd.xz;
  rd.xy = rot(0.28) * rd.xy;
  vec3 p = vec3(0.4, 0.3, iTime * 0.18);
  vec3 acc = vec3(0.0);
  for (int i = 0; i < 22; i++) {
    vec3 q = abs(fract(p * 0.08) * 2.0 - 1.0);
    float m = 1.0;
    for (int k = 0; k < 7; k++) {
      q = abs(q);
      q = q * (1.85 / clamp(dot(q, q), 0.12, 1.0)) - vec3(0.72, 0.64, 0.88);
      m *= 1.12;
    }
    float d = length(q) / m;
    vec3 glow = mix(vec3(0.45, 0.65, 1.25), vec3(1.15, 0.55, 0.28), fract(float(i) * 0.17));
    acc += glow * (0.016 / (d + 0.015));
    p += rd * (0.16 + d * 0.05);
  }
  acc = 1.0 - exp(-acc * 0.9);
  fragColor = vec4(pow(acc, vec3(0.9)), 1.0);
}
