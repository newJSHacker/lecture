# Lecture 7 — WebGL compute hacks

**Course:** GPU Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** histogram, reduce names  
**Board first:** mip as reduce

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

1. Mipmap as a reduction.
2. Atomic names (limited in WebGL).
3. When to readback.
4. Don't histogram in JS over pixels if the GPU can.
5. Prefix sum name only.

---

## 1. Reduce

Average luminance for auto-exposure is a mip chain. Teaching: generateMips or blit down.

## 2. Atomics

WebGL2 has almost none for FS. WebGPU compute has atomics. That's a reason to move.

## 3. Readback

Async pixel pack names. Stall if you wait.

## Live coding (60 min)

Auto-exposure-ish: downsample a scene tex; log average; feed exposure.

---

## Lab

1. show mip debug.
2. don't readPixels every frame.

---

## Homework

1. Written: reduce.
2. demo or Three.js + explanation.

---

## Quiz (10 min)

1. mip reduce (4)
2. why atomics (3)
3. stall (3)

## Snippet

```js
gl.generateMipmap(gl.TEXTURE_2D);
```

---

## Common mistakes

- CPU loop over getImageData 1080p.
- atomics in a blog copied to WebGL1.

---

## Board drawings

1. Pyramid.

