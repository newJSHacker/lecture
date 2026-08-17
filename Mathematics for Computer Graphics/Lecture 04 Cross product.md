# Lecture 4 — Cross product

**Course:** Mathematics for Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** 2D signed area, 3D perpendicular  
**Board first:** right-hand rule

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

1. 2D cross as signed area.
2. 3D cross perpendicular to both.
3. Connect to orient().
4. Area of parallelogram.
5. Right-handed frame.

---

## 1. 2D

ax by − ay bx. Same as computational geometry `orient` kernel.

## 2. 3D

i × j = k. Determinant of the 3×3 mnemonic. Lighting normals = cross of edges.

## 3. Handedness

IGWT is right-handed. Flipping two vertices flips the normal.

## Live coding (60 min)

2D: signed area of a triangle. 3D: show n = (b-a)×(c-a) on a drawn triangle.

---

## Lab

1. orient clone.
2. Normal of a triangle in the xy plane.

---

## Homework

1. Written: right-hand rule.
2. Code: tests i×j=k.

---

## Quiz (10 min)

1. 2D cross (2,0)×(0,3) (3)
2. i×j (3)
3. why winding matters (4)

## Snippet

```js
function cross2(a,b){ return a.x*b.y - a.y*b.x; }
```

---

## Common mistakes

- Left-handed 'until it looks right'.
- Unsigned area only.

---

## Board drawings

1. Hands.
2. Triangle normal.

