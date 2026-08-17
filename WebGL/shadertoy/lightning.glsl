// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Lightning: branching bolt. Can strobe — warn the room.

float hash12(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * 0.1031);
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.x + p3.y) * p3.z);
}
float noise(vec2 p) {
  vec2 i = floor(p), f = fract(p);
  vec2 u = f * f * (3.0 - 2.0 * f);
  return mix(mix(hash12(i), hash12(i + vec2(1,0)), u.x),
             mix(hash12(i + vec2(0,1)), hash12(i + vec2(1,1)), u.x), u.y);
}

float bolt(vec2 p, vec2 a, vec2 b, float seed) {
  vec2 pa = p - a, ba = b - a;
  float h = clamp(dot(pa, ba) / dot(ba, ba), 0.0, 1.0);
  vec2 n = normalize(vec2(-ba.y, ba.x));
  float off = (noise(vec2(h * 8.0, seed + iTime * 20.0)) - 0.5) * 0.18;
  return length(pa - ba * h - n * off);
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 p = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  vec3 col = vec3(0.02, 0.03, 0.06);
  float flash = step(0.92, fract(sin(floor(iTime * 2.4)) * 43758.5));
  flash = max(flash, step(0.0, iMouse.z));
  vec2 a = vec2(-0.05, 0.55);
  vec2 b = vec2(0.08, -0.45);
  float d = bolt(p, a, b, 1.0);
  d = min(d, bolt(p, mix(a, b, 0.45), vec2(0.35, -0.05), 2.2));
  d = min(d, bolt(p, mix(a, b, 0.6), vec2(-0.32, -0.2), 3.1));
  float core = 1.0 - smoothstep(0.0, 0.012, d);
  float glow = 1.0 - smoothstep(0.0, 0.08, d);
  col += (vec3(0.6, 0.75, 1.0) * glow * 0.45 + vec3(1.0) * core) * (0.15 + 0.85 * flash);
  col += vec3(0.15, 0.18, 0.25) * flash * 0.25;
  fragColor = vec4(col, 1.0);
}
