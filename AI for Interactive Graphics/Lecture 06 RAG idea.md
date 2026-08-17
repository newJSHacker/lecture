# Lecture 6 — RAG idea

**Course:** AI for Interactive Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** retrieve then generate  
**Board first:** docs → chunks → query → prompt

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

1. RAG: search your notes, then ask the model.
2. Chunking name.
3. Don't dump the whole curriculum into a prompt.
4. Citations in the answer.
5. A toy: search week markdown locally.

---

## 1. Why

A museum app that answers from **your** captions, not from the model's memory.

## 2. Toy

Split a few markdown files; keyword search is enough. Vector DB optional extra.

## 3. Failure

Wrong chunk → confident nonsense. Show a miss.

## Live coding (60 min)

Query box over 3 local captions; show retrieved chunk + mocked answer.

---

## Lab

1. a miss case.
2. cite filename.

---

## Homework

1. Written: why retrieve.
2. demo.

---

## Quiz (10 min)

1. chunk (3)
2. why cite (4)
3. miss (3)

## Snippet

```js
const hits = docs.filter(d => d.text.includes(q)).slice(0,3);
```

---

## Common mistakes

- embeddings as required infrastructure week 6.
- no citations.

---

## Board drawings

1. Retrieve then prompt.

