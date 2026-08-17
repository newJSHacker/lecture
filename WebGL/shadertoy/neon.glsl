// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// 2D SDF neon: distance-as-glow, cheap bloom. Front-page look.

float sdCircle(vec2 p, float r) { return length(p) - r; }
float sdSegment(vec2 p, vec2 a, vec2 b) {
  vec2 pa = p - a, ba = b - a;
  float h = clamp(dot(pa, ba) / dot(ba, ba), 0.0, 1.0);
  return length(pa - ba * h);
}
float sdBox(vec2 p, vec2 b) {
  vec2 d = abs(p) - b;
  return length(max(d, 0.0)) + min(max(d.x, d.y), 0.0);
}

vec3 glow(float d, vec3 c, float k) {
  return c * (k / (abs(d) + k));
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  float t = iTime;
  vec3 col = vec3(0.02, 0.03, 0.05);

  float ring = sdCircle(p, 0.42 + 0.02 * sin(t * 2.0));
  col += glow(ring, vec3(0.2, 0.85, 1.0), 0.012);

  vec2 q = p;
  float a = t * 0.7;
  q = mat2(cos(a), -sin(a), sin(a), cos(a)) * q;
  float hex = sdBox(q, vec2(0.22)) - 0.04;
  col += glow(hex, vec3(1.0, 0.25, 0.7), 0.01);

  float bar = sdSegment(p, vec2(-0.55, -0.28), vec2(0.55, -0.28 + 0.08 * sin(t * 3.0))) - 0.012;
  col += glow(bar, vec3(1.0, 0.85, 0.2), 0.008);

  float d2 = sdCircle(p - vec2(0.55 * cos(t), 0.35 * sin(t * 1.3)), 0.06);
  col += glow(d2, vec3(0.4, 1.0, 0.5), 0.01);

  col += col * col * 0.35;
  fragColor = vec4(col, 1.0);
}
