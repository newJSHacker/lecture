# Lecture 8 — Midterm and JS in the page

**Course:** Web Technologies  
**Time:** 75 min lecture + 60 min live coding  
**This week:** midterm; script and DOM intro  
**Board first:** script at end of body

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

1. Sit midterm on HTML/CSS/HTTP.
2. Load a script.
3. document.querySelector.
4. textContent vs innerHTML policy.
5. Defer vs end of body.

---

## 1. Midterm

HTML tree, box model, flex vs grid, viewport, GET.

## 2. JS in the page

querySelector, click listener. innerHTML with user strings is a security lecture — use textContent by default.

## 3. Order

Script after the DOM nodes it needs, or DOMContentLoaded.

## Live coding (60 min)

A button that toggles a class on the body (dark mode fake).

---

## Lab

1. Three planted CSS bugs to fix.
2. A counter button.

---

## Homework

1. Midterm reflection + toggle lab finished.

---

## Quiz (10 min)

1. None.

## Snippet

```js
document.querySelector('#btn').addEventListener('click', () => {});
```

---

## Common mistakes

- innerHTML with form values.
- Script in head without defer.

---

## Board drawings

1. Midterm topics.
2. DOM node.

