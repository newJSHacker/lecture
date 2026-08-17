# 08 Three.js Snippets

Runnable Three.js demos and copy-paste JS for **IGWT** Course 8 (and lights/PBR bits of 11).

Do this **after** a student can draw a triangle in [[07 WebGL and Shader Snippets]]. Three.js hides the pipeline; keep asking “what is this in GL?”

## Start

1. [[ThreeJS/00 Index]]
2. Open `ThreeJS/demos/01-hello-cube.html` (needs network once: CDN)
3. [[ThreeJS/01 Scene Camera Renderer]]

Import map (every demo):

```html
<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.170.0/examples/jsm/"
  }
}
</script>
```

Pinned **r170**. If the CDN is blocked, download the same files into `ThreeJS/vendor/` and point the import map at them.

## What is in the folder

| Path | What it is |
| --- | --- |
| [[ThreeJS/00 Index]] | Demo map |
| [[ThreeJS/01 Scene Camera Renderer]] | Canvas, camera, loop, resize, color space |
| [[ThreeJS/02 Lights and Shadows]] | Lights, shadow maps |
| [[ThreeJS/03 Materials and Textures]] | Standard/physical, canvas textures |
| [[ThreeJS/04 Scene Graph and Animation]] | Groups, Clock, solar-system pattern |
| [[ThreeJS/05 Picking]] | Raycaster, layers |
| [[ThreeJS/06 Loaders]] | glTF, texture, dispose |
| [[ThreeJS/07 ShaderMaterial]] | Raw/ShaderMaterial, uniforms |
| [[ThreeJS/08 Performance]] | Instancing, frustum, LOD |
| [[ThreeJS/09 Postprocess]] | Composer, bloom |
| [[ThreeJS/10 Debug]] | Helpers, HUD, “what is this in GL?” |
| `ThreeJS/demos/` | One-idea HTML files |
| `ThreeJS/js/` | Copy-paste modules (read in an editor; demos stay self-contained for `file://`) |

## Teaching use

- Week 1: demos 01–04, [[ThreeJS/01 Scene Camera Renderer]]
- Week 2: 05–07, lights and materials
- Week 3: 08–10, picking + shader
- Week 4: 11–15, loader, particles, env, bloom
- Always: [[ThreeJS/10 Debug]]

## License

Teaching notes. Reuse with attribution.
