# Lecture 11 — HTTP and fetch

**Week 11 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** JSON APIs  
**Success check:** fetch a JSON URL.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Web Technologies/code/09-fetch.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: JSON APIs | Invariant: the browser requests, parses, then paints`

## Board at the end (they photograph this)

```
fetch → then/await → json
Request arrow.
JSON list.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** fetch. Returns a Promise.

**Ask:** fetch a JSON URL? Wait seven seconds. Take two answers.

**Board:** parked strip. Then fetch → then/await → json.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *JSON APIs*.

**Do not:** Ignoring !ok.

### Minutes 10–12 — Frame

**Say:** Today’s question: JSON APIs. Kernel: JSON APIs. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Ignoring !ok.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** fetch. Returns a Promise.

**Say:** Status. `if (!res.ok) throw`.

**Say:** CORS. A browser policy.

**Ask:** fetch a JSON URL? Wait seven seconds. Take two answers.

**They do:** On paper: Error state in the UI.

**Do not:** lecture HTML as a visual design tool. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Load `/data.json` with three records; render a list.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Error state in the UI.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Error state in the UI.; Loading text.. Homework: Written: CORS in one paragraph.; Code: fetch + render + error.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: JSON APIs | Plant the first common mistake. |
| 10–30 | Load `/data.json` with three records; render a list. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Web Technologies/code/09-fetch.html` as the after-class check, not as the lecture.

---

## Lab

1. Error state in the UI.
2. Loading text.

---

## Homework

1. Written: CORS in one paragraph.
2. Code: fetch + render + error.

---

## Quiz next meeting (they hear this now)

1. res.ok (3)
2. JSON.parse vs res.json (3)
3. Why file:// fetch fails (4)


## Snippet

```js
const data = await (await fetch('data.json')).json();
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 11]].

---

## Notes you may still need (from the outline)

**1. fetch.** Returns a Promise. async/await in this week at teaching level; Modern JS goes deeper.

**2. Status.** `if (!res.ok) throw`. Students skip this and parse an HTML 404 as JSON.

**3. CORS.** A browser policy. Local files and foreign APIs fail. Use a local JSON file served by a static server.

---

## Common mistakes

1. Ignoring !ok.
2. Hardcoding GitHub tokens in the page — never.

## If we run long, cut

CORS

## If we run short, add

Loading text.
