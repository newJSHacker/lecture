# Lecture 1 — How the web works

**Week 1 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** client → HTTP → server → HTML; open the Network tab  
**Success check:** they can name client and server and point at Network for a missing file

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `Web Technologies/code/01-skeleton.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: see a request | Invariant: the browser requests, parses, then paints`

## Board at the end (they photograph this)

```
client  →  HTTP  →  server  →  HTML/CSS/JS

URL:  scheme  host  port  path  ?query

200 ok    404 missing    500 server broke
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | DevTools Network with a 404 row circled | do not draw Chrome’s UI |

---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** IGWT lives in the browser, not a desktop OpenGL window first. Today we watch a request. If you cannot see a request, you will later call a missing texture a shader bug.

**Ask:** If the page is blank, where do you look first — the desktop, me, or Network? Wait seven seconds.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *URL, HTTP, browser*.

**Do not:** Teaching HTML as Photoshop.

### Minutes 8–12 — Frame

**Say:** The browser is an engine: request, parse HTML, apply CSS, run JS. HTTPS is HTTP plus TLS — name only. GET vs POST at teaching level: GET is a read, POST submits.

**Ask:** Who listens on a port — the browser or the server?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Draw client and server as two boxes. The arrow is HTTP. Status codes live on the response.

**Board:** URL anatomy. Circle path. Query is optional today.

**Say:** DevTools: Elements, Console, Network. Network is the lab instrument for six semesters. No CDN in this program — we serve local files.

**Ask:** GET vs POST in one sentence?

**They do:** On paper: the request cycle for index.html plus one CSS file. Two arrows.

**Do not:** Lecture HTML as a visual design tool. Use a CDN.

### Minutes 35–50 — Show

**Say:** Serve this folder with python -m http.server. Load index.html. Then visit a missing path and read 404 out loud. Demo Web Technologies/code/01-skeleton.html.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Log document.title in the console. Then draw the cycle. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: request cycle + title log. Homework: 200 vs 404; serve a local folder. Quiz: who listens on a port, GET vs POST, where is Network.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Blank page + console | Plant: they look at the editor, not Network. |
| 10–30 | http.server + 200 | Plant file:// and a missing CSS. |
| 30–45 | 404 on a fake path | Read the status out loud. |
| 45–60 | They log title | Circulate. No CDN. |

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

None this meeting.


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

_none_

---

## Common mistakes

1. Teaching HTML as Photoshop.
2. Ignoring Network.

## If we run long, cut

TLS details. Keep request cycle + Network.

## If we run short, add

Headers as a name: Content-Type.
