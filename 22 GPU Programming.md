# GPU Programming

A 15-week university course for the **Interactive Graphics and Web Technologies (IGWT)** program.

Treat the GPU as a throughput machine: FBO ping-pong, particles, a fluids teaser, then WebGPU + WGSL compute — with an honest WebGL fallback story.

Source of teaching format: [[02 Curriculum Design Advice]]

**Lecture notes:** [[GPU Programming/00 Lectures]]  
**Exercises:** [[GPU Programming/exercises/00 Index]]

---

## Where this course sits

Semester **4**. [[17 WebGL Programming]] and [[20 Shader Programming]].

---

## Course goal

By the end, a student can ship a GPU simulation with a packing diagram and explain when to stay on WebGL2.

---

## Teaching structure

| Part | Duration | What happens |
| --- | --- | --- |
| Lecture | 75 min | Concepts, one derivation or architecture picture |
| Live coding | 60 min | Professor implements the week's kernel |
| Lab | 2–3 hours | Students finish a starter |
| Homework | 4–6 hours | Code + short written |
| Quiz | 10 min | Definitions and one picture |

**Language / tools:** WebGL2 required. WebGPU where the lab browsers allow. No CUDA required.

Never lecture from slides only.

---

## Assessment

| Component | Weight | Notes |
| --- | --- | --- |
| Labs (12) | 25% | Must run |
| Homework (8) | 20% | Mix of code and written |
| Quizzes (10) | 10% | Weekly |
| Midterm (Week 8) | 15% | Written |
| Final project | 30% | Demo + 6–8 page report |

---

## Week-by-week summary

| Week | Topic | Students do |
| ---: | --- | --- |
| 1 | GPGPU idea | GPU as throughput |
| 2 | FBO ping-pong | A→B→A textures |
| 3 | Particle state in textures | pos in RG, vel in BA |
| 4 | Transform feedback name | VS output captured |
| 5 | Forces and integration | Euler, clamp |
| 6 | Fluids teaser | divergence-free idea |
| 7 | WebGL compute hacks | histogram, reduce names |
| 8 | Midterm and WebGPU intro | midterm; device/queue |
| 9 | WGSL triangle | vertex_index, clip |
| 10 | Compute pass | workgroups |
| 11 | Particles in WebGPU | buffer of structs |
| 12 | When to stay on WebGL | compatibility, tools |
| 13 | A small sim studio | choose ping-pong or compute |
| 14 | Project studio | GPGPU or WebGPU mini |
| 15 | Presentations | 12+5 |

---

## What to skip

CUDA as the only path, Vulkan, production fluid research.

---

## Textbooks / refs

WebGPU ungp / MDN. GPU Gems (selected). WebGL2 GPGPU articles.

---

## One-sentence teaching principle

If they cannot draw the memory layout, they are running a sample, not programming a GPU.
