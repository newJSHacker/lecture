# 25 — Common sense and anecdotes for lectures

Parent: [[Teaching/05 Lecture Craft]]. Session timing: [[Teaching/24 Session Guides]].

These are **30–90 second** stories you can say out loud, then return to the kernel. They are not entertainment. Each one carries one computer-science idea that students already know from ordinary life, and that IGWT will later name.

## How to use

Pick **one** per meeting. Say it in the Frame (minute 8–11) or when the room stalls. Then write the invariant on the board.

| Do | Do not |
| --- | --- |
| One story → one sentence of CS → back to the demo | Three stories in a row |
| Name the real incident if you use one (year, what broke) | Invent fps, dollar losses, or “a friend at Google” |
| End with “so in this course we…” | Let the anecdote become the lecture |
| Prefer a story that predicts today’s lab bug | Jokes that punch down, or Therac-25 as comedy |

If they ask for more history, send them a link after class. You are teaching graphics, not a documentary.

**Say (the landing line, every time):** “The story is not the point. The point is the invariant I am about to write.”

---

## Fast picker (by course)

| Course | Anecdote to open with | Kernel it protects |
| --- | --- | --- |
| Programming | Recipe card vs cook; fenceposts; looking under the lamp; phone book; nested dolls | Function, off-by-one, debug the evidence, search, recursion |
| Web | Restaurant; `file://` living room; key under the mat | Request/response, modules, secrets |
| Math for CG | Whose left?; stamps vs arrows; rubber-band ruler | Frames, point ≠ vector, float |
| CG I / WebGL | Two kitchens; same cookie on every plate; map ≠ territory | CPU/GPU, shader, spaces |
| Three.js | IKEA nested boxes; wrong-size clothes | Scene graph, units |
| Blender | Mars orbiter (units); photocopy of a window | Metres, IBL ≠ GI |
| Shaders / RTR | Mail slot; measuring the soup | Buffer, measure don’t invent |
| GPU | Assembly line vs one carpenter | SIMD / occupancy (idea only) |
| Interactive / R3F | Two clocks in the house | rAF vs React |
| XR | Interlock on a saw | Safety is a requirement |
| AI graphics | Key under the mat; unlabeled photograph | Proxy, provenance |
| Comp Geo | Three people in a line; fenceposts | Degeneracy, indexing |
| Capstone | Smoke alarm; stairs-only building | Tests, a11y |
| Advanced CG | Photocopy of a window | IBL is not a path tracer |

---

## Everyday common sense (say these first)

### 1. Recipe card vs cook

**Say:** “A recipe is not dinner. The card says *what* and *in what order*. The cook is the machine that follows it tonight, with *this* flour. If the card says ‘add salt’ and you have no salt, the cook does not invent a new cuisine. It stops, or it substitutes badly. A **function** is the card. **Arguments** are tonight’s ingredients. **Return** is the plate you can hand to the next cook.”

**Point:** A program is a procedure, not a wish. Names on the card must match what is in the kitchen.

**Where:** [[Programming/Lecture 01 What a program is]], [[Programming/Lecture 05 Functions]].

**Do not:** spend five minutes on cooking. Write `f(x) → y` and move.

### 2. Fenceposts, not fences

**Say:** “Ten metres of fence with a post every metre: how many posts? Eleven, not ten. You count the **posts**, not the **spans**. Loops and arrays make the same mistake: `i < n` vs `i <= n`, pixels 0..width-1, triangle indices.”

**Point:** Off-by-one is a counting error, not a typing error.

**Where:** Programming loops; [[Computational Geometry/Lecture 07 Polygon Triangulation]]; canvas pixel loops.

**Board:** Draw 4 spans, 5 posts. Label `n` and `n+1`.

### 3. Looking under the lamp

**Say:** “You dropped your keys in the alley. You search under the streetlamp because that is where the light is. That is not search. That is comfort. Debugging the console because it is pretty, while the mesh is black because the camera looks the wrong way, is the same habit.”

**Point:** Debug the **evidence** (the picture, the error, the invariant), not the tool you like.

**Where:** any live-coding recovery; [[Teaching/06 Live Coding Pedagogy]].

**Ask:** “Where is the light in *this* bug — the console, or the framebuffer?”

### 4. Whose left?

