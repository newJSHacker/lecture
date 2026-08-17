import * as THREE from "three";

export function gridInstances(geo, mat, nx, nz, spacing = 1) {
  const n = nx * nz;
  const mesh = new THREE.InstancedMesh(geo, mat, n);
  const dummy = new THREE.Object3D();
  const color = new THREE.Color();
  let i = 0;
  for (let z = 0; z < nz; z++) {
    for (let x = 0; x < nx; x++, i++) {
      dummy.position.set((x - (nx - 1) / 2) * spacing, 0, (z - (nz - 1) / 2) * spacing);
      dummy.updateMatrix();
      mesh.setMatrixAt(i, dummy.matrix);
      mesh.setColorAt(i, color.setHSL(i / n, 0.55, 0.5));
    }
  }
  mesh.instanceMatrix.needsUpdate = true;
  if (mesh.instanceColor) mesh.instanceColor.needsUpdate = true;
  return mesh;
}
