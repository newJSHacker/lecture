# 04 — Scene graph and animation

Parent: [[08 Three.js Snippets]]

Demo: `demos/06-solar-system.html`.

## Groups (the point of Three.js)

```js
const solar = new THREE.Group();
const earthPivot = new THREE.Group();
const moonPivot = new THREE.Group();
earthPivot.add(earth);
moonPivot.add(moon);
earth.add(moonPivot);
solar.add(sun, earthPivot);
scene.add(solar);

earthPivot.position.x = 3;
moonPivot.position.x = 0.8;

const clock = new THREE.Clock();
function frame() {
  const dt = clock.getDelta();
  const t = clock.getElapsedTime();
  earthPivot.rotation.y += dt * 0.4;
  moonPivot.rotation.y += dt * 1.6;
  earth.rotation.y = t * 1.2;
  renderer.render(scene, camera);
  requestAnimationFrame(frame);
}
```

A mesh’s `position` is **relative to its parent**. That is the whole lecture.

## Transforms

```js
mesh.position.set(1, 0, 0);
mesh.rotation.order = "YXZ"; // or Quaternion
mesh.quaternion.setFromAxisAngle(new THREE.Vector3(0, 1, 0), Math.PI / 4);
mesh.scale.setScalar(1.5);
mesh.updateMatrixWorld();
```

Prefer quaternions for interpolation. Euler yaw/pitch is fine for orbit.

## Look-at

```js
mesh.lookAt(target.position);
camera.lookAt(0, 0, 0);
```

`lookAt` changes rotation. Do not mix with a custom quaternion the same frame unless you mean to.

## AnimationMixer (glTF clips)

```js
const mixer = new THREE.AnimationMixer(model);
const action = mixer.clipAction(gltf.animations[0]);
action.play();
function frame() {
  mixer.update(clock.getDelta());
}
```

No clips → no mixer. Do not add an empty mixer “just in case.”

## Object3D traversal

```js
model.traverse((o) => {
  if (o.isMesh) {
    o.castShadow = true;
    o.receiveShadow = true;
  }
});
```
