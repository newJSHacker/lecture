// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// RGB expanding rings / lattice glow. Can pulse — warn the room.
// Genre made famous on Shadertoy; this implementation is original.

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 col = vec3(0.0);
  float t = iTime;
  for (int i = 0; i < 3; i++) {
    float fi = float(i);
    float z = t * 0.85 + fi * 0.65;
    vec2 q = p * (0.9 + 0.18 * sin(z + fi));
    float ang = atan(q.y, q.x) + z * 0.35;
    float r = length(q);
    vec2 cell = vec2(ang / 6.2831853, r - 0.12 * sin(z * 1.5));
    float d = length(fract(cell * vec2(7.0, 5.0)) - 0.5);
    float glow = 0.016 / max(d, 0.0015);
    col[i] = glow * (0.45 + 0.55 * sin(r * 9.0 - z * 2.2));
  }
  col *= 0.7 / (0.22 + length(p));
  fragColor = vec4(col, 1.0);
}
