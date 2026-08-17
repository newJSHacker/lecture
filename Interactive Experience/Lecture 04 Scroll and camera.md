# Lecture 4 — Scroll and camera

**Course:** Interactive Experience Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** scroll controls, storytelling  
**Board first:** scroll y → camera or mix

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

1. Map scroll to a camera path **or** to a mix value.
2. Lenis/drei ScrollControls names.
3. Don't hijack scroll without a skip.
4. One story beat this week.
5. Reduced motion.

---

## 1. Narrative

Awwwards-style pages are often scroll → 3D. Students overbuild. One beat: scroll 0–1 rotates a product.

## 2. a11y

`prefers-reduced-motion`. A non-scroll path to the same content.

## 3. Perf

Don't lerp 100 meshes from scroll without instancing.

## Live coding (60 min)

Scroll 0–1 spins or dollies a glTF/primitive.

---

## Lab

1. reduced-motion CSS media extra.
2. progress bar.

---

## Homework

1. Written: skip/reduce policy.
2. demo.

---

## Quiz (10 min)

1. progress 0-1 (3)
2. reduced motion (4)
3. hijack risk (3)

## Snippet

```jsx
useFrame(() => { mesh.rotation.y = progress.current * Math.PI; });
```

---

## Common mistakes

- full locomotive + 3 scenes as week 4.
- no alternative to scroll.

---

## Board drawings

1. Scroll strip.

