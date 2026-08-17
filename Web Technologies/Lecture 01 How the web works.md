# Lecture 1 — How the web works

**Course:** Web Technologies  
**Time:** 75 min lecture + 60 min live coding  
**This week:** URL, HTTP, browser  
**Board first:** client → HTTP → server → HTML

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 10 | Quiz from last week (Week 1: course contract) |
| 25 | Core definition and one picture |
| 45 | Worked examples / derivation |
| 65 | Live pitfalls and policy |
| 75 | Preview lab, then stand up for live coding |

---

## Learning goals

1. Name client and server.
2. Read a URL's parts.
3. Say GET vs POST at teaching level.
4. Open DevTools Network.
5. Course contract.

---

## 1. The browser is an engine

It requests documents, parses HTML, applies CSS, runs JS. IGWT lives here — not in a desktop OpenGL window first.

## 2. HTTP

Request/response. Status 200, 404, 500. Headers as metadata. HTTPS is HTTP plus TLS — name only.

## 3. DevTools

Elements, Console, Network. This is the lab instrument for 6 semesters.

## Live coding (60 min)

Fetch this course README via GitHub raw or a local server; show status codes by visiting a missing path.

---

## Lab

1. Draw the request cycle for loading index.html + a CSS file.
2. Log document.title.

---

## Homework

1. Written: 200 vs 404.
2. A local folder served with python -m http.server.

---

## Quiz (10 min)

1. What listens on a port (2)
2. GET vs POST (4)
3. Where is Network tab (4)

## Snippet

```html
<!-- index.html -->
<script src="main.js"></script>
```

---

## Common mistakes

- Teaching HTML as Photoshop.
- Ignoring Network.

---

## Board drawings

1. Client-server.
2. URL anatomy.

