# 18 — Course-by-course teaching notes

Curriculum map: [[01 subjects]]. Weekly machine: [[02 Curriculum Design Advice]]. This note is the **instructor’s field guide**: what is hard, what to freeze, what to assess.

## 1. Introduction to Programming

**Hard:** students think typing is thinking; they cannot debug.

**Freeze:** one language all term.

**Do:** lots of tiny programs with visible output; a style guide; autograder for functions.

**Do not:** start with a framework.

**Assess:** functions, loops, a small project they can explain line by line.

**Live coding:** errors on purpose. Read the stack trace out loud.

## 2. Web Technologies

**Hard:** the browser is an operating system; they only see tags.

**Freeze:** HTML/CSS/JS without a bundler for weeks.

**Do:** DevTools as a lab instrument; one layout they clone badly on purpose.

**Do not:** a full React app in week 2.

**Assess:** a page they can inspect; explain reflow vs paint at a basic level.

## 3. Mathematics for Computer Graphics

**Hard:** math class energy; they do not see a camera.

**Freeze:** 2D first, then 3D; one convention for column/row.

**Do:** every week a picture and a tiny code check (even in Python).

**Do not:** proofs without a geometric object.

**Assess:** transform a point; interpret a dot product; a short oral with a whiteboard.

## Computational Geometry (Semester 2)

Full plan: [[04 Computational Geometry]]. Notes: [[Computational Geometry/00 Lectures]].

**Hard:** degeneracy and floating point; they want libraries.

**Freeze:** `orient` sign and the shared visualizer.

**Do:** hidden fixtures; plant collinear points.

**Do not:** 3D computational geometry in week 4.

**Assess:** kernel tests + visual + a short invariant question.

## 4. Computer Graphics I

**Hard:** spaces (object/world/view/clip); they mix them.

**Freeze:** right-handed, one engine (Three.js **or** a tiny custom pipeline, not both at once).

**Do:** move the camera live; draw the spaces every lecture.

**Do not:** PBR in week 2.

**Assess:** a scene with a camera they can explain; a paper transform.

## 5. Modern JavaScript Development

**Hard:** tooling as identity; they configure instead of thinking.

**Freeze:** one bundler or none; TypeScript only if you will grade types.

**Do:** modules, async, performance of a real loop (particles, not TODO apps only).

**Assess:** a small library with tests; a performance note.

## 6. Interactive Web Development

**Hard:** animation as decoration; they cannot reason about time.

**Do:** requestAnimationFrame, easing, one GSAP sequence they rebuild.

**Do not:** five libraries.

**Assess:** a motion they can retarget; accessibility of motion (prefers-reduced-motion).

## 7. WebGL Programming

**Hard:** state machine + shaders + buffers at once.

**Freeze:** raw WebGL (or a 50-line wrapper you wrote). No Three.js this course.

**Do:** triangle → square → cube → texture → light. Draw the pipeline every time. Live-code from [[07 WebGL and Shader Snippets]] demos 01–08.

**Do not:** start with a 1,000-line engine.

**Assess:** they can get a black screen to a triangle using the checklist ([[Teaching/06 Live Coding Pedagogy]]).

## 8. Three.js Development

**Hard:** the library hides the pipeline they just learned; they forget it.

**Do:** keep asking “what is this in GL?” Load glTF; lights; a simple optimize (instance or fewer lights).

**Do not:** every add-on in the examples folder.

**Assess:** a loaded model, one interaction, a README that runs.

## 9. Blender for Real-Time Graphics

**Hard:** film habits (too many polys, huge textures, wrong scale).

**Freeze:** glTF export path; meters; texel density target.

**Do:** budget sheet (tris, maps, materials). Look at the model in the Three.js viewer the same day.

**Assess:** an asset that runs at a stated budget, not a beautiful sculpture that dies on mobile.

## 10. Shader Programming

**Hard:** they copy Book of Shaders aesthetics without a model of the pipeline.

**Do:** one change → one picture. Noise, then a use (terrain, fire). Warn for flashing. Starters: [[07 WebGL and Shader Snippets]] demos 09–12.

**Assess:** five small shaders with comments on the math, or two deeper ones. Oral: “what is in the fragment?”

## 11. Real-Time Rendering

**Hard:** vocabulary explosion (PBR, IBL, AO, HDR).

**Do:** one effect per week, with a before/after and a cost.

**Do not:** implement every paper.

**Assess:** a scene with two effects they can turn off and measure.

## 12. GPU Programming

**Hard:** GPGPU mental model; they think the CPU loop is the same.

**Do:** particles or a small sim; then a WebGPU preview without abandoning the term’s stack.

**Assess:** a measurement and a limitation paragraph.

## 13. Interactive Experience Development

**Hard:** design taste + engineering; they hide in one.

**Do:** R3F (or equivalent) as architecture, not magic. Scroll, UI, audio as systems.

**Assess:** a small award-style slice that is finishable; critique on criteria ([[Teaching/07 Labs and Studio]]).

## 14. Virtual & Augmented Reality

**Hard:** hardware inequality; comfort (locomotion, IPD, nausea).

**Do:** interaction first, headset second. Provide lab headsets. Comfort checklist.

**Assess:** an interaction that works seated if needed; a safety/comfort note.

## 15. AI for Interactive Graphics

**Hard:** they generate assets they cannot control; ethics is a slide they skip.

**Do:** AI as a pipeline stage with licenses, disclosure, and a human-editable output. See [[Teaching/12 Academic Integrity and AI]].

**Assess:** a system that uses an API **and** a critique of failure modes, not a folder of pretty images.

## 16. Advanced Computer Graphics

**Hard:** papers. Undergraduates drown.

**Do:** one paper carefully; implement a toy version; compare to the production approximation.

**Assess:** a reproduction attempt with honesty about what they did not implement.

## 17. Capstone

**Hard:** teams, scope, denial.

**Do:** sprints, reviews, external demo, individual orals. [[Graduation Requirements]]

**Do not:** a new research field in 15 weeks.

**Assess:** running system + docs + talk + individual understanding.

## Exercise

For the course you teach next, write the **Hard / Freeze / Do / Do not / Assess** five lines on a card. If you cannot, you are still covering, not teaching.
