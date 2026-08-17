Full 15-week notes for every course: [[00 IGWT Lectures]]. Printable: [IGWT.pdf](IGWT.pdf). How to run a meeting: [[Teaching/24 Session Guides]].

IGWT is one argument, not a pile of electives. A student learns to **see a value**, then **put a pixel**, then **talk to the GPU**, then **ship an experience in the browser**. Each course below is a missing skill if you skip it — not a flavour.

The four flagship courses of the specialization are **Computer Graphics I**, **WebGL**, **Shader Programming + Real-Time Rendering**, and **Interactive Web**. The rest exist so those four are honest.

---

## Semester 1

### 1. Introduction to Programming

Plan: [[12 Introduction to Programming]] · notes: [[Programming/00 Lectures]]

- Python or JavaScript (JavaScript unless the department already standardized on Python)
- Algorithms
- Problem Solving

**Why you need it.** A renderer is a program. If you cannot name a value, branch, loop, write a function that **returns**, and read a stack trace, you cannot later write `putPixel`, `orient`, or `clamp`. The black screen in WebGL is the same disease as a silent `undefined` in week 1: you cannot debug what you cannot see. This course is computational thinking in the language the rest of IGWT uses, so Canvas, WebGL, and Three.js are not a second language.

**Where it is useful.** Every later lab. Computer Graphics I is nested loops over pixels. Computational Geometry is predicates in functions with tests. Modern JS and the capstone assume modules, search, and `console.assert`. Jobs: any software role; specifically the **kernel** of a graphics tool (tests, a function, a loop) rather than clicking an editor.

Teaching principle: *if they cannot write a loop and a function, they cannot write a renderer.*

---

### 2. Web Technologies

Plan: [[13 Web Technologies]] · notes: [[Web Technologies/00 Lectures]]

- HTML
- CSS
- JavaScript
- HTTP
- Browser Fundamentals

**Why you need it.** IGWT ships **in the browser**, not first in a desktop OpenGL window. A canvas, a HUD, a glTF file, and an AI proxy all arrive as HTTP, HTML, CSS, and a DOM. If you cannot inspect Elements and Network, you will treat a 404 texture as a “shader bug” for four semesters. Semantic HTML and the box model are how a configurator UI sits on top of WebGL without becoming a screenshot.

**Where it is useful.** Interactive Web (animation loop on a page). Three.js and R3F HUDs. XR fallback pages. AI course: `fetch` to a **server** proxy, never a key in the frontend. Capstone: README that actually loads. Jobs: front-end engineering, visualization websites, product pages with 3D, anything that must work on a phone browser.

Teaching principle: *if they cannot inspect the DOM, they cannot debug a configurator UI on top of WebGL.*

---

### 3. Mathematics for Computer Graphics

Plan: [[14 Mathematics for Computer Graphics]] · notes: [[Mathematics for Computer Graphics/00 Lectures]]

- Vectors
- Matrices
- Geometry
- Linear Algebra
- Trigonometry

**Why you need it.** A cube is vertices. A camera is a matrix. Lighting is a dot product. A triangle’s front face is a cross product. If you cannot say **point vs vector**, or why translation needs a homogeneous `1`, you will copy `M` from a blog and mix row-vector formulas with this program’s column vectors. This is not a linear-algebra major. It is the algebra Computer Graphics I will spend on pictures.

**Where it is useful.** Computer Graphics I (pipeline, `lookAt`, Lambert). Computational Geometry (`orient` is 2D cross). WebGL camera uniforms. Shaders (lerp, noise domains, SDF). Blender: the same axes and units. Jobs: games, CAD, robotics kinematics, any role that multiplies a point by a matrix and must know which space it is in.

Teaching principle: *if they cannot say whether something is a point or a vector, they cannot write M correctly.*

---

### Computational Geometry (recommended, Semester 2)

Teach after Mathematics for Computer Graphics and Introduction to Programming. Full plan: [[04 Computational Geometry]]

- Geometric predicates and degeneracy
- Convex hulls
- Segment intersection (sweep line)
- Polygon triangulation
- Voronoi diagrams and Delaunay triangulation
- kd-trees / point location
- Applications in picking, collision, meshes, and terrain

**Why you need it.** Graphics looks continuous and is answered with **discrete tests**: did this click hit the polygon? do these walls cross? which triangle contains the ray? who is the nearest site to this pixel? Naive code fails on collinear points and floating-point lies. Predicates (`orient`) before constructions; degeneracy is the course, not an appendix. Computer Graphics I tells you the colour of a pixel; this course tells you **which** geometric object you meant.

**Where it is useful.** Picking in a configurator. Collision and CSG-ish clips. Terrain and meshes (Delaunay). Ray–triangle and BVH as the same idea in 3D. Advanced CG tracers. Jobs: GIS, CAD kernels, game physics/query, mapping, mesh processing.

