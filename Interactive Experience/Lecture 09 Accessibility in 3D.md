# Lecture 9 — Accessibility in 3D

**Course:** Interactive Experience Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** keyboard, labels, motion  
**Board first:** tab to parts; aria on HUD

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

1. Keyboard select next part.
2. ARIA on HUD controls.
3. Captions if audio.
4. Document canvas limits.
5. [[Teaching/10 Inclusive Teaching and Accessibility]].

---

## 1. 3D is hostile by default

Orbit is a mouse skill. Provide: reset camera, keyboard cycle, HUD text for the selected part.

## 2. Color

Not the only channel. Selection outline + label.

## 3. Seizure

No 3Hz strobe. Bloom caps.

## Live coding (60 min)

Keyboard cycles three parts; HUD names them.

---

## Lab

1. focus styles.
2. reduced motion stops auto orbit.

---

## Homework

1. Written: a11y checklist 10 items.
2. demo.

---

## Quiz (10 min)

1. why HUD text (3)
2. keyboard (4)
3. strobe (3)

## Snippet

```jsx
<button onClick={selectNext}>Next part</button>
```

---

## Common mistakes

- canvas-only with no DOM.
- outline:none everywhere.

---

## Board drawings

1. Tab order.

