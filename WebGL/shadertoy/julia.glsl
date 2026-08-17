// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Julia set (quadratic). Drag to move c. Palette cycles slowly.

vec3 pal(float t) {
  return 0.55 + 0.45 * cos(6.2831853 * (t + vec3(0.0, 0.27, 0.57)));
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec2 z = uv * 1.65;
  vec2 c = vec2(-0.4 + 0.3 * sin(iTime * 0.23), 0.6 * cos(iTime * 0.17));
  if (iMouse.z > 0.0) {
    c = (iMouse.xy - 0.5 * iResolution.xy) / iResolution.y;
  }
  float i, n = 70.0;
  for (i = 0.0; i < 70.0; i++) {
    z = vec2(z.x * z.x - z.y * z.y, 2.0 * z.x * z.y) + c;
    if (dot(z, z) > 16.0) break;
  }
  float v = i - log2(log2(max(dot(z, z), 1.0001))) + 4.0;
  vec3 col = (i >= n) ? vec3(0.02, 0.02, 0.04) : pal(v * 0.05);
  fragColor = vec4(col, 1.0);
}
