// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Cheap volumetric clouds: density along a sky ray, beer attenuation.
// Genre made famous on Shadertoy; this implementation is original.

float hash12(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * 0.1031);
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.x + p3.y) * p3.z);
}
float noise(vec3 p) {
  vec3 i = floor(p), f = fract(p);
  f = f * f * (3.0 - 2.0 * f);
  vec2 a = i.xy + i.z * vec2(17.0, 29.0);
  float n0 = mix(mix(hash12(a), hash12(a + vec2(1,0)), f.x),
                 mix(hash12(a + vec2(0,1)), hash12(a + vec2(1,1)), f.x), f.y);
  a += vec2(17.0, 29.0);
  float n1 = mix(mix(hash12(a), hash12(a + vec2(1,0)), f.x),
                 mix(hash12(a + vec2(0,1)), hash12(a + vec2(1,1)), f.x), f.y);
  return mix(n0, n1, f.z);
}
float fbm(vec3 p) {
  float v = 0.0, a = 0.5;
  for (int i = 0; i < 5; i++) { v += a * noise(p); p = p * 2.05 + 11.3; a *= 0.5; }
  return v;
}

vec3 sky(vec3 rd) {
  vec3 c = mix(vec3(0.55, 0.7, 0.95), vec3(0.15, 0.32, 0.7), pow(max(rd.y, 0.0), 0.55));
  vec3 sun = normalize(vec3(0.35, 0.25, 0.7));
  c += vec3(1.0, 0.85, 0.5) * pow(max(dot(rd, sun), 0.0), 160.0);
  return c;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 ro = vec3(0.0, 0.6, iTime * 0.12);
  vec3 rd = normalize(vec3(uv, 1.15));
  vec3 col = sky(rd);
  if (rd.y > 0.02) {
    float t0 = (1.2 - ro.y) / rd.y;
    float t1 = (2.4 - ro.y) / rd.y;
    float dens = 0.0;
    vec3 sun = normalize(vec3(0.35, 0.25, 0.7));
    for (int i = 0; i < 18; i++) {
      float fi = (float(i) + 0.5) / 18.0;
      float t = mix(t0, t1, fi);
      vec3 p = ro + rd * t;
      float n = fbm(p * 0.55 + vec3(iTime * 0.05, 0.0, 0.0));
      float d = smoothstep(0.42, 0.78, n);
      dens += d * 0.085;
    }
    dens = 1.0 - exp(-dens * 2.2);
    float light = 0.55 + 0.45 * max(dot(rd, sun), 0.0);
    vec3 cloud = mix(vec3(0.55, 0.6, 0.7), vec3(1.0), light);
    col = mix(col, cloud, dens * smoothstep(0.02, 0.12, rd.y));
  }
  fragColor = vec4(col, 1.0);
}
