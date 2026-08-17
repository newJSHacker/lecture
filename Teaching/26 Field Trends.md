# 26 — Field trends you can say in a lecture

Parent: [[Teaching/25 Common Sense Anecdotes]]. Craft: [[Teaching/05 Lecture Craft]].

Anecdotes are timeless. **Trends go stale.** This note is dated **August 2026**. Refresh before a new semester (checklist at the bottom). Do not treat a blog’s coverage percentage or a vendor’s “Nx faster” as a fact you write on the board.

These are **40–90 second** Frame lines: what the field is doing *this year*, then the invariant this course still owns.

## How to use

| Do | Do not |
| --- | --- |
| One trend → “so we still…” → today’s kernel | A 15-minute news roundup |
| Name a year and a mechanism | Invent fps, market share, or “everyone uses X” |
| Separate **fashion** (renderer, SaaS name) from **durable CS** (spaces, types, budgets) | Drop WebGL because WebGPU shipped |
| Send a link after class if they want the paper | Make the midterm “explain last week’s Twitter” |

**Say (landing line):** “The trend is the weather. The kernel is the climate. Today we are studying the climate.”

Pick **either** one anecdote **or** one trend per meeting, not both, unless the trend *is* the anecdote (key under the mat + API keys).

---

## Fast picker (by course)

| Course | Trend to mention (Aug 2026) | What you still teach |
| --- | --- | --- |
| Programming | Assistants write the first draft; you still own the bug | Loop, function, stack trace |
| Web | Accessibility is law in the EU market, not a taste | DOM, HTTP, box model |
| Math for CG | Models still multiply the wrong matrix | Point vs vector, frames |
| CG I / WebGL | WebGPU is in major browsers; WebGL is still the idea | Pipeline, triangle, winding |
| Three.js | `WebGPURenderer` / TSL are the engine’s future path | Scene, camera, renderer, units |
| Blender / assets | Prompt-to-mesh is a **draft**; topology is the skill | Metres, UVs, glTF |
| Shaders / RTR | Path tracing looks free in demos; budgets are not | Forward path, PCF, measure |
| GPU | Compute in the browser is normal | Data-parallel recipe |
| Interactive / R3F | “Vibe” a scene; one clock still owns time | rAF vs React |
| XR | Capture looks photoreal; comfort still fails first | Safety, hit-test, fallback page |
| AI graphics | Text-to-3D is a product category; unlabeled is still a fail | Proxy, inspect, provenance |
| Comp Geo | Splats are another primitive, not a predicate | `orient`, degeneracy |
| Capstone | Ship on a phone browser; pin your deps | Tests, a11y, README that loads |
| Advanced CG | IBL and 3DGS are looks; GI is transport | What “bounce” means |

---

## Durable vs fashion (write this once, week 1)

| Fashion (names change) | Durable (this program) |
| --- | --- |
| WebGPU vs WebGL vs a wrapper | Vertices, raster, framebuffer, spaces |
| TSL vs GLSL vs WGSL | A shader is a program over data |
| Three.js vs Babylon vs PlayCanvas | Scene graph, camera, lights, assets |
| Meshy vs Tripo vs Rodin | Inspect: normals, holes, scale, UVs, license |
| 3DGS vs NeRF vs mesh | A representation has a contract (edit? collide? animate?) |
| “Unlimited geometry” in a game engine | A **budget** on the machine in front of you |
| The model that wrote the code | You can explain the black screen |

**Do not:** skip the left column. Mention it so they do not think the course is obsolete. **Do not** replace the right column with the left.

---

## Trends (as of August 2026)

### 1. WebGPU left the experimental sticker

**Say:** “For years WebGPU was ‘Chrome plus a flag.’ By 2026 the major browsers ship it — Safari 26 closed the last big gap in late 2025. Compute shaders in a tab are a normal idea, not a research demo. **We still start in WebGL.** The pipeline — vertex, raster, fragment, framebuffer — did not get replaced. WebGPU is a better kitchen. It is not a different physics of drawing.”