**Say:** “I tell you ‘the door is on the left.’ Left of *whom*? Me facing you, or you facing the door? Until we name the **frame**, ‘left’ is not a fact. In graphics, +Y is ‘up’ only after we say whose up: math, canvas, Blender, glTF, the camera.”

**Point:** Coordinates are meaningless without a named space.

**Where:** [[14 Mathematics for Computer Graphics]], CG I week 1, [[Blender/Lecture 01 Blender UI and units]], Three.js conventions.

**Board:** `object → world → view → clip`. Freeze RH, Y-up, look −Z.

### 5. Stamps vs arrows

**Say:** “A stamp on an envelope is a **place**. An arrow on a sign is a **direction**. You can add two arrows. You cannot add two stamps and get a stamp that means anything, unless you first pick an origin and treat them as arrows from that origin. **Point** is not **vector**. Subtract two points: vector. Add a point and a vector: point. Add two points: a programming accident.”

**Point:** Types in geometry are not decoration.

**Where:** Math for CG; any transform lecture.

**Do not:** start with dual spaces. Two drawings are enough.

### 6. Rubber-band ruler

**Say:** “If you measure a table with a rubber band, two people will disagree in the last millimetre. Floats are a rubber band: they are good enough for a picture, deadly if you write `if (area == 0)`. Three people standing almost in a line look collinear until you zoom in.”

**Point:** Equality of floats is a policy (`epsilon`), not a law.

**Where:** [[Computational Geometry/Lecture 02 Geometric Primitives]]; any degeneracy talk; shader branching on `==`.

**Do not:** invent a magic epsilon for all courses. Say “choose relative to the scale of the scene.”

### 7. Restaurant (request / response)

**Say:** “You do not walk into the kitchen. You give the waiter a **ticket** (URL, method, headers). The kitchen returns a **plate** (status, body). If the kitchen is on fire, you still get a plate: it might say 500. The browser is the dining room. **HTTP** is the ticket language. Refreshing is asking for another plate, not ‘fixing the chef.’”

**Point:** Client and server are different machines with a contract.

**Where:** [[Web Technologies/Lecture 01 How the web works]]; fetch in Interactive Web; [[AI for Interactive Graphics/Lecture 02 APIs and keys]].

### 8. Key under the mat

**Say:** “You would not tape the house key to the front door and call it security. Putting an API key in client JavaScript is that. Anyone who can load the page can copy the key. A **proxy** is the lockbox inside the house: the browser asks *your* server; your server holds the key.”

**Point:** Secrets do not travel to the client. Ever.

**Where:** [[AI for Interactive Graphics/Lecture 02 APIs and keys]]; any fetch demo.

**Do not:** live-demo a real paid key in a gist.

### 9. Serving dinner from the living room (`file://`)

**Say:** “Opening `index.html` from the desktop is eating in the living room: no waiter, no kitchen rules. ES modules, many loaders, and some workers expect a **server** — a restaurant with an address. ‘It works on my machine when I double-click’ is not a deployment.”

**Point:** Protocol and origin matter. Serve locally.

**Where:** Web, Modern JS, Three.js week 1, any `import` lecture.

### 10. IKEA nested boxes (scene graph)

**Say:** “The instruction sheet says: put the door on the cabinet, put the cabinet on the wall. If you rotate the wall, the door comes along. You do not rotate the door in world space by guessing. **Parent transforms** are the nested boxes. Local space is ‘relative to this piece.’”

**Point:** A scene graph is not a list of meshes. It is nested frames.

**Where:** [[ThreeJS Development/Lecture 01 Scene, camera, renderer]], CG I hierarchy, Blender parenting.

### 11. Wrong-size clothes (units and scale)

**Say:** “A jacket marked ‘M’ from two factories is not the same M. A mesh exported in centimetres into a world that assumes metres is a giant or a speck. The asset is not ‘wrong.’ The **contract** was unnamed.”

**Point:** Freeze SI metres, or write the unit on the export checklist.

**Where:** [[Blender/Lecture 01 Blender UI and units]], [[Blender/Lecture 11 glTF export]], Capstone budgets.

**Industry punch (30 seconds):** Mars Climate Orbiter, 1999: one team sent pound-force seconds, the other expected newton-seconds. The spacecraft was lost. **Units are an interface.**

### 12. Photocopy of a window (IBL ≠ GI)

