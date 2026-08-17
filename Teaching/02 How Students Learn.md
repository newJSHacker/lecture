# 02 — How students learn

Teaching that ignores how memory and attention work becomes a slide show. This note is the minimum cognitive science an IGWT instructor should use.

## Working memory is small

Students can hold only a few new pieces at once. A WebGL first lecture that introduces buffers, shaders, the GL context, clip space, and npm in 70 minutes will overflow almost everyone.

**Move:** one new idea per 15–20 minutes, then a 3-minute check.

| Overloaded lecture | Repaired lecture |
| --- | --- |
| “Today: pipeline, VBOs, VAOs, GLSL, uniforms, textures” | “Today: one triangle. The pipeline exists so this triangle can happen.” |
| 40 new API names | 6 names, written on the board, reused |
| Shader + React + bundler on day 1 | Canvas 2D or a single HTML file first |

## Cognitive load (three kinds)

1. **Intrinsic** — the idea is actually hard (clip space, degeneracy, PBR). You cannot remove this. You can sequence it.
2. **Extraneous** — the way you present it adds junk (tiny font, unexplained repo, broken starter, three competing diagrams).
3. **Germane** — effort that builds the schema (predict the next pixel, trace one vertex).

Your job is to cut extraneous load so students can spend effort on germane load.

**IGWT extraneous-load classics:**

- Asking them to install three toolchains in the first lab
- Switching handedness conventions mid-semester without a flag
- Showing a production repo as the first example
- Talking while a shader is compiling and the error is off-screen
- Using a different variable naming scheme than the starter

## Dual coding

Geometry and graphics are spatial. Say it **and** draw it. Then make it move.

| Topic | Words only (weak) | Word + picture + motion (strong) |
| --- | --- | --- |
| Convex hull | “Smallest convex set” | Rubber band animation, then code |
| MVP matrix | “Model, view, projection” | Move the cube, then the camera, then the frustum |
| Fragment shader | “Runs per fragment” | Color by `gl_FragCoord`, then by UV |
| Sweep line | “Status is the segments the line hits” | Vertical line moving, status listed live |

If you cannot draw it, you are not ready to lecture it.

## Retrieval beats rereading

Students who only rewatch your recording feel fluent and fail the quiz. Fluency is not knowledge.

Build retrieval into the week:

- Opening: two questions from last week, on paper or a tiny quiz
- Mid-lecture: “Write the sign of `orient` for this picture”
- Lab start: “From memory, list the pipeline stages”
- Homework: one question with no notes, then the rest with notes

Weekly quizzes in [[02 Curriculum Design Advice]] exist for this reason. Do not cancel them because they are annoying to grade. Make them short. See [[Teaching/09 Assessment Design]].

## Worked examples before open problems

Novices learn procedures from studying complete solutions while attention is guided. Experts underestimate this because they no longer need it.

Sequence for a new algorithm or shader:

1. You implement it, narrating decisions and mistakes.
2. They trace your code on a new input.
3. They change one parameter and predict the picture.
4. They implement a close variant from a starter.
5. Only then: a blank-file or project-sized task.

Skipping to step 5 is how labs become copy-paste sessions.

## Desirable difficulty

Struggle that is **in the problem** helps. Struggle that is **in the tooling** rarely helps.

| Desirable | Not desirable |
| --- | --- |
| Why this point is left of the line | npm peer-dependency hell |
| Finding the illegal edge | A 400-line starter with no comments |
| A shader that compiles but looks wrong | A machine that cannot install GPU drivers in the lab |

Fix environment pain before class. Put the intellectual pain in the predicate, the invariant, or the visual bug.

## Motivation (brief and practical)

Students work when three things are present (self-determination, in classroom language):

- **Competence:** “I can make a triangle / a hull / a material.” Early wins.
- **Autonomy:** constrained choices (“pick the scene, not the stack”).
- **Relatedness:** names, pair work, public demos that are kind.

Grades motivate compliance. Visible progress motivates craft. Use both.

## Novice–expert differences in this field

| Novice | Expert (you) |
| --- | --- |
| Sees a black screen as “WebGL is broken” | Sees a black screen as a checklist (clear color, camera, winding, depth, shader compile) |
| Copies a matrix from Stack Overflow | Asks which space the vector is in |
| Treats NaN as random | Treats NaN as a predicate or divide |
| Wants the library to hide GL | Wants to know what the library hid |

Teach the expert’s **checklist**, not only the expert’s **result**.

## Transfer does not happen by magic

A student who can convex-hull in the visualizer will not automatically pick a mesh in Three.js. You must assign the transfer.

At the end of a topic, give a 15-minute “where this shows up” slide that is actually a task:

- Hull → silhouette of a 2D gadget in a configurator
- Delaunay → terrain from a height sample
- BVH → click-to-select a part
- Shader normals → a bent normal on a baked asset

## Misconceptions you should plan to hit

Keep a running list per course. Examples:

- “Clockwise vs counter-clockwise does not matter if it looks fine on my machine”
- “A texture is just an image; color space is optional”
- “More triangles always look better”
- “`position.set` and a transform matrix are interchangeable thoughts”
- “If it runs at 60 FPS in the lab, it is optimized”
- “AI-generated shader code is a starting point I understand”

Address each with a demo that breaks the belief.

## Sleep, spacing, and cramming

A 15-week course already spaces practice if you reuse old kernels. Do that on purpose: Week 7 should still call `orient`. Week 13 should still break on a degenerate mesh.

Say this once, early: the night before the midterm is too late to learn clip space.

## Exercise

Take your next lecture. Cut it until a student can do **one** retrieval task at minute 25 and **one** construction task at minute 55. If you cannot, the lecture has too many ideas.
