# Lecture 1 — GPGPU idea

**Course:** GPU Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** GPU as throughput  
**Board first:** data parallel vs graphics

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

1. Contrast CPU latency vs GPU throughput.
2. A fragment shader as a kernel.
3. When graphics API is a compute hack.
4. Don't start in CUDA if the program is web-first.
5. Course map to WebGPU.

---

## 1. Why this course

Particles, fluids teasers, image filters, and an honest WebGPU intro. Graphics students already write FS kernels; GPGPU is the same hardware with fewer triangles.

## 2. Web vs native

CUDA/OpenCL exist. IGWT still ships in a browser: FBO ping-pong, transform feedback name, then WebGPU compute.

## 3. Limits

No pointers in FS. Fixed output size. Readback is slow.

## Live coding (60 min)

Fullscreen FS that writes a gradient 'simulation' into a texture (static).

---

## Lab

1. time uniform.
2. why this is a kernel.

---

## Homework

1. Written: CPU vs GPU 1 page.
2. screenshot.

---

## Quiz (10 min)

1. throughput (3)
2. readback (4)
3. CUDA this program? (3)

## Snippet

```glsl
outColor = vec4(uv, 0.5+0.5*sin(u_time), 1.0);
```

---

## Common mistakes

- teaching only CUDA slides in a web degree.
- readPixels every frame.

---

## Board drawings

1. Throughput bars.