---

## Semester 2

### 4. Computer Graphics I

Full plan: [[10 Computer Graphics I]] · lecture notes: [[Computer Graphics/00 Lectures]]

- Rendering pipeline of spaces (object → pixel)
- Software rasterizer (Canvas `ImageData`, barycentric, z-buffer)
- Transformations and scene graphs
- Cameras (`lookAt`) and projection
- Lambert / Blinn-Phong, gamma
- Textures
- Map the same scene onto WebGL / Three.js in Week 13 (not the weekly engine)

**Why you need it.** Until you have filled a triangle yourself, the GPU is a shrine. This course builds the arrow `geometry + camera + light + material → framebuffer` in JavaScript so WebGL and Three.js later are **maps of a pipeline you already wrote**, not magic. Six spaces (object → world → view → clip → NDC → pixels) is the board photograph of the whole specialization. Conventions are frozen here: right-handed, Y-up, look −Z, `P*V*M`, CCW ([[WebGL/01 Conventions]]).

**Where it is useful.** WebGL (`gl_Position` is clip). Three.js (`Mesh` is a draw call). Real-Time Rendering (Lambert was bounce 0). Shaders (barycentric, UVs, gamma). Capstone: you can name which stage is slow. Jobs: rendering engineer, technical artist who can talk to engineers, anyone who must not confuse a material slider with a projection matrix.

This is a **flagship** course.

---

### 5. Modern JavaScript Development

Plan: [[15 Modern JavaScript Development]] · notes: [[Modern JavaScript/00 Lectures]]

- ES6+
- Modules
- Tooling
- TypeScript (optional)
- Performance

**Why you need it.** Semester 1 JS is a console program. A renderer, a Three.js app, and a capstone are **multi-file modules** with `fetch`, tests, and no hidden globals. `file://` breaking ES modules is the same lesson as serving WebGL demos. If the kernel is not a module with a test, it will not survive week 14.

**Where it is useful.** WebGL and Three.js import maps (local vendor, no CDN). Interactive Experience (React as a host). AI course (async APIs). Capstone repo layout. Jobs: web engineering, graphics tools in JS, any team that reviews pull requests instead of one 400-line file.

Teaching principle: *if it is not a module with a test, it is not a kernel.*

---

### 6. Interactive Web Development

Plan: [[16 Interactive Web Development]] · notes: [[Interactive Web/00 Lectures]]

- Canvas API
- SVG
- CSS Animation
- GSAP
- Browser Rendering

**Why you need it.** 3D is not the first interactive picture. **Time** (`requestAnimationFrame`), **input** (pointer mapping), and **a clear** are the kernel of every later loop — including WebGL’s `drawArrays` and WebXR’s frame callback. CSS and GSAP teach motion on the document; Canvas 2D teaches a framebuffer you own. Libraries only after that works. WebGL is the next semester, not this one.

**Where it is useful.** HUDs over Three.js. Data visualization. 2D editors, SVG+canvas hybrids, scroll-driven scenes. Capstone UI that is not orbit-only. Jobs: interactive agencies, newsroom graphics, web games, marketing sites that must animate without a 3D engine.

Teaching principle: *time, input, and a clear are the kernel; libraries only after that works.*

This is a **flagship** course (interactive web technologies).

---

## Semester 3

### 7. WebGL Programming

Plan: [[17 WebGL Programming]] · notes: [[WebGL Programming/00 Lectures]] · catalog: [[07 WebGL and Shader Snippets]]

- WebGL API
- Buffers
- Shaders
- Uniforms
- Textures
- Rendering

**Why you need it.** The browser’s GPU API is WebGL (then WebGPU in the GPU course). CPU fills buffers; GPU runs the shader; you must explain **every uniform**. Three.js is forbidden as the first triangle: if they cannot explain `gl_Position`, they are not allowed to hide in an engine yet. This is Computer Graphics I **on the device**, with GLSL ES, depth, textures, and your own camera matrices.

**Where it is useful.** Shader Programming (fullscreen and mesh shaders). Real-Time Rendering (the passes you will name). GPU Programming (FBO ping-pong starts here). Three.js (what the engine hid). Jobs: custom materials, WebGL engines, debug of black screens, any role that cannot wait for a framework bugfix.

Teaching principle: *if they cannot explain gl_Position, they are not allowed to hide in Three.js yet.*

This is a **flagship** course.

---

### 8. Three.js Development

Plan: [[18 Three.js Development]] · notes: [[ThreeJS Development/00 Lectures]] · catalog: [[08 Three.js Snippets]]

- Scene
- Camera
- Materials
- Lighting
- Animation
- Model Loading
- Optimization

