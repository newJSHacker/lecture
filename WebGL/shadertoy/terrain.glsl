// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// fBm height-field terrain, sky, fog. Drag to look around.
// Genre made famous on Shadertoy; this implementation is original.

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
  for (int i = 0; i < 6; i++) { v += a * noise(p); p = m * p; a *= 0.5; }
  return v;
}

float height(vec2 xz) {
  return fbm(xz * 0.12) * 2.4 + 0.35 * fbm(xz * 0.55);
}

vec3 sky(vec3 rd) {
  vec3 c = mix(vec3(0.62, 0.72, 0.88), vec3(0.22, 0.42, 0.75), pow(max(rd.y, 0.0), 0.5));
  vec3 sun = normalize(vec3(0.4, 0.18, 0.7));
  c += vec3(1.0, 0.8, 0.45) * pow(max(dot(rd, sun), 0.0), 180.0);
  return c;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  float yaw = (iMouse.z > 0.0) ? (iMouse.x / iResolution.x - 0.5) * 2.5 : 0.2;
  vec3 ro = vec3(iTime * 0.7, 1.8, iTime * 0.35);
  ro.y += height(ro.xz) * 0.15 + 0.9;
  vec3 fwd = normalize(vec3(sin(yaw), -0.22, cos(yaw)));
  vec3 right = normalize(cross(fwd, vec3(0, 1, 0)));
  vec3 up = cross(right, fwd);
  vec3 rd = normalize(fwd + uv.x * right + uv.y * up);

  float t = 0.0, hit = 0.0;
  for (int i = 0; i < 90; i++) {
    vec3 p = ro + rd * t;
    float d = p.y - height(p.xz);
    if (d < 0.02) { hit = 1.0; break; }
    t += max(d * 0.45, 0.04);
    if (t > 55.0) break;
  }

  vec3 col = sky(rd);
  if (hit > 0.5) {
    vec3 p = ro + rd * t;
    float e = 0.08;
    vec3 n = normalize(vec3(
      height(p.xz - vec2(e, 0.0)) - height(p.xz + vec2(e, 0.0)),
      2.0 * e,
      height(p.xz - vec2(0.0, e)) - height(p.xz + vec2(0.0, e))
    ));
    vec3 l = normalize(vec3(0.4, 0.7, 0.35));
    float dif = max(dot(n, l), 0.0);
    vec3 rock = mix(vec3(0.22, 0.2, 0.16), vec3(0.4, 0.38, 0.3), n.y);
    vec3 grass = vec3(0.18, 0.32, 0.12);
    vec3 matc = mix(rock, grass, smoothstep(0.45, 0.85, n.y));
    matc = mix(matc, vec3(0.85, 0.88, 0.9), smoothstep(1.6, 2.2, p.y));
    col = matc * (0.22 + 0.78 * dif);
    col = mix(sky(rd), col, exp(-0.025 * t));
  }
  fragColor = vec4(pow(col, vec3(0.92)), 1.0);
}
