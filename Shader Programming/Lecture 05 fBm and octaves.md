# Lecture 5 — fBm and octaves

**Course:** Shader Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** sum scaled noise  
**Board first:** amp 1/2/4, freq 1/2/4

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

1. Sum 4–6 octaves.
2. Amplitude halves as frequency doubles.
3. Domain warp name.
4. Don't 12 octaves on mobile.
5. Link [[WebGL/demos/10-noise-fbm.html]].

---

## 1. fBm

Fractional Brownian motion as a *recipe*, not a proof. Terrain height, clouds, marble (warp).

## 2. Parameters

octaves, lacunarity (~2), gain (~0.5). Students crank octaves until fps dies.

## 3. Warp

`noise(p + noise(p))` marble. Show once.

## Live coding (60 min)

fBm slider for octaves; screenshot 1 vs 6.

---

## Lab

1. warp extra.
2. measure cost sentence.

---

## Homework

1. Written: one octave vs fBm.
2. GLSL fbm.

---

## Quiz (10 min)

1. lacunarity (3)
2. why gain 0.5 (4)
3. mobile octaves (3)

## Snippet

```glsl
float fbm(vec2 p){ float a=0.5,s=0.0; for(int i=0;i<5;i++){ s+=a*noise(p); p*=2.0; a*=0.5;} return s; }
```

---

## Common mistakes

- unrolled 20 octaves.
- using fBm as lighting.

---

## Board drawings

1. Octave stack.

