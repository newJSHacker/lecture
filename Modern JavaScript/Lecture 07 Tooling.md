# Lecture 7 — Tooling

**Week 7 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** package.json scripts; Vite for apps that need a bundler; commit the lockfile  
**Success check:** they npm init, add a test script that runs node asserts, and can say why node_modules is not in git

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/07-loop.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: one project a TA can npm install && npm test | Invariant: reproducible install is the lockfile; node_modules is generated; no CDN as a bundler`

## Board at the end (they photograph this)

```
package.json
  scripts: { "dev": "vite", "test": "node test.js" }
  dependencies vs devDependencies

package-lock.json    COMMIT
node_modules/        .gitignore

static serve still OK for tiny labs
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Modules in the browser needed a server. Apps with many files need a bundler. Course policy: Vite when you need it; python -m http.server when you do not. Installing a new bundler mid-lecture is forbidden.

**Ask:** Do we commit node_modules? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *npm, vite, scripts*.

**Do not:** Committing node_modules.

### Minutes 10–12 — Frame

**Say:** npm init. scripts are the API for TAs. lockfile = reproducible lab machines. Global npm installs as the only method is a smell. Import maps named — Vite is what we scaffold today.

**Ask:** dev vs build — which command do they run in class?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why a bundler: many imports, later TS. Tiny labs still static-serve.

**Board:** scripts, lockfile, gitignore node_modules.

**Say:** Scaffold vite vanilla; import last week’s math module; npm run dev. No CDN script tags.

**Ask:** Why commit the lockfile?

**They do:** On paper: a scripts block with dev and test. Write .gitignore one line: node_modules.

**Do not:** Install a new bundler mid-lecture. Use a CDN.

### Minutes 35–50 — Show

**Say:** Scaffold vite vanilla; import the math module; run dev. Plant committing node_modules. Plant a CDN <script> ‘just this once’. There is no Vite HTML in code/ — 07-loop.html is a later dt demo, not today’s scaffold.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Add a script test that runs node asserts on lerp. Eight minutes. README: npm install, npm test, npm run dev.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: test script + README. Homework: why lockfile; vite project in a repo subfolder. Quiz: node_modules in git?, dev vs build, lockfile. Midterm next week: weeks 1–7.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | npm init + gitignore | Plant node_modules add. |
| 10–30 | vite scaffold + import math.js | Plant CDN. Remove it. |
| 30–45 | scripts.test = node test.js | They see PASS. |
| 45–60 | They write README serve/dev | Circulate. |

Point them at `Modern JavaScript/code/07-loop.html` as the after-class check, not as the lecture.

---

## Lab

1. Add a script test that runs node asserts.
2. README.

---

## Homework

1. Written: why lockfile.
2. Code: vite project in repo subfolder.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```json
{ "scripts": { "dev": "vite" } }
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 07]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Committing node_modules.
2. Global npm installs as the only method.

## If we run long, cut

Lockfile sermon if init is slow. Keep scripts + gitignore.

## If we run short, add

README: three commands.
