# Lecture 8 — Midterm and latency

**Course:** AI for Interactive Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** midterm; streaming, placeholders  
**Board first:** TTFT; skeleton UI

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

1. Sit midterm: ethics, proxy, textures, 3D limits, agents, RAG, logs.
2. Time to first token.
3. Streaming UI.
4. Don't block the render loop on fetch.
5. Cancel tokens.

---

## 1. Midterm

architecture + ethics.

## 2. UX

3D should orbit while text streams. Placeholders on textures.

## 3. Cost

Retries cost money. Cache mocks in dev.

## Live coding (60 min)

Orbit a cube while a mocked stream fills a HUD.

---

## Lab

1. abort button.
2. timeout UI.

---

## Homework

1. Reflection + latency notes.

---

## Quiz (10 min)

1. None.

## Snippet

```js
const ctrl = new AbortController();
fetch(url, { signal: ctrl.signal });
```

---

## Common mistakes

- await gen before starting rAF.
- no abort.

---

## Board drawings

1. Stream + orbit.

