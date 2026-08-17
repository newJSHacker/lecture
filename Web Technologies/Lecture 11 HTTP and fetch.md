# Lecture 11 — HTTP and fetch

**Week 11 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** fetch('data.json'); response.ok; await json(); no secrets  
**Success check:** they load local JSON and render a list; they can explain 404 vs throw

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Web Technologies/code/09-fetch.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: data in, DOM out | Invariant: fetch talks HTTP; keys never in the frontend; local JSON is enough this week`

## Board at the end (they photograph this)

```
const res = await fetch('data.json');
if (!res.ok) throw new Error(res.status);
const data = await res.json();

GET local file   404 → !ok
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** AI course and capstone will fetch. Today: a local JSON file served from this folder. CORS and file:// will bite — we serve.

**Ask:** Does fetch throw on 404? Wait. Want: no — you check res.ok.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *JSON APIs*.

**Do not:** Ignoring !ok.

### Minutes 10–12 — Frame

**Say:** async/await preview (Modern JS owns the deep version). try/catch. No API keys. No CDN.

**Ask:** Why serve instead of file://?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Request, response, body. JSON.parse is what .json() does.

**Board:** ok check. Then map to DOM from Lecture 9.

**Say:** GET is default. POST named, not used without a server.

**Ask:** What is in data.json if the file is an array of {name}?

**They do:** On paper: the three lines: fetch, ok, json.

**Do not:** Lecture HTML as a visual design tool. Use a CDN.

### Minutes 35–50 — Show

**Say:** Load people.json, render ul. Demo 09-fetch.html. Plant file:// fail. Plant ignoring !ok.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Render names from JSON. Handle 404 with a visible message. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: fetch + list + 404 message. Homework: why file:// breaks. Quiz: res.ok, await json, no keys.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | fetch local | Plant file://. |
| 15–40 | ok + json | Plant missing ok. |
| 40–55 | Render list | They connect Lecture 9. |
| 55–60 | They add 404 text | Circulate. |

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

None this meeting.


## Snippet

```js
const data = await (await fetch('data.json')).json();
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 11]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Ignoring !ok.
2. Hardcoding GitHub tokens in the page — never.

## If we run long, cut

Auth headers. Keep local JSON + ok.

## If we run short, add

AbortController name.