**Say:** “A photograph of a sunny window taped to the wall is not sunlight. It can look convincing. It does not bounce. **IBL** is the photograph. **Global illumination** is opening the window. Students will call both ‘lighting.’ Stop them.”

**Point:** Image-based lighting is a look, not a transport simulation.

**Where:** [[Blender/Lecture 05 Principled BSDF]], RTR IBL week, [[Advanced Computer Graphics/Lecture 01 Global illumination idea]].

### 13. Two kitchens (CPU and GPU)

**Say:** “The dining room (CPU) writes a ticket: ‘draw these triangles with this recipe.’ The industrial kitchen (GPU) cooks **the same recipe for every plate** at once. You do not walk into that kitchen and change the recipe per plate without a cost. A **shader** is the recipe posted on the kitchen wall.”

**Point:** CPU orchestrates; GPU instances a program over vertices/fragments.

**Where:** [[WebGL Programming/Lecture 01 GPU pipeline and a triangle]], [[Shader Programming/Lecture 01 The shader as a program]], [[GPU Programming/Lecture 01 GPGPU idea]].

**Do not:** invent occupancy percentages. Measure or omit.

### 14. Mail slot (buffers)

**Say:** “You do not hand the postman a thought. You put paper in a **slot** of a known size. If the letter is longer than the slot, it does not ‘mostly work.’ It is a different letter or a torn one. GPU **buffers** are typed slots: attributes, uniforms, textures. Wrong layout is not a style issue.”

**Point:** Memory layout is part of the API.

**Where:** WebGL buffers; GPU memory lectures; packed vertex formats.

### 15. Same cookie cutter (instancing / shaders)

**Say:** “One cutter, a thousand cookies. The cutter does not know cookie 47’s name. It knows **this dough, this stamp**. A vertex shader does not know your mesh’s biography. It knows `position`, `normal`, `uv` for **this** vertex.”

**Point:** Graphics programs are data-parallel. Per-object logic belongs on the CPU or in instance attributes.

**Where:** shaders; GPU instancing; Three.js `InstancedMesh` if you teach it.

### 16. Map is not the territory

**Say:** “The subway map is not the city. Clip space is not the room. A UV map is not the mesh. When the picture is wrong, ask: **which map did we draw on, and which territory did we mean?**”

**Point:** Spaces and parameterizations are models. Bugs are often “right computation, wrong space.”

**Where:** any matrix lecture; UV week in Blender; shadow maps in RTR.

### 17. Three people in a line

**Say:** “From the balcony they look like one person. From the floor you see three. A geometric **predicate** (left of a line, inside a triangle) is unstable when the input is almost degenerate. Algorithms that assume general position will lie to you on real meshes.”

**Point:** Degeneracy is normal data, not a corner case you skip.

**Where:** [[Computational Geometry/Lecture 02 Geometric Primitives]], hulls, triangulation.

### 18. Two clocks in the house

**Say:** “The oven clock and the wall clock disagree by two minutes. Dinner is still edible. An animation clock (`requestAnimationFrame`) and a UI clock (React state) that both ‘own’ the cube’s angle will fight. Pick **one source of truth** for time.”

**Point:** One clock for the scene. UI may trigger, not tick the integrator.

**Where:** [[Interactive Web/Lecture 01 Canvas 2D API]], [[Interactive Experience/Lecture 01 R3F architecture]].

### 19. Library vs desk (cache)

**Say:** “You keep the book you use every hour on the desk, not in the stacks. A **cache** is the desk: small, fast, sometimes stale. ‘I changed the shader and nothing happened’ is often a desk with yesterday’s book (browser cache, stale uniform, texture not marked needsUpdate).”

**Point:** Fast paths lie when they are stale. Know what you invalidated.

**Where:** Web performance; Three.js materials; GPU bind groups (idea).

### 20. Stairs-only building (accessibility)

**Say:** “A beautiful lobby with only stairs is not ‘done.’ Keyboard, captions, motion, contrast, XR comfort — these are doors, not decoration. Ship the stairs-only build and you failed a requirement, not a taste test.”

**Point:** Accessibility is in the spec. See [[Teaching/10 Inclusive Teaching and Accessibility]].

**Where:** Web layout; Interactive Web; Capstone performance/a11y sprint; XR.

### 21. Smoke alarm (tests and asserts)

