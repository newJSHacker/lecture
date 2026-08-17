# Lecture 2 — Buffers and attributes

**Week 2 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** ARRAY_BUFFER, layout  
**Success check:** createBuffer.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: ARRAY_BUFFER, layout | Invariant: CPU fills buffers; GPU runs the shader; P*V*M; CCW`

## Board at the end (they photograph this)

```
attribute loc ↔ stride
Layout.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** GPU memory. CPU arrays are uploaded.

**Ask:** createBuffer? Wait seven seconds. Take two answers.

**Board:** parked strip. Then attribute loc ↔ stride.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *ARRAY_BUFFER, layout*.

**Do not:** Never enabling the attrib.

### Minutes 10–12 — Frame

**Say:** Today’s question: ARRAY_BUFFER, layout. Kernel: ARRAY_BUFFER, layout. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: never enabling the attrib.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** GPU memory. CPU arrays are uploaded.

**Say:** Layout. size, type, stride, offset.

**Say:** Demo. 02 colored triangle, 03 indexed quad.

**Ask:** createBuffer? Wait seven seconds. Take two answers.

**They do:** On paper: Indexed quad.

**Do not:** wrap the first triangle in Three.js. Freeze conventions.

### Minutes 35–50 — Show

**Say:** Live demo: Interleaved pos+color; draw.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Indexed quad.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Indexed quad.; A wrong stride bug then fix.. Homework: Written: stride.; Code: indexed quad.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: ARRAY_BUFFER, layout | Plant the first common mistake. |
| 10–30 | Interleaved pos+color; draw. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. bindBuffer (3)
2. stride 0 meaning (4)
3. location -1 (3)


## Snippet

```js
gl.vertexAttribPointer(loc, 3, gl.FLOAT, false, 0, 0);
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 02]].

---

## Notes you may still need (from the outline)

**1. GPU memory.** CPU arrays are uploaded. Changing every frame is allowed but cost.

**2. Layout.** size, type, stride, offset.

**3. Demo.** 02 colored triangle, 03 indexed quad.

---

## Common mistakes

1. never enabling the attrib.
2. WebGL1 attrib vs in mix.

## If we run long, cut

Demo

## If we run short, add

A wrong stride bug then fix.
