# Lecture 6 — Anchors and persistence

**Course:** Virtual and Augmented Reality  
**Time:** 75 min lecture + 60 min live coding  
**This week:** world-locked pose  
**Board first:** anchor → getPose each frame

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

1. Create an anchor at a hit.
2. Update each frame.
3. Limits of web persistence.
4. Don't promise a saved palace across months.
5. Delete anchors.

---

## 1. Anchors

A stable pose in the XR world. Device and UA dependent.

## 2. Persistence

True world maps are platform features. Student honesty: 'this session' vs 'forever'.

## 3. Scale

Meters again. A 10 m cube is a bug.

## Live coding (60 min)

Place two anchored cubes; walk; they stay.

---

## Lab

1. clear all.
2. scale 0.2 m object.

---

## Homework

1. Written: session vs persistent.
2. demo.

---

## Quiz (10 min)

1. anchor (3)
2. getPose (3)
3. honesty (4)

## Snippet

```js
const anchor = await frame.createAnchor(pose, space);
```

---

## Common mistakes

- cloud anchors as required.
- unanchored floating UI.

---

## Board drawings

1. Pinned cubes.

