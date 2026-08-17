# Lecture 1 — WebXR overview

**Week 1 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** immersive vs inline  
**Success check:** Feature detect `navigator.xr`.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `XR/code/01-detect.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: immersive vs inline | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
session types: vr / ar
Session boxes.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** What WebXR is. Browser API for VR/AR sessions.

**Ask:** Feature detect `navigator.xr`? Wait seven seconds. Take two answers.

**Board:** parked strip. Then session types: vr / ar.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *immersive vs inline*.

**Do not:** Quest-only homework with no fallback.

### Minutes 8–12 — Frame

**Say:** Today’s question: immersive vs inline. Kernel: immersive vs inline. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Quest-only homework with no fallback.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** What WebXR is. Browser API for VR/AR sessions.

**Say:** Hardware. Quest, desktop HMD, phones (AR).

**Say:** Permissions. Camera for AR.

**Ask:** Feature detect `navigator.xr`? Wait seven seconds. Take two answers.

**They do:** On paper: localhost HTTPS note.

**Do not:** require a headset to pass week 1. Desktop fallback.

### Minutes 35–50 — Show

**Say:** Live demo: Detect XR; show session modes; start inline Three.js scene with XRButton if available.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** localhost HTTPS note.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: localhost HTTPS note.; fallback screenshot.. Homework: Written: session types.; detect page.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: immersive vs inline | Plant the first common mistake. |
| 10–30 | Detect XR; show session modes; start inline Three.js scene with XRButton if available. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `XR/code/01-detect.html` as the after-class check, not as the lecture.

---

## Lab

1. localhost HTTPS note.
2. fallback screenshot.

---

## Homework

1. Written: session types.
2. detect page.

---

## Quiz next meeting (they hear this now)

1. immersive-vr (3)
2. why HTTPS (4)
3. gesture (3)


## Snippet

```js
const ok = await navigator.xr?.isSessionSupported('immersive-vr');
```

---

## Extra exercises

See [[XR/exercises/Week 01]].

---

## Notes you may still need (from the outline)

**1. What WebXR is.** Browser API for VR/AR sessions. Three.js `XRButton` / `WebXRManager` wrap it. This course is **interaction design + API**, not a Unity VR degree.

**2. Hardware.** Quest, desktop HMD, phones (AR). Labs need a **non-headset path**: inline canvas + documented emulator or video of a TA headset.

**3. Permissions.** Camera for AR. User gesture to `requestSession`.

---

## Common mistakes

1. Quest-only homework with no fallback.
2. http:// LAN IP without secure context.

## If we run long, cut

Permissions

## If we run short, add

fallback screenshot.
