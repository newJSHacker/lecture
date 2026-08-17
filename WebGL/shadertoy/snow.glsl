// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Snow: several parallax flake layers.

float hash12(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * 0.1031);
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.x + p3.y) * p3.z);
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = fragCoord / iResolution.xy;
  vec3 col = mix(vec3(0.15, 0.18, 0.22), vec3(0.45, 0.5, 0.55), uv.y);
  col = mix(col, vec3(0.7, 0.74, 0.78), smoothstep(0.15, 0.0, uv.y));
  for (int L = 0; L < 3; L++) {
    float fl = float(L);
    float scale = 12.0 + fl * 18.0;
    vec2 q = uv * scale;
    q.y += iTime * (0.25 + fl * 0.2);
    q.x += iTime * 0.08 * (fl + 1.0);
    vec2 id = floor(q);
    vec2 f = fract(q) - 0.5;
    float rnd = hash12(id + fl * 7.3);
    f += (rnd - 0.5) * 0.4;
    float r = 0.015 + 0.02 * hash12(id + 2.2);
    float flake = smoothstep(r, 0.0, length(f));
    col += flake * (0.35 + 0.25 * fl);
  }
  fragColor = vec4(col, 1.0);
}
