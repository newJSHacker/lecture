# Interactive Experience Development

A 15-week university course for the **Interactive Graphics and Web Technologies (IGWT)** program.

Ship 3D + UI: React Three Fiber, HUD, scroll/story, audio, loading, a11y, and measured performance — experiences, not only scenes.

Source of teaching format: [[02 Curriculum Design Advice]]

**Lecture notes:** [[Interactive Experience/00 Lectures]]  
**Exercises:** [[Interactive Experience/exercises/00 Index]]

---

## Where this course sits

Semester **5**. [[18 Three.js Development]] and [[16 Interactive Web Development]]. React basics (or a one-week crash in Week 1 lab).

---

## Course goal

By the end, a student can defend a small interactive experience with a shot list, a HUD, a keyboard path, and a budget table.

---

## Teaching structure

| Part | Duration | What happens |
| --- | --- | --- |
| Lecture | 75 min | Concepts, one derivation or architecture picture |
| Live coding | 60 min | Professor implements the week's kernel |
| Lab | 2–3 hours | Students finish a starter |
| Homework | 4–6 hours | Code + short written |
| Quiz | 10 min | Definitions and one picture |

**Language / tools:** Vite, React, R3F, drei. Vanilla Three.js + DOM is an allowed alternative.

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
| 1 | R3F architecture | Canvas, reconciler |
| 2 | React state vs 3D | useState, useFrame |
| 3 | HTML overlay HUD | Dom, portals |
| 4 | Scroll and camera | scroll controls, storytelling |
| 5 | Motion and drei helpers | easing, CameraControls |
| 6 | Audio visualization | analyser → scale |
| 7 | Physics name | rapier / cannon-es |
| 8 | Midterm and loading UX | midterm; Suspense |
| 9 | Accessibility in 3D | keyboard, labels, motion |
| 10 | Story beats | shot list, camera, light |
| 11 | Performance budget | instancing, dpr, draw calls |
| 12 | Creative coding habits | constraints, seeds |
| 13 | Critique | Awwwards-style review |
| 14 | Project studio | interactive experience |
| 15 | Presentations | 12+5 |

---

## What to skip

Next.js as the course, full CMS, multiplayer, writing Three.js core.

---

## Textbooks / refs

R3F docs. drei docs (selected). Web Technologies notes for overlay CSS.

---

## One-sentence teaching principle

If the only interface is orbit-drag, it is a scene, not an experience.
