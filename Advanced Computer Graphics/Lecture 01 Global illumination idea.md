# Lecture 1 — Global illumination idea

**Course:** Advanced Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** direct vs indirect  
**Board first:** bounce paths; energy

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

1. Define direct vs indirect light.
2. Why ambient is a lie.
3. Color bleeding name.
4. Don't start with a production path tracer.
5. Connect to Lambert as only bounce 0.

---

## 1. The gap

RTR PBR is mostly **local**: lights + IBL as a stand-in for the rest of the world. GI is light after **leaving** other surfaces.

## 2. Taxonomy

Radiosity, path tracing, photon mapping, irradiance volumes, screen-space GI, probes. This course **names** them and implements teaching-scale versions of two: radiosity idea + a tiny path tracer.

## 3. Energy

Each bounce loses energy (unless metal). White rooms still go grey if you forget albedo < 1.

## Live coding (60 min)

A diagram: lamp, wall, dark side of a cube — what RTR misses. Screenshot a Three.js scene vs a GI reference still (can be from a paper, cited).

---

## Lab

1. list 5 GI methods in a table: realtime?
2. albedo < 1 note.

---

## Homework

1. Written: why IBL is not full GI.
2. figure.

---

## Quiz (10 min)

1. indirect (3)
2. bleeding (3)
3. IBL vs GI (4)

## Snippet

```
L_out = emit + ∫ BRDF * L_in * n·ω dω
```

---

## Common mistakes

- 'PBR already is GI'.
- unbounded albedo 2.0.

---

## Board drawings

1. One bounce vs many.

