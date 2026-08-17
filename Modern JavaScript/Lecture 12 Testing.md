# Lecture 12 — Testing

**Course:** Modern JavaScript Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** assert, tiny runner  
**Board first:** PASS / FAIL list

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

1. console.assert.
2. A tiny test html.
3. Arrange-act-assert.
4. Don't delete failing fixtures.
5. CI name only.

---

## 1. Culture

CG kernel tests and geometry fixtures. Same habit.

## 2. Runner

A page that prints PASS/FAIL. No Jest required.

## 3. CI

GitHub Actions named; not required this term.

## Live coding (60 min)

Port lerp/clamp tests to a test.html.

---

## Lab

1. 5 more fixtures.
2. A deliberately failing test then fix.

---

## Homework

1. Written: why hidden fixtures.
2. Code: test page.

---

## Quiz (10 min)

1. AAA (3)
2. assert (3)
3. deleting tests (4)

## Snippet

```js
function assert(n,c){ if(!c) throw new Error(n); }
```

---

## Common mistakes

- Tests that only log 'ok'.
- Deleting FAIL cases.

---

## Board drawings

1. PASS list.

