# 13 — Noise snippets

Parent: [[07 WebGL and Shader Snippets]]

Noise in a fragment shader is a **hash of coordinates**, not `Math.random()`. These functions are deterministic so they match across pixels and frames.

Warn students before flashing high-contrast noise ([[Teaching/10 Inclusive Teaching and Accessibility]]).

## Integer hash → [0,1]

```glsl
float hash11(float p) {
  p = fract(p * 0.1031);
  p *= p + 33.33;
  p *= p + p;
  return fract(p);
}

float hash12(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * 0.1031);
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.x + p3.y) * p3.z);
}

vec2 hash22(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * vec3(0.1031, 0.1030, 0.0973));
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.xx + p3.yz) * p3.zy);
}

vec3 hash33(vec3 p) {
  p = fract(p * vec3(0.1031, 0.1030, 0.0973));
  p += dot(p, p.yxz + 33.33);
  return fract((p.xxy + p.yxx) * p.zyx);
}
```

## Value noise (2D)

```glsl
float valueNoise(vec2 p) {
  vec2 i = floor(p);
  vec2 f = fract(p);
  vec2 u = f * f * (3.0 - 2.0 * f);
  float a = hash12(i);
  float b = hash12(i + vec2(1.0, 0.0));
  float c = hash12(i + vec2(0.0, 1.0));
  float d = hash12(i + vec2(1.0, 1.0));
  return mix(mix(a, b, u.x), mix(c, d, u.x), u.y);
}
```

## Gradient noise (2D, Perlin-style)

```glsl
float gradNoise(vec2 p) {
  vec2 i = floor(p);
  vec2 f = fract(p);
  vec2 u = f * f * (3.0 - 2.0 * f);
  float n00 = dot(hash22(i) * 2.0 - 1.0, f);
  float n10 = dot(hash22(i + vec2(1.0, 0.0)) * 2.0 - 1.0, f - vec2(1.0, 0.0));
  float n01 = dot(hash22(i + vec2(0.0, 1.0)) * 2.0 - 1.0, f - vec2(0.0, 1.0));
  float n11 = dot(hash22(i + vec2(1.0, 1.0)) * 2.0 - 1.0, f - vec2(1.0, 1.0));
  return mix(mix(n00, n10, u.x), mix(n01, n11, u.x), u.y);
}
```

## fBm

```glsl
float fbm(vec2 p) {
  float v = 0.0;
  float a = 0.5;
  mat2 m = mat2(1.6, 1.2, -1.2, 1.6);
  for (int i = 0; i < 5; i++) {
    v += a * valueNoise(p);
    p = m * p;
    a *= 0.5;
  }
  return v;
}
```

Use `gradNoise` for terrain; value noise is cheaper and blotchier.

## Domain warp

```glsl
vec2 q = vec2(fbm(uv), fbm(uv + 4.1));
float n = fbm(uv + 4.0 * q);
```

Demo: `10-noise-fbm.html`.

## 3D value noise (volume / fire)

```glsl
float valueNoise3(vec3 p) {
  vec3 i = floor(p);
  vec3 f = fract(p);
  vec3 u = f * f * (3.0 - 2.0 * f);
  float n000 = hash13(i);
  float n100 = hash13(i + vec3(1,0,0));
  float n010 = hash13(i + vec3(0,1,0));
  float n110 = hash13(i + vec3(1,1,0));
  float n001 = hash13(i + vec3(0,0,1));
  float n101 = hash13(i + vec3(1,0,1));
  float n011 = hash13(i + vec3(0,1,1));
  float n111 = hash13(i + vec3(1,1,1));
  return mix(
    mix(mix(n000, n100, u.x), mix(n010, n110, u.x), u.y),
    mix(mix(n001, n101, u.x), mix(n011, n111, u.x), u.y),
    u.z);
}

float hash13(vec3 p) {
  p = fract(p * 0.1031);
  p += dot(p, p.zyx + 31.32);
  return fract((p.x + p.y) * p.z);
}
```

## Voronoi / cellular

```glsl
vec2 voronoi(vec2 p) {
  vec2 n = floor(p);
  vec2 f = fract(p);
  float md = 8.0;
  vec2 mr;
  for (int j = -1; j <= 1; j++)
  for (int i = -1; i <= 1; i++) {
    vec2 g = vec2(float(i), float(j));
    vec2 o = hash22(n + g);
    vec2 r = g + o - f;
    float d = dot(r, r);
    if (d < md) { md = d; mr = r; }
  }
  return vec2(sqrt(md), hash12(n + mr));
}
```

`x` is distance to nearest site; `y` is an id. Good for tiles, cracked earth, cells.

## Tileable 2D (repeat period `rep`)

```glsl
float hashTile(vec2 p, float rep) {
  return hash12(mod(p, rep));
}
```

For value noise, hash the **integer cell** with `mod(i, rep)` before fetching corners.

## Useful maps from noise

```glsl
float n = fbm(uv * 4.0);
float ridge = 1.0 - abs(n * 2.0 - 1.0);
float billow = abs(n * 2.0 - 1.0);
float terrace = floor(n * 5.0) / 5.0;
```

## Random in a shader without UV (screen)

```glsl
float rnd = hash12(gl_FragCoord.xy + vec2(u_time * 17.0, 0.0));
```

For dither, use a Bayer matrix or `hash12(gl_FragCoord.xy)` added at ~1/255.

## What not to do

- `fract(sin(dot(uv, vec2(12.9898,78.233))) * 43758.5453)` as the only hash — it bands on some GPUs. Fine for a first lecture; replace later.
- Animating by adding `u_time` to **both** x and y of fbm without a direction — looks like TV static. Scroll: `fbm(uv + vec2(0.0, u_time * 0.1))`.
