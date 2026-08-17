// IGWT teaching shader. Paste into https://www.shadertoy.com (Image tab).
// Voxel DDA through a hashed height field. Drag to look.

float hash12(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * 0.1031);
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.x + p3.y) * p3.z);
}

float voxelH(vec2 c) {
  float h = hash12(c);
  if (h < 0.16) return 1.0;
  return 1.0 + floor(h * 5.0);
}

vec3 voxelAlbedo(vec2 c, float y) {
  float rnd = hash12(c + 19.7);
  vec3 grass = vec3(0.28, 0.55, 0.18);
  vec3 dirt = vec3(0.45, 0.32, 0.18);
  vec3 stone = vec3(0.45, 0.46, 0.48);
  vec3 water = vec3(0.12, 0.32, 0.55);
  if (hash12(c) < 0.16) return water;
  if (y > voxelH(c) - 0.5) return mix(grass, dirt, rnd * 0.35);
  return mix(stone, dirt, rnd);
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
  vec2 uv = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;
  float yaw = (iMouse.z > 0.0) ? (iMouse.x / iResolution.x - 0.5) * 3.0 : iTime * 0.15;
  vec3 ro = vec3(iTime * 1.4, 8.5, 4.0 + iTime * 0.4);
  vec3 fwd = normalize(vec3(sin(yaw), -0.45, cos(yaw)));
  vec3 right = normalize(cross(fwd, vec3(0, 1, 0)));
  vec3 up = cross(right, fwd);
  vec3 rd = normalize(fwd + uv.x * right + uv.y * up);

  vec3 pos = floor(ro);
  vec3 delta = abs(1.0 / max(abs(rd), vec3(1e-4)));
  vec3 stepv = sign(rd);
  vec3 tmax = (stepv * (0.5 - fract(ro)) + 0.5) * delta;

  vec3 col = mix(vec3(0.55, 0.72, 0.95), vec3(0.3, 0.5, 0.85), uv.y * 0.5 + 0.5);
  vec3 nrm = vec3(0.0);
  float hit = 0.0;
  for (int i = 0; i < 80; i++) {
    if (pos.y < voxelH(pos.xz) && pos.y >= 0.0) {
      hit = 1.0;
      break;
    }
    if (tmax.x < tmax.y) {
      if (tmax.x < tmax.z) { pos.x += stepv.x; tmax.x += delta.x; nrm = vec3(-stepv.x, 0, 0); }
      else { pos.z += stepv.z; tmax.z += delta.z; nrm = vec3(0, 0, -stepv.z); }
    } else {
      if (tmax.y < tmax.z) { pos.y += stepv.y; tmax.y += delta.y; nrm = vec3(0, -stepv.y, 0); }
      else { pos.z += stepv.z; tmax.z += delta.z; nrm = vec3(0, 0, -stepv.z); }
    }
    if (pos.y < -1.0 || pos.y > 14.0) break;
  }

  if (hit > 0.5) {
    vec3 l = normalize(vec3(0.4, 0.8, 0.3));
    float dif = max(dot(nrm, l), 0.18);
    col = voxelAlbedo(pos.xz, pos.y) * dif;
    float dist = length(pos + 0.5 - ro);
    col = mix(vec3(0.55, 0.7, 0.9), col, exp(-0.028 * dist));
  }
  fragColor = vec4(pow(col, vec3(0.92)), 1.0);
}
