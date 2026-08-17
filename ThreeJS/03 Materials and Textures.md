# 03 — Materials and textures

Parent: [[08 Three.js Snippets]]

Demos: `demos/04-materials.html`, `demos/05-canvas-texture.html`, `demos/17-tone-mapping.html`.

## Which material

| Class | Lighting | Use |
| --- | --- | --- |
| `MeshBasicMaterial` | none | unlit, debug UV, sprites |
| `MeshLambertMaterial` | Lambert | cheap, no spec |
| `MeshPhongMaterial` | Blinn-Phong | shiny plastic (old demos) |
| `MeshStandardMaterial` | PBR metal/rough | **default for the course** |
| `MeshPhysicalMaterial` | PBR + clearcoat / transmission | glass, car paint |
| `MeshNormalMaterial` | none | debug normals |
| `MeshDepthMaterial` | none | debug depth |

```js
const std = new THREE.MeshStandardMaterial({
  color: 0xc45c38,
  roughness: 0.35,
  metalness: 0.0,
  envMapIntensity: 1.0,
});
```

## Canvas texture (no CORS)

```js
const cnv = document.createElement("canvas");
cnv.width = cnv.height = 64;
const ctx = cnv.getContext("2d");
for (let y = 0; y < 8; y++) for (let x = 0; x < 8; x++) {
  ctx.fillStyle = (x + y) % 2 ? "#2850b4" : "#f0f0f0";
  ctx.fillRect(x * 8, y * 8, 8, 8);
}
const tex = new THREE.CanvasTexture(cnv);
tex.colorSpace = THREE.SRGBColorSpace;
tex.wrapS = tex.wrapT = THREE.RepeatWrapping;
tex.repeat.set(2, 2);
tex.anisotropy = renderer.capabilities.getMaxAnisotropy();
```

After drawing into an existing canvas: `tex.needsUpdate = true`.

## Color space

```js
albedo.colorSpace = THREE.SRGBColorSpace;
roughnessMap.colorSpace = THREE.NoColorSpace; // linear data
normalMap.colorSpace = THREE.NoColorSpace;
```

## Physical extras

```js
const glass = new THREE.MeshPhysicalMaterial({
  color: 0xffffff,
  transmission: 0.9,
  thickness: 0.4,
  roughness: 0.05,
  ior: 1.5,
  attenuationColor: 0x88ccff,
  attenuationDistance: 1.2,
});
```

Transmission is expensive. One glass object in a student project is enough.

## Shared materials

If two meshes share a material, changing `mesh.material.color` changes both. Clone when you need a unique tint:

```js
mesh.material = mesh.material.clone();
mesh.material.color.set(0x33aa66);
```
