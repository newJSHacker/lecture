# Lecture 1 — R3F architecture

**Course:** Interactive Experience Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** Canvas, reconciler  
**Board first:** JSX tree = scene graph

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

1. Create a Vite + R3F app.
2. Canvas wraps WebGL.
3. mesh is Object3D.
4. Don't start a new Three.js class hierarchy.
5. Map last semester's scene to JSX.

---

## 1. What R3F is

React Three Fiber is a **reconciler**: React state commits become Three.js object graphs. It is not a different renderer math. [[18 Three.js Development]] still applies.

## 2. Why a course

Product sites, scroll stories, and HUDs need **UI + 3D**. R3F is how IGWT ships that without two competing scene graphs.

## 3. Vite

Modules, JSX, fast refresh. file:// will not work. `npm run dev`.

## Live coding (60 min)

A box, orbit controls, ambient+dir. Same cube as Three.js week 1.

---

## Lab

1. color as a prop.
2. resize is default — still cap dpr.

---

## Homework

1. Written: reconciler in 8 sentences.
2. repo.

---

## Quiz (10 min)

1. Canvas is (3)
2. mesh maps to (4)
3. why Vite (3)

## Snippet

```jsx
<Canvas camera={{ position: [0, 1, 4] }}>
  <mesh><boxGeometry/><meshStandardMaterial/></mesh>
</Canvas>
```

## Extra exercises

1. Table: R3F prop → Object3D field (8 rows).
2. Draw Canvas vs HTML overlay.
3. Cap `dpr={[1,2]}` and say why.

---

## Common mistakes

- CRA 2018 tutorials.
- no dpr cap.

---

## Board drawings

1. JSX = graph.

