# Lecture 3 — Modules

**Week 3 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** named export / import; type=module; serve the folder  
**Success check:** they split lerp into math.js and import it; they can say why file:// failed

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/08-modules.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: two files, one named export | Invariant: a file is an API; no hidden globals; file:// often breaks modules`

## Board at the end (they photograph this)

```
// math.js
export function lerp(a, b, t) { return a + (b-a)*t; }

// main.js   <script type="module" src="main.js">
import { lerp } from './math.js';

file://  →  often fails     python -m http.server
named exports = course policy
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Optional: console CORS / module error on file:// | photograph the error; do not draw Chrome |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** If it is not a module with a test, it is not a kernel. Today the file boundary is the API. Mixing a CDN script until it ‘works’ is how secrets and version skew arrive.

**Ask:** Why did import fail when you double-clicked the HTML? Wait. Want: file:// / modules / CORS.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *export import*.

**Do not:** Mixing remote script URLs with local modules until it 'works'.

### Minutes 10–12 — Frame

**Say:** Named exports for kernels. Default is optional, not the policy. Browsers need type=module and a local server. Bundlers preview — Vite is next week, not today.

**Ask:** Relative path: './math.js' — may you omit the .js in the browser? Want: no, not without a bundler.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** export is the public list. import names what you take. Nothing else leaks.

**Board:** two files, one arrow between them labeled lerp.

**Say:** Serve: python -m http.server or npx serve in the folder. No CDN. No remote script URL glued to a local import.

**Ask:** Named vs default — which does this course write for kernels?

**They do:** On paper: three modules — math.js (lerp, clamp), io.js (name only), main.js imports both.

**Do not:** Install a new bundler mid-lecture. Use a CDN.

### Minutes 35–50 — Show

**Say:** Split lerp into math.js; import in main.js. Plant file://. Read the error. Then serve. Demo Modern JavaScript/code/08-modules.html is the reminder page — you still write the two files live.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Three modules on disk. README: how to serve. Eight minutes for lerp+import even if io.js is a stub.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: three modules + README serve. Homework: ESM vs classic script; import clamp. Quiz: export syntax, why serve, named vs default.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | type=module + file:// | Plant double-click. Error out loud. |
| 10–30 | math.js lerp + import | Plant missing .js or wrong path. |
| 30–45 | http.server | They reload; import works. |
| 45–60 | They add clamp export | Circulate. No CDN. |

Point them at `Modern JavaScript/code/08-modules.html` as the after-class check, not as the lecture.

---

## Lab

1. Three modules.
2. README serve.

---

## Homework

1. Written: ESM vs classic script.
2. Code: import.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
import { lerp } from './math.js';
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 03]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Mixing remote script URLs with local modules until it 'works'.

## If we run long, cut

Bundlers preview. Keep named export + serve.

## If we run short, add

README serve: one command, one URL.
