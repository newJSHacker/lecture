# 11 — Vertex and fragment patterns

Parent: [[07 WebGL and Shader Snippets]]

All snippets are **GLSL ES 3.00** (`#version 300 es`) unless noted.

## Minimal pair (clip-space triangle)

```glsl
#version 300 es
in vec2 a_position;
void main() {
  gl_Position = vec4(a_position, 0.0, 1.0);
}
```

```glsl
#version 300 es
precision highp float;
out vec4 outColor;
void main() {
  outColor = vec4(0.91, 0.31, 0.22, 1.0);
}
```

`a_position` in [−1,1] is already NDC if `z=0,w=1`.

## Pass-through MVP + world position / normal / UV

```glsl
#version 300 es
layout(location = 0) in vec3 a_position;
layout(location = 1) in vec3 a_normal;
layout(location = 2) in vec2 a_uv;
uniform mat4 u_proj, u_view, u_model;
uniform mat3 u_normal;
out vec3 v_worldPos;
out vec3 v_worldN;
out vec2 v_uv;
void main() {
  vec4 w = u_model * vec4(a_position, 1.0);
  v_worldPos = w.xyz;
  v_worldN = normalize(u_normal * a_normal);
  v_uv = a_uv;
  gl_Position = u_proj * u_view * w;
}
```

## View-space position (fog, lighting)

```glsl
vec3 viewPos = (u_view * vec4(v_worldPos, 1.0)).xyz;
```

Or compute in the vertex shader and pass `v_viewPos`.

## Billboard (face camera, keep world position)

```glsl
vec3 camRight = vec3(u_view[0][0], u_view[1][0], u_view[2][0]);
vec3 camUp    = vec3(u_view[0][1], u_view[1][1], u_view[2][1]);
vec3 world = a_center + camRight * a_position.x * a_size + camUp * a_position.y * a_size;
gl_Position = u_proj * u_view * vec4(world, 1.0);
```

`a_position` is the quad corner in [−0.5,0.5].

## Point sprites

```glsl
gl_PointSize = u_size * (u_scale / gl_Position.w);
```

Fragment:

```glsl
vec2 p = gl_PointCoord * 2.0 - 1.0;
if (dot(p, p) > 1.0) discard;
```

`gl_PointCoord` origin is upper-left. Soft circle: `1.0 - smoothstep(0.7, 1.0, length(p))`.

## Skinned vertex (two bones, teaching size)

```glsl
in vec4 a_joints;  // as float indices
in vec4 a_weights;
uniform mat4 u_bones[32];
mat4 skin =
  a_weights.x * u_bones[int(a_joints.x)] +
  a_weights.y * u_bones[int(a_joints.y)] +
  a_weights.z * u_bones[int(a_joints.z)] +
  a_weights.w * u_bones[int(a_joints.w)];
vec4 world = u_model * skin * vec4(a_position, 1.0);
```

Normalize weights if they do not sum to 1. Do not start Course 7 here.

## Derivative-based wireframe (no barycentric VBO)

```glsl
float edge = min(min(v_bary.x, v_bary.y), v_bary.z);
float w = fwidth(edge);
float line = 1.0 - smoothstep(0.0, w * 1.2, edge);
```

Needs `v_bary` from the CPU (see demo 18) **or** `GL_NV_fragment_shader_barycentric` (not on the web). `fwidth` is a fragment-only call.

## Clip / discard

```glsl
if (v_worldPos.y < u_clipY) discard;
```

`discard` kills early-z on many GPUs. Prefer a clip plane in the vertex shader for opaque meshes:

```glsl
gl_ClipDistance[0] = v_worldPos.y - u_clipY;
```

Requires `gl.enable(gl.CLIP_DISTANCE0)` (WebGL2).

## Gamma helpers

```glsl
vec3 toLinear(vec3 c) { return pow(c, vec3(2.2)); }
vec3 toSRGB(vec3 c)   { return pow(c, vec3(1.0 / 2.2)); }
```

Apply `toLinear` to sampled albedo if the texture is sRGB and the format is unsigned-byte RGBA. Apply `toSRGB` once at the end.

## Precision

Use `highp` for positions and ray marching. `mediump` on fragment is enough for albedo tints on mobile, but it will break a long ray march.

## WebGL1 pair (demo 25)

```glsl
attribute vec2 a_position;
void main() {
  gl_Position = vec4(a_position, 0.0, 1.0);
}
```

```glsl
precision mediump float;
void main() {
  gl_FragColor = vec4(0.91, 0.31, 0.22, 1.0);
}
```
