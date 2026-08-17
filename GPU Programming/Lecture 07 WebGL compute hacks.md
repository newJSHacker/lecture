# Lecture 7 — WebGL compute hacks

**Week 7 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** histogram, reduce names  
**Success check:** Mipmap as a reduction.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: histogram, reduce names | Invariant: data lives where the kernel runs`

## Board at the end (they photograph this)

```
mip as reduce
Pyramid.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Reduce. Average luminance for auto-exposure is a mip chain.

**Ask:** Mipmap as a reduction? Wait seven seconds. Take two answers.

**Board:** parked strip. Then mip as reduce.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *histogram, reduce names*.

**Do not:** CPU loop over getImageData 1080p.

### Minutes 10–12 — Frame

**Say:** Today’s question: histogram, reduce names. Kernel: histogram, reduce names. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: CPU loop over getImageData 1080p.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Reduce. Average luminance for auto-exposure is a mip chain.

**Say:** Atomics. WebGL2 has almost none for FS.

**Say:** Readback. Async pixel pack names.

**Ask:** Mipmap as a reduction? Wait seven seconds. Take two answers.

**They do:** On paper: show mip debug.

**Do not:** require CUDA. WebGL/WebGPU in the browser.

### Minutes 35–50 — Show

**Say:** Live demo: Auto-exposure-ish: downsample a scene tex; log average; feed exposure.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** show mip debug.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: show mip debug.; don't readPixels every frame.. Homework: Written: reduce.; demo or Three.js + explanation.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: histogram, reduce names | Plant the first common mistake. |
| 10–30 | Auto-exposure-ish: downsample a scene tex; log average; feed exposure. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `GPU Programming/code/01-pong.html` as the after-class check, not as the lecture.

---

## Lab

1. show mip debug.
2. don't readPixels every frame.

---

## Homework

1. Written: reduce.
2. demo or Three.js + explanation.

---

## Quiz next meeting (they hear this now)

1. mip reduce (4)
2. why atomics (3)
3. stall (3)


## Snippet

```js
gl.generateMipmap(gl.TEXTURE_2D);
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 07]].

---

## Notes you may still need (from the outline)

**1. Reduce.** Average luminance for auto-exposure is a mip chain. Teaching: generateMips or blit down.

**2. Atomics.** WebGL2 has almost none for FS. WebGPU compute has atomics. That's a reason to move.

**3. Readback.** Async pixel pack names. Stall if you wait.

---

## Common mistakes

1. CPU loop over getImageData 1080p.
2. atomics in a blog copied to WebGL1.

## If we run long, cut

Readback

## If we run short, add

don't readPixels every frame.
