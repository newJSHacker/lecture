# Lecture 13 — Import in Three.js

**Course:** Blender for Real-Time Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** scale, shadows, colors  
**Board first:** loader.load → traverse shadows

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

1. Load the glb in the existing Three.js demo pattern.
2. Fix scale if needed.
3. traverse for `castShadow`.
4. Color space.
5. Don't rewrite the engine.

---

## 1. The handshake

This week is the reason the course exists. Asset from Blender → [[18 Three.js Development]] loader.

## 2. Bugs

Scale 0.01, black material (metal+rough+no env), inverted normals, missing UVs, animation not in export.

## 3. Env

Standard material needs an environment to look like the Blender preview.

## Live coding (60 min)

A 40-line loader page using local `ThreeJS/vendor/` showing the student glb + a directional light.

---

## Lab

1. Shadow on a plane.
2. AxesHelper to check size.

---

## Homework

1. Written: bug you hit and the fix.
2. URL or file:// note.

---

## Quiz (10 min)

1. traverse (3)
2. black metal cause (4)
3. Y-up (3)

## Snippet

```js
loader.load('crate.glb', (g) => scene.add(g.scene));
```

---

## Common mistakes

- Re-exporting 20 times without the viewer step.
- Unlit material to 'fix' black.

---

## Board drawings

1. Loader box.
2. 1 m cube reference.

