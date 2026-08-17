# 10 — Debug and “what is this in GL?”

Parent: [[08 Three.js Snippets]]

Demo: `demos/12-fog-helpers.html`.

## Helpers (leave them on in week 1)

```js
scene.add(new THREE.AxesHelper(1.5));
scene.add(new THREE.GridHelper(10, 10, 0x444444, 0x2a2a2a));
scene.add(new THREE.DirectionalLightHelper(sun, 0.5));
scene.add(new THREE.CameraHelper(sun.shadow.camera));
```

`BoxHelper`, `PolarGridHelper`, `ArrowHelper` as needed.

## Fog

```js
scene.fog = new THREE.Fog(0x1a1a1e, 8, 22);
scene.background = scene.fog.color;
```

or `FogExp2(color, density)`.

## Normal / UV debug materials

```js
mesh.material = new THREE.MeshNormalMaterial();
// or
mesh.material = new THREE.MeshBasicMaterial({ map: uvGrid });
```

## Log the program

```js
console.log(renderer.capabilities.isWebGL2);
console.log(renderer.info);
```

## Map to Course 7

| Student sees | Make them say |
| --- | --- |
| Black mesh | lights? `visible`? camera looking? scale 0? |
| Mesh too dark | color space, no lights, metalness 1 without env |
| Shadows missing | `castShadow` / `receiveShadow` / `shadowMap.enabled` / light camera |
| Stretch on resize | `aspect` + `updateProjectionMatrix` |
| 400 draw calls | should be InstancedMesh |
| Shadertoy on a cube | UVs vs `gl_FragCoord` |

## Lab question (every week)

> Point at this object. Is the number you changed in **object**, **world**, **view**, or **clip** space?

If they cannot answer, they are using Three.js as a toy, not as a graphics course.
