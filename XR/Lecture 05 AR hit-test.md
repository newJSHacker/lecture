# Lecture 5 — AR hit-test

**Course:** Virtual and Augmented Reality  
**Time:** 75 min lecture + 60 min live coding  
**This week:** plane detection idea  
**Board first:** hit-test source → pose

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

1. immersive-ar.
2. hit-test API names.
3. Place a cube on a plane.
4. Don't require LiDAR theory.
5. Light estimation name.

---

## 1. AR

Phone or headset. Hit-test gives a pose on a detected plane. Anchors persist it (next week).

## 2. Web

Chrome Android / Quest. Desktop often **no AR** — fallback: mouse-place on a fake plane in inline.

## 3. Privacy

Camera. Policy in the syllabus.

## Live coding (60 min)

Place an object on a plane (real hit-test **or** inline fake plane).

---

## Lab

1. document device.
2. remove last extra.

---

## Homework

1. Written: fallback if no AR.
2. demo.

---

## Quiz (10 min)

1. hit-test (4)
2. privacy (3)
3. inline fallback (3)

## Snippet

```js
const src = await session.requestHitTestSource({ space: viewerSpace });
```

---

## Common mistakes

- ARKit-only native app as the homework.
- no fallback.

---

## Board drawings

1. Phone + plane.

