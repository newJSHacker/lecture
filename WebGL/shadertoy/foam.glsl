// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Shore foam: voronoi cells + moving band.

float hash12(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * 0.1031);
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.x + p3.y) * p3.z);
}
vec2 hash22(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * vec3(0.1031, 0.1030, 0.0973));
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.xx + p3.yz) * p3.zy);
}
float noise(vec2 p) {
  vec2 i = floor(p), f = fract(p);
  vec2 u = f * f * (3.0 - 2.0 * f);
  return mix(mix(hash12(i), hash12(i + vec2(1,0)), u.x),
             mix(hash12(i + vec2(0,1)), hash12(i + vec2(1,1)), u.x), u.y);
}

float voro(vec2 p) {
  vec2 n = floor(p), f = fract(p);
  float md = 8.0;
  for (int j = -1; j <= 1; j++)
  for (int i = -1; i <= 1; i++) {
    vec2 g = vec2(float(i), float(j));
    vec2 o = hash22(n + g);
    md = min(md, length(g + o - f));
  }
  return md;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = fragCoord / iResolution.xy;
  vec2 p = uv * vec2(iResolution.x / iResolution.y, 1.0);
  float shore = uv.y + 0.04 * sin(uv.x * 12.0 + iTime) + 0.03 * noise(p * 4.0 + iTime * 0.2);
  vec3 sea = mix(vec3(0.05, 0.2, 0.28), vec3(0.15, 0.4, 0.42), uv.y);
  vec3 sand = vec3(0.55, 0.48, 0.35);
  vec3 col = mix(sea, sand, smoothstep(0.42, 0.48, shore));
  float band = smoothstep(0.36, 0.44, shore) * smoothstep(0.52, 0.44, shore);
  float cells = 1.0 - smoothstep(0.15, 0.45, voro(p * 18.0 + vec2(iTime * 0.4, 0.0)));
  col = mix(col, vec3(0.92, 0.95, 0.97), band * cells);
  fragColor = vec4(col, 1.0);
}