**Point:** New API, same graphics contract. Lab machines may still be WebGL-only; freeze what the room can run.

**Where:** [[WebGL Programming/Lecture 01 GPU pipeline and a triangle]], [[GPU Programming/Lecture 01 GPGPU idea]], Three.js week 1.

**Do not:** quote a coverage percent or a speedup. **Do not** make week 1 WGSL.

### 2. Three.js is walking toward WebGPU / TSL

**Say:** “The engine you will meet at internships is increasingly `WebGPURenderer`, with materials authored as **nodes** (TSL) that compile to WGSL or GLSL. Old `ShaderMaterial` / `onBeforeCompile` paths do not all survive that move. **This course still teaches Scene, camera, renderer, and glTF.** If you understand those, a renderer swap is a migration. If you only memorized one import path, you are stuck in last year’s snippet.”

**Point:** Engines change entry points. The scene graph does not.

**Where:** [[ThreeJS Development/Lecture 01 Scene, camera, renderer]], R3F architecture.

**Do not:** require students to migrate the vendor copy mid-term. Freeze the engine version in the course pack.

### 3. Gaussian splats are entering the standard shelf

**Say:** “Photoreal captures are often **3D Gaussian splats**, not a triangle mesh. In February 2026 Khronos published a **release candidate** for `KHR_gaussian_splatting` — putting splats *into glTF* so viewers do not each invent a `.ply` dialect. As of this note it is still a candidate, not a finished law. **A splat is a look.** It does not give you clean UVs, a hull, or a collider. Picking and CAD still need geometry you can name.”

**Point:** New primitive, old question: what operations does this representation support?

**Where:** CG I “what is a mesh”; [[Blender/Lecture 11 glTF export]]; [[AI for Interactive Graphics/Lecture 04 3D from prompts]]; Advanced CG.

**Do not:** assign “implement a splat rasterizer” in WebGL week 2. **Do not** say the extension is ratified unless you re-check Khronos.

### 4. Prompt-to-3D is a product, not a thesis

**Say:** “Text- and image-to-mesh is a crowded SaaS category in 2026. SIGGRAPH talks are already about whether the output **survives an engine**, not whether it fools a screenshot. That is our lecture: inspect normals, holes, scale, UVs, license. A one-click mesh as the whole homework is a fail. Cleanup is the skill. The vendor name on the slide will be wrong next year. The inspection table will not.”

**Point:** Generation is a draft. The pipeline after the draft is the course.

**Where:** [[AI for Interactive Graphics/Lecture 04 3D from prompts]], Blender import, Capstone assets.

**Do not:** rank Meshy vs Tripo in class. **Do not** paste a vendor latency as if we measured it.

### 5. Three representations, three jobs

**Say:** “The field now juggles **meshes** (edit, rig, collide), **NeRFs** (view-dependent glow, heavy to edit), and **3DGS** (fast novel view, weak as CAD). Jobs will ask you which one you shipped and why. ‘It looks 3D’ is not an answer.”

**Point:** Representation is a design choice with a contract.

**Where:** AI graphics; Advanced CG; Capstone reviews.

### 6. Assistants write code; you still debug

**Say:** “Industry default in 2026 is an assistant in the editor. Students will paste. That does not change the black screen. If you cannot read the stack trace, the assistant is a faster way to be lost. This program grades **explanation and a running file**, not a transcript of the chat.”

**Point:** AI is a tool. Integrity and debug skill are the course. See [[Teaching/12 Academic Integrity and AI]].

**Where:** Programming week 1; every live-coding recovery.

### 7. Types showed up at the internship

**Say:** “A lot of job JS is **TypeScript**. We still freeze **one** language here (JS unless the department already standardized on Python) so the kernel is values, not `tsc`. When they see `vec3` in a `.ts` file, it is the same stamp-vs-arrow idea: the type is a contract the compiler nags you about. GLSL already had types. They were not optional.”

