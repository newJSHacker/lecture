// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// SDF primitive gallery: sphere, box, torus, capsule, plane. Drag to orbit.

float sdSphere(vec3 p, float r) { return length(p) - r; }
float sdBox(vec3 p, vec3 b) {
  vec3 q = abs(p) - b;
  return length(max(q, 0.0)) + min(max(q.x, max(q.y, q.z)), 0.0);
}
float sdTorus(vec3 p, vec2 t) {
  vec2 q = vec2(length(p.xz) - t.x, p.y);
  return length(q) - t.y;
}
float sdCapsule(vec3 p, vec3 a, vec3 b, float r) {
  vec3 pa = p - a, ba = b - a;
  float h = clamp(dot(pa, ba) / dot(ba, ba), 0.0, 1.0);
  return length(pa - ba * h) - r;
}

vec2 map(vec3 p) {
  float d = sdSphere(p - vec3(-1.15, 0.45, 0.0), 0.45);
  float id = 1.0;
  float box = sdBox(p - vec3(0.0, 0.4, 0.15), vec3(0.35, 0.4, 0.35));
  if (box < d) { d = box; id = 2.0; }
  float tor = sdTorus(p - vec3(1.2, 0.35, 0.0), vec2(0.38, 0.12));
  if (tor < d) { d = tor; id = 3.0; }
  float cap = sdCapsule(p, vec3(-0.35, 0.15, 1.05), vec3(0.35, 0.85, 1.05), 0.12);
  if (cap < d) { d = cap; id = 4.0; }
  float pl = p.y;
  if (pl < d) { d = pl; id = 0.0; }
  return vec2(d, id);
}

vec3 normal(vec3 p) {
  vec2 e = vec2(0.0015, 0.0);
  return normalize(vec3(
    map(p + e.xyy).x - map(p - e.xyy).x,
    map(p + e.yxy).x - map(p - e.yxy).x,
    map(p + e.yyx).x - map(p - e.yyx).x
  ));
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  float ang = (iMouse.z > 0.0) ? (iMouse.x / iResolution.x) * 6.28318 : iTime * 0.25;
  vec3 ro = vec3(3.2 * sin(ang), 1.55, 3.2 * cos(ang));
  vec3 ta = vec3(0.0, 0.4, 0.2);
  vec3 ww = normalize(ta - ro);
  vec3 uu = normalize(cross(ww, vec3(0, 1, 0)));
  vec3 vv = cross(uu, ww);
  vec3 rd = normalize(uv.x * uu + uv.y * vv + 1.6 * ww);

  float t = 0.0, id = -1.0;
  for (int i = 0; i < 80; i++) {
    vec2 h = map(ro + rd * t);
    if (h.x < 0.001 || t > 18.0) { id = h.y; break; }
    t += h.x;
  }

  vec3 sky = mix(vec3(0.55, 0.7, 0.9), vec3(0.15, 0.28, 0.5), uv.y * 0.5 + 0.5);
  vec3 col = sky;
  if (t < 18.0) {
    vec3 p = ro + rd * t;
    vec3 n = normal(p);
    vec3 l = normalize(vec3(0.5, 0.8, 0.3));
    float dif = max(dot(n, l), 0.0);
    float amb = 0.22 + 0.18 * n.y;
    float spec = pow(max(dot(n, normalize(l - rd)), 0.0), 48.0);
    vec3 matc = vec3(0.55);
    if (id < 0.5) matc = mix(vec3(0.22), vec3(0.32), step(0.0, sin(p.x * 4.0) * sin(p.z * 4.0)));
    else if (id < 1.5) matc = vec3(0.85, 0.25, 0.2);
    else if (id < 2.5) matc = vec3(0.25, 0.55, 0.9);
    else if (id < 3.5) matc = vec3(0.95, 0.75, 0.2);
    else matc = vec3(0.3, 0.8, 0.45);
    col = matc * (amb + dif) + vec3(1.0) * spec * 0.35;
    float sh = 1.0, st = 0.03;
    for (int i = 0; i < 24; i++) {
      float h = map(p + l * st).x;
      sh = min(sh, 8.0 * h / st);
      st += clamp(h, 0.02, 0.2);
    }
    col *= 0.35 + 0.65 * clamp(sh, 0.0, 1.0);
  }
  fragColor = vec4(pow(col, vec3(0.92)), 1.0);
}
