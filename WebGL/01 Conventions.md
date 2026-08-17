# 01 — Conventions

Parent: [[07 WebGL and Shader Snippets]]

Disagreeing about conventions is the main source of “my cube is inside out.” Freeze these for a term.

## Spaces

```
object (model) → world → view (camera) → clip → NDC → framebuffer pixels
```

| Space | Who | Typical names |
| --- | --- | --- |
| Object | Mesh verts | `a_position` |
| World | After model matrix | `v_worldPos` |
| View | Camera at origin, looking −Z | `u_view * world` |
| Clip | After projection, before divide | `gl_Position` |
| NDC | After perspective divide, xyz in [−1,1] | GPU |
| Pixel | `gl_FragCoord.xy` | Fragment shader |

This program: **right-handed, Y-up, camera looks down −Z**, **column-major** `mat4` in the order `proj * view * model * vec4(p,1)`.

Normals: `mat3(transpose(inverse(model)))` if the model has non-uniform scale. For uniform scale, `mat3(model)` is enough.

## Winding and culling

- Vertex order **counter-clockwise** is front (OpenGL default).
- `gl.cullFace(gl.BACK)` after `enable(CULL_FACE)`.
- If a model from Blender looks inside-out, the export winding or the `frontFace` setting is wrong — not “WebGL is broken.”

## Clip and depth

- `gl_Position.w` is not 1 after perspective. Do not divide in the vertex shader; the GPU does it.
- Depth range is [0,1] in the framebuffer. `enable(DEPTH_TEST)` and `depthFunc(LEQUAL)` are the usual pair.
- Near plane too close → z-fighting. Start with near `0.1`, far `100`.

## Color

- Textures from canvases and most PNGs are **sRGB**. Sampling as linear vs sRGB changes lighting.
- Do lighting in **linear** space. Apply `pow(color, vec3(1.0/2.2))` at the end of the fragment shader unless you use `EXT_sRGB` / WebGL2 sRGB framebuffers.
- Never encode “category” in color alone in a teaching figure; also label. See [[Teaching/10 Inclusive Teaching and Accessibility]].

## GLSL versions

| API | Shader first line |
| --- | --- |
| WebGL1 | `#ifdef GL_ES\nprecision highp float;\n#endif` (GLSL ES 1.00) |
| WebGL2 | `#version 300 es` then `precision highp float;` |

WebGL2: `attribute` → `in`, `varying` → `in`/`out`, `gl_FragColor` → you declare `out vec4 outColor`, `texture2D` → `texture`.

## Black-screen checklist

Same list as [[Teaching/06 Live Coding Pedagogy]]:

1. Canvas in the DOM and sized (not 0×0 CSS / backing store)
2. Clear color you would notice (`0.1, 0.1, 0.12, 1`)
3. Shader compile and **link** logs
4. Camera looks at the object
5. Object in front of the near plane
6. Winding / culling
7. Depth test / write
8. Attributes bound to the locations you used
9. Texture finished uploading (async)
10. Color / alpha making it invisible (premultiplied, `discard`, alpha 0)

## Debug shaders (keep these)

Normal as color:

```glsl
outColor = vec4(normalize(v_normal) * 0.5 + 0.5, 1.0);
```

UV as color:

```glsl
outColor = vec4(v_uv, 0.0, 1.0);
```

Depth as gray (after you linearize, or raw for a quick look):

```glsl
outColor = vec4(vec3(gl_FragCoord.z), 1.0);
```
