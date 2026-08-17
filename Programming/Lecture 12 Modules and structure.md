# Lecture 12 — Modules and structure

**Week 12 of 15** · Introduction to Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** `export function lerp` in `math.js`; `import` from `main.js`; serve locally  
**Success check:** lerp runs from a second file on a local server, not as a 400-line paste

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Programming/code/05-clamp.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: split a program without globals | Invariant: a file is a set of named functions; `file://` often blocks modules`

## Board at the end (they photograph this)

```
main.js  ──import──►  math.js   export function lerp …

<script type="module" src="main.js"></script>

python -m http.server     (not file://)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Error screenshot of CORS / module on `file://` | the red text is a photo |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Later: `kernel.js` vs `raster.js`. Today: `math.js` with clamp and lerp. A 400-line file is not simplicity.

**Ask:** Why might `import` fail when you double-click HTML? Wait. Want: `file://` / modules / CORS.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *`export function lerp` in `math.js`; `import` from `main.js`; serve locally*.

**Do not:** One 400-line file 'for simplicity'.

### Minutes 10–12 — Frame

**Say:** `type="module"` and `export function`. Same rule as WebGL demos. Interface: named functions, no hidden globals.

**Ask:** Name two files you expect in Computer Graphics I’s kernel.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Script order vs modules. Modules are deferred and strict.

**Board:** arrows main → math. Export / import syntax.

**Say:** README run line is part of the program. Circular imports: do not.

**Ask:** What is the export syntax for lerp?

**They do:** Write the import line for lerp on paper.

**Do not:** Mix Python syntax into a JS term. Skip the attempt.

### Minutes 35–50 — Show

**Say:** Move clamp/lerp into math.js. Break it on `file://` on purpose if the room allows, then serve.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Three-file mini: math, strings, main. README: how to serve.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Homework: why `file://` breaks modules; one export/import pair. Quiz: export syntax, why serve, two CG I file names.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Split lerp | Forget type=module. |
| 15–35 | Serve | Plant file:// failure. |
| 35–50 | README one line | They copy the command. |
| 50–60 | They add clamp export | Circulate. |

Point them at `Programming/code/05-clamp.html` as the after-class check, not as the lecture.

---

## Lab

1. Three-file mini: math, strings, main.
2. README: how to serve.

---

## Homework

1. Written: why file:// breaks modules.
2. Code: one export/import pair.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
export function lerp(a,b,t){ return a + (b-a)*t; }
```

---

## Extra exercises

See [[Programming/exercises/Week 12]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. One 400-line file 'for simplicity'.
2. Forgetting to serve.

## If we run long, cut

Bundlers. Keep export/import + serve.

## If we run short, add

`import { lerp as mix }` name only.
