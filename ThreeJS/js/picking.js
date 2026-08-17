// Copy-paste. Pair with the import map in 08 Three.js Snippets.md
import * as THREE from "three";

export function ndcFromEvent(event, canvas, out) {
  const r = canvas.getBoundingClientRect();
  out.x = ((event.clientX - r.left) / r.width) * 2 - 1;
  out.y = -((event.clientY - r.top) / r.height) * 2 + 1;
  return out;
}

export function pick(event, canvas, camera, objects) {
  const pointer = new THREE.Vector2();
  ndcFromEvent(event, canvas, pointer);
  const raycaster = new THREE.Raycaster();
  raycaster.setFromCamera(pointer, camera);
  const hits = raycaster.intersectObjects(objects, false);
  return hits[0] || null;
}
