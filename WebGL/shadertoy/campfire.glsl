// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Campfire: ground, logs, glow, and a smaller flame.

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
float sdCapsule(vec2 p, vec2 a, vec2 b, float r) {
  vec2 pa = p - a, ba = b - a;
  float h = clamp(dot(pa, ba) / dot(ba, ba), 0.0, 1.0);
  return length(pa - ba * h) - r;
}
vec3 fireRamp(float x) {
  x = clamp(x, 0.0, 1.0);
  vec3 c = mix(vec3(0.0), vec3(0.8, 0.1, 0.0), smoothstep(0.1, 0.35, x));
  c = mix(c, vec3(1.0, 0.5, 0.05), smoothstep(0.3, 0.6, x));
  return mix(c, vec3(1.0, 0.95, 0.7), smoothstep(0.55, 0.95, x));
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 sky = mix(vec3(0.02, 0.03, 0.06), vec3(0.08, 0.05, 0.04), smoothstep(-0.2, 0.8, p.y));
  float ground = smoothstep(0.01, -0.02, p.y + 0.32);
  vec3 col = mix(sky, vec3(0.05, 0.04, 0.03), ground);

  float log1 = sdCapsule(p, vec2(-0.22, -0.30), vec2(0.20, -0.26), 0.035);
  float log2 = sdCapsule(p, vec2(-0.16, -0.24), vec2(0.24, -0.34), 0.03);
  float logs = min(log1, log2);
  col = mix(col, vec3(0.12, 0.07, 0.04), 1.0 - smoothstep(0.0, 0.008, logs));

  vec2 q = p - vec2(0.0, -0.18);
  float shape = 1.0 - length(vec2(q.x * 2.6, q.y * 1.1));
  shape = smoothstep(0.0, 0.5, shape);
  vec2 nUv = vec2(q.x * 4.0, q.y * 5.0 - iTime * 1.8);
  nUv.x += 0.45 * fbm(nUv);
  float flame = pow(max(fbm(nUv) * shape, 0.0), 1.2);
  col += fireRamp(flame);

  float glow = exp(-8.0 * length(p - vec2(0.0, -0.22)));
  col += vec3(1.0, 0.35, 0.05) * glow * 0.35;
  fragColor = vec4(col, 1.0);
}
