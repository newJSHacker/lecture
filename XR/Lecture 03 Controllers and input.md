# Lecture 3 — Controllers and input

**Course:** Virtual and Augmented Reality  
**Time:** 75 min lecture + 60 min live coding  
**This week:** select, squeeze, rays  
**Board first:** target ray + squeeze

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

1. XRInputSource.
2. selectstart/selectend.
3. Gamepad mapping name.
4. Don't assume two identical controllers.
5. Laser line debug.

---

## 1. Input

Hands, controllers, gaze (last resort). `select` is the click.

## 2. Three.js

XRControllerModelFactory / Raycaster from controller.

## 3. Haptics

pulse name. Optional.

## Live coding (60 min)

Point and `select` to change a cube color.

---

## Lab

1. show ray.
2. squeeze extra.

---

## Homework

1. Written: input source fields.
2. demo.

---

## Quiz (10 min)

1. select (3)
2. target ray (4)
3. one controller (3)

## Snippet

```js
controller.addEventListener('select', onSelect);
```

---

## Common mistakes

- mouse-only and calling it VR.
- no ray debug.

---

## Board drawings

1. Controller + ray.

