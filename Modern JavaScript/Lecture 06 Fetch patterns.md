# Lecture 6 — Fetch patterns

**Week 6 of 15** · Modern JavaScript Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** fetch JSON; AbortController; no API keys in the frontend  
**Success check:** they abort a previous search fetch and can say where a key must not live

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Modern JavaScript/code/06-closure.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: GET local JSON, cancel in-flight, never ship a key | Invariant: fetch talks HTTP; a race without abort is a stale answer; secrets are not in git`

## Board at the end (they photograph this)

```
const c = new AbortController();
fetch(url, { signal: c.signal });
c.abort();                 // new search

if (!res.ok) throw …       // 404 is not a throw from fetch

KEY SKULL   —  not in source, not in the bundle
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** AI course and capstone will fetch. Today: local data.json, abort on a new search, and a skull on the board for keys. A CDN or a pasted token is a fail.

**Ask:** Does fetch throw on HTTP 404? Wait. Want: no — check res.ok.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *JSON, abort, cache*.

**Do not:** Keys in source.

### Minutes 10–12 — Frame

**Say:** GET JSON is the lab. POST to a local mock is extra. Headers named. Cache: the browser may reuse GET — we do not invent cache timings. Abort cancels the previous in-flight request.

**Ask:** Where do API keys live? Want: server / env / never the repo.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Request, response, body. .json() parses. Serve — file:// breaks fetch the same way it broke modules.

**Board:** AbortController. Race: slow response arrives after a new query.

**Say:** Secrets. No keys in source. AI course will repeat this. Handle 500 with a visible message.

**Ask:** What does abort() do to an await fetch?

**They do:** On paper: search-as-you-type: abort previous, then fetch. Three boxes.

**Do not:** Install a new bundler mid-lecture. Use a CDN.

### Minutes 35–50 — Show

**Say:** Search-as-you-type fake: abort previous. Serve Modern JavaScript/code/ and fetch data.json (see 04-async.html). Plant a key in a const. Erase it. Plant ignoring !ok.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Abort on a second button click. Handle 404/500 with text on the page. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: abort + handle 500; optional POST to a local mock. Homework: why keys not in git; abort code. Quiz: AbortController, where keys live, GET cache name.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | fetch data.json + ok | Plant file:// and missing ok. |
| 10–30 | AbortController | Plant race: late response overwrites. |
| 30–45 | Key skull | Plant a fake key. Delete. No CDN. |
| 45–60 | They abort on second click | Circulate. |

Point them at `Modern JavaScript/code/06-closure.html` as the after-class check, not as the lecture.

---

## Lab

1. POST to a local mock extra.
2. Handle 500.

---

## Homework

1. Written: why keys not in git.
2. Code: abort.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
const c = new AbortController();
fetch(url, { signal: c.signal });
```

---

## Extra exercises

See [[Modern JavaScript/exercises/Week 06]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Keys in source.
2. No abort, race of answers.

## If we run long, cut

POST mock if abort is still shaky. Keep GET + abort + no keys.

## If we run short, add

Handle 500 with a visible status.
