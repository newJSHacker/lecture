# 08 — Performance

Parent: [[08 Three.js Snippets]]

Demos: `demos/08-instancing.html`, `demos/15-lod.html`.

## InstancedMesh

```js
const n = 400;
const mesh = new THREE.InstancedMesh(geo, mat, n);
const dummy = new THREE.Object3D();
const color = new THREE.Color();
for (let i = 0; i < n; i++) {
  dummy.position.set((i % 20) - 9.5, 0, Math.floor(i / 20) - 9.5);
  dummy.scale.setScalar(0.35);
  dummy.updateMatrix();
  mesh.setMatrixAt(i, dummy.matrix);
  mesh.setColorAt(i, color.setHSL(i / n, 0.55, 0.5));
}
mesh.instanceMatrix.needsUpdate = true;
if (mesh.instanceColor) mesh.instanceColor.needsUpdate = true;
scene.add(mesh);
```

One draw call. Changing one instance: `setMatrixAt` + `needsUpdate`.

## Frustum culling

Default `mesh.frustumCulled = true`. For huge world matrices that confuse the AABB, set `frustumCulled = false` **or** fix `geometry.computeBoundingSphere()`.

## LOD

```js
const lod = new THREE.LOD();
lod.addLevel(high, 0);
lod.addLevel(mid, 8);
lod.addLevel(low, 18);
scene.add(lod);
```

## Merge / reuse

- Same geometry + same material → one InstancedMesh, not 400 Mesh
- `texture.anisotropy` only as high as needed
- Cap pixel ratio at 2
- Shadows: 1024 is enough in class; 4096 is a laptop fan

## Renderer info HUD

```js
const { calls, triangles } = renderer.info.render;
hud.textContent = calls + " draws, " + triangles + " tris";
```

`renderer.info.autoReset` is true. Read it after `render()`.

## Dispose

See [[ThreeJS/06 Loaders]]. Leaking geometries is the usual “it got slow after 20 minutes” bug in labs.
