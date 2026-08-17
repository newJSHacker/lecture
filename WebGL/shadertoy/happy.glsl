// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Jumping SDF character: squash/stretch, eyes, ground contact. Original blob.

float smin(float a, float b, float k) {
  float h = clamp(0.5 + 0.5 * (b - a) / k, 0.0, 1.0);
  return mix(b, a, h) - k * h * (1.0 - h);
}

vec2 map(vec3 p) {
  float jump = abs(sin(iTime * 3.2));
  float squash = 1.0 - 0.28 * jump;
  vec3 q = p;
  q.y -= 0.28 + jump * 0.62;
  q.y /= squash;
  float body = length(q * vec3(1.0, 0.92, 1.05)) - 0.34;
  vec3 hp = p - vec3(0.0, 0.52 + jump * 0.62, 0.0);
  float head = length(hp) - 0.2;
  float d = smin(body, head, 0.07);
  float id = 1.0;
  vec3 eyeL = hp - vec3(-0.07, 0.04, 0.16);
  vec3 eyeR = hp - vec3(0.07, 0.04, 0.16);
  float eyes = min(length(eyeL) - 0.045, length(eyeR) - 0.045);
  if (eyes < d) { d = eyes; id = 3.0; }
  float pupil = min(length(eyeL - vec3(0.0, 0.0, 0.02)) - 0.02,
                    length(eyeR - vec3(0.0, 0.0, 0.02)) - 0.02);
  if (pupil < d) { d = pupil; id = 4.0; }
  float ground = p.y + 0.42;
  if (ground < d) { d = ground; id = 2.0; }
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
  vec3 ro = vec3(0.0, 0.35, 2.4);
  vec3 rd = normalize(vec3(uv, -1.5));
  float t = 0.0, id = -1.0;
  for (int i = 0; i < 70; i++) {
    vec2 h = map(ro + rd * t);
    if (h.x < 0.001 || t > 10.0) { id = h.y; break; }
    t += h.x;
  }
  vec3 sky = mix(vec3(0.75, 0.85, 0.95), vec3(0.4, 0.6, 0.9), uv.y * 0.5 + 0.4);
  vec3 col = sky;
  if (t < 10.0) {
    vec3 p = ro + rd * t;
    vec3 n = normal(p);
    vec3 l = normalize(vec3(0.4, 0.8, 0.35));
    float dif = max(dot(n, l), 0.0);
    vec3 matc = vec3(0.95, 0.55, 0.2);
    if (id > 1.5 && id < 2.5) {
      matc = mix(vec3(0.35, 0.55, 0.28), vec3(0.5, 0.7, 0.35), step(0.0, sin(p.x * 8.0) * sin(p.z * 8.0)));
    } else if (id > 2.5 && id < 3.5) matc = vec3(0.95);
    else if (id > 3.5) matc = vec3(0.08);
    col = matc * (0.25 + 0.75 * dif);
    float jump = abs(sin(iTime * 3.2));
    vec2 sh = p.xz;
    float shadow = smoothstep(0.55, 0.12, length(sh) + jump * 0.15);
    if (id > 1.5 && id < 2.5) col *= 1.0 - 0.45 * shadow;
  }
  fragColor = vec4(pow(col, vec3(0.92)), 1.0);
}
