// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Rising flame: shape mask + domain-warped fBm + heat ramp.

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

vec3 fireRamp(float x) {
  x = clamp(x, 0.0, 1.0);
  vec3 c = vec3(0.0);
  c = mix(c, vec3(0.35, 0.02, 0.0), smoothstep(0.05, 0.22, x));
  c = mix(c, vec3(0.85, 0.12, 0.02), smoothstep(0.18, 0.42, x));
  c = mix(c, vec3(1.00, 0.45, 0.05), smoothstep(0.38, 0.62, x));
  c = mix(c, vec3(1.00, 0.85, 0.35), smoothstep(0.58, 0.82, x));
  c = mix(c, vec3(1.00, 0.98, 0.90), smoothstep(0.78, 1.00, x));
  return c;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  float wind = (iMouse.z > 0.0) ? (iMouse.x / iResolution.x - 0.5) * 0.8 : 0.15 * sin(iTime * 0.7);
  vec2 q = p + vec2(wind * (p.y + 0.6), 0.0);
  float shape = 1.0 - length(vec2(q.x * 2.1, (q.y + 0.15) * 0.72));
  shape = smoothstep(0.0, 0.55, shape);
  vec2 nUv = vec2(q.x * 3.0, q.y * 4.2 - iTime * 1.6);
  nUv.x += 0.55 * fbm(nUv + iTime * 0.25);
  float n = fbm(nUv);
  float flame = n * shape;
  flame = pow(max(flame, 0.0), 1.15);
  vec3 col = fireRamp(flame);
  float smoke = fbm(vec2(q.x * 2.0, q.y * 1.4 - iTime * 0.35)) * smoothstep(-0.1, 0.6, q.y) * (1.0 - shape);
  col += vec3(0.12, 0.12, 0.14) * smoke * 0.55;
  col *= 0.25 + 0.75 * smoothstep(-0.7, 0.2, p.y);
  fragColor = vec4(col, 1.0);
}
