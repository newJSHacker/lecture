# 02 — Lights and shadows

Parent: [[08 Three.js Snippets]]

Demos: `demos/03-lights-shadows.html`, `demos/20-shadow-contact.html`.

## Light types (teaching set)

```js
scene.add(new THREE.AmbientLight(0xffffff, 0.15));
scene.add(new THREE.HemisphereLight(0x9bb7ff, 0x3a2a1a, 0.45));

const sun = new THREE.DirectionalLight(0xfff2dd, 1.6);
sun.position.set(4, 6, 3);
sun.castShadow = true;
scene.add(sun);

const bulb = new THREE.PointLight(0xff6622, 8, 12, 2); // intensity, distance, decay
bulb.position.set(-1, 2, 1);
scene.add(bulb);

const spot = new THREE.SpotLight(0xffffff, 6, 20, Math.PI / 7, 0.4, 1);
spot.position.set(2, 5, 2);
spot.target.position.set(0, 0, 0);
scene.add(spot);
scene.add(spot.target);
```

`RectAreaLight` needs `RectAreaLightUniformsLib.init()` and only works with Standard/Physical.

## Shadow map (directional)

```js
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

sun.castShadow = true;
sun.shadow.mapSize.set(1024, 1024);
sun.shadow.camera.near = 0.5;
sun.shadow.camera.far = 20;
sun.shadow.camera.left = -6;
sun.shadow.camera.right = 6;
sun.shadow.camera.top = 6;
sun.shadow.camera.bottom = -6;
sun.shadow.bias = -0.0004;
sun.shadow.normalBias = 0.02;

mesh.castShadow = true;
mesh.receiveShadow = true;
ground.receiveShadow = true;
```

Acne → more `bias` / `normalBias`. Peter-panning → less bias. Peter-panning + acne together → shadow camera too tight or map too small.

## Debug the shadow camera

```js
scene.add(new THREE.CameraHelper(sun.shadow.camera));
```

If the helper does not contain the mesh, the shadow will clip.

## What this is in GL

A directional shadow is demo `WebGL/demos/22-shadow-map.html`: light-space MVP, depth compare, bias. Three.js writes that pass for you. Students should still say “bias” and “map size” out loud.