**Say:** “A smoke alarm that never rings is not proof there is no fire. It may have no battery. A demo that ‘looks fine’ with no assert on winding order, on `NaN`, on load failure, is an alarm with no battery.”

**Point:** Tests check **contracts**. Pretty pixels are not a contract.

**Where:** Programming; Capstone; any loader/`glTF` import.

### 22. Unlabeled photograph (provenance)

**Say:** “A beautiful texture with no source, no license, no prompt log, and no ‘this is generated’ note is an unlabeled photograph in a medical file. You cannot defend it. **Asset tables** exist so week 15 is not a lawsuit.”

**Point:** Provenance is part of the deliverable in AI graphics and capstone.

**Where:** [[AI for Interactive Graphics/Lecture 03 Image as texture]], [[AI for Interactive Graphics/Lecture 07 Integrity workflows]], Capstone docs sprint.

### 23. Doctor, not plastic surgeon (debugging)

**Say:** “A doctor asks where it hurts and runs a test. They do not start by replacing the patient’s bones because the textbook chapter was ‘bones.’ Students rewrite the whole shader because the mesh is black. First: camera? light? winding? shader compile log?”

**Point:** Bisect. Change one thing. Read the error.

**Where:** every live-coding session.

### 24. Measuring the soup (performance)

**Say:** “You do not guess the salt by staring at the pot from across the room. You taste. **Do not invent frame times.** If you did not measure on this machine, do not quote a number. Say ‘it felt heavy’ or open the profiler.”

**Point:** Performance claims need a method. House rule of this program.

**Where:** [[Real-Time Rendering/Lecture 01 Forward rendering review]], [[GPU Programming/Lecture 01 GPGPU idea]], Capstone, Three.js budgets.

### 25. Time machine of drafts (version control)

**Say:** “School essays used to be one printout. Git is labeled drafts: you can return to Tuesday without reconstructing Tuesday from memory. ‘Final_final2_really’ is not a time machine. It is a pile.”

**Point:** Commit meaning, not panic. [[Capstone/Lecture 01 Teams and problems]].

### 26. Phone book (search)

**Say:** “A paper phone book is already sorted. You do not start at Aaron and walk to Zhang. You open the middle, throw away half, repeat. That is **binary search**. If the book is *not* sorted — a pile of business cards — half-splitting is superstition. You sort first, or you scan.”

**Point:** The algorithm assumes a structure. Wrong structure, wrong method.

**Where:** [[Programming/Lecture 09 Search]], [[Programming/Lecture 10 Sorting and complexity]].

### 27. Nested dolls (recursion)

**Say:** “A doll opens and there is a smaller doll with the *same job*: open until you hit the solid one. **Recursion** is a function that solves a smaller instance of the same problem, plus a **stop**. Directories inside directories. A scene graph walking children. If you forget the solid doll, you never return.”

**Point:** Base case first. Then the smaller call. Then combine.

**Where:** [[Programming/Lecture 11 Recursion]]; scene-graph traversal; CSG if you ever show it.

### 28. Folders, not a pile (trees)

**Say:** “Your course files are not a shoebox. `Lecture/` contains `WebGL/`, which contains `code/`. To find a file you walk **down**. That shape is a **tree**. The DOM is a tree. The scene graph is a tree. A cycle (‘this folder contains itself’) is a bug, not a feature.”

**Point:** Hierarchy is data, not decoration.

**Where:** DOM week in Web; Three.js; file modules in Programming.

---

## Named incidents (use sparingly — they carry weight)

Tell these only when the everyday story is not enough, or when you need students to feel that **interfaces and types are not homework**.

