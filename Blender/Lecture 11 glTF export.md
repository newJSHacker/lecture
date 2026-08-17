# Lecture 11 — glTF export

**Course:** Blender for Real-Time Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** glb, transform, extras  
**Board first:** File → Export → glTF 2.0

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 10 | Quiz from last week (Week 1: course contract) |
| 25 | Core definition and one picture |
| 45 | Worked examples / derivation |
| 65 | Live pitfalls and policy |
| 75 | Preview lab, then stand up for live coding |

---

## Learning goals

1. Export .glb.
2. Apply modifiers on export.
3. Include animations if any.
4. Draco name.
5. Open in a glTF viewer before Three.js.

---

## 1. Why glTF

Khronos standard. Three.js `GLTFLoader`. One file (glb) vs json+bin+png.

## 2. Settings

+Y up. Apply modifiers. UVs. Normals. Punctual lights optional. Unused materials off.

## 3. Validate

Load the crate in `ThreeJS/demos/10-gltf-pattern.html` (or a tiny local loader using `ThreeJS/vendor/`). If it is wrong here, a website viewer will not save you. No CDN.

## Live coding (60 min)

Export the crate; view in a glTF viewer; screenshot.

---

## Lab

1. With and without Draco extra.
2. Log triangle count vs blend.

---

## Homework

1. Written: glb vs gltf.
2. The .glb in the repo (small).

---

## Quiz (10 min)

1. glb vs gltf (3)
2. apply modifiers (3)
3. why viewer first (4)

## Snippet

```
Export glTF 2.0 → Format: glTF Binary (.glb) → +Y Up
```

---

## Common mistakes

- Exporting .blend to the web.
- FBX as the only pipeline 'because Unity'.

---

## Board drawings

1. Export checklist.

