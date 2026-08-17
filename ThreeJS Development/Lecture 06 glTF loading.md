# Lecture 6 — glTF loading

**Course:** Three.js Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** GLTFLoader, scale, shadows  
**Board first:** model.scene

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

1. GLTFLoader + DRACO name.
2. add model.scene.
3. scale/center.
4. traverse for shadows.
5. Don't load in the render loop.

---

## 1. Format

Blender course exports this.

## 2. Async

loading manager. Placeholder cube.

## 3. Demo

model load demo.

## Live coding (60 min)

Load a tiny glTF (or a public example with license). Traverse set castShadow.

---

## Lab

1. error UI.
2. box3 center.

---

## Homework

1. Written: why glTF.
2. Code: load.

---

## Quiz (10 min)

1. who is scene (3)
2. traverse (4)
3. load in rAF? (3)

## Snippet

```js
loader.load('m.glb', (g) => scene.add(g.scene));
```

---

## Common mistakes

- hotlinking huge sketchfab without credit.
- loading every frame.

---

## Board drawings

1. glTF box.

