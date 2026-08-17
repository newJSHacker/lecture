// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Mandelbrot zoom. Click/drag to pick a zoom target (else a known bulb).

vec3 pal(float t) {
  return 0.5 + 0.5 * cos(6.2831853 * (vec3(0.0, 0.15, 0.25) + t * vec3(1.0, 0.8, 0.6) + vec3(0.0, 0.33, 0.67)));
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec2 target = vec2(-0.743643887037151, 0.131825904205330);
  if (iMouse.z > 0.0) {
    vec2 m = (iMouse.xy - 0.5 * iResolution.xy) / iResolution.y;
    target = m * 2.2 + vec2(-0.5, 0.0);
  }
  float zoom = exp(-mod(iTime * 0.22, 8.0));
  vec2 c = target + uv * (2.4 * zoom);
  vec2 z = vec2(0.0);
  float i, n = 80.0;
  for (i = 0.0; i < 80.0; i++) {
    z = vec2(z.x * z.x - z.y * z.y, 2.0 * z.x * z.y) + c;
    if (dot(z, z) > 16.0) break;
  }
  float v = i - log2(log2(dot(z, z))) + 4.0;
  vec3 col = (i >= n) ? vec3(0.0) : pal(v * 0.06 + iTime * 0.04);
  fragColor = vec4(col, 1.0);
}
