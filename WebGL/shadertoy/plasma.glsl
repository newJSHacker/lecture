// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Classic sine plasma. Can flicker — warn the room.

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = fragCoord / iResolution.xy;
  vec2 p = uv * 2.0 - 1.0;
  p.x *= iResolution.x / iResolution.y;
  float t = iTime;
  float v = 0.0;
  v += sin(p.x * 4.0 + t);
  v += sin(p.y * 5.0 + t * 1.3);
  v += sin((p.x + p.y) * 3.0 + t * 0.7);
  v += sin(length(p) * 6.0 - t * 1.5);
  vec3 col = 0.5 + 0.5 * cos(vec3(0.0, 2.0, 4.0) + v + t * 0.4);
  fragColor = vec4(col, 1.0);
}