| Incident | Year | 40-second version | CS point | IGWT landing |
| --- | --- | --- | --- | --- |
| Mars Climate Orbiter | 1999 | Pound-force seconds vs newton-seconds. Vehicle lost. | Units are an API | Blender / glTF / “1” is not a metre |
| Ariane 5 Flight 501 | 1996 | A 64-bit number stuffed into a 16-bit register. Overflow. Rocket destroyed. | Types and conversion are not paperwork | Typed arrays, `int` in GLSL, `toFixed` is not a type |
| Pentium FDIV | 1994 | A hardware divider was wrong in rare cases. Trust but **test** the black box. | Your GPU/driver/library can be wrong | Golden image, NaN hunt |
| Y2K | 1999–2000 | Two-digit years. The representation was the bug. | Data layout outlives the programmer | Indexes, timestamps, texture formats |
| Heartbleed | 2014 | A read past the end of a buffer. Memory that was not yours leaked. | Bounds | `DataView`, buffer sizes, C++ if they ever leave JS |
| npm `left-pad` | 2016 | One tiny package unpublished; builds worldwide broke. | Supply chain | **No CDN** in this program; vendor what you teach |
| Knight Capital | 2012 | A leftover flag turned on dead code in production. | Unused paths are still code | Feature flags, “I’ll just comment this” |
| Excel / `SEPT2` gene names | (ongoing) | Spreadsheets coerced names into dates. | Implicit types | `'3'+1`, CSV, JSON numbers vs strings |
| YouTube / Gangnam Style | 2014 | View counter hit 32-bit max. They moved to 64-bit. | Integer width | Indices, instance counts, `Uint16` vs `Uint32` |

**Do not:** turn any of these into a 15-minute history lecture. **Do not** use Therac-25 as a joke. If you mention medical or radiation accidents, say: software interlocks are ethics, then point at XR comfort and “do not skip the safety check.”

**Say (after a named incident):** “We will not be launching a rocket. We will launch a page that 40 classmates must run. The same class of mistake — unnamed units, silent overflow, a dependency we did not pin — still applies.”

---

## Tiny CS facts that *feel* like common sense

Use as 20-second asides, not stories.

| What they already believe | What you say | Where |
| --- | --- | --- |
| `'3'+1` is 4 | It is `'31'`. Glue is not arithmetic. Types decide. | Programming L2 |
| `NaN === NaN` | False. “Not a number” is not a value you can find with `===`. | Math, shaders |
| Sorting a copy vs the original | `sort` mutates. The list on the table *is* the list. | JS |
| “The image is 800px so the mesh is 800 units” | Pixels are not world metres. | Canvas vs Three |
| Canvas Y grows down | Math Y grows up. Two countries, one screen. | 2D / CG I |
| More triangles → better silhouette | Until the budget and the shading model disagree. Measure. | RTR |
| Three.js *is* computer graphics | It is an **engine**. CG I / WebGL week 1 still own the algorithm. | CG I, WebGL L1 |
| A black mesh means “WebGL is broken” | Camera, lights, winding, shader log — in that order. | All 3D |
| `== 0` for area | Use a tolerance or an exact predicate. | Comp Geo |
| Midterm week is a lecture | It is an exam meeting. Name it. | [[Teaching/24 Session Guides]] |

---

## One-liners you can park on the board

These are not anecdotes. They are the **invariant** the anecdote was for. Photograph these.

- A name is not the thing. A URL is not the file. A texture is not the material.
- Count posts, not spans.
- Name the frame before you say “up.”
- Point − point = vector. Point + vector = point. Point + point = a bug.
- The map is not the territory.
- Secrets stay on the server.
- Serve the page; do not double-click it and call it done.
- IBL is a photograph of light. GI is transport.
- One clock for the scene.
- Do not invent the frame time.
- Degeneracy is normal.
- Pretty is not tested.

---

## When the room is dead

Do not tell a longer story. Do **this** instead ([[Teaching/13 Classroom Difficulties]]):

1. Broken picture on the projector (30 s silent).
2. “Write why it is black” (2 min).
3. Then, if you still need a hook, use **Whose left?** or **Looking under the lamp** — they take 40 seconds.

Anecdotes rescue **attention**. They do not rescue a missing attempt phase.

---

## What not to collect

- Unverified “NASA hired 10,000 bugs” folklore.
- Quotes that never happened (the internet is full of them).
- Stories that need a victim for the laugh.
- Your own industry trauma as a 20-minute monologue.

If you cannot source the incident with a year and a mechanism, use the everyday version instead. **Whose left?** will still teach frames. The orbiter is optional salt.

---

## Prep on Sunday

When you fill the one-pager in [[Teaching/03 Lesson Planning]]:

1. Kernel in one noun phrase.
2. **One** row from the fast picker above.
3. The landing sentence written in the session guide **Say** block — not improvised from memory when you are tired.

Gold-standard session guides already have a Frame. Put the anecdote there, then cut it if time dies. The kernel stays.
