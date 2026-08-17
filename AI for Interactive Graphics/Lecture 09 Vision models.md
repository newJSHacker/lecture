# Lecture 9 — Vision models

**Course:** AI for Interactive Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** image in, labels out  
**Board first:** frame → API → HUD

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

1. Send a canvas snapshot (downscaled) to a mock/real vision endpoint.
2. Don't stream 4k 30Hz.
3. Privacy: no faces without consent.
4. Throttle.
5. Button, not a silent loop.

---

## 1. Snapshot

Capture the canvas (or a crop) at 256px. Send to a mock or real vision endpoint. Show the label on the HUD.

## 2. Use

Describe a part, detect a QR, accessibility captions.

## 3. Cost/latency

One shot on button, not every frame.

## Live coding (60 min)

Button: capture 256px snapshot; show returned label (mock OK).

---

## Lab

1. privacy note.
2. throttle.

---

## Homework

1. Written: why not every frame.
2. demo.

---

## Quiz (10 min)

1. downscale (3)
2. privacy (4)
3. throttle (3)

## Snippet

```js
canvas.toBlob(cb, 'image/jpeg', 0.7);
```

---

## Common mistakes

- webcam to vendor 30fps class demo on classmates.
- 4k PNG.

---

## Board drawings

1. Snapshot button.