**Why you need it.** Production web 3D is almost never raw `drawArrays` for a whole product. Three.js is the **engine** you will ship — and it is a map of WebGL, not a replacement for it. Load glTF, light it, pick a mesh, and say which WebGL objects the engine hid. Local vendor only (no CDN). If they cannot map `Mesh` to a draw call, they are using a magic box.

**Where it is useful.** Blender export target. R3F (same scene graph in React). XR helpers. AI: generated image as a texture on a real mesh. Capstone configurators, museums, walkthroughs. Jobs: product visualization, web 3D, e-commerce 3D, architectural viewers.

Teaching principle: *if they cannot map Mesh to a draw call, they are using a magic box.*

---

### 9. Blender for Real-Time Graphics

Plan: [[19 Blender for Real-Time Graphics]] · notes: [[Blender/00 Lectures]]

- Modeling
- UV Mapping
- Materials
- Animation
- Export to glTF

**Why you need it.** Half of a “graphics bug” is the **asset**: unknown units, unapplied rotation, inverted normals, UVs that do not exist, a 4k texture on a bolt, Principled slots that do not match glTF. This course is real-time export, not a film VFX major. If it is wrong in a glTF viewer, the engine is not the bug.

**Where it is useful.** Every Three.js / R3F / XR / capstone scene that is not a primitive. Baking maps for WebGL. Triangle budgets you will measure, not invent. Jobs: technical artist, real-time asset pipeline, anyone who hands a `.glb` to an engineer.

Teaching principle: *if it is wrong in a glTF viewer, the engine is not the bug.*

---

## Semester 4

### 10. Shader Programming

Plan: [[20 Shader Programming]] · notes: [[Shader Programming/00 Lectures]]

- GLSL
- Vertex Shader
- Fragment Shader
- Noise
- Ray Marching
- Signed Distance Fields (SDF)
- Procedural Generation

**Why you need it.** Look lives on the GPU as a **program**, not a JPEG. Noise, SDF, and ray marching make oceans, fire, and fonts without a mesh farm. A Shadertoy you cannot pause, uniform, and debug is a clip, not a course. This sits on WebGL + math: GLSL is C-like, but the mental model is “this runs per vertex or per pixel.”

**Where it is useful.** Real-Time Rendering materials and post. GPU particles (same language). Three.js `ShaderMaterial` without cargo-cult. Advanced CG (volumes as a cousin of ray marching). Jobs: shader / look-dev artist, procedural content, stylized games, web hero effects.

Teaching principle: *a shader you cannot pause, uniform, and debug is a clip, not a program.*

This is a **flagship** course (with Real-Time Rendering).

---

### 11. Real-Time Rendering

Plan: [[21 Real-Time Rendering]] · notes: [[Real-Time Rendering/00 Lectures]]

- Physically Based Rendering (PBR)
- HDR
- Bloom
- Shadow Mapping
- Ambient Occlusion
- Post-processing

**Why you need it.** Computer Graphics I and WebGL drew **local** light (Lambert, Blinn). Products expect metal-rough PBR, shadows, HDR, and a post stack — and a **frame budget**. A look without a named pass list and a measurement on a named device is a screenshot, not real-time rendering. Do not invent fps; measure or omit. IBL is not full GI (that wait is Advanced CG).

**Where it is useful.** Capstone look-dev. Three.js as an oracle after the picture is drawn on the board. GPU post passes. Talking to art about why bloom is not “more light.” Jobs: real-time look-dev, games, visualization, any role that must drop a pass to hit 60 on a laptop.

Teaching principle: *a look without a stack graph and a measurement is a screenshot, not real-time rendering.*

This is a **flagship** course.

---

### 12. GPU Programming

Plan: [[22 GPU Programming]] · notes: [[GPU Programming/00 Lectures]]

- GPGPU
- Framebuffer Objects (FBO)
- Particle Systems
- Simulations
- Introduction to WebGPU

**Why you need it.** Drawing triangles is one use of the GPU. Particles, fluids teasers, ping-pong FBOs, and compute are **data-parallel programs**. If they cannot draw the memory layout, they are running a sample, not programming a GPU. WebGPU is introduced after WebGL compute hacks so they see why a new API exists — not as week 1.

**Where it is useful.** Simulation-heavy capstones. Post and particles in RTR. Advanced CG (who does the work: raster vs tracer vs compute). Jobs: GPGPU, physics/particle tools, WebGPU migration, scientific viz in the browser.

Teaching principle: *if they cannot draw the memory layout, they are running a sample, not programming a GPU.*

---

## Semester 5

### 13. Interactive Experience Development

Plan: [[23 Interactive Experience Development]] · notes: [[Interactive Experience/00 Lectures]]

- React Three Fiber
- Motion
- UI Integration
- Audio Visualization
- Creative Coding

