# Lecture 2 — React state vs 3D

**Course:** Interactive Experience Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** useState, useFrame  
**Board first:** state = discrete; frame = 60Hz

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

1. useFrame for motion.
2. useState for UI discrete events.
3. Don't setState every frame.
4. refs for Object3D.
5. One source of truth.

---

## 1. Two clocks

React re-renders are for **UI**. The WebGL loop is `useFrame`. Mixing them janks.

## 2. refs

`useRef` on a mesh to spin in useFrame without React render.

## 3. Lifting state

Selected part id in React; color on the mesh from that id.

## Live coding (60 min)

Click a box to select (state); spin in useFrame via ref.

---

## Lab

1. jank demo: setState in useFrame then fix.
2. dpr.

---

## Homework

1. Written: when setState is wrong.
2. code.

---

## Quiz (10 min)

1. useFrame vs useState (4)
2. why ref (3)
3. jank (3)

## Snippet

```jsx
useFrame((_, dt) => { ref.current.rotation.y += dt; });
```

---

## Common mistakes

- setState({t}) every frame.
- new material every render.

---

## Board drawings

1. Two clocks.

