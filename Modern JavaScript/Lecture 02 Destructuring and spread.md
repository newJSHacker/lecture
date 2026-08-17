# Lecture 2 — Destructuring and spread

**Course:** Modern JavaScript Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** pattern match lite  
**Board first:** {x,y} = p

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

1. Destructure objects/arrays.
2. Spread copy.
3. Rest params.
4. Rename fields.
5. Shallow copy warning.

---

## 1. Destructure

const {x,y}=p. Parameters too.

## 2. Spread

[...a, x]. Object spread shallow.

## 3. Rest

(...args).

## Live coding (60 min)

Swap via destucture; clone an array; clone a point.

---

## Lab

1. Merge two option objects.
2. Deep copy discussion.

---

## Homework

1. Written: shallow vs deep.
2. Code: 8 tests.

---

## Quiz (10 min)

1. clone array (3)
2. rename destucture (3)
3. shallow pitfall (4)

## Snippet

```js
const { x, y } = p;
const q = { ...p, y: 0 };
```

---

## Common mistakes

- Thinking spread deep-copies nested meshes.

---

## Board drawings

1. Patterns.

