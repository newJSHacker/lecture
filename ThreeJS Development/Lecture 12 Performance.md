# Lecture 12 — Performance

**Course:** Three.js Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** draw calls, instancing, LOD name  
**Board first:** stats.js

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

1. Count draw calls.
2. InstancedMesh.
3. Merge name.
4. pixelRatio cap.
5. Don't optimize textures last if they are 8k.

---

## 1. Budgets

Blender course polycounts. Mobile vs desktop.

## 2. Instancing

WebGL week 12 in engine form.

## 3. Profiling

renderer.info.

## Live coding (60 min)

200 meshes vs InstancedMesh; log info.render.

---

## Lab

1. pixelRatio 1 vs 2.
2. stats.

---

## Homework

1. Written: a budget table (invented numbers forbidden — measure).
2. Code: instanced.

---

## Quiz (10 min)

1. draw call (3)
2. InstancedMesh (4)
3. info.render (3)

## Snippet

```js
console.log(renderer.info.render);
```

---

## Common mistakes

- invented fps.
- 8k textures on a cube.

---

## Board drawings

1. Budget.

