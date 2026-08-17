// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Waterfall: cliff SDF, falling sheet, pool, mist.

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
float sdBox(vec2 p, vec2 b) {
  vec2 d = abs(p) - b;
  return length(max(d, 0.0)) + min(max(d.x, d.y), 0.0);
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 sky = mix(vec3(0.45, 0.62, 0.78), vec3(0.72, 0.84, 0.92), p.y * 0.5 + 0.5);
  vec3 col = sky;

  float cliffL = sdBox(p - vec2(-0.62, 0.05), vec2(0.28, 0.7));
  float cliffR = sdBox(p - vec2(0.64, -0.05), vec2(0.22, 0.75));
  float rock = min(cliffL, cliffR);
  rock += 0.04 * fbm(p * 6.0);
  vec3 rockCol = mix(vec3(0.22, 0.20, 0.18), vec3(0.38, 0.34, 0.28), fbm(p * 8.0));
  col = mix(col, rockCol, 1.0 - smoothstep(0.0, 0.01, rock));

  float sheet = abs(p.x + 0.04 * sin(p.y * 8.0 + iTime)) - 0.16;
  sheet = 1.0 - smoothstep(0.0, 0.04, sheet);
  sheet *= smoothstep(-0.55, -0.15, p.y) * smoothstep(0.85, 0.35, p.y);
  vec2 flow = vec2(p.x * 6.0, p.y * 10.0 + iTime * 4.5);
  float streaks = fbm(flow);
  vec3 water = mix(vec3(0.25, 0.45, 0.55), vec3(0.75, 0.88, 0.95), streaks);
  col = mix(col, water, sheet * 0.9);

  float poolY = -0.42;
  float pool = smoothstep(0.02, -0.08, p.y - poolY) * smoothstep(0.7, 0.15, abs(p.x));
  vec2 pu = vec2(p.x * 4.0 + iTime * 0.3, p.y * 8.0);
  vec3 poolC = mix(vec3(0.12, 0.28, 0.35), vec3(0.45, 0.7, 0.75), fbm(pu));
  col = mix(col, poolC, pool * 0.85);

  float foam = sheet * smoothstep(-0.25, -0.42, p.y) * (0.5 + 0.5 * fbm(p * 20.0 + iTime * 3.0));
  foam += pool * exp(-18.0 * abs(p.x)) * smoothstep(-0.35, -0.42, p.y);
  col = mix(col, vec3(0.92, 0.95, 0.98), clamp(foam, 0.0, 1.0));

  float mist = fbm(p * 3.0 + vec2(0.0, -iTime * 0.2)) * smoothstep(-0.1, -0.5, p.y);
  col = mix(col, vec3(0.8, 0.85, 0.9), mist * 0.35);
  fragColor = vec4(col, 1.0);
}
