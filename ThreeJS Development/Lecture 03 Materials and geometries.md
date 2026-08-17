# Lecture 3 — Materials and geometries

**Course:** Three.js Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** BoxGeometry, Standard vs Basic  
**Board first:** MeshStandardMaterial

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

1. Box/Sphere/Plane.
2. MeshBasic vs Lambert vs Standard.
3. wireframe.
4. Dispose geometries when replacing.
5. UVs on built-ins.

---

## 1. Basic

Unlit. Debug.

## 2. Standard

PBR-ish. Real-Time Rendering later.

## 3. Custom

ShaderMaterial is shader course.

## Live coding (60 min)

Three meshes three materials.

---

## Lab

1. wireframe toggle.
2. shared geometry.

---

## Homework

1. Written: Basic vs Standard.
2. Code: trio.

---

## Quiz (10 min)

1. unlit material (3)
2. dispose (4)
3. Standard is PBR? (3)

## Snippet

```js
new THREE.MeshStandardMaterial({ color: 0x8899aa, metalness: 0.1, roughness: 0.6 });
```

---

## Common mistakes

- leaking geometries in a loop.

---

## Board drawings

1. Material table.

