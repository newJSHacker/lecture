# 17 — Particles, instancing, GPGPU

Parent: [[07 WebGL and Shader Snippets]]

Demos: `14-instancing.html`, `15-particles.html`, `23-gpgpu-pingpong.html`.

## Instancing (WebGL2)

Per-instance attribute: translation (or a whole mat4 as four vec4s).

```js
gl.bindBuffer(gl.ARRAY_BUFFER, instBuf);
gl.enableVertexAttribArray(3);
gl.vertexAttribPointer(3, 3, gl.FLOAT, false, 0, 0);
gl.vertexAttribDivisor(3, 1);
gl.drawArraysInstanced(gl.TRIANGLES, 0, 36, N);
```

Vertex:

```glsl
layout(location = 3) in vec3 a_instancePos;
vec3 pos = a_position * u_scale + a_instancePos;
```

`divisor 0` = per vertex; `1` = per instance.

Instance color:

```glsl
layout(location = 4) in vec3 a_instanceColor;
out vec3 v_color;
```

## Point particles (CPU-updated)

```js
gl.enable(gl.BLEND);
gl.blendFunc(gl.SRC_ALPHA, gl.ONE); // additive
gl.depthMask(false);
gl.drawArrays(gl.POINTS, 0, n);
gl.depthMask(true);
gl.disable(gl.BLEND);
```

Vertex:

```glsl
gl_PointSize = u_size / gl_Position.w;
```

Fragment: discard outside a circle (see [[WebGL/11 Vertex and Fragment]]).

Reset blend and depthMask or the next opaque pass is wrong.

## Transform feedback (WebGL2, optional lecture)

```js
gl.beginTransformFeedback(gl.POINTS);
gl.enable(gl.RASTERIZER_DISCARD);
gl.drawArrays(gl.POINTS, 0, n);
gl.disable(gl.RASTERIZER_DISCARD);
gl.endTransformFeedback();
```

Bind a buffer to `TRANSFORM_FEEDBACK_BUFFER`. Varyings must be listed with `gl.transformFeedbackVaryings` **before** link. Easy to get wrong; ping-pong textures are a gentler Course 12.

## GPGPU ping-pong (RGBA float positions)

Two textures: `read` and `write`. A fullscreen pass samples `read` and writes `write`. Then swap.

Position texture: `xy = pos.xy`, `zw = vel.xy` (2D) or two textures for 3D.

```glsl
vec4 s = texture(u_state, v_uv);
vec2 pos = s.xy;
vec2 vel = s.zw;
vel += u_acc * u_dt;
pos += vel * u_dt;
if (pos.x < -1.0 || pos.x > 1.0) vel.x *= -0.8;
if (pos.y < -1.0 || pos.y > 1.0) vel.y *= -0.8;
outColor = vec4(pos, vel);
```

Create textures with `RGBA16F` or `RGBA32F` and `gl.texImage2D(..., gl.RGBA, gl.FLOAT, null)`. Check `EXT_color_buffer_float` for rendering to them.

Then a **render** pass: one point per texel, vertex shader samples the state texture using `gl_VertexID` → UV.

```glsl
int id = gl_VertexID;
vec2 uv = (vec2(id % u_w, id / u_w) + 0.5) / vec2(u_w, u_h);
vec4 s = texture(u_state, uv);
gl_Position = vec4(s.xy, 0.0, 1.0);
gl_PointSize = 3.0;
```

## Curl / flow (2D)

```glsl
float n1 = valueNoise(pos * 2.0 + vec2(0.0, u_time * 0.1));
float n2 = valueNoise(pos * 2.0 + vec2(5.2, u_time * 0.1));
vec2 acc = vec2(n2 - 0.5, n1 - 0.5) * 0.4;
```

## Soft particles (intersect scene depth)

```glsl
float sceneZ = texture(u_sceneDepth, gl_FragCoord.xy / u_res).r;
float fade = clamp((sceneZ - gl_FragCoord.z) * u_soft, 0.0, 1.0);
outColor.a *= fade;
```

Needs a depth texture from the opaque pass.

## Budget talk (say this in lab)

| Count | Approach |
| ---: | --- |
| < 2k | CPU update + POINTS |
| 2k–50k | instancing or TF |
| 50k–1M | GPGPU ping-pong |
| more | compute (WebGPU) or give up on the laptop |

## Common bugs

- Forgot `vertexAttribDivisor` → every instance is the same
- Float FBO incomplete → no `EXT_color_buffer_float`
- Additive blend left on
- `PointSize` clamped; check `ALIASED_POINT_SIZE_RANGE`
- Sampling the texture you are writing (no ping-pong)
