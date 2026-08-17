# Lecture 10 — Sprint: robustness

**Course:** Capstone Project  
**Time:** 75 min lecture + 60 min live coding  
**This week:** load fail, bad GLB, offline  
**Board first:** errors you can show

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

1. Broken glTF path.
2. Timeout.
3. Unsupported WebGL.
4. Don't only the happy path.
5. A support matrix.

---

## 1. Robust

TAs will break files. Feature detect. Inline fallback if XR.

## 2. Support

Browser × OS table. Honest no.

## 3. Logging

No secrets in logs.

## Live coding (60 min)

Three failure demos.

---

## Lab

1. support matrix.
2. user-visible errors.

---

## Homework

1. Matrix in README.

---

## Quiz (10 min)

1. WebGL fail (3)
2. bad glb (4)
3. XR fallback (3)

---

## Common mistakes

- crash stack as the UI.
- matrix all 'yes' untested.

---

## Board drawings

1. Red states.

