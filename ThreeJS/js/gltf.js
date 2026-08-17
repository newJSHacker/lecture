import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { DRACOLoader } from "three/addons/loaders/DRACOLoader.js";

export function makeGltfLoader() {
  const draco = new DRACOLoader();
  draco.setDecoderPath(new URL("../vendor/jsm/libs/draco/gltf/", import.meta.url).href);
  const loader = new GLTFLoader();
  loader.setDRACOLoader(draco);
  return loader;
}

export function enableShadows(root) {
  root.traverse((o) => {
    if (o.isMesh) {
      o.castShadow = true;
      o.receiveShadow = true;
    }
  });
}

export function disposeObject(root) {
  root.traverse((o) => {
    if (o.geometry) o.geometry.dispose();
    const m = o.material;
    if (!m) return;
    for (const mat of Array.isArray(m) ? m : [m]) {
      for (const k of Object.keys(mat)) {
        const v = mat[k];
        if (v && v.isTexture) v.dispose();
      }
      mat.dispose();
    }
  });
}
