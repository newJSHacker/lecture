# Lecture 5 — Animation

**Course:** Three.js Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** clock, mixer name  
**Board first:** Clock.getDelta

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

1. Clock dt.
2. rotation +=.
3. AnimationMixer name for glTF.
4. Don't use Date.now only.
5. Pause.

---

## 1. dt

Same as Interactive Web.

## 2. Clips

Week 6 glTF may include clips.

## 3. GSAP

Can tween Object3D; still one rAF.

## Live coding (60 min)

Spin + bounce with dt.

---

## Lab

1. pause.
2. mixer extra if a clip exists.

---

## Homework

1. Written: mixer vs rAF rotate.
2. Code: dt.

---

## Quiz (10 min)

1. getDelta (3)
2. mixer (4)
3. pause (3)

## Snippet

```js
const dt = clock.getDelta();
```

---

## Common mistakes

- rotation = t without dt on variable fps.

---

## Board drawings

1. Clock.

