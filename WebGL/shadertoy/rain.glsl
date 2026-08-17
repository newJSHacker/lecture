// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Rain: streaks in view, wet dark ground, occasional splash rings.

float hash12(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * 0.1031);
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.x + p3.y) * p3.z);
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = fragCoord / iResolution.xy;
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 col = mix(vec3(0.08, 0.09, 0.11), vec3(0.16, 0.18, 0.2), uv.y);

  float ground = smoothstep(0.02, -0.05, p.y + 0.25);
  col = mix(col, vec3(0.05, 0.06, 0.07), ground);
  float sheen = pow(max(0.0, 1.0 - abs(p.x * 0.4 + 0.2)), 8.0) * ground;
  col += vec3(0.12, 0.14, 0.16) * sheen;

  for (int i = 0; i < 3; i++) {
    float fi = float(i);
    vec2 q = uv * vec2(40.0 + fi * 12.0, 12.0 + fi * 4.0);
    q.y += iTime * (6.0 + fi * 2.0);
    vec2 id = floor(q);
    vec2 f = fract(q);
    float rnd = hash12(id + fi * 13.1);
    if (rnd > 0.35) {
      float streak = smoothstep(0.08, 0.0, abs(f.x - 0.5)) * smoothstep(0.0, 0.4, f.y) * (1.0 - ground);
      col += vec3(0.55, 0.6, 0.65) * streak * 0.25;
    }
  }

  vec2 sp = p - vec2(-0.15, -0.28);
  float ring = abs(length(sp) - fract(iTime * 0.7 + hash12(floor(sp * 3.0))) * 0.12);
  col += vec3(0.4) * (1.0 - smoothstep(0.0, 0.008, ring)) * ground * 0.5;
  fragColor = vec4(col, 1.0);
}
