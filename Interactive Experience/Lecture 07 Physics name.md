# Lecture 7 — Physics name

**Course:** Interactive Experience Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** rapier / cannon-es  
**Board first:** collider ≠ mesh

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

1. A physics engine is an **oracle** for collision, like Raycaster.
2. Collider can be simpler than the render mesh.
3. Don't write GJK this week.
4. Sleeping bodies.
5. Fixed timestep name.

---

## 1. Honesty

[[04 Computational Geometry]] is the algorithms course. Here students **use** a engine and must say so.

## 2. @react-three/rapier

Optional. A falling box is enough.

## 3. Networking

Skip. Single player.

## Live coding (60 min)

A floor + dropping cubes; reset.

---

## Lab

1. collider wireframe extra.
2. one sentence oracle vs kernel.

---

## Homework

1. Written: collider vs mesh.
2. demo.

---

## Quiz (10 min)

1. oracle (4)
2. fixed dt (3)
3. convex hull name (3)

## Snippet

```jsx
<RigidBody><mesh><boxGeometry/></mesh></RigidBody>
```

---

## Common mistakes

- claiming they implemented physics.
- 1000 convex hulls.

---

## Board drawings

1. Collider vs render.

