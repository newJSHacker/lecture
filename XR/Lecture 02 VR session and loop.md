# Lecture 2 — VR session and loop

**Course:** Virtual and Augmented Reality  
**Time:** 75 min lecture + 60 min live coding  
**This week:** reference space  
**Board first:** local-floor vs viewer

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

1. requestSession immersive-vr.
2. reference space.
3. XR frame loop vs rAF.
4. Don't ignore `xr.setReferenceSpaceType`.
5. Exit session cleanup.

---

## 1. Spaces

viewer, local, local-floor, bounded-floor, unbounded. Teaching: local-floor for room-scale-ish.

## 2. Loop

Three.js handles `setAnimationLoop` with XR. Students should still know the pose comes from the frame.

## 3. Comfort

Week 9. This week: standing origin.

## Live coding (60 min)

Enter VR on a headset **or** record a TA doing it; student still writes the session code.

---

## Lab

1. end session button.
2. floor plane.

---

## Homework

1. Written: reference space.
2. code.

---

## Quiz (10 min)

1. local-floor (4)
2. who owns rAF (3)
3. cleanup (3)

## Snippet

```js
renderer.xr.enabled = true;
```

---

## Common mistakes

- never testing exit.
- unbounded tracking as week 2 required.

---

## Board drawings

1. Floor origin.

