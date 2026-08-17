# 15 — Postprocess snippets

Parent: [[07 WebGL and Shader Snippets]]

Draw the scene to an FBO, then draw a fullscreen triangle sampling that texture. Demo: `13-framebuffer-post.html`.

## Fullscreen vertex (one triangle)

```glsl
#version 300 es
const vec2 v[3] = vec2[3](vec2(-1.0, -1.0), vec2(3.0, -1.0), vec2(-1.0, 3.0));
out vec2 v_uv;
void main() {
  vec2 p = v[gl_VertexID];
  v_uv = p * 0.5 + 0.5;
  gl_Position = vec4(p, 0.0, 1.0);
}
```

No VBO required in WebGL2 if you use `gl_VertexID`. The helper also has `GL.fullscreenVerts()` if you want an attribute.

## Vignette

```glsl
float vig = v_uv.x * v_uv.y * (1.0 - v_uv.x) * (1.0 - v_uv.y);
vig = pow(vig * 16.0, 0.4);
color *= vig;
```

## Chromatic aberration

```glsl
vec2 d = (v_uv - 0.5) * u_amount;
vec3 c;
c.r = texture(u_tex, v_uv + d).r;
c.g = texture(u_tex, v_uv).g;
c.b = texture(u_tex, v_uv - d).b;
```

## Film grain

```glsl
float g = hash12(v_uv * u_res + u_time) - 0.5;
color += g * 0.04;
```

## Contrast / saturation / lift

```glsl
color = (color - 0.5) * u_contrast + 0.5;
float luma = dot(color, vec3(0.2126, 0.7152, 0.0722));
color = mix(vec3(luma), color, u_sat);
color += u_lift;
```

## Tone map (Reinhard, ACES-lite)

```glsl
vec3 reinhard(vec3 x) { return x / (1.0 + x); }

vec3 aces(vec3 x) {
  const float a = 2.51, b = 0.03, c = 2.43, d = 0.59, e = 0.14;
  return clamp((x * (a * x + b)) / (x * (c * x + d) + e), 0.0, 1.0);
}
```

Use these **before** `toSRGB` if the scene is HDR-ish (bloom, strong lights).

## Bright pass + blur (bloom-lite)

Bright pass:

```glsl
float b = max(max(c.r, c.g), c.b);
vec3 bright = c * smoothstep(u_thresh, u_thresh + 0.2, b);
```

9-tap box (cheap):

```glsl
vec3 blur9(sampler2D tex, vec2 uv, vec2 px) {
  vec3 s = vec3(0.0);
  for (int y = -1; y <= 1; y++)
  for (int x = -1; x <= 1; x++)
    s += texture(tex, uv + vec2(x, y) * px).rgb;
  return s / 9.0;
}
```

A real bloom is downsample → separable Gaussian → add. Teach the 9-tap first.

## FXAA-lite (luma edges)

```glsl
float luma(vec3 c) { return dot(c, vec3(0.299, 0.587, 0.114)); }
vec2 px = 1.0 / u_res;
float l = luma(texture(u_tex, v_uv).rgb);
float lL = luma(texture(u_tex, v_uv + vec2(-px.x, 0)).rgb);
float lR = luma(texture(u_tex, v_uv + vec2( px.x, 0)).rgb);
float lD = luma(texture(u_tex, v_uv + vec2(0, -px.y)).rgb);
float lU = luma(texture(u_tex, v_uv + vec2(0,  px.y)).rgb);
vec2 dir = vec2(lL - lR, lD - lU);
dir = clamp(dir * 8.0, -1.0, 1.0) * px;
vec3 c = 0.5 * (
  texture(u_tex, v_uv + dir).rgb +
  texture(u_tex, v_uv - dir).rgb);
```

This is a teaching blur-along-edge, not NVIDIA FXAA 3.11.

## Invert / posterize / kernel

```glsl
color = 1.0 - color;
color = floor(color * 5.0) / 5.0;
```

Sharpen:

```glsl
vec3 c = texture(u_tex, v_uv).rgb * 5.0
       - texture(u_tex, v_uv + vec2(px.x, 0)).rgb
       - texture(u_tex, v_uv - vec2(px.x, 0)).rgb
       - texture(u_tex, v_uv + vec2(0, px.y)).rgb
       - texture(u_tex, v_uv - vec2(0, px.y)).rgb;
```

## Depth of field (circle of confusion from depth texture)

```glsl
float z = texture(u_depth, v_uv).r;
float coc = clamp(abs(z - u_focus) * u_scale, 0.0, 1.0);
vec3 sharp = texture(u_tex, v_uv).rgb;
vec3 blur = blur9(u_tex, v_uv, px * 3.0);
color = mix(sharp, blur, coc);
```

Needs a **linear** depth if you stored `gl_FragCoord.z`; raw NDC depth is nonlinear. For class, store view-space `z` in a color attachment instead.

## Copy pass (identity)

Always keep an identity post shader. When the picture is wrong, bind it. If identity is wrong, the FBO is wrong, not the FX.
