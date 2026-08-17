# Lecture 2 — APIs and keys

**Week 2 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** server proxy  
**Success check:** A tiny proxy (Node/fetch) that holds the key.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/01-proxy-mock.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: server proxy | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
browser → your server → vendor
Proxy box.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Architecture. The browser never sees the vendor key.

**Ask:** A tiny proxy (Node/fetch) that holds the key? Wait seven seconds. Take two answers.

**Board:** parked strip. Then browser → your server → vendor.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *server proxy*.

**Do not:** Key in GitHub.

### Minutes 10–12 — Frame

**Say:** Today’s question: server proxy. Kernel: server proxy. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: key in GitHub.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Architecture. The browser never sees the vendor key.

**Say:** Mock. If no budget: a mock server returns canned JSON/images.

**Say:** ToS. Read the vendor policy.

**Ask:** A tiny proxy (Node/fetch) that holds the key? Wait seven seconds. Take two answers.

**They do:** On paper: error states.

**Do not:** put API keys in client JS. Do not skip integrity.

### Minutes 35–50 — Show

**Say:** Live demo: fetch('/api/complete') against a mock or real proxy; display text.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** error states.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: error states.; timeout.. Homework: Written: why proxy.; code.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: server proxy | Plant the first common mistake. |
| 10–30 | fetch('/api/complete') against a mock or real proxy; display text. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. who holds the key (4)
2. mock allowed? (3)
3. rate limit (3)


## Snippet

```js
const r = await fetch('/api/complete', { method: 'POST', body: JSON.stringify({ prompt }) });
```

---

## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 02]].

---

## Notes you may still need (from the outline)

**1. Architecture.** The browser never sees the vendor key. Same as any production app.

**2. Mock.** If no budget: a mock server returns canned JSON/images. The **client architecture** is the lab.

**3. ToS.** Read the vendor policy. Student work, not resale.

---

## Common mistakes

1. key in GitHub.
2. unbounded student spend.

## If we run long, cut

ToS

## If we run short, add

timeout.
