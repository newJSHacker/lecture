// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Ripples: click/drag (iMouse) to drop rings. Also idle rain drops.

float hash12(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * 0.1031);
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.x + p3.y) * p3.z);
}

float ring(vec2 p, vec2 c, float t, float life) {
  float d = length(p - c);
  float r = t * 0.45;
  float w = 0.012 + 0.01 * t;
  float wave = exp(-3.0 * t) * sin((d - r) * 40.0);
  return wave * smoothstep(w, 0.0, abs(d - r)) * step(t, life);
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 col = mix(vec3(0.05, 0.12, 0.16), vec3(0.1, 0.28, 0.32), 0.5 + 0.5 * p.y);
  float h = 0.0;
  for (int i = 0; i < 8; i++) {
    float fi = float(i);
    float rnd = hash12(vec2(fi, 2.7));
    float t = mod(iTime * 0.6 + rnd * 5.0, 4.0);
    vec2 c = vec2(rnd * 1.6 - 0.8, hash12(vec2(fi, 9.1)) * 1.0 - 0.5);
    h += ring(p, c, t, 3.5);
  }
  if (iMouse.z > 0.0) {
    vec2 m = (iMouse.xy - 0.5 * iResolution.xy) / iResolution.y;
    h += ring(p, m, 0.15, 2.0) * 2.0;
  }
  vec3 N = normalize(vec3(-dFdx(h), 0.15, -dFdy(h)));
  float spec = pow(max(N.y, 0.0), 20.0);
  col += vec3(0.7, 0.9, 1.0) * h * 0.35 + spec * 0.15;
  fragColor = vec4(col, 1.0);
}
