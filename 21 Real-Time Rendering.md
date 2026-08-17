# Real-Time Rendering

A 15-week university course for the **Interactive Graphics and Web Technologies (IGWT)** program.

PBR, HDR, bloom, shadow maps, AO/deferred *ideas*, a documented post stack, and measured budgets — looks students can defend.

Source of teaching format: [[02 Curriculum Design Advice]]

**Lecture notes:** [[Real-Time Rendering/00 Lectures]]  
**Exercises:** [[Real-Time Rendering/exercises/00 Index]]

---

## Where this course sits

Semester **4**. [[17 WebGL Programming]] and [[20 Shader Programming]]. Three.js allowed as an oracle after the picture is drawn.

---

## Course goal

By the end, a student can look-dev a small scene, name every pass, and show a measured table on a named device.

---

## Teaching structure

| Part | Duration | What happens |
| --- | --- | --- |
| Lecture | 75 min | Concepts, one derivation or architecture picture |
| Live coding | 60 min | Professor implements the week's kernel |
| Lab | 2–3 hours | Students finish a starter |
| Homework | 4–6 hours | Code + short written |
| Quiz | 10 min | Definitions and one picture |

**Language / tools:** WebGL2 and/or Three.js. Spector.js optional. No Unreal as the weekly engine.

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
| 1 | Forward rendering review | one pass, lights in FS |
| 2 | Metal-rough PBR | Cook-Torrance names |
| 3 | IBL idea | irradiance + prefiltered spec |
| 4 | HDR and tonemap | Reinhard / ACES names |
| 5 | Bloom | bright pass + blur + add |
| 6 | Shadow maps | depth from light |
| 7 | PCF and filter | tap neighbors |
| 8 | Midterm and SSAO idea | midterm; AO as post |
| 9 | Deferred idea | G-buffer then lights |
| 10 | Post stack | order of operations |
| 11 | Anti-aliasing names | MSAA, TAA, FXAA |
| 12 | Profiling | GPU vs CPU, budgets |
| 13 | Look-dev a scene | one asset, full stack |
| 14 | Project studio | real-time look |
| 15 | Presentations | 12+5 |

---

## What to skip

Writing a film path tracer, Nanite, full cascaded shadows as required, UE5.

---

## Textbooks / refs

Real-Time Rendering 4th (selected chapters). Karis/Epic notes. LearnOpenGL PBR (ideas).

---

## One-sentence teaching principle

A look without a stack graph and a measurement is a screenshot, not real-time rendering.
