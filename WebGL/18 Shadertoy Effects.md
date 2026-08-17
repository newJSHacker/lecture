# 18 — Shadertoy-style effects

Parent: [[07 WebGL and Shader Snippets]]

Shadertoy is the usual place students steal fire and water from. These notes give **original teaching shaders** in the same *shape* as Shadertoy so they can paste into [shadertoy.com](https://www.shadertoy.com) (Image tab, no textures) or run locally.

Open `WebGL/shadertoy/index.html`. Each `.glsl` file is one Image shader.

**Not copies of named Shadertoy classics.** The uniforms and `mainImage` entry point match Shadertoy. The pictures are IGWT lab pieces. Warn before fire, lightning, and plasma ([[Teaching/10 Inclusive Teaching and Accessibility]]).

## Shadertoy contract

```glsl
void mainImage(out vec4 fragColor, in vec2 fragCoord)
```

| Uniform | Meaning |
| --- | --- |
| `vec3 iResolution` | `xy` = pixel size, `z` = aspect (we pass 1) |
| `float iTime` | Seconds |
| `vec4 iMouse` | `xy` = pixel position while dragging, else last / zero |
| `int iFrame` | Frame index |

UV that matches most Shadertoy comments:

```glsl
vec2 uv = fragCoord / iResolution.xy;              // 0..1
vec2 p  = (fragCoord - 0.5 * iResolution.xy) / iResolution.y; // aspect-correct, 0 at center
```

The local player (`shadertoy/player.js`) wraps your file in `#version 300 es` and calls `mainImage`. On Shadertoy, paste the `.glsl` only — do not paste `#version`.

## How a “fire” shader is built (teach this)

1. **Shape mask** — a teardrop or SDF so noise is not a full-screen television.
2. **Domain warp** — offset UV by fBm so the shape flickers.
3. **Scroll** — add `iTime` on **Y** (up) for fire, **−Y** for waterfall.
4. **Color ramp** — black → red → orange → yellow → white. Do not use raw noise as RGB.
5. **Ember / smoke** — a second, slower fBm in a cooler color.

Water is the same recipe with a **horizontal** scroll, a **fresnel** mix to sky, and a **specular** tick.

Waterfall = vertical water + **rock SDF** + **foam** where the column hits a pool.

## Local gallery

| File | Picture |
| --- | --- |
| `shadertoy/fire.glsl` | Rising flame, color ramp |
| `shadertoy/campfire.glsl` | Logs + glow + flame |
| `shadertoy/lava.glsl` | Cracks, slow flow, emissive veins |
| `shadertoy/smoke.glsl` | Soft billows, gray-blue |
| `shadertoy/waterfall.glsl` | Cliff, falling sheet, pool, mist |
| `shadertoy/water.glsl` | Top-down pond, caustic sparkle |
| `shadertoy/ocean.glsl` | Ray-marched waves, sun, sky |
| `shadertoy/river.glsl` | Banks + flow + foam on rocks |
| `shadertoy/rain.glsl` | Streaks + wet ground sheen |
| `shadertoy/clouds.glsl` | fBm cloud layer, sun rim |
| `shadertoy/caustics.glsl` | Swimming-pool light |
| `shadertoy/ripples.glsl` | Mouse drops, interfering rings |
| `shadertoy/fountain.glsl` | Jet + spray + basin |
| `shadertoy/underwater.glsl` | Godrays, murk, caustic floor |
| `shadertoy/aurora.glsl` | Vertical curtains |
| `shadertoy/lightning.glsl` | Branching bolt (strobe — warn) |
| `shadertoy/mist.glsl` | Ground fog, trees as dark cards |
| `shadertoy/snow.glsl` | Layers of flakes |
| `shadertoy/sparks.glsl` | Embers advected up |
| `shadertoy/plasma.glsl` | Classic sine plasma (strobe — warn) |
| `shadertoy/steam.glsl` | Hot vent, white noise wisps |
| `shadertoy/foam.glsl` | Shore break, voronoi bubbles |

## Lab prompts

- Fire: change only the **ramp**. Then only the **scroll speed**. Then only the **shape**.
- Waterfall: remove the rock SDF. What is left? Put it back.
- Ocean: flatten the waves (`amp *= 0.1`). The lighting should still read as water if fresnel remains.
- Ripples: click. Explain why two rings can cancel.

## Paste checklist (Shadertoy)

1. New shader → Image tab.
2. Delete the default.
3. Paste one `.glsl` file.
4. Do not add a Buffer or iChannel unless the comment says so (none of these need one).
5. If it is black: you pasted `#version 300 es` — remove it.

## Related

- Noise primitives: [[WebGL/13 Noise]]
- SDF: [[WebGL/14 SDF and Ray Marching]]
- Earlier tiny fire/water recipes: [[WebGL/16 Effects]]
- Mesh water (vertex displacement): `demos/20-water.html`
