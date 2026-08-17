// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Ray-marched metaballs: polynomial blob field, fake refraction tint.

float blob(vec3 p, vec3 c, float r) {
  float d = length(p - c);
  return r * r / max(d * d, 1e-4);
}

float field(vec3 p) {
  float t = iTime;
  float f = 0.0;
  f += blob(p, vec3(0.55 * sin(t * 0.9), 0.35 * cos(t * 1.1), 0.2 * sin(t * 0.7)), 0.42);
  f += blob(p, vec3(0.5 * cos(t * 0.8 + 1.2), 0.4 * sin(t * 1.3), 0.25 * cos(t * 0.6)), 0.38);
  f += blob(p, vec3(0.45 * sin(t * 1.2 + 2.0), 0.3 * cos(t * 0.9 + 0.4), 0.3 * sin(t * 1.05)), 0.36);
  f += blob(p, vec3(0.0, -0.15, 0.0), 0.28);
  return f;
}

float map(vec3 p) {
  return 1.0 - field(p);
}

vec3 normal(vec3 p) {
  vec2 e = vec2(0.002, 0.0);
  return normalize(vec3(
    map(p + e.xyy) - map(p - e.xyy),
    map(p + e.yxy) - map(p - e.yxy),
    map(p + e.yyx) - map(p - e.yyx)
  ));
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 ro = vec3(0.0, 0.1, 2.6);
  vec3 rd = normalize(vec3(uv, -1.5));
  float t = 0.0, hit = 0.0;
  for (int i = 0; i < 70; i++) {
    float d = map(ro + rd * t);
    if (d < 0.002) { hit = 1.0; break; }
    t += d * 0.55;
    if (t > 6.0) break;
  }
  vec3 bg = mix(vec3(0.06, 0.07, 0.1), vec3(0.2, 0.22, 0.28), uv.y * 0.5 + 0.5);
  vec3 col = bg;
  if (hit > 0.5) {
    vec3 p = ro + rd * t;
    vec3 n = normal(p);
    vec3 l = normalize(vec3(0.4, 0.7, 0.5));
    float dif = max(dot(n, l), 0.0);
    float spec = pow(max(dot(n, normalize(l - rd)), 0.0), 64.0);
    float fre = pow(1.0 - max(dot(n, -rd), 0.0), 3.0);
    vec3 matc = mix(vec3(0.15, 0.55, 0.85), vec3(0.95, 0.35, 0.55), 0.5 + 0.5 * n.y);
    col = matc * (0.2 + 0.8 * dif) + vec3(1.0) * spec * 0.55 + bg * fre * 0.45;
  }
  fragColor = vec4(pow(col, vec3(0.92)), 1.0);
}
