# Vendored three.js r170

Offline copies. **No CDN.**

| Path | What |
| --- | --- |
| `three.module.js` | Core library |
| `jsm/` | Addons used by the demos (OrbitControls, GLTFLoader, post, RoomEnvironment) |
| `jsm/libs/draco/gltf/` | Draco decoder (JS + WASM) |
| `THREE_LICENSE` | MIT license from three.js |

Demos in `../demos/` import these through an import map. Serve the **`ThreeJS/`** folder (`python -m http.server`) so ES modules resolve.

If a `vendor/_npm/` folder exists, it is only a download cache. Do not ship it. The demos use the files listed above.

```html
<script type="importmap">
{
  "imports": {
    "three": "../vendor/three.module.js",
    "three/addons/": "../vendor/jsm/"
  }
}
</script>
```
