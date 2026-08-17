// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Mandelbulb (power 8): distance estimate, orbit-trap color. Drag to orbit.

float mandelDE(vec3 pos, out float trap) {
  vec3 z = pos;
  float dr = 1.0, r = 0.0;
  trap = 1e10;
  for (int i = 0; i < 7; i++) {
    r = length(z);
    if (r > 2.0) break;
    float th = acos(clamp(z.y / r, -1.0, 1.0));
    float ph = atan(z.z, z.x);
    float zr = pow(r, 8.0);
    dr = pow(r, 7.0) * 8.0 * dr + 1.0;
    th *= 8.0;
    ph *= 8.0;
    z = zr * vec3(sin(th) * cos(ph), cos(th), sin(th) * sin(ph)) + pos;
    trap = min(trap, length(z));
  }
  return 0.5 * log(r) * r / dr;
}

vec3 normal(vec3 p) {
  vec2 e = vec2(0.0012, 0.0);
  float t;
  return normalize(vec3(
    mandelDE(p + e.xyy, t) - mandelDE(p - e.xyy, t),
    mandelDE(p + e.yxy, t) - mandelDE(p - e.yxy, t),
    mandelDE(p + e.yyx, t) - mandelDE(p - e.yyx, t)
  ));
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  float ang = (iMouse.z > 0.0) ? (iMouse.x / iResolution.x) * 6.28318 : iTime * 0.12;
  vec3 ro = vec3(2.4 * sin(ang), 0.55, 2.4 * cos(ang));
  vec3 ww = normalize(-ro);
  vec3 uu = normalize(cross(ww, vec3(0, 1, 0)));
  vec3 vv = cross(uu, ww);
  vec3 rd = normalize(uv.x * uu + uv.y * vv + 1.8 * ww);

  float t = 0.0, trap = 0.0, hit = 0.0;
  for (int i = 0; i < 90; i++) {
    float d = mandelDE(ro + rd * t, trap);
    if (d < 0.001) { hit = 1.0; break; }
    t += clamp(d, 0.002, 0.25);
    if (t > 8.0) break;
  }

  vec3 col = vec3(0.02, 0.03, 0.06) + vec3(0.04, 0.05, 0.1) * (uv.y + 0.5);
  if (hit > 0.5) {
    vec3 p = ro + rd * t;
    vec3 n = normal(p);
    vec3 l = normalize(vec3(0.6, 0.7, 0.3));
    float dif = max(dot(n, l), 0.0);
    float fre = pow(1.0 - max(dot(n, -rd), 0.0), 3.0);
    vec3 matc = 0.5 + 0.5 * cos(vec3(0.2, 0.5, 0.9) + trap * 4.5 + vec3(0.0, 2.0, 4.0));
    col = matc * (0.18 + 0.85 * dif) + vec3(0.9, 0.95, 1.0) * fre * 0.35;
  }
  fragColor = vec4(pow(col, vec3(0.9)), 1.0);
}
