// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// River: banks, current, foam around rock islands.

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

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  float bank = 0.38 + 0.06 * sin(p.y * 3.0) + 0.04 * fbm(vec2(p.y * 2.0, 0.0));
  float river = 1.0 - smoothstep(bank - 0.02, bank + 0.02, abs(p.x));
  vec3 grass = mix(vec3(0.18, 0.28, 0.12), vec3(0.32, 0.42, 0.16), fbm(p * 8.0));
  vec2 flow = vec2(p.x * 5.0, p.y * 4.0 - iTime * 1.4);
  float n = fbm(flow);
  vec3 water = mix(vec3(0.08, 0.22, 0.28), vec3(0.25, 0.5, 0.52), n);
  vec3 col = mix(grass, water, river);

  vec2 r1 = p - vec2(-0.05, 0.15);
  vec2 r2 = p - vec2(0.12, -0.25);
  float rock = min(length(r1) - 0.07, length(r2) - 0.05);
  col = mix(col, vec3(0.25, 0.22, 0.2), 1.0 - smoothstep(0.0, 0.01, rock));
  float foam = river * (1.0 - smoothstep(0.02, 0.12, rock)) * (0.4 + 0.6 * fbm(p * 16.0 + iTime));
  foam += river * smoothstep(bank - 0.04, bank, abs(p.x)) * 0.45;
  col = mix(col, vec3(0.9, 0.93, 0.95), clamp(foam, 0.0, 1.0));
  fragColor = vec4(col, 1.0);
}
