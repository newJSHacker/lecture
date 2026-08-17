# Three.js snippet index

Parent: [[08 Three.js Snippets]]

Open `ThreeJS/demos/`. Each file is `type="module"` and loads **three r170** from jsDelivr. Needs the network the first time.

## Demos

| File | Idea |
| --- | --- |
| `demos/01-hello-cube.html` | Scene, PerspectiveCamera, WebGLRenderer, Mesh |
| `demos/02-orbit.html` | OrbitControls |
| `demos/03-lights-shadows.html` | Directional light + shadow map + plane |
| `demos/04-materials.html` | Basic / Lambert / Phong / Standard / Physical |
| `demos/05-canvas-texture.html` | CanvasTexture, no CORS |
| `demos/06-solar-system.html` | Groups, nested transforms, Clock |
| `demos/07-raycaster.html` | Click to pick, highlight |
| `demos/08-instancing.html` | InstancedMesh |
| `demos/09-shader-material.html` | ShaderMaterial + time uniform |
| `demos/10-gltf-pattern.html` | GLTFLoader pattern (procedural stand-in + real load snippet) |
| `demos/11-particles.html` | Points + BufferGeometry |
| `demos/12-fog-helpers.html` | Fog, GridHelper, AxesHelper |
| `demos/13-environment.html` | Hemisphere + RoomEnvironment-style IBL-lite |
| `demos/14-resize.html` | Pixel ratio, canvas CSS vs drawing buffer |
| `demos/15-lod.html` | LOD three levels |
| `demos/16-custom-buffer.html` | BufferGeometry from arrays (comp-geom bridge) |
| `demos/17-tone-mapping.html` | ACES + outputColorSpace |
| `demos/18-bloom.html` | EffectComposer + UnrealBloomPass |
| `demos/19-sprites-labels.html` | Sprite / canvas label |
| `demos/20-shadow-contact.html` | PCF shadows, bias |

## Catalogs

| Note | Contents |
| --- | --- |
| [[ThreeJS/01 Scene Camera Renderer]] | Boot sequence |
| [[ThreeJS/02 Lights and Shadows]] | Light types, shadow knobs |
| [[ThreeJS/03 Materials and Textures]] | PBR fields, color space |
| [[ThreeJS/04 Scene Graph and Animation]] | Groups, quaternions, mixer |
| [[ThreeJS/05 Picking]] | Raycaster |
| [[ThreeJS/06 Loaders]] | glTF checklist |
| [[ThreeJS/07 ShaderMaterial]] | GLSL in Three |
| [[ThreeJS/08 Performance]] | Draw calls, dispose |
| [[ThreeJS/09 Postprocess]] | Composer |
| [[ThreeJS/10 Debug]] | Helpers, GL mapping |

## How to use in a lab

1. Open one demo.
2. Change one number (camera `fov`, `metalness`, instance count).
3. Ask: world / view / clip — which space did you just change?
4. Copy a snippet from a catalog into a blank HTML with the import map from [[08 Three.js Snippets]].
