# Lecture 11 — Three.js XR helpers

**Course:** Virtual and Augmented Reality  
**Time:** 75 min lecture + 60 min live coding  
**This week:** VRButton, controllers  
**Board first:** XRButton.createButton(renderer)

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

1. Wire VRButton/ARButton.
2. XREstimatedLight name.
3. Controllers from examples.
4. Don't hide all of this as magic — students read the button source once.
5. Copy from Three.js examples with citation.

---

## 1. Helpers

The examples folder is an oracle. Students must still explain session + input.

## 2. AR light

XREstimatedLight. Fallback dir light.

## 3. Hands

Hand tracking name. Optional extra.

## Live coding (60 min)

A three.js example stripped to 80 lines they can explain.

---

## Lab

1. cite the example URL.
2. remove unused passes.

---

## Homework

1. Written: what the helper hid.
2. demo.

---

## Quiz (10 min)

1. VRButton (3)
2. estimated light (4)
3. what you deleted (3)

## Snippet

```js
document.body.appendChild(VRButton.createButton(renderer));
```

---

## Common mistakes

- full example dump, cannot explain.
- no citation.

---

## Board drawings

1. Button + scene.

