# WebGL Programming

A 15-week university course for the **Interactive Graphics and Web Technologies (IGWT)** program.

The GPU API: buffers, shaders, uniforms, textures, depth, FBOs. Students struggle a little on purpose.

Source of teaching format: [[02 Curriculum Design Advice]]

**Lecture notes:** [[WebGL Programming/00 Lectures]]  
**Exercises:** [[WebGL Programming/exercises/00 Index]]

---

## Where this course sits

Semester **3**. [[10 Computer Graphics I]] and JS modules. Do not start from Three.js.

---

## Course goal

By the end, a student can draw a lit textured mesh with their own GLSL and explain every uniform.

---

## Teaching structure

| Part | Duration | What happens |
| --- | --- | --- |
| Lecture | 75 min | Concepts, one derivation or architecture picture |
| Live coding | 60 min | Professor implements the week's kernel |
| Lab | 2–3 hours | Students finish a starter |
| Homework | 4–6 hours | Code + short written |
| Quiz | 10 min | Definitions and one picture |

**Language / tools:** WebGL2, [[WebGL/demos]], [[07 WebGL and Shader Snippets]]. No Three.js in labs.

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
| 1 | GPU pipeline and a triangle | WebGL2 context, first triangle |
| 2 | Buffers and attributes | ARRAY_BUFFER, layout |
| 3 | GLSL ES 3.00 | version, precision, in/out |
| 4 | Uniforms | mat4, time, colors |
| 5 | A cube and depth | indices, DEPTH_TEST, cull |
| 6 | Textures | upload, UV, sampling |
| 7 | Camera matrices | P V M in the shader |
| 8 | Midterm and lighting start | midterm; Lambert in FS |
| 9 | Phong / Blinn in GLSL | varyings, gamma |
| 10 | Multiple objects | scene loop, many uniforms |
| 11 | Framebuffer objects | render to texture |
| 12 | Instancing | divisor, one draw |
| 13 | Debug and a mini engine | checklist, abstraction |
| 14 | Project studio | mini WebGL engine |
| 15 | Presentations | 12+5 |

---

## What to skip

Vulkan, WebGPU (GPU course), full engine editor.

---

## Textbooks / refs

WebGL2 fundamentals (webgl2fundnfundn). Khronos WebGL spec as reference. CG I notes.

---

## One-sentence teaching principle

If they cannot explain gl_Position, they are not allowed to hide in Three.js yet.
