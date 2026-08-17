# Lecture 2 — Color and gamma

**Course:** Shader Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** linear vs sRGB  
**Board first:** pow(c, 2.2) decode

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

1. Decode sRGB to linear for lighting.
2. Encode back for display.
3. See banding vs correct.
4. Don't pow twice.
5. Albedo textures are sRGB.

---

## 1. CG I again

[[Computer Graphics/Lecture 11 Blinn Phong and Gamma]]. Now it is three lines in GLSL.

## 2. Where

Do lighting in linear. `pow(x, vec3(2.2))` is a teaching approximation, not a color-management product.

## 3. Textures

WebGL sRGB textures / `SRGB8_ALPHA8` names. Three.js `colorSpace`.

## Live coding (60 min)

Gradient with and without gamma encode; screenshot both.

---

## Lab

1. Light a Lambert quad in linear.
2. Toggle encode.

---

## Homework

1. Written: why lighting in sRGB looks wrong.
2. Code: encode helper.

---

## Quiz (10 min)

1. decode formula teaching (4)
2. double gamma (3)
3. albedo space (3)

## Snippet

```glsl
vec3 toLinear(vec3 c){ return pow(c, vec3(2.2)); }
vec3 toSRGB(vec3 c){ return pow(c, vec3(1.0/2.2)); }
```

---

## Common mistakes

- pow on normals.
- Skipping encode and blaming the monitor.

---

## Board drawings

1. Two gradients.

