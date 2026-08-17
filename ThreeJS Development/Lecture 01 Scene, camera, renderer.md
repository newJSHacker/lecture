# Lecture 1 — Scene, camera, renderer

**Course:** Three.js Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** the three objects  
**Board first:** scene.add(mesh)

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

1. Construct Scene/PerspectiveCamera/WebGLRenderer.
2. setSize + pixel ratio cap.
3. append domElement.
4. animation loop.
5. Not a replacement for not knowing PVM.

---

## 1. Engine as a map

Scene is a graph. Camera has P and V. Renderer is the WebGL path.

## 2. Demos

[[08 Three.js Snippets]] · [[ThreeJS/demos/index.html]] 01.

## 3. After WebGL

Students should point to uniforms they already wrote.

## Live coding (60 min)

A cube, orbit from demo 01–02.

---

## Lab

1. resize handler.
2. color background.

---

## Homework

1. Written: Scene vs WebGL program.
2. Code: cube.

---

## Quiz (10 min)

1. three objects (3)
2. domElement (3)
3. why WebGL first (4)

## Snippet

```js
const renderer = new THREE.WebGLRenderer({ antialias: true });
```

---

## Common mistakes

- starting IGWT in Three.js semester 2.
- pixelRatio unbounded.

---

## Board drawings

1. Three boxes.

