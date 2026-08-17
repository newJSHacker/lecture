// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Caustics: interfering sines, typical pool-floor look.

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = fragCoord / iResolution.xy;
  vec2 p = uv * vec2(iResolution.x / iResolution.y, 1.0) * 6.0;
  float t = iTime * 0.7;
  float a = sin(p.x + t) + sin(p.y * 1.3 + t * 1.1);
  float b = sin(p.x * 1.2 - p.y + t * 0.8) + sin(dot(p, vec2(0.7, 1.1)) + t);
  float c = sin(length(p) - t * 1.4);
  float k = a * b * 0.35 + c * 0.25;
  float cau = pow(0.5 + 0.5 * k, 3.0);
  vec3 floorC = mix(vec3(0.05, 0.18, 0.22), vec3(0.15, 0.45, 0.4), uv.y);
  vec3 col = floorC + vec3(0.4, 0.85, 0.9) * cau * 0.85;
  fragColor = vec4(col, 1.0);
}
