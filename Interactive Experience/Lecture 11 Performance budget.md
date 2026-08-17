# Lecture 11 — Performance budget

**Course:** Interactive Experience Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** instancing, dpr, draw calls  
**Board first:** drei Instances; info.render

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

1. InstancedMesh / Instances.
2. dpr cap.
3. Don't animate 500 JSX meshes.
4. Measure.
5. Same honesty as RTR week 12.

---

## 1. R3F cost

Each `<mesh>` is an object. Lists of 1k meshes should be instanced or drei `<Instances>`.

## 2. Textures

Blender budgets still apply.

## 3. Dev vs prod

Strict mode double-mount. Don't panic; dispose.

## Live coding (60 min)

200 trees: naive vs instanced; log counts.

---

## Lab

1. dpr 1 vs 2.
2. one table.

---

## Homework

1. Written: measured table.
2. code.

---

## Quiz (10 min)

1. Instances (4)
2. dpr (3)
3. strict double (3)

## Snippet

```jsx
<Instances limit={200}>{/* ... */}</Instances>
```

---

## Common mistakes

- invented fps.
- 500 MeshStandardMaterials.

---

## Board drawings

1. Budget.

