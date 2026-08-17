# Lecture 12 — Modules and structure

**Course:** Introduction to Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** split files, functions as API  
**Board first:** boxes: main.js → math.js

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

1. Split helpers into a second file.
2. Know script order or type=module.
3. Export a function.
4. Avoid circular dumps.
5. Write a README run line.

---

## 1. Why files

Later: kernel.js vs raster.js. Now: `math.js` with clamp/lerp.

## 2. Browser modules

`type="module"` and `export function`. file:// may fail — use a static server. Same rule as WebGL demos.

## 3. Interface

A file is a set of named functions. No hidden globals.

## Live coding (60 min)

Move clamp/lerp into math.js; import in main.

---

## Lab

1. Three-file mini: math, strings, main.
2. README: how to serve.

---

## Homework

1. Written: why file:// breaks modules.
2. Code: one export/import pair.

---

## Quiz (10 min)

1. export syntax (3)
2. Why serve locally (4)
3. Name two files in CG I kernel (3)

## Snippet

```js
export function lerp(a,b,t){ return a + (b-a)*t; }
```

---

## Common mistakes

- One 400-line file 'for simplicity'.
- Forgetting to serve.

---

## Board drawings

1. File arrows.
2. export/import.

