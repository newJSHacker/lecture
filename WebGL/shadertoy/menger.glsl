// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Menger sponge: recursive box fold, orbit camera.

float sdBox(vec3 p, vec3 b) {
  vec3 q = abs(p) - b;
  return length(max(q, 0.0)) + min(max(q.x, max(q.y, q.z)), 0.0);
}

float menger(vec3 p) {
  float d = sdBox(p, vec3(1.0));
  float s = 1.0;
  for (int i = 0; i < 4; i++) {
    vec3 a = mod(p * s, 2.0) - 1.0;
    s *= 3.0;
    vec3 r = abs(1.0 - 3.0 * abs(a));
    float da = max(r.x, r.y);
    float db = max(r.y, r.z);
    float dc = max(r.z, r.x);
    float c = (min(da, min(db, dc)) - 1.0) / s;
    d = max(d, c);
  }
  return d;
}

vec3 normal(vec3 p) {
  vec2 e = vec2(0.0015, 0.0);
  return normalize(vec3(
    menger(p + e.xyy) - menger(p - e.xyy),
    menger(p + e.yxy) - menger(p - e.yxy),
    menger(p + e.yyx) - menger(p - e.yyx)
  ));
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  float ang = (iMouse.z > 0.0) ? (iMouse.x / iResolution.x) * 6.28318 : iTime * 0.18;
  float elev = 0.45 + 0.15 * sin(iTime * 0.3);
  vec3 ro = vec3(2.8 * sin(ang) * cos(elev), 2.8 * sin(elev), 2.8 * cos(ang) * cos(elev));
  vec3 ww = normalize(-ro);
  vec3 uu = normalize(cross(ww, vec3(0, 1, 0)));
  vec3 vv = cross(uu, ww);
  vec3 rd = normalize(uv.x * uu + uv.y * vv + 1.7 * ww);

  float t = 0.0, hit = 0.0;
  for (int i = 0; i < 90; i++) {
    float d = menger(ro + rd * t);
    if (d < 0.001) { hit = 1.0; break; }
    t += d;
    if (t > 12.0) break;
  }

  vec3 col = vec3(0.03, 0.04, 0.07) + vec3(0.08) * (uv.y + 0.4);
  if (hit > 0.5) {
    vec3 p = ro + rd * t;
    vec3 n = normal(p);
    vec3 l = normalize(vec3(0.5, 0.8, 0.25));
    float dif = max(dot(n, l), 0.0);
    float ao = 0.55 + 0.45 * n.y;
    vec3 matc = 0.5 + 0.5 * cos(vec3(0.4, 0.7, 1.1) + n.xzy * 1.8 + vec3(0.0, 2.1, 4.2));
    col = matc * (0.15 + 0.85 * dif) * ao;
    col += vec3(1.0) * pow(max(dot(n, normalize(l - rd)), 0.0), 40.0) * 0.2;
  }
  fragColor = vec4(pow(col, vec3(0.9)), 1.0);
}
