# Lecture 2 — APIs and keys

**Course:** AI for Interactive Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** server proxy  
**Board first:** browser → your server → vendor

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

1. A tiny proxy (Node/fetch) that holds the key.
2. Rate limit idea.
3. Costs.
4. Don't teach students to leak keys 'just for class' — use a shared proxy with a class key rotated.
5. Logs without storing prompts that are private.

---

## 1. Architecture

The browser never sees the vendor key. Same as any production app.

## 2. Mock

If no budget: a mock server returns canned JSON/images. The **client architecture** is the lab.

## 3. ToS

Read the vendor policy. Student work, not resale.

## Live coding (60 min)

fetch('/api/complete') against a mock or real proxy; display text.

---

## Lab

1. error states.
2. timeout.

---

## Homework

1. Written: why proxy.
2. code.

---

## Quiz (10 min)

1. who holds the key (4)
2. mock allowed? (3)
3. rate limit (3)

## Snippet

```js
const r = await fetch('/api/complete', { method: 'POST', body: JSON.stringify({ prompt }) });
```

---

## Common mistakes

- key in GitHub.
- unbounded student spend.

---

## Board drawings

1. Proxy box.

