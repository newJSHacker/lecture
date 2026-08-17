# Lecture 3 — Path tracing teaching

**Course:** Advanced Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** Monte Carlo, cosine sample  
**Board first:** throughput *= brdf; p += n

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

1. A camera ray, a bounce, a light sample **or** uniform hemisphere.
2. Noise vs spp.
3. Don't write production MIS in week 3 unless extra.
4. Canvas or tiny WebGL accumulation.

---

## 1. MC

Average many random paths. Variance is the speckle. More spp → slower, cleaner.

## 2. Sampling

Cosine-weighted hemisphere for diffuse. Next event estimation name.

## 3. Scope

Spheres + Lambert + one area light is a complete teaching tracer. Cornell box extra.

## Live coding (60 min)

Accumulate a 2-sphere Lambert scene on Canvas; spp slider.

---

## Lab

1. gamma encode display.
2. one more bounce extra.

---

## Homework

1. Written: why noise.
2. code.

---

## Quiz (10 min)

1. spp (3)
2. why random (4)
3. Lambert sample (3)

## Snippet

```js
color.add(trace(ray)); n++; display(color.clone().multiplyScalar(1/n));
```

---

## Common mistakes

- one path and calling it a tracer.
- copied GPUPathTracer unread.

---

## Board drawings

1. Paths + average.

