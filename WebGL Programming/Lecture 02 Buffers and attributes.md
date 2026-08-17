# Lecture 2 — Buffers and attributes

**Week 2 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** ARRAY_BUFFER, vertexAttribPointer layout, ELEMENT_ARRAY_BUFFER  
**Success check:** they can createBuffer, upload, enable the attrib, and draw an indexed quad

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: layout you can debug | Invariant: CPU arrays are dead until uploaded; layout is size/type/stride/offset`

## Board at the end (they photograph this)

```
bind ARRAY_BUFFER → bufferData → enableVertexAttribArray
vertexAttribPointer(loc, size, FLOAT, false, stride, offset)

stride 0  =  tightly packed
interleaved pos+color: stride 24, color offset 12

ELEMENT_ARRAY_BUFFER → drawElements
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Last time: a triangle that was already clip. Today the GPU must be told how bytes become a_position. A wrong stride is a Picasso, not a math bug.

**Ask:** What does stride 0 mean? Wait. Want: tightly packed; GPU infers from size*sizeof(type).

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *ARRAY_BUFFER, layout*.

**Do not:** Never enabling the attrib.

### Minutes 10–12 — Frame

**Say:** createBuffer, bindBuffer, bufferData STATIC_DRAW. Location −1 means the name is unused or misspelled. Demo 02 colored triangle, 03 indexed quad.

**Ask:** Why enableVertexAttribArray?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** CPU Float32Array is not GPU memory until bufferData.

**Board:** interleaved vs separate. Numbers: 3 floats pos + 3 color = 24 bytes.

**Say:** Indexed quad: four verts, six indices. UNSIGNED_SHORT.

**Ask:** bindBuffer — which target for indices?

**They do:** On paper: pointer for interleaved pos+color. Two lines.

**Do not:** Wrap the first triangle in Three.js. Unfreeze conventions.

### Minutes 35–50 — Show

**Say:** Interleaved pos+color from 02-colored-triangle.html then 03-indexed-quad.html. Plant never enabling the attrib. Plant WebGL1 attribute vs in mix.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Indexed quad. Then a wrong stride, then fix. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: indexed quad + stride bug. Homework: stride paragraph; indexed quad. Quiz: bindBuffer, stride 0, location −1.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | createBuffer + bind | Plant forgot bind. |
| 10–30 | Interleaved pos+color; draw | Plant stride 0 when data is interleaved. |
| 30–45 | drawElements quad | UNSIGNED_BYTE by accident. |
| 45–60 | They index a quad | Circulate. |

Point them at `WebGL Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. Indexed quad.
2. A wrong stride bug then fix.

---

## Homework

1. Written: stride.
2. Code: indexed quad.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
gl.vertexAttribPointer(loc, 3, gl.FLOAT, false, 0, 0);
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 02]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. never enabling the attrib.
2. WebGL1 attrib vs in mix.

## If we run long, cut

VAO theory dump. Keep pointer + indexed quad.

## If we run short, add

A wrong stride bug then fix, on purpose.