**Why you need it.** A spinning cube with orbit controls is a **scene**, not an experience. This course adds a shot list, a HUD, a keyboard path, accessibility, loading UX, and a budget table. React Three Fiber is the usual web-product shape: two clocks (React state vs the frame loop) that students must not fight silently. Creative coding habits without throwing away engineering.

**Where it is useful.** Capstone product shape. XR spatial UI (same interaction questions). AI configurator (UI + 3D). Jobs: creative technologist, experiential / museum web, any 3D page that must work with a keyboard and a screen reader story.

Teaching principle: *if the only interface is orbit-drag, it is a scene, not an experience.*

---

### 14. Virtual & Augmented Reality

Plan: [[24 Virtual and Augmented Reality]] · notes: [[XR/00 Lectures]]

- WebXR
- VR
- AR
- Interaction Design

**Why you need it.** The same Three.js / WebGL stack, in a **headset**, with tracking, comfort, and controllers. Extra polygons lose to nausea and a missing fallback. If it cannot run inline in the lab, it is not the weekly deliverable — the headset is extra evidence. Desktop/WebXR emulation is required so the course is not a hardware lottery.

**Where it is useful.** Museum and training capstones. Industrial AR (hit-test, anchors) as a thin slice, not a Unity major. Jobs: WebXR, location-based entertainment, industrial AR viewers — still in the browser unless the department adds a native track.

Teaching principle: *if it cannot run inline in the lab, it is not the weekly deliverable — headset is extra evidence.*

---

### 15. AI for Interactive Graphics

Plan: [[25 AI for Interactive Graphics]] · notes: [[AI for Interactive Graphics/00 Lectures]]

- AI-assisted Content Creation
- AI Agents
- Image Generation
- AI APIs
- AI-enhanced Web Applications

**Why you need it.** Assets, textures, and even 3D-from-prompts will show up in student projects whether you teach them or not. The course is **not** training GPT. It is: a proxy so keys never sit in client JS, an asset table (prompt, model, licence, date), latency, evaluation, and integrity ([[Teaching]] handbook). If the key is in the repo or the asset is unlabeled, the project fails before aesthetics.

**Where it is useful.** Configurator + generated materials. Vision/audio as inputs to a scene. Capstone features that must be cited and reversible. Jobs: AI-assisted content pipelines, product tools that call an API honestly — not “AI artist” as a substitute for Blender or shaders.

Teaching principle: *if the key is in the repo or the asset is unlabeled, the project fails before aesthetics.*

---

## Semester 6

### 16. Advanced Computer Graphics

Plan: [[26 Advanced Computer Graphics]] · notes: [[Advanced Computer Graphics/00 Lectures]]

- Global Illumination
- Volumetric Rendering
- Deferred Rendering
- Rendering Optimization

**Why you need it.** Real-Time Rendering PBR is mostly **local**: lights plus IBL as a stand-in for the rest of the world. Global illumination is light after **leaving** other surfaces. Volumes, teaching-scale path tracing or radiosity, deferred vs forward, and **how to read a paper** so they can state a claim and a limitation. If they cannot, they copied a demo. This is also the research-facing course for a thesis.

**Where it is useful.** Thesis topics. Honest talk in a capstone (“our IBL is not GI”). Jobs: rendering research, high-end look-dev, reading SIGGRAPH-style papers without drowning.

Teaching principle: *if they cannot state the claim and the limitation, they copied a demo.*

---

### 17. Capstone Project

Plan: [[27 Capstone Project]] · notes: [[Capstone/00 Lectures]]

Students build a complete interactive application, such as:

- Product configurator
- Scientific visualization
- Interactive museum
- 3D game prototype
- Architectural walkthrough
- Medical visualization (viz, not a device)
- Creative graphics demo

**Why you need it.** The rest of IGWT is skills. Graduation and hiring ask for one **runnable system**: problem (users, not a tech list), spec, architecture, vertical slice, sprints, measured budgets, README on a lab machine, freeze, defense. The happy path on a lab machine is the project; everything else is a slide. This is not a second thesis and not a startup pitch without software.

**Where it is useful.** [[Graduation Requirements]]: capstone weight, demo, documentation, oral defense. Portfolio. The interview. Jobs: the thing you point at when asked “what have you shipped?”

Teaching principle: *the happy path on a lab machine is the project; everything else is a slide.*

---

## If you want to become known for this field

Define the specialization around four flagship courses:

1. **Computer Graphics I**
2. **WebGL & Shader Programming**
3. **Real-Time Rendering**
4. **Interactive Web Technologies**

Together they are still relatively rare as a coherent undergraduate track. Structure them as **Interactive Graphics and Web Technologies (IGWT)** — graphics, visualization, game technology, web development, XR, and AI-powered interactive systems as one pipeline, not as borrowed CS electives.