**Point:** Types are named contracts. We teach the contract first.

**Where:** Programming; Modern JS; shaders (`vec3` vs `float`).

### 8. Accessibility is a market rule, not extra credit

**Say:** “The European Accessibility Act **applies from 28 June 2025** for many consumer digital services sold in the EU. 2026 is the first full year people are checking. Keyboard, contrast, captions, an accessibility statement — this is how you ship, not a bonus slide. A canvas-only 3D page with no DOM fallback is a product risk, not a style.”

**Point:** A11y is in the spec. Stairs-only building from the anecdote note is now also a legal weather report.

**Where:** Web Technologies; Interactive Web; Capstone; [[Teaching/10 Inclusive Teaching and Accessibility]].

**Do not:** play lawyer about whether *this* student project is in scope. Teach the habit.

### 9. glTF is still how the web carries 3D

**Say:** “Film and DCC talk **OpenUSD**. The browser still eats **glTF** (and now, tentatively, splats *inside* glTF). Export checklists exist because ‘it opened in Blender’ is not ‘it opened in Three.js.’ Units, metres, winding, one texture set.”

**Point:** Interchange format is an interface. Same class of bug as Mars orbiter units.

**Where:** [[Blender/Lecture 11 glTF export]], Three.js loaders, Capstone.

### 10. Real-time path tracing is a demo, not a free lunch

**Say:** “Game and GPU vendors will show **path-traced** stills that look like film. On a phone tab, you still have a budget. This course still owns forward rendering, shadow maps, PCF, and ‘measure, don’t invent the frame time.’ When a student says ‘why not just path-trace?’ the answer is: because the machine in front of you is not the keynote laptop.”

**Point:** Looks are not a pipeline. RTR is constraints.

**Where:** [[Real-Time Rendering/Lecture 01 Forward rendering review]], [[Real-Time Rendering/Lecture 07 PCF and filter]], Capstone budgets.

### 11. Compute on the GPU is a web skill now

**Say:** “Particles, sorts for splats, even on-device ML — people put that work in **compute shaders** because the CPU walk is the old bottleneck. GPU Programming is not a niche elective for 2026. It is why ‘the same recipe every plate’ from the anecdote note matters.”

**Point:** Data-parallel programs are how you use the kitchen.

**Where:** [[GPU Programming/Lecture 01 GPGPU idea]], shaders.

**Do not:** assign an LLM in WGSL as homework.

### 12. WebXR is still a URL, still a stomach

**Say:** “Stores want installs. The open web still wants a **link**. WebXR is how this program ships XR without an app-store week. Comfort, locomotion, and a 2D fallback page did not get optional because captures look photoreal.”

**Point:** Distribution is a URL. Safety is a requirement.

**Where:** [[XR/Lecture 01 WebXR overview]], XR safety week.

### 13. Supply chain is why we vendor

**Say:** “The `left-pad` story is old. The habit is not: a deleted package, a CDN Tuesday, a typo in an import. **This program still has no CDN.** You vendor what you teach. Capstone pins versions. That is 2026 industry hygiene, not nostalgia.”

**Point:** Dependencies are part of the binary.

**Where:** Web week 1; Three.js; Capstone.

### 14. Secrets in the page are still the intern bug

**Say:** “Every year a tutorial puts an API key in client JS because ‘it worked in the demo.’ Models got cheaper. The key under the mat did not get safer. Proxy on the server, or do not call the API.”

**Point:** Same invariant as [[AI for Interactive Graphics/Lecture 02 APIs and keys]].

### 15. Third-party cookies and ‘just add analytics’

**Say:** “Browsers spent years killing the old tracking cookie. ‘Drop this script’ is no longer a harmless footer. For class sites: first-party, local, no surprise network. For jobs: know that **privacy is part of Web Technologies**, not a legal elective.”

**Point:** Network tab is a lab instrument. Surprise requests are a bug.

