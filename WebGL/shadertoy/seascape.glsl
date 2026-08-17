// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Seascape: height-field waves, fresnel sky, sun path. Drag to look.
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

float sea(vec2 xz) {
  float h = 0.0, a = 0.42, f = 0.85;
  vec2 d = normalize(vec2(1.0, 0.35));
  for (int i = 0; i < 6; i++) {
    float ph = iTime * (1.1 + 0.15 * float(i));
    h += a * sin(dot(xz, d) * f + ph);
    d = vec2(d.x * 0.72 - d.y * 0.69, d.x * 0.69 + d.y * 0.72);
    a *= 0.52;
    f *= 1.85;
  }
  h += 0.05 * noise(xz * 3.2 + iTime * 0.35);
  return h;
}

vec3 sky(vec3 rd, vec3 sun) {
  float h = max(rd.y, 0.0);
  vec3 c = mix(vec3(0.72, 0.55, 0.38), vec3(0.18, 0.38, 0.72), pow(h, 0.45));
  c += vec3(1.0, 0.85, 0.45) * pow(max(dot(rd, sun), 0.0), 220.0);
  c += vec3(1.0, 0.5, 0.2) * pow(max(dot(rd, sun), 0.0), 5.0) * 0.28;
  return c;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  float yaw = (iMouse.z > 0.0) ? (iMouse.x / iResolution.x - 0.5) * 1.6 : 0.18;
  float pit = (iMouse.z > 0.0) ? (0.5 - iMouse.y / iResolution.y) * 0.5 : 0.12;
  vec3 ro = vec3(0.0, 1.35, iTime * 0.55);
  vec3 fwd = normalize(vec3(sin(yaw), -0.18 - pit, cos(yaw)));
  vec3 right = normalize(cross(fwd, vec3(0, 1, 0)));
  vec3 up = cross(right, fwd);
  vec3 rd = normalize(fwd + uv.x * right + uv.y * up);
  vec3 sun = normalize(vec3(0.55, 0.22, 0.65));

  vec3 col;
  if (rd.y < 0.0) {
    float t = (0.0 - ro.y) / rd.y;
    vec3 pos = ro + rd * t;
    float e = 0.12;
    vec3 N = normalize(vec3(
      sea(pos.xz - vec2(e, 0.0)) - sea(pos.xz + vec2(e, 0.0)),
      2.0 * e,
      sea(pos.xz - vec2(0.0, e)) - sea(pos.xz + vec2(0.0, e))
    ));
    vec3 R = reflect(rd, N);
    float fre = pow(1.0 - max(dot(N, -rd), 0.0), 4.0);
    vec3 water = mix(vec3(0.01, 0.07, 0.12), sky(R, sun), 0.35 + 0.65 * fre);
    water += vec3(1.0, 0.92, 0.7) * pow(max(dot(N, sun), 0.0), 90.0);
    float foam = smoothstep(0.28, 0.55, sea(pos.xz * 0.35 + 12.0));
    water = mix(water, vec3(0.85, 0.92, 0.95), foam * 0.18 * (1.0 - fre));
    col = mix(sky(rd, sun), water, exp(-0.014 * t));
  } else {
    col = sky(rd, sun);
  }
  fragColor = vec4(pow(col, vec3(0.9)), 1.0);
}
