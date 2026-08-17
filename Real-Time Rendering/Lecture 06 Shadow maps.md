# Lecture 6 — Shadow maps

**Course:** Real-Time Rendering  
**Time:** 75 min lecture + 60 min live coding  
**This week:** depth from light  
**Board first:** light P V → depth tex → compare

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

1. Render depth from the light.
2. Compare in the main pass.
3. Bias.
4. Don't start with cascades.
5. Acne vs peter-panning.

---

## 1. Algorithm

A camera at the light. Store depth. If the main pixel is farther than the map, it's in shadow.

## 2. Projection

Ortho for directional. Perspective for spot. Frustum must cover the scene — too tight acne, too loose jaggy.

## 3. WebGL

DEPTH_COMPONENT texture. Three.js does this; students should still draw the light frustum.

## Live coding (60 min)

Plane + cube; directional shadow; bias slider.

---

## Lab

1. show shadow map as grayscale extra.
2. mapSize 512 vs 2048 measured.

---

## Homework

1. Written: compare function.
2. Code or three.js with explanation of bias.

---

## Quiz (10 min)

1. who renders the map (4)
2. bias (3)
3. ortho why (3)

## Snippet

```glsl
float shadow = (zLight > mapZ + bias) ? 0.3 : 1.0;
```

---

## Common mistakes

- CSM speech without a single map.
- bias 0.1.

---

## Board drawings

1. Two cameras.

