// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Underwater: murk, godrays, caustic floor.

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

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = fragCoord / iResolution.xy;
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 deep = vec3(0.0, 0.05, 0.08);
  vec3 mid = vec3(0.02, 0.18, 0.22);
  vec3 col = mix(deep, mid, uv.y);

  float floorY = -0.35;
  float floorM = smoothstep(0.02, -0.08, p.y - floorY);
  vec2 fp = vec2(p.x * 4.0, iTime * 0.3);
  float cau = pow(0.5 + 0.5 * sin(fp.x + iTime) * sin(fp.x * 1.3 - iTime * 0.7), 3.0);
  vec3 sand = vec3(0.15, 0.22, 0.18) + vec3(0.3, 0.7, 0.7) * cau * 0.5;
  col = mix(col, sand, floorM);

  float rays = 0.0;
  for (int i = 0; i < 5; i++) {
    float fi = float(i);
    float x = sin(iTime * 0.2 + fi) * 0.15 + fi * 0.12 - 0.4;
    rays += smoothstep(0.06, 0.0, abs(p.x - x - p.y * 0.15)) * (0.15 + 0.1 * noise(vec2(p.y * 3.0, fi)));
  }
  col += vec3(0.25, 0.45, 0.4) * rays * (0.4 + 0.6 * uv.y);

  float bits = smoothstep(0.92, 1.0, noise(p * 40.0 + iTime));
  col += bits * 0.08;
  col *= 0.85 + 0.15 * uv.y;
  fragColor = vec4(col, 1.0);
}
