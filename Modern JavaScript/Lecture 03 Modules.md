# Lecture 3 — Modules

**Course:** Modern JavaScript Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** export import  
**Board first:** files as API

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

1. export function.
2. import named vs default policy.
3. type=module.
4. Serve locally.
5. Cycle warning.

---

## 1. Named exports

Course policy: named exports for kernels. Default optional.

## 2. Browsers

file:// often fails. npx serve.

## 3. Bundlers preview

Vite next week.

## Live coding (60 min)

Split lerp into math.js; import in main.js.

---

## Lab

1. Three modules.
2. README serve.

---

## Homework

1. Written: ESM vs classic script.
2. Code: import.

---

## Quiz (10 min)

1. export syntax (4)
2. why serve (3)
3. named vs default (3)

## Snippet

```js
import { lerp } from './math.js';
```

---

## Common mistakes

- Mixing remote script URLs with local modules until it 'works'.

---

## Board drawings

1. Arrows between files.

