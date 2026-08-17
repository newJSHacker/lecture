# Lecture 4 — HDR and tonemap

**Course:** Real-Time Rendering  
**Time:** 75 min lecture + 60 min live coding  
**This week:** Reinhard / ACES names  
**Board first:** hdr → [0,1] display

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

1. Store HDR color.
2. Reinhard as teaching: c/(1+c).
3. ACES name.
4. Exposure slider.
5. Don't clip at 1 in the lighting pass.

---

## 1. Need

Sun is >> 1. Bloom needs leftover energy.

## 2. Operators

Reinhard, filmic, ACES. Pick one for the lab. Document it.

## 3. sRGB

Tonemap then encode, or a combined output pass.

## Live coding (60 min)

Overbright cube; exposure; Reinhard.

---

## Lab

1. ACES extra name in comments.
2. false-color HDR extra.

---

## Homework

1. Written: why not clamp.
2. Code: reinhard.

---

## Quiz (10 min)

1. Reinhard (3)
2. exposure (3)
3. order vs gamma (4)

## Snippet

```glsl
vec3 reinhard(vec3 x){ return x / (1.0 + x); }
```

---

## Common mistakes

- tonemap per light.
- gamma then tonemap backwards.

---

## Board drawings

1. HDR bar.

