# 01 — Scene, camera, renderer

Parent: [[08 Three.js Snippets]]

Demo: `demos/01-hello-cube.html`, `demos/14-resize.html`.

## Minimum boot

```js
import * as THREE from "three";

const canvas = document.getElementById("c");
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(canvas.clientWidth, canvas.clientHeight, false);
renderer.outputColorSpace = THREE.SRGBColorSpace;

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x1a1a1e);

const camera = new THREE.PerspectiveCamera(50, canvas.clientWidth / canvas.clientHeight, 0.1, 100);
camera.position.set(2.4, 1.6, 3.2);
camera.lookAt(0, 0, 0);

const geo = new THREE.BoxGeometry(1, 1, 1);
const mat = new THREE.MeshStandardMaterial({ color: 0xe85d3a, roughness: 0.45, metalness: 0.05 });
scene.add(new THREE.Mesh(geo, mat));
scene.add(new THREE.HemisphereLight(0xffffff, 0x334455, 1.1));

function frame(t) {
  renderer.render(scene, camera);
  requestAnimationFrame(frame);
}
requestAnimationFrame(frame);
```

## Resize (always)

```js
function resize() {
  const w = canvas.clientWidth, h = canvas.clientHeight;
  const dpr = Math.min(devicePixelRatio, 2);
  if (canvas.width !== Math.floor(w * dpr) || canvas.height !== Math.floor(h * dpr)) {
    renderer.setPixelRatio(dpr);
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  }
}
```

Call `resize()` at the start of `frame`. Forgetting `updateProjectionMatrix` stretches the cube.

## Cameras

```js
const persp = new THREE.PerspectiveCamera(50, aspect, 0.1, 100);
const ortho = new THREE.OrthographicCamera(-2 * aspect, 2 * aspect, 2, -2, 0.1, 100);
```

Near `0.1`, far `100` is the teaching default. Near `0.001` causes z-fighting.

## Color management (r152+)

```js
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;
// MeshStandardMaterial.color is sRGB. Texture.colorSpace = THREE.SRGBColorSpace for albedo.
```

Do **not** set `texture.colorSpace = SRGB` on a linear data map (roughness, metalness, normal).

## Orthographic HUD camera (optional)

```js
const hudCam = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
```

## What this is in GL

| Three.js | WebGL |
| --- | --- |
| `scene` + `matrixWorld` | model matrix |
| `camera.matrixWorldInverse` | view matrix |
| `camera.projectionMatrix` | projection |
| `renderer.render` | clear, bind program, draw |
| `outputColorSpace` | last gamma / framebuffer |
