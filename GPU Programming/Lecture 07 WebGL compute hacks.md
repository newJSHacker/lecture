# Lecture 7 — WebGL compute hacks

**Week 7 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** reduce: mip chain as average; histogram named; no getImageData 1080p loop  
**Success check:** they can treat generateMipmap (or blit down) as a reduce and avoid readPixels every frame

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: a pyramid, not a readback | Invariant: WebGL FS has almost no atomics; a CPU histogram of the canvas is not GPGPU`

## Board at the end (they photograph this)

```
scene tex
  → mip 1
  → mip 2
  → …  1×1  ≈  mean luminance

atomics:  WebGL2 FS ≈ none;  WebGPU compute has them
readback: async pack name; stall if you wait
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Average luminance for auto-exposure is a mip chain. Teaching: generateMips or blit down. CPU loop over getImageData at 1080p is the plant. Atomics in a WebGL1 blog post do not port.

**Ask:** Does generateMipmap reduce? Wait. Want: yes, as a teaching reduce.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *histogram, reduce names*.

**Do not:** CPU loop over getImageData 1080p.

### Minutes 10–12 — Frame

**Say:** Show mip debug. Auto-exposure-ish: log average, feed exposure — still a named pass. Do not readPixels every frame. WebGPU atomics are a reason to move after the midterm.

**Ask:** Why almost no atomics in WebGL FS?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Pyramid on the board. 1×1 is the reduce.

**Board:** mip as reduce. Circle no getImageData.

**Say:** Histogram is a name; mip is the lab.

**Ask:** What stalls a frame?

**They do:** On paper: the pyramid sizes (power of two sketch).

**Do not:** Require CUDA. Stay in the browser (WebGL/WebGPU).

### Minutes 35–50 — Show

**Say:** Downsample a scene tex; log average; feed exposure. Plant getImageData 1080p. Plant readPixels every frame. Mip debug view.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Show mip debug. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: mip debug + don't readPixels every frame. Homework: reduce paragraph; demo. Quiz: mip reduce, why atomics, stall. Midterm next week.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Mip pyramid | Plant getImageData loop. |
| 10–30 | 1×1 as mean | Plant readPixels every frame. |
| 30–45 | Exposure feed | Named, not a fps claim. |
| 45–60 | They debug mips | Circulate. |

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

None this meeting.


## Snippet

```js
gl.generateMipmap(gl.TEXTURE_2D);
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 07]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. CPU loop over getImageData 1080p.
2. atomics in a blog copied to WebGL1.

## If we run long, cut

A real histogram SSBO. Keep mip reduce + no stall.

## If we run short, add

Async pixel pack as a name.
