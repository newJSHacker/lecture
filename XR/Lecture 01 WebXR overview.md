# Lecture 1 — WebXR overview

**Week 1 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** immersive-vr / immersive-ar vs inline; feature detect; lab fallback required  
**Success check:** they can run isSessionSupported and screenshot an inline fallback — no headset lottery

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `XR/code/01-detect.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: detect + inline; headset is extra evidence | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
inline          always the lab deliverable
immersive-vr    headset extra
immersive-ar    often missing on desktop

navigator.xr?.isSessionSupported('immersive-vr')
HTTPS / localhost     user gesture     no CDN
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** This is interaction design + the WebXR API, not a Unity degree. If it cannot run inline in the lab, it is not the weekly deliverable. Headset is extra evidence — never a lottery for the grade.

**Ask:** If there is no Quest in the room, did you fail week 1? Wait. Want: no — inline + detect.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *immersive vs inline*.

**Do not:** Quest-only homework with no fallback.

### Minutes 8–12 — Frame

**Say:** Three.js XRButton wraps requestSession. Camera permission is AR later. Secure context: localhost or HTTPS. http:// LAN IP is a plant.

**Ask:** Who must grant the session — a script on load, or a user gesture?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Session types. Draw three boxes: inline, vr, ar.

**Board:** detect snippet. Circle fallback.

**Say:** TA headset video is evidence, not a substitute for student session code.

**Ask:** Why HTTPS?

**They do:** On paper: detect + what you screenshot if xr is undefined.

**Do not:** Require a headset to pass week 1. Skip the desktop fallback.

### Minutes 35–50 — Show

**Say:** Detect modes; inline Three scene; XRButton if available. Plant Quest-only homework. Plant http://. Demo XR/code/01-detect.html.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** isSessionSupported + a fallback sentence on the page. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: HTTPS note; fallback screenshot. Homework: session types. Quiz: immersive-vr, HTTPS, gesture.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Detect xr | Plant Quest-only. |
| 10–30 | Inline scene | Plant no fallback. |
| 30–45 | Secure context | Plant LAN http. |
| 45–60 | They write the fallback line | Circulate. |

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

None this meeting.


## Snippet

```js
const ok = await navigator.xr?.isSessionSupported('immersive-vr');
```

---

## Extra exercises

See [[XR/exercises/Week 01]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Quest-only homework with no fallback.
2. http:// LAN IP without secure context.

## If we run long, cut

Permissions deep-dive. Keep detect + fallback.

## If we run short, add

Fallback screenshot on the board as a checklist item.
