# Mathematics for Computer Graphics

A 15-week university course for the **Interactive Graphics and Web Technologies (IGWT)** program.

Vectors, matrices, frames, and interpolation as they are used in a renderer — not a full linear-algebra major.

Source of teaching format: [[02 Curriculum Design Advice]]

**Lecture notes:** [[Mathematics for Computer Graphics/00 Lectures]]  
**Exercises:** [[Mathematics for Computer Graphics/exercises/00 Index]]

---

## Where this course sits

Semester **1**. High-school algebra and trig. Programming in parallel helps.

---

## Course goal

By the end, a student can compute dot/cross, multiply small matrices, use homogeneous translation, lerp, and explain a coordinate frame.

---

## Teaching structure

| Part | Duration | What happens |
| --- | --- | --- |
| Lecture | 75 min | Concepts, one derivation or architecture picture |
| Live coding | 60 min | Professor implements the week's kernel |
| Lab | 2–3 hours | Students finish a starter |
| Homework | 4–6 hours | Code + short written |
| Quiz | 10 min | Definitions and one picture |

**Language / tools:** Paper + JS canvas visualizers. No MATLAB required.

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
| 1 | Coordinates and why math | axes, points, units |
| 2 | Vectors | magnitude, add, scale |
| 3 | Dot product | projection, cosine |
| 4 | Cross product | 2D signed area, 3D perpendicular |
| 5 | Lines and planes | parametric, implicit |
| 6 | Matrices 2×2 and 3×3 | multiply, identity |
| 7 | Inverse and systems | 2×2 inverse, det |
| 8 | Midterm and homogeneous | midterm; then w |
| 9 | Rotations in 2D/3D | Ry, composition |
| 10 | Trigonometry for graphics | sin, polar, triangles |
| 11 | Interpolation and curves | lerp, Bezier intro |
| 12 | Frames and change of basis | origin + axes |
| 13 | Into Computer Graphics I | PVM preview |
| 14 | Project studio | math visualizer |
| 15 | Presentations | 12+5 |

---

## What to skip

Eigenvalues as a lab, SVD, quaternions as required code, calculus-heavy curves.

---

## Textbooks / refs

Marschner/Shirley math chapters. 3Blue1Brown Essence of Linear Algebra (videos). Department calc as support, not the syllabus.

---

## One-sentence teaching principle

If they cannot say whether something is a point or a vector, they cannot write M correctly.
