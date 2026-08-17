# Lecture 2 — Object3D and transforms

**Course:** Three.js Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** position rotation scale  
**Board first:** matrixWorld

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

1. position/quaternion/scale.
2. add parent.
3. matrixWorld.
4. updateMatrixWorld.
5. Don't mix euler orders blindly.

---

## 1. Graph

CG I scene graph with nicer API.

## 2. Euler

order property. Gimbal from math course.

## 3. Demo

hierarchy demo if present.

## Live coding (60 min)

Parent a cube to another; spin parent.

---

## Lab

1. axesHelper.
2. lookAt extra.

---

## Homework

1. Written: matrixWorld is M.
2. Code: parent.

---

## Quiz (10 min)

1. position units (3)
2. matrixWorld (4)
3. euler order (3)

## Snippet

```js
parent.add(child);
```

---

## Common mistakes

- scale -1 'to flip' without winding talk.

---

## Board drawings

1. Tree.

