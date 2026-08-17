# Lecture 7 — Keyframe animation

**Course:** Blender for Real-Time Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** I-key, graph editor  
**Board first:** loc/rot/scale tracks

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

1. Insert loc/rot keyframes.
2. Move on the timeline.
3. Linear vs bezier handles.
4. Don't animate by moving the object without keys.
5. Loop a 24-frame spin.

---

## 1. What engines see

glTF can store animation clips. Three.js `AnimationMixer` plays them. A spinning logo is enough this week.

## 2. Graph editor

Ease-in. Constant for stepped. Students leave default bezier and get 'bounce' they did not want.

## 3. Object vs bone

Bones next week. This week: object transforms.

## Live coding (60 min)

A lid opening 0–24 frames; play in viewport.

---

## Lab

1. Looping rotation.
2. Export thought: will this be a clip?

---

## Homework

1. Written: what a F-curve is.
2. 24-frame gif or mp4 of viewport.

---

## Quiz (10 min)

1. insert key (2)
2. linear vs bezier (4)
3. mixer later (4)

## Snippet

```
I → Location Rotation  |  Graph Editor → Vector handles
```

---

## Common mistakes

- Auto-key on by accident, 400 garbage keys.
- Animating in edit mode verts for a rigid lid.

---

## Board drawings

1. Dope sheet.
2. Lid arc.

