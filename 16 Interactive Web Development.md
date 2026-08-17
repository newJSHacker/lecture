# Interactive Web Development

A 15-week university course for the **Interactive Graphics and Web Technologies (IGWT)** program.

Motion on the web: Canvas, SVG, CSS/GSAP, input, audio, and a tiny entity loop — without pretending it is a 3D engine.

Source of teaching format: [[02 Curriculum Design Advice]]

**Lecture notes:** [[Interactive Web/00 Lectures]]  
**Exercises:** [[Interactive Web/exercises/00 Index]]

---

## Where this course sits

Semester **2**. [[13 Web Technologies]] and Programming loops/functions.

---

## Course goal

By the end, a student can ship an interactive 2D experience with a correct animation loop and pointer mapping.

---

## Teaching structure

| Part | Duration | What happens |
| --- | --- | --- |
| Lecture | 75 min | Concepts, one derivation or architecture picture |
| Live coding | 60 min | Professor implements the week's kernel |
| Lab | 2–3 hours | Students finish a starter |
| Homework | 4–6 hours | Code + short written |
| Quiz | 10 min | Definitions and one picture |

**Language / tools:** Browser, Canvas 2D, SVG, optional local GSAP (`Interactive Web/vendor/gsap.min.js`). No CDN.

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
| 1 | Canvas 2D API | getContext, paths |
| 2 | The animation loop | rAF, dt, time |
| 3 | Pointer input | offset, buttons, touch |
| 4 | SVG | DOM graphics, viewBox |
| 5 | CSS transitions | hover, states |
| 6 | CSS keyframes | loops, steps |
| 7 | GSAP intro | tweens, timelines |
| 8 | Midterm and compositor | midterm; layers |
| 9 | Scroll and intersection | IO, sticky |
| 10 | Hybrid SVG + Canvas | overlay UI |
| 11 | Audio + canvas | Web Audio, analyser |
| 12 | A mini 2D engine | entities, loop, input |
| 13 | Polish and performance | pooling, culling 2D |
| 14 | Project studio | interactive page |
| 15 | Presentations | 12+5 |

---

## What to skip

Full game engines, WebGL (that's the next semester course), React.

---

## Textbooks / refs

MDN Canvas/SVG. GSAP docs (selected). HTML5 Game loops articles.

---

## One-sentence teaching principle

Time, input, and a clear are the kernel; libraries only after that works.
