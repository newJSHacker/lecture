# 16 — Effect snippets

Parent: [[07 WebGL and Shader Snippets]]

Small visual recipes. Each should be one lab, not a stack.

## Dissolve

```glsl
float n = valueNoise(v_uv * 8.0);
float d = n - u_cutoff;
if (d < 0.0) discard;
float edge = 1.0 - smoothstep(0.0, u_edge, d);
vec3 color = mix(albedo, u_edgeColor, edge);
```

Demo: `19-dissolve.html`. Animate `u_cutoff` from −0.1 to 1.1.

## Checker / grid (no texture)

```glsl
vec2 c = floor(v_uv * u_cells);
float chk = mod(c.x + c.y, 2.0);
vec2 g = abs(fract(v_uv * u_cells) - 0.5);
float line = 1.0 - smoothstep(0.45, 0.5, max(g.x, g.y));
```

## Triplanar mapping

```glsl
vec3 n = abs(normalize(v_worldN));
n = pow(n, vec3(u_sharp));
n /= n.x + n.y + n.z + 1e-5;
vec3 x = texture(u_tex, v_worldPos.zy * u_scale).rgb;
vec3 y = texture(u_tex, v_worldPos.xz * u_scale).rgb;
vec3 z = texture(u_tex, v_worldPos.xy * u_scale).rgb;
vec3 albedo = x * n.x + y * n.y + z * n.z;
```

Use on terrain and CSG where UVs are painful.

## Parallax (steep, teaching)

```glsl
float h = texture(u_height, v_uv).r;
vec2 offset = v_viewTS.xy / (v_viewTS.z + 0.42) * (h * u_scale);
vec2 uv = v_uv - offset;
```

`v_viewTS` is the view vector in tangent space. Easy to break; show a brick texture.

## Water (sum of sines)

```glsl
float wave(vec2 p, vec2 dir, float freq, float amp, float speed) {
  return sin(dot(p, dir) * freq + u_time * speed) * amp;
}
float h =
  wave(xz, normalize(vec2(1.0, 0.3)), 4.0, 0.04, 1.6) +
  wave(xz, normalize(vec2(-0.4, 1.0)), 7.0, 0.02, 2.1);
```

Normal from height field:

```glsl
float e = 0.05;
float hx = height(xz + vec2(e, 0.0)) - height(xz - vec2(e, 0.0));
float hz = height(xz + vec2(0.0, e)) - height(xz - vec2(0.0, e));
vec3 N = normalize(vec3(-hx, 2.0 * e, -hz));
```

Demo: `20-water.html`.

## Fire / lava

```glsl
float n = fbm(vec2(uv.x * 2.0, uv.y * 3.0 - u_time * 0.4));
n += 0.5 * fbm(vec2(uv.x * 6.0, uv.y * 8.0 - u_time));
float f = smoothstep(0.2, 0.9, n * (1.0 - uv.y));
vec3 col = mix(vec3(0.1, 0.0, 0.0), vec3(1.0, 0.55, 0.05), f);
col = mix(col, vec3(1.0, 0.95, 0.6), pow(f, 4.0));
```

## Sky + sun

```glsl
vec3 rd = normalize(v_worldPos); // or camera ray
vec3 sky = mix(u_horizon, u_zenith, pow(max(rd.y, 0.0), 0.4));
float sun = pow(max(dot(rd, u_sunDir), 0.0), 256.0);
sky += vec3(1.0, 0.85, 0.5) * sun;
```

Demo: `21-sky.html`.

## Hatching (luma → stripes)

```glsl
float l = dot(color, vec3(0.3, 0.6, 0.1));
float h = sin((v_uv.x + v_uv.y) * 80.0);
float ink = smoothstep(0.0, 0.2, l - 0.15 - h * 0.08);
```

## Matcap (see [[WebGL/12 Lighting]])

Procedural matcap if you have no image:

```glsl
vec2 m = vn.xy * 0.5 + 0.5;
float d = length(m - 0.5);
vec3 col = mix(vec3(0.15, 0.18, 0.22), vec3(0.9, 0.92, 0.95), 1.0 - d);
col += pow(max(1.0 - length(m - vec2(0.35, 0.65)), 0.0), 8.0);
```

## Barycentric wireframe

```glsl
float e = min(min(v_bary.x, v_bary.y), v_bary.z);
float w = fwidth(e);
float line = 1.0 - smoothstep(0.0, w * 1.15, e);
vec3 color = mix(albedo, u_lineColor, line);
```

Demo: `18-barycentric-wire.html`.

## Vertex color / height color

```glsl
vec3 col = mix(u_sand, u_grass, smoothstep(-0.2, 0.4, v_worldPos.y));
col = mix(col, u_snow, smoothstep(0.7, 1.1, v_worldPos.y));
```

## Dithered transparency (no sort)

```glsl
float a = texture(u_tex, v_uv).a;
if (a < hash12(gl_FragCoord.xy)) discard;
```

Useful for foliage. No blend state.

## Polar / kaleido UV

```glsl
vec2 p = v_uv * 2.0 - 1.0;
float r = length(p);
float a = atan(p.y, p.x);
a = mod(a, 6.28318 / u_slices);
p = vec2(cos(a), sin(a)) * r;
```

## Screen-door / Bayer (4×4)

```glsl
float bayer4(vec2 fc) {
  int x = int(mod(fc.x, 4.0));
  int y = int(mod(fc.y, 4.0));
  int m[16];
  // 0,8,2,10 / 12,4,14,6 / 3,11,1,9 / 15,7,13,5
  m[0]=0;m[1]=8;m[2]=2;m[3]=10;
  m[4]=12;m[5]=4;m[6]=14;m[7]=6;
  m[8]=3;m[9]=11;m[10]=1;m[11]=9;
  m[12]=15;m[13]=7;m[14]=13;m[15]=5;
  return float(m[y * 4 + x]) / 16.0;
}
```

GLSL ES 3.00 allows the array. Use it to dither a cutoff.

## Motion (UV scroll)

```glsl
vec2 uv = v_uv + vec2(u_time * 0.03, 0.0);
```

Wrap with `fract` if the texture is REPEAT.
