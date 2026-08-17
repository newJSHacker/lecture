# Lecture 10 — Events

**Course:** Web Technologies  
**Time:** 75 min lecture + 60 min live coding  
**This week:** bubble, preventDefault  
**Board first:** click on button inside form

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

1. addEventListener.
2. event.target.
3. preventDefault on submit.
4. keydown for a small game.
5. Know bubble vs capture names.

---

## 1. The event object

type, target, currentTarget. Keyboard `event.key`.

## 2. Delegation

One listener on ul for many li. Graphics: one pointer listener on canvas.

## 3. Default actions

Forms navigate; links navigate. preventDefault when the page should stay.

## Live coding (60 min)

Canvas or div: click to place a dot (DOM or Canvas 2D).

---

## Lab

1. Keyboard move a box.
2. Delegation on a list.

---

## Homework

1. Written: bubble in 6 sentences.
2. Code: draw dots on click.

---

## Quiz (10 min)

1. preventDefault why (3)
2. target vs currentTarget (4)
3. key vs code (3)

## Snippet

```js
form.addEventListener('submit', (e) => { e.preventDefault(); });
```

---

## Common mistakes

- onclick attributes.
- Forgetting preventDefault and wondering why the page reloads.

---

## Board drawings

1. Bubble arrows.
2. Canvas clicks.

