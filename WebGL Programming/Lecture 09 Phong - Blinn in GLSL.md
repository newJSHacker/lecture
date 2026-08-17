# Lecture 9 — Phong / Blinn in GLSL

**Course:** WebGL Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** varyings, gamma  
**Board first:** h = normalize(l+v)

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

1. Blinn-Phong FS.
2. vary v_worldPos.
3. gamma encode.
4. Multiple lights extra.
5. Not PBR yet.

---

## 1. Same as CG I Week 11

Now in GLSL.

## 2. Interpolation

normalize after interpolating n.

## 3. Gamma

pow(c, vec3(1.0/2.2)).

## Live coding (60 min)

Blinn cube; shininess slider.

---

## Lab

1. gamma toggle.
2. two lights extra.

---

## Homework

1. Written: why normalize n in FS.
2. Code: blinn.

---

## Quiz (10 min)

1. half vector (4)
2. gamma where (3)
3. PBR? (3)

## Snippet

```glsl
vec3 h = normalize(l + v);
```

---

## Common mistakes

- gamma twice.
- n not normalized.

---

## Board drawings

1. Highlight.

