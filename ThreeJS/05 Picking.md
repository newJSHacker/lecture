# 05 — Picking (raycaster)

Parent: [[08 Three.js Snippets]]

Demo: `demos/07-raycaster.html`.

## Pointer to NDC

```js
const raycaster = new THREE.Raycaster();
const pointer = new THREE.Vector2();

function ndc(event) {
  const r = canvas.getBoundingClientRect();
  pointer.x = ((event.clientX - r.left) / r.width) * 2 - 1;
  pointer.y = -((event.clientY - r.top) / r.height) * 2 + 1;
}

canvas.addEventListener("pointerdown", (e) => {
  ndc(e);
  raycaster.setFromCamera(pointer, camera);
  const hits = raycaster.intersectObjects(pickables, false);
  if (hits.length) {
    const mesh = hits[0].object;
    mesh.material.emissive?.setHex(0x333333);
  }
});
```

`y` is flipped. Forgetting the minus sign picks the floor.

`recursive` true if the pickable is a Group.

## Layers

```js
camera.layers.enable(1);
ghost.layers.set(1); // only visible / pickable with that mask
raycaster.layers.set(0); // ignore ghosts
```

## GPU picking (later)

For dense instancing, a raycaster on CPU is O(n). Teach CPU picking first. Instanced picking: `InstancedMesh.raycast` works in current three; still cap instance count in class.

## What this is in GL

A ray in world space vs triangles. Same idea as BVH picking in [[05 Sample Graduation Thesis]]. Three.js uses a BVH only if you add one; default is brute force.
