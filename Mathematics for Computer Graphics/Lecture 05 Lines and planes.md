# Lecture 5 — Lines and planes

**Course:** Mathematics for Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** parametric, implicit  
**Board first:** line p(t)=a+t d

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

1. Write a parametric line.
2. Implicit 2D line ax+by+c=0 teaching.
3. Ray vs segment (t domain).
4. Plane n·(x-p)=0.
5. Intersect ray vs plane idea.

---

## 1. Parametric

p(t) = a + t d. Segment t∈[0,1], ray t≥0. Same as CG geometry objects.

## 2. Planes

A triangle defines a plane. Ray–triangle later uses this plus barycentric.

## 3. Distance

Point to line in 2D via cross/|d|. Optional.

## Live coding (60 min)

Drag a ray across a plane (line in 2D); mark t.

---

## Lab

1. onSegment using t and bounding box.
2. Ray–line intersection 2D.

---

## Homework

1. Written: ray vs segment.
2. Code: t for closest point on segment extra.

---

## Quiz (10 min)

1. t domain of a segment (3)
2. plane equation (4)
3. ray vs line (3)

## Snippet

```js
const p = { x: a.x + t*d.x, y: a.y + t*d.y };
```

---

## Common mistakes

- t unclamped calling it a segment.
- n not unit for distance without dividing.

---

## Board drawings

1. Parametric.
2. Plane.

