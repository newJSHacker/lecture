# Lecture 11 — HTTP and fetch

**Course:** Web Technologies  
**Time:** 75 min lecture + 60 min live coding  
**This week:** JSON APIs  
**Board first:** fetch → then/await → json

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

1. fetch a JSON URL.
2. Handle non-OK status.
3. Parse JSON.
4. Render into the DOM.
5. Know CORS exists.

---

## 1. fetch

Returns a Promise. async/await in this week at teaching level; Modern JS goes deeper.

## 2. Status

`if (!res.ok) throw`. Students skip this and parse an HTML 404 as JSON.

## 3. CORS

A browser policy. Local files and foreign APIs fail. Use a local JSON file served by a static server.

## Live coding (60 min)

Load `/data.json` with three records; render a list.

---

## Lab

1. Error state in the UI.
2. Loading text.

---

## Homework

1. Written: CORS in one paragraph.
2. Code: fetch + render + error.

---

## Quiz (10 min)

1. res.ok (3)
2. JSON.parse vs res.json (3)
3. Why file:// fetch fails (4)

## Snippet

```js
const data = await (await fetch('data.json')).json();
```

---

## Common mistakes

- Ignoring !ok.
- Hardcoding GitHub tokens in the page — never.

---

## Board drawings

1. Request arrow.
2. JSON list.

