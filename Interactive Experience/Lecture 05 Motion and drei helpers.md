# Lecture 5 — Motion and drei helpers

**Course:** Interactive Experience Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** easing, CameraControls  
**Board first:** spring vs lerp

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

1. Lerp vs spring (react-spring/drei).
2. CameraControls name.
3. Don't both Orbit and scroll-camera without a mode.
4. Kill animations on unmount.
5. GSAP optional, one system.

---

## 1. Feel

Product sites use springs. Games often lerp. Pick one library and stay.

## 2. Camera

CameraControls vs OrbitControls. Conflict is a common bug.

## 3. Cleanup

R3F unmount must dispose geometries if you create them in useLayoutEffect — or use JSX geometries.

## Live coding (60 min)

Spring a camera or a part on click.

---

## Lab

1. mode toggle orbit vs story.
2. dispose note.

---

## Homework

1. Written: spring vs lerp.
2. demo.

---

## Quiz (10 min)

1. conflict (4)
2. dispose (3)
3. one motion system (3)

## Snippet

```jsx
<OrbitControls makeDefault />
```

---

## Common mistakes

- GSAP + spring + CSS all on one property.
- leaking geometries.

---

## Board drawings

1. Modes.

