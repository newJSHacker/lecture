# AI for Interactive Graphics

A 15-week university course for the **Interactive Graphics and Web Technologies (IGWT)** program.

Use models as components in interactive graphics: proxies, textures, honest 3D-gen limits, tool-using agents, RAG, latency, and evaluation — with integrity logs and no frontend secrets.

Source of teaching format: [[02 Curriculum Design Advice]]

**Lecture notes:** [[AI for Interactive Graphics/00 Lectures]]  
**Exercises:** [[AI for Interactive Graphics/exercises/00 Index]]

---

## Where this course sits

Semester **5**. [[18 Three.js Development]] or [[23 Interactive Experience Development]]. Web fetch from [[13 Web Technologies]].

---

## Course goal

By the end, a student can ship one AI-backed graphics feature with a proxy, an asset table, and a scored eval — without leaking keys.

---

## Teaching structure

| Part | Duration | What happens |
| --- | --- | --- |
| Lecture | 75 min | Concepts, one derivation or architecture picture |
| Live coding | 60 min | Professor implements the week's kernel |
| Lab | 2–3 hours | Students finish a starter |
| Homework | 4–6 hours | Code + short written |
| Quiz | 10 min | Definitions and one picture |

**Language / tools:** Node proxy or mock server, Three.js/R3F, vendor API optional.

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
| 1 | Scope and ethics | what this course is not |
| 2 | APIs and keys | server proxy |
| 3 | Image as texture | gen → glTF/Three |
| 4 | 3D from prompts | limits of image-to-3D |
| 5 | Agents that act | tools, loops |
| 6 | RAG idea | retrieve then generate |
| 7 | Integrity workflows | what students must log |
| 8 | Midterm and latency | midterm; streaming, placeholders |
| 9 | Vision models | image in, labels out |
| 10 | Audio | STT/TTS names |
| 11 | Configurator + AI | constrained generation |
| 12 | Evaluation | rubrics for gen |
| 13 | A thin slice | one AI feature in a scene |
| 14 | Project studio | AI + graphics mini |
| 15 | Presentations | 12+5 |

---

## What to skip

Training large models, CUDA ML from scratch, medical/legal product claims.

---

## Textbooks / refs

Vendor API docs (selected). Teaching handbook integrity chapter. RAG survey (teaching level).

---

## One-sentence teaching principle

If the key is in the repo or the asset is unlabeled, the project fails before aesthetics.
