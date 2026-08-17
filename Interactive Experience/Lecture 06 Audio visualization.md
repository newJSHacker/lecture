# Lecture 6 — Audio visualization

**Course:** Interactive Experience Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** analyser → scale  
**Board first:** byte frequency → instance scale

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

1. User-gesture AudioContext.
2. AnalyserNode.
3. Drive instanced mesh or bars.
4. Don't autoplay.
5. Same as Interactive Web, now in 3D.

---

## 1. Gesture

Browsers block autoplay. A Play button is the lab.

## 2. Data

fftSize. Map bins to instances. Cap N.

## 3. a11y

Don't rely on audio only; show a mute and a visual that works silent.

## Live coding (60 min)

Play a short licensed loop; 32 bars as boxes.

---

## Lab

1. mute.
2. fallback still image.

---

## Homework

1. Written: autoplay policy.
2. demo.

---

## Quiz (10 min)

1. why click first (4)
2. fftSize (3)
3. silent path (3)

## Snippet

```js
const ctx = new AudioContext(); analyser.fftSize = 64;
```

---

## Common mistakes

- autoplay surprise.
- copyrighted full songs as the asset without license.

---

## Board drawings

1. Bars in 3D.

