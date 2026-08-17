// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Ocean: ray-marched plane, summed sines, sky, sun spec.

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

float wave(vec2 xz) {
  float h = 0.0;
  h += 0.22 * sin(dot(xz, vec2(0.8, 0.3)) * 1.3 + iTime * 1.1);
  h += 0.12 * sin(dot(xz, vec2(-0.6, 0.9)) * 2.1 + iTime * 1.7);
  h += 0.06 * sin(dot(xz, vec2(0.2, -1.0)) * 3.4 + iTime * 2.3);
  h += 0.04 * noise(xz * 2.5 + iTime * 0.4);
  return h;
}

vec3 sky(vec3 rd) {
  vec3 z = vec3(0.25, 0.45, 0.75);
  vec3 h = vec3(0.75, 0.62, 0.5);
  vec3 s = mix(h, z, pow(max(rd.y, 0.0), 0.45));
  vec3 sun = normalize(vec3(0.45, 0.28, 0.6));
  s += vec3(1.0, 0.85, 0.5) * pow(max(dot(rd, sun), 0.0), 256.0);
  s += vec3(1.0, 0.55, 0.25) * pow(max(dot(rd, sun), 0.0), 6.0) * 0.25;
  return s;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 ro = vec3(0.0, 1.6, iTime * 0.4);
  vec3 rd = normalize(vec3(uv.x, uv.y - 0.15, 1.4));
  float t = (0.0 - ro.y) / rd.y;
  vec3 col;
  if (t > 0.0 && rd.y < 0.0) {
    vec3 pos = ro + rd * t;
    float e = 0.08;
    float hx = wave(pos.xz + vec2(e, 0.0)) - wave(pos.xz - vec2(e, 0.0));
    float hz = wave(pos.xz + vec2(0.0, e)) - wave(pos.xz - vec2(0.0, e));
    vec3 N = normalize(vec3(-hx, 2.0 * e, -hz));
    vec3 R = reflect(rd, N);
    vec3 water = mix(vec3(0.02, 0.08, 0.12), sky(R), 0.55 + 0.45 * pow(1.0 - max(dot(N, -rd), 0.0), 3.0));
    vec3 L = normalize(vec3(0.45, 0.55, 0.6));
    water += vec3(1.0, 0.9, 0.6) * pow(max(dot(N, L), 0.0), 80.0);
    float fog = exp(-0.012 * t);
    col = mix(sky(rd), water, fog);
  } else {
    col = sky(rd);
  }
  fragColor = vec4(pow(col, vec3(0.92)), 1.0);
}
