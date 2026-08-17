# Lecture 2 — APIs and keys

**Week 2 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** browser → your proxy → vendor; mock is first-class; key never in the repo  
**Success check:** they can fetch('/api/complete') against a mock or proxy and show .env is not in git

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/01-proxy-mock.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: a proxy or an honest mock | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
browser  →  POST /api/complete  →  proxy  →  vendor
                ↑
              mock JSON is a valid lab

key in GitHub  =  fail
unbounded spend  =  fail
ToS: student work, not resale
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** The browser never sees the vendor key. Same as any production app. If there is no budget, a mock server is the lab — architecture still counts. Demo 01-proxy-mock.html.

**Ask:** Does a mock mean you skipped the course? Wait. Want: no — you still have a proxy shape.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *server proxy*.

**Do not:** Key in GitHub.

### Minutes 10–12 — Frame

**Say:** Error states and timeout. No CDN vendor SDK required. Read ToS at teaching level — we are not lawyers.

**Ask:** What happens on 401 from the proxy?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Three boxes. Key lives in the middle box.

**Board:** fetch POST. Mock returns canned JSON.

**Say:** .gitignore .env. Unbounded student spend is a plant.

**Ask:** Why not VITE_OPENAI_KEY?

**They do:** On paper: the three boxes and where the key sits.

**Do not:** Put API keys in client JS. Skip integrity.

### Minutes 35–50 — Show

**Say:** fetch('/api/complete') against mock. Plant key in the HTML. Plant infinite retries. Timeout.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Button → mock complete → show JSON. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: error states; timeout. Homework: why the key is not in the client. Quiz: proxy, mock OK, no GitHub key.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Three boxes | Plant client key. |
| 15–40 | Mock fetch | Plant real key in repo. |
| 40–55 | Timeout / error | Unbounded spend plant. |
| 55–60 | They hide .env | Circulate. |

Point them at `AI for Interactive Graphics/code/01-proxy-mock.html` as the after-class check, not as the lecture.

---

## Lab

1. error states.
2. timeout.

---

## Homework

1. Written: why proxy.
2. code.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
const r = await fetch('/api/complete', { method: 'POST', body: JSON.stringify({ prompt }) });
```

---

## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 02]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. key in GitHub.
2. unbounded student spend.

## If we run long, cut

ToS law. Keep proxy + mock.

## If we run short, add

Timeout UI.