**Where:** Web Technologies; Capstone README / ethics.

### 16. CSS got features; the box model did not retire

**Say:** “Container queries, native nesting, view transitions — internships will use them. Week 2 of Web is still **document, cascade, box**. If they cannot inspect a layout, a view transition is choreography on a broken stage.”

**Point:** New CSS is not a substitute for the box model.

**Where:** Web Technologies layout weeks.

### 17. PBR is the default look; energy is still a sentence

**Say:** “Principled / metallic-roughness is what glTF carries. Students will treat it as a preset named ‘realistic.’ It is still a **model** with parameters. IBL is still not GI.”

**Point:** Photocopy of a window remains the anecdote.

**Where:** [[Blender/Lecture 05 Principled BSDF]], RTR materials.

### 18. Mobile is the real exam

**Say:** “iPhones now run WebGPU in Safari. That does not mean the lab’s 4GB laptop is the customer. Capstone still ships a **budget** and a test on a phone in someone’s bag. Thermal throttle is a real-time renderer.”

**Point:** Measure on the target. Do not invent the frame time.

**Where:** Capstone; RTR; XR performance.

---

## What students will ask (and the one-sentence answer)

| They say | You say |
| --- | --- |
| “Why WebGL if WebGPU exists?” | Because you must see the pipeline once without an engine. Then the new API is a dialect. |
| “Why not only splats?” | Because your configurator must pick, price, and animate parts. Splats don’t bill a SKU. |
| “Why model in Blender if AI meshes?” | Because the gen mesh fails inspection. Cleanup and units are the job. |
| “Why write shaders?” | Because TSL/nodes still compile to a program over vertices and pixels. Someone must know that program. |
| “Why not skip math?” | Because the model will still be in the wrong space. You will not notice until the shadow crawls. |
| “Is this course outdated?” | Names on npm are. `P*V*M`, HTTP, and a named frame are not. |

---

## Do not chase (this year or any year)

- Rewriting the 15-week WebGL course into WGSL because a thread said WebGL is dead.
- A midterm question on a SaaS pricing page.
- “Nanite in the browser” as an excuse for unbounded triangle dumps.
- A guest lecture that is only a product demo with no student attempt.
- Quoting SIGGRAPH keynote fps on the board.

If a trend would delete a kernel in [[01 subjects]], it is not a trend you teach. It is a distraction.

---

## Pairing with anecdotes

| Trend | Anecdote from [[Teaching/25 Common Sense Anecdotes]] |
| --- | --- |
| WebGPU kitchen | Two kitchens (CPU/GPU) |
| TSL / one shader two backends | Same cookie cutter |
| Splats in glTF | Map is not the territory |
| Prompt-to-mesh | Unlabeled photograph; wrong-size clothes |
| Assistants | Looking under the lamp |
| EAA / a11y | Stairs-only building |
| Path tracing demos | Measuring the soup |
| API keys | Key under the mat |
| No CDN | Restaurant + supply chain (`left-pad`) |
| Units / glTF | Mars Climate Orbiter |

---

## Refresh this note (once per semester)

Sunday before week 1, spend **20 minutes**:

1. Can I Use / MDN: WebGPU, WebXR — still “shipped” on the browsers your lab uses?
2. Khronos: is `KHR_gaussian_splatting` still RC or ratified? Fix the sentence. Do not guess.
3. Three.js: did the course vendor pin change? If yes, update the freeze, not the kernel.
4. One AI-graphics product still in the news — **do not** add it as required software; add it as “inspect this class of output.”
5. Delete any speedup number you did not measure.

If you did not refresh, say “as of last year’s note” out loud. Students can smell a fake 2024 statistic in 2026.

---

## Prep on Sunday

On the one-pager ([[Teaching/03 Lesson Planning]]):

1. Kernel (climate).
2. **Either** one anecdote **or** one trend (weather), not a stack of both.
3. The sentence “so we still…” already written in the session guide.

The attempt phase stays. News does not replace them typing.
