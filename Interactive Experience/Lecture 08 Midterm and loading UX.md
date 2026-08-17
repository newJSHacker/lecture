# Lecture 8 — Midterm and loading UX

**Course:** Interactive Experience Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** midterm; Suspense  
**Board first:** fallback = progress

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

1. Sit midterm: reconciler, state vs frame, HUD, scroll, audio, physics-oracle.
2. useLoader / Suspense.
3. Progress bar.
4. Don't freeze the tab on a 50MB glb.
5. Error boundary name.

---

## 1. Midterm

architecture and the two clocks.

## 2. Loading

drei `useProgress`. Placeholder cube. Compress glb (Blender course).

## 3. UX

Timeout message. Reduce motion still applies.

## Live coding (60 min)

Suspense fallback while a glTF loads (or a fake delay).

---

## Lab

1. error if missing file.
2. progress %.

---

## Homework

1. Reflection + loading screenshot.

---

## Quiz (10 min)

1. None.

## Snippet

```jsx
<Suspense fallback={<Loader/>}><Model/></Suspense>
```

---

## Common mistakes

- no fallback, white screen.
- 50MB unbudgeted model.

---

## Board drawings

1. Fallback.

