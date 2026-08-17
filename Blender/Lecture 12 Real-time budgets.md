# Lecture 12 — Real-time budgets

**Course:** Blender for Real-Time Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** tris, batches, maps  
**Board first:** table: platform → tri cap

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

1. Count triangles.
2. Count materials (draw calls).
3. Texture memory rough math.
4. LOD name.
5. Don't ship 2M tris for a bottle.

---

## 1. Budgets

Mobile vs desktop. A student product viewer: tens of thousands of tris is plenty. A city: LOD and instancing (Three.js / WebGL courses).

## 2. Batches

Each material can be a draw. Atlas when you can. Don't make 40 materials for 40 bolts.

## 3. Measure

Three.js `renderer.info` next week. This week: a written budget for *their* asset.

## Live coding (60 min)

Fill a budget sheet for your crate/mug: tris, maps, materials.

---

## Lab

1. Decimate extra and compare.
2. One atlas vs three materials.

---

## Homework

1. Written: budget table with **measured** counts.
2. If you cut, what you cut.

---

## Quiz (10 min)

1. draw call (3)
2. why atlas (4)
3. LOD (3)

## Snippet

```
tris | materials | 1024² maps | target platform
```

---

## Common mistakes

- Invented '60 fps' without a device.
- Nanite speech on a crate.

---

## Board drawings

1. Budget table.

