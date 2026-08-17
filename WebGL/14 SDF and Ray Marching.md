# 14 — SDF and ray marching

Parent: [[07 WebGL and Shader Snippets]]

Signed distance: **negative inside**, positive outside. Combine with `min` / `max`, not boolean mesh CSG.

Demo: `11-sdf-raymarch.html`.

## Primitives (2D, for screens and masks)

```glsl
float sdCircle(vec2 p, float r) { return length(p) - r; }

float sdBox(vec2 p, vec2 b) {
  vec2 d = abs(p) - b;
  return length(max(d, 0.0)) + min(max(d.x, d.y), 0.0);
}

float sdSegment(vec2 p, vec2 a, vec2 b) {
  vec2 pa = p - a, ba = b - a;
  float h = clamp(dot(pa, ba) / dot(ba, ba), 0.0, 1.0);
  return length(pa - ba * h);
}

float sdEquilateralTriangle(vec2 p, float r) {
  float k = sqrt(3.0);
  p.x = abs(p.x) - r;
  p.y = p.y + r / k;
  if (p.x + k * p.y > 0.0) p = vec2(p.x - k * p.y, -k * p.x - p.y) / 2.0;
  p.x -= clamp(p.x, -2.0 * r, 0.0);
  return -length(p) * sign(p.y);
}
```

## Primitives (3D)

```glsl
float sdSphere(vec3 p, float r) { return length(p) - r; }

float sdBox(vec3 p, vec3 b) {
  vec3 q = abs(p) - b;
  return length(max(q, 0.0)) + min(max(q.x, max(q.y, q.z)), 0.0);
}

float sdRoundBox(vec3 p, vec3 b, float r) { return sdBox(p, b) - r; }

float sdTorus(vec3 p, vec2 t) {
  vec2 q = vec2(length(p.xz) - t.x, p.y);
  return length(q) - t.y;
}

float sdCapsule(vec3 p, vec3 a, vec3 b, float r) {
  vec3 pa = p - a, ba = b - a;
  float h = clamp(dot(pa, ba) / dot(ba, ba), 0.0, 1.0);
  return length(pa - ba * h) - r;
}

float sdPlane(vec3 p, vec3 n, float h) { return dot(p, n) + h; }

float sdCylinder(vec3 p, float r, float h) {
  vec2 d = abs(vec2(length(p.xz), p.y)) - vec2(r, h);
  return min(max(d.x, d.y), 0.0) + length(max(d, 0.0));
}
```

## CSG

```glsl
float opU(float a, float b) { return min(a, b); }
float opS(float a, float b) { return max(a, -b); }
float opI(float a, float b) { return max(a, b); }

float smin(float a, float b, float k) {
  float h = clamp(0.5 + 0.5 * (b - a) / k, 0.0, 1.0);
  return mix(b, a, h) - k * h * (1.0 - h);
}
```

## Repeat and transform

```glsl
vec3 opRep(vec3 p, vec3 c) { return mod(p + 0.5 * c, c) - 0.5 * c; }

vec3 rotY(vec3 p, float a) {
  float c = cos(a), s = sin(a);
  return vec3(c * p.x - s * p.z, p.y, s * p.x + c * p.z);
}
```

## Scene and normal

```glsl
float map(vec3 p) {
  float s = sdSphere(p - vec3(0.0, 0.6, 0.0), 0.6);
  float b = sdBox(p, vec3(1.4, 0.12, 1.4));
  return smin(s, b, 0.2);
}

vec3 calcNormal(vec3 p) {
  const vec2 e = vec2(1e-3, 0.0);
  return normalize(vec3(
    map(p + e.xyy) - map(p - e.xyy),
    map(p + e.yxy) - map(p - e.yxy),
    map(p + e.yyx) - map(p - e.yyx)
  ));
}
```

## Sphere tracer

```glsl
float march(vec3 ro, vec3 rd) {
  float t = 0.0;
  for (int i = 0; i < 80; i++) {
    float d = map(ro + rd * t);
    if (d < 0.001) return t;
    t += d;
    if (t > 40.0) break;
  }
  return -1.0;
}
```

Camera ray from UV in [−1,1] with aspect:

```glsl
vec3 rd = normalize(vec3(uv * vec2(aspect, 1.0), -1.2));
```

Rotate `rd` by the same basis as the camera.

## Soft shadow (from a point toward the light)

```glsl
float softShadow(vec3 ro, vec3 rd, float mint, float maxt, float k) {
  float res = 1.0;
  float t = mint;
  for (int i = 0; i < 24; i++) {
    float h = map(ro + rd * t);
    res = min(res, k * h / t);
    t += clamp(h, 0.02, 0.2);
    if (res < 0.01 || t > maxt) break;
  }
  return clamp(res, 0.0, 1.0);
}
```

## Ambient occlusion (cheap)

```glsl
float ao(vec3 p, vec3 n) {
  float occ = 0.0;
  float sca = 1.0;
  for (int i = 0; i < 5; i++) {
    float h = 0.01 + 0.12 * float(i) / 4.0;
    float d = map(p + n * h);
    occ += (h - d) * sca;
    sca *= 0.95;
  }
  return clamp(1.0 - 3.0 * occ, 0.0, 1.0);
}
```

## 2D outline from an SDF

```glsl
float d = sdCircle(uv, 0.4);
float fill = 1.0 - smoothstep(0.0, 0.002, d);
float stroke = 1.0 - smoothstep(0.0, 0.004, abs(d));
vec3 col = vec3(0.1);
col = mix(col, vec3(0.91, 0.31, 0.22), fill);
col = mix(col, vec3(1.0), stroke);
```

## Limits to tell students

Ray marching is **O(pixels × steps × scene cost)**. A 4K screen with 128 steps and a heavy fbm map will melt a laptop. Cap steps, cap resolution, or march a small FBO.
