// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Steam / hot vent: white wisps rising from a grate.

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
  for (int i = 0; i < 5; i++) { v += a * noise(p); p *= 2.05; a *= 0.5; }
  return v;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 col = vec3(0.08, 0.08, 0.09);
  float grate = step(0.0, sin(p.x * 70.0)) * smoothstep(-0.42, -0.38, p.y) * smoothstep(-0.48, -0.42, -p.y);
  grate *= smoothstep(0.28, 0.22, abs(p.x));
  col = mix(col, vec3(0.18), grate);

  vec2 q = vec2(p.x * 2.5, p.y * 2.0 - iTime * 0.35);
  q.x += 0.4 * fbm(q + iTime * 0.1);
  float s = fbm(q);
  float mask = exp(-6.0 * p.x * p.x) * smoothstep(-0.45, 0.1, p.y) * smoothstep(0.7, 0.0, p.y);
  float steam = smoothstep(0.4, 0.75, s) * mask;
  col = mix(col, vec3(0.75, 0.78, 0.8), steam);
  fragColor = vec4(col, 1.0);
}
