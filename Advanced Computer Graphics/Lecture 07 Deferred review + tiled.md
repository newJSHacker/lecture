# Lecture 7 — Deferred review + tiled

**Course:** Advanced Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** lights in tiles  
**Board first:** screen tiles → light lists

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

1. Restate G-buffer.
2. Tiled/clustered: assign lights to tiles.
3. Don't a AAA clustered engine.
4. Debug: light count heatmap.
5. Forward+ name.

---

## 1. Many lights

Deferred and clustered exist because forward dies. Students implement a **CPU** tile list for N lights on a 2D grid, or a heatmap fake.

## 2. Clustered

3D bins in the frustum. Name.

## 3. WebGL

A light heatmap overlay is a valid lab.

## Live coding (60 min)

N point lights; heatmap of overlapping lights per tile (2D).

---

## Lab

1. cull by distance extra.
2. compare naive vs tiled count.

---

## Homework

1. Written: why tiles.
2. heatmap screenshot.

---

## Quiz (10 min)

1. tile list (4)
2. clustered (3)
3. heatmap (3)

## Snippet

```js
// for each light, add index to tiles overlapping its screen AABB
```

---

## Common mistakes

- 1000 Mesh point-light helpers as the algorithm.
- no debug view.

---

## Board drawings

1. Grid overlay.

