# Lecture 4 — Uniforms

**Week 4 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** uniforms: mat4, u_time, colors; getUniformLocation once  
**Success check:** they spin a cube with u_time and can say uniform vs attribute

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: CPU values that reach the shader | Invariant: a uniform is constant for one draw; column-major matches kernel.js`

## Board at the end (they photograph this)

```
attribute  =  per vertex     (buffer)
uniform    =  per draw       (CPU sets)

gl.uniformMatrix4fv(loc, false, m);   // false = already column-major

u_time   u_color
location null → name unused or typo
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Last week the color was baked in the shader. Today the CPU talks. PVM is still a name — we rotate in the shader with u_time. Demo 04-rotating-cube.html.

**Ask:** Do you call getUniformLocation inside the fragment? Wait. Want: once after link, cache it.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *mat4, time, colors*.

**Do not:** Row-major by accident.

### Minutes 10–12 — Frame

**Say:** false in uniformMatrix4fv means the array is already column-major. Row-major by accident transposes the world. Missing name → location null, silent no-op.

**Ask:** Uniform vs attribute in one sentence?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Constants for a draw. Change M next week per object; today one object.

**Board:** u_time slider. CPU/GPU arrow.

**Say:** Do not getUniformLocation every pixel. Cache.

**Ask:** What does false mean in uniformMatrix4fv?

**They do:** On paper: two uniforms you would set for a tinted spinner.

**Do not:** Wrap the first triangle in Three.js. Unfreeze conventions.

### Minutes 35–50 — Show

**Say:** Spin with u_time; then a color uniform. Demo 04-rotating-cube.html. Plant row-major. Plant querying location in the rAF hot path.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Pause time with a flag. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: pause time; two objects different uniforms extra. Homework: uniform vs attribute; time. Quiz: vs attribute, column-major, missing name.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | u_color uniform | Plant forgot useProgram before set. |
| 10–30 | u_time spin | Plant row-major mat4. |
| 30–45 | Cache locations | Plant getUniformLocation in draw. |
| 45–60 | They pause time | Circulate. |

Point them at `WebGL Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. Pause time.
2. Two objects different uniforms extra.

---

## Homework

1. Written: uniform vs attribute.
2. Code: time.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
gl.uniform1f(gl.getUniformLocation(prog,'u_time'), t);
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 04]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. row-major by accident.
2. getUniformLocation every pixel.

## If we run long, cut

Full PVM today. Keep time + color + column-major.

## If we run short, add

Two objects, different color uniforms.
