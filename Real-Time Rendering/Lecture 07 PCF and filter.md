# Lecture 7 — PCF and filter

**Course:** Real-Time Rendering  
**Time:** 75 min lecture + 60 min live coding  
**This week:** tap neighbors  
**Board first:** 3×3 compare average

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

1. Percentage closer filtering.
2. Poisson name.
3. Cost vs quality.
4. Don't 15×15 on mobile.
5. Still one cascade.

---

## 1. PCF

Average binary tests in a kernel. Soft-looking edges, still a 2D map.

## 2. VSM name

Advanced CG / week later. Moments. Light leak.

## 3. API

sampler2DShadow / compare mode names.

## Live coding (60 min)

Toggle hard vs 3×3 PCF; screenshot.

---

## Lab

1. count taps in comments.
2. acne still possible — say why.

---

## Homework

1. Written: PCF vs blur the depth (wrong).
2. Code.

---

## Quiz (10 min)

1. PCF (4)
2. why not blur depth (3)
3. tap count (3)

## Snippet

```glsl
float s=0.0; for(int i=0;i<9;i++) s += compare(uv+off[i]); s/=9.0;
```

---

## Common mistakes

- blurring the depth texture and calling it PCF.
- PCSS as required lab.

---

## Board drawings

1. 9 taps.

