# Lecture 1 — How the web works

**Week 1 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** URL, HTTP, browser  
**Success check:** Name client and server.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `Web Technologies/code/01-skeleton.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: URL, HTTP, browser | Invariant: the browser requests, parses, then paints`

## Board at the end (they photograph this)

```
client → HTTP → server → HTML
Client-server.
URL anatomy.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** The browser is an engine. It requests documents, parses HTML, applies CSS, runs JS.

**Ask:** client and server? Wait seven seconds. Take two answers.

**Board:** parked strip. Then client → HTTP → server → HTML.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *URL, HTTP, browser*.

**Do not:** Teaching HTML as Photoshop.

### Minutes 8–12 — Frame

**Say:** Today’s question: URL, HTTP, browser. Kernel: URL, HTTP, browser. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Teaching HTML as Photoshop.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** The browser is an engine. It requests documents, parses HTML, applies CSS, runs JS.

**Say:** HTTP. Request/response.

**Say:** DevTools. Elements, Console, Network.

**Ask:** client and server? Wait seven seconds. Take two answers.

**They do:** On paper: Draw the request cycle for loading index.html + a CSS file.

**Do not:** lecture HTML as a visual design tool. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: Fetch this course README via GitHub raw or a local server; show status codes by visiting a missing path.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Draw the request cycle for loading index.html + a CSS file.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Draw the request cycle for loading index.html + a CSS file.; Log document.title.. Homework: Written: 200 vs 404.; A local folder served with python -m http.server.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: URL, HTTP, browser | Plant the first common mistake. |
| 10–30 | Fetch this course README via GitHub raw or a local server; show status codes by visiting a missing path. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Web Technologies/code/01-skeleton.html` as the after-class check, not as the lecture.

---

## Lab

1. Draw the request cycle for loading index.html + a CSS file.
2. Log document.title.

---

## Homework

1. Written: 200 vs 404.
2. A local folder served with python -m http.server.

---

## Quiz next meeting (they hear this now)

1. What listens on a port (2)
2. GET vs POST (4)
3. Where is Network tab (4)


## Snippet

```html
<!-- index.html -->
<script src="main.js"></script>
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 01]].

---

## Notes you may still need (from the outline)

**1. The browser is an engine.** It requests documents, parses HTML, applies CSS, runs JS. IGWT lives here — not in a desktop OpenGL window first.

**2. HTTP.** Request/response. Status 200, 404, 500. Headers as metadata. HTTPS is HTTP plus TLS — name only.

**3. DevTools.** Elements, Console, Network. This is the lab instrument for 6 semesters.

---

## Common mistakes

1. Teaching HTML as Photoshop.
2. Ignoring Network.

## If we run long, cut

DevTools

## If we run short, add

Log document.title.
