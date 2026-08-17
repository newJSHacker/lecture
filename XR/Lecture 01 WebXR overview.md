# Lecture 1 — WebXR overview

**Course:** Virtual and Augmented Reality  
**Time:** 75 min lecture + 60 min live coding  
**This week:** immersive vs inline  
**Board first:** session types: vr / ar

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

1. Feature detect `navigator.xr`.
2. immersive-vr vs immersive-ar vs inline.
3. HTTPS / localhost.
4. Don't require a headset on day 1 — emulator/name the fallback.
5. Safety: space to move.

---

## 1. What WebXR is

Browser API for VR/AR sessions. Three.js `XRButton` / `WebXRManager` wrap it. This course is **interaction design + API**, not a Unity VR degree.

## 2. Hardware

Quest, desktop HMD, phones (AR). Labs need a **non-headset path**: inline canvas + documented emulator or video of a TA headset.

## 3. Permissions

Camera for AR. User gesture to `requestSession`.

## Live coding (60 min)

Detect XR; show session modes; start inline Three.js scene with XRButton if available.

---

## Lab

1. localhost HTTPS note.
2. fallback screenshot.

---

## Homework

1. Written: session types.
2. detect page.

---

## Quiz (10 min)

1. immersive-vr (3)
2. why HTTPS (4)
3. gesture (3)

## Snippet

```js
const ok = await navigator.xr?.isSessionSupported('immersive-vr');
```

---

## Common mistakes

- Quest-only homework with no fallback.
- http:// LAN IP without secure context.

---

## Board drawings

1. Session boxes.

