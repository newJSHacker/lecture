# 06 — Loaders (glTF)

Parent: [[08 Three.js Snippets]]

Demo: `demos/10-gltf-pattern.html`.

## The load you will actually write

```js
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { DRACOLoader } from "three/addons/loaders/DRACOLoader.js";

const draco = new DRACOLoader();
draco.setDecoderPath("https://www.gstatic.com/draco/v1/decoders/");
const loader = new GLTFLoader();
loader.setDRACOLoader(draco);

loader.load(
  "models/hero.glb",
  (gltf) => {
    const root = gltf.scene;
    root.traverse((o) => {
      if (o.isMesh) {
        o.castShadow = true;
        o.receiveShadow = true;
      }
    });
    scene.add(root);
  },
  (ev) => { /* percent = ev.loaded / ev.total */ },
  (err) => console.error(err)
);
```

## Checklist (read with students)

- Export **glTF 2.0 / glb**, meters, +Y up
- Apply scale in Blender before export
- One texture set, not 8k extras
- `texture.colorSpace` on albedo after load if it looks too dark/bright
- `renderer.outputColorSpace = SRGBColorSpace`
- Shadows: `castShadow` on meshes, light configured
- Dispose the previous model if you reload

## Texture loader

```js
const tex = await new THREE.TextureLoader().loadAsync("albedo.jpg");
tex.colorSpace = THREE.SRGBColorSpace;
tex.wrapS = tex.wrapT = THREE.RepeatWrapping;
```

`file://` plus a relative jpg often fails CORS. Use a static server or a CanvasTexture in week 1.

## Dispose (memory)

```js
function disposeObject(root) {
  root.traverse((o) => {
    if (o.geometry) o.geometry.dispose();
    const m = o.material;
    if (!m) return;
    const list = Array.isArray(m) ? m : [m];
    for (const mat of list) {
      for (const k of Object.keys(mat)) {
        const v = mat[k];
        if (v && v.isTexture) v.dispose();
      }
      mat.dispose();
    }
  });
}
```

## Offline class

If the network is dead, the demo uses a torus-knot stand-in and still runs the **same** `traverse` / shadow / scale code you would run on `gltf.scene`.
