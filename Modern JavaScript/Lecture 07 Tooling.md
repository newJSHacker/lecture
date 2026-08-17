# Lecture 7 — Tooling

**Week 7 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** npm, vite, scripts  
**Success check:** npm init.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/07-loop.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: npm, vite, scripts | Invariant: one binding, one module, no hidden globals`

## Board at the end (they photograph this)

```
package.json scripts
Scripts.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Why a bundler. Import maps vs Vite.

**Ask:** npm init? Wait seven seconds. Take two answers.

**Board:** parked strip. Then package.json scripts.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *npm, vite, scripts*.

**Do not:** Committing node_modules.

### Minutes 10–12 — Frame

**Say:** Today’s question: npm, vite, scripts. Kernel: npm, vite, scripts. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Committing node_modules.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why a bundler. Import maps vs Vite.

**Say:** package.json. scripts, dependencies vs devDependencies.

**Say:** Lockfile. Commit it.

**Ask:** npm init? Wait seven seconds. Take two answers.

**They do:** On paper: Add a script test that runs node asserts.

**Do not:** install a new bundler mid-lecture. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Scaffold vite vanilla; import the math module; run dev.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Add a script test that runs node asserts.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Add a script test that runs node asserts.; README.. Homework: Written: why lockfile.; Code: vite project in repo subfolder.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: npm, vite, scripts | Plant the first common mistake. |
| 10–30 | Scaffold vite vanilla; import the math module; run dev. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. node_modules in git? (3)
2. dev vs build (4)
3. lockfile (3)


## Snippet

```json
{ "scripts": { "dev": "vite" } }
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 07]].

---

## Notes you may still need (from the outline)

**1. Why a bundler.** Import maps vs Vite. Course: Vite for Semester 2+ projects that need it. Static serve still OK for tiny labs.

**2. package.json.** scripts, dependencies vs devDependencies.

**3. Lockfile.** Commit it. Reproducible lab machines.

---

## Common mistakes

1. Committing node_modules.
2. Global npm installs as the only method.

## If we run long, cut

Lockfile

## If we run short, add

README.
