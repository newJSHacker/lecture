# Lecture 6 — Fetch patterns

**Course:** Modern JavaScript Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** JSON, abort, cache  
**Board first:** AbortController name

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

1. Headers.
2. POST JSON teaching.
3. AbortController.
4. Don't store secrets in frontend.
5. Idempotent GET.

---

## 1. APIs

GET JSON. POST for later backends.

## 2. Abort

Cancel on new search.

## 3. Secrets

No API keys in the repo. AI course will repeat this.

## Live coding (60 min)

Search-as-you-type fake: abort previous.

---

## Lab

1. POST to a local mock extra.
2. Handle 500.

---

## Homework

1. Written: why keys not in git.
2. Code: abort.

---

## Quiz (10 min)

1. AbortController (4)
2. where keys live (3)
3. GET cache (3)

## Snippet

```js
const c = new AbortController();
fetch(url, { signal: c.signal });
```

---

## Common mistakes

- Keys in source.
- No abort, race of answers.

---

## Board drawings

1. Race.
2. Key skull.

