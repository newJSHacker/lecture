"""Full-script GOLD for semester-5/6 IGWT courses (75 meetings)."""


def register(GOLD: dict) -> None:
    _ied(GOLD)
    _xr(GOLD)
    _ai(GOLD)
    _acg(GOLD)
    _cap(GOLD)


def _ied(GOLD: dict) -> None:
    C = "Interactive Experience Development"
    GOLD[(C, 1)] = dict(
        kernel="JSX in <Canvas> is a reconciler onto a Three.js graph; npm run dev",
        success="they can run Vite, put a mesh in Canvas, and say this is not a new lighting model",
        invariant="3D and DOM are two clocks",
        goal="a cube in Canvas, not a 2018 CRA tutorial",
        board="""```
JSX tree  →  commit  →  Three.js graph

<Canvas>
  <mesh>
    <boxGeometry />
    <meshStandardMaterial />
  </mesh>
</Canvas>

npm run dev     not file://     no CDN
```""",
        slides=[],
        hook_say="Three.js Development still owns the renderer math. R3F is how IGWT ships UI + 3D without two competing scene graphs. If the only interface is orbit-drag, it is a scene, not an experience — that fight starts at Canvas.",
        hook_ask="Is R3F a different renderer, or a reconciler onto Three.js? Wait seven seconds.",
        frame_say="Vite, JSX, fast refresh. file:// will not load modules. Vanilla Three + DOM is allowed if they already have a scene — still two clocks. Cap dpr. No CDN.",
        frame_ask="Where does a <mesh> live after commit — the React tree, the GPU, or a Three.js Object3D?",
        build=[
            "**Say:** Reconciler: React state commits become object graphs. Same cube as Three.js week 1: box, orbit, ambient+dir.",
            "**Board:** JSX tree → graph. Circle Canvas. Color is a prop, not a CSS background.",
            "**Say:** CRA 2018 tutorials are a plant. We freeze Vite. Resize is default; still cap dpr.",
        ],
        ask_build="Why does file:// fail here?",
        they_build="On paper: nest lights + mesh under Canvas and mark which node is Three.js.",
        show_say="Vite + a box. Plant a CDN three import. Fix: local package. Demo Interactive Experience/code/01-hud.html if Vite dies.",
        attempt_say="Color as a prop on the material. Eight minutes.",
        land_say="Photograph the board. Lab: color prop + dpr cap. Homework: reconciler in eight sentences + repo. Quiz: Canvas, mesh maps to Object3D, why Vite.",
        live=[
            ("0–10", "Canvas + mesh", "Plant CRA / CDN."),
            ("10–30", "Orbit + lights", "Plant missing Canvas."),
            ("30–45", "dpr cap", "Plant retina melt."),
            ("45–60", "They set color as a prop", "Circulate. No CDN."),
        ],
        cut="drei Html. Keep Canvas + reconciler.",
        add="Resize is default — still write the dpr cap.",
    )
    GOLD[(C, 2)] = dict(
        kernel="useState is the UI clock; useFrame + ref is the 3D clock",
        success="they can show jank from setState every frame and move rotation onto a ref",
        invariant="3D and DOM are two clocks",
        goal="select in React; spin in useFrame",
        board="""```
React clock     useState / click     re-render
WebGL clock     useFrame(_, dt)      mesh.ref

setState({ t }) every frame  =  jank
new Material() every render  =  leak
```""",
        slides=[],
        hook_say="Last time: a graph. Today: two clocks. React re-renders are for HUD. The WebGL loop is useFrame. Mixing them is the live-coding crime of this course.",
        hook_ask="If a cube must spin, do you put t in useState? Wait. Want: no — ref + dt.",
        frame_say="Click selects (state). Spin uses useRef on the mesh. Lifting: selected id in React; color on the mesh from that id. We do not invent fps.",
        frame_ask="Why does a new material every render hurt?",
        build=[
            "**Say:** Discrete UI vs per-frame motion. Write both clocks.",
            "**Board:** setState({t}) crossed out. useFrame += dt on ref.current.rotation.",
            "**Say:** Plant jank, then fix. Demo 02-two-clocks.html if R3F is down — same split: button vs rAF.",
        ],
        ask_build="When is useState correct for 3D?",
        they_build="On paper: selected id in React; rotation in useFrame. Two arrows.",
        show_say="Click a box to select; spin via ref. Plant setState in useFrame. Read the hitch out loud. Do not quote fps.",
        attempt_say="Move rotation onto a ref. Leave selected in useState. Eight minutes.",
        land_say="Lab: jank demo then fix; dpr. Homework: when setState is wrong. Quiz: useFrame vs useState, why ref, what jank is.",
        live=[
            ("0–10", "Click = state", "Plant t in useState."),
            ("10–30", "Spin via ref + dt", "Plant setState every frame."),
            ("30–45", "New material every render", "Fix: one material."),
            ("45–60", "They split the clocks", "Circulate."),
        ],
        cut="Lifting state across routes. Keep two clocks.",
        add="dpr reminder on the Canvas.",
    )
    GOLD[(C, 3)] = dict(
        kernel="HTML overlay HUD; pointer-events none except controls",
        success="a button changes a mesh and the canvas still receives orbit except on the button",
        invariant="3D and DOM are two clocks",
        goal="a HUD that is HTML, not WebGL text",
        board="""```
DOM HUD  (labels, buttons, focus)
   ↕  pointer-events
<canvas>  Three / R3F

.hud { position:absolute; inset:0; pointer-events:none; }
.hud button { pointer-events:auto; }
```""",
        slides=[],
        hook_say="Web Technologies already painted this stack. The canvas is a layer; HTML on top is the product UI. All-UI-as-WebGL-text fails keyboard and labels.",
        hook_ask="If the overlay is inset 0, why can I not orbit? Wait. Want: it ate pointer-events.",
        frame_say="Price tag + one mesh. Button sets color through React state (clock 1). drei Html is a pin, not the whole HUD — cost is extra DOM.",
        frame_ask="When is drei Html the right tool vs a page HUD?",
        build=[
            "**Say:** Layers. Canvas then HUD. Labels live in HTML.",
            "**Board:** pointer-events split. Circle auto on the button.",
            "**Say:** Focus-visible on buttons. 3D picking vs button clicks — do not mix silently.",
        ],
        ask_build="Why not draw the price with a canvas texture this week?",
        they_build="On paper: HUD CSS plus one button → material.color.",
        show_say="Price tag HUD; button recolors a mesh. Plant overlay eating all clicks. Then add pointer-events. Demo 01-hud.html.",
        attempt_say="HUD button + orbit still works around it. Eight minutes.",
        land_say="Lab: follow-label extra; focus-visible. Homework: pointer-events paragraph. Quiz: none vs auto, why HTML HUD, focus.",
        live=[
            ("0–10", "Absolute HUD", "Plant WebGL text."),
            ("10–30", "pointer-events split", "Plant overlay eating orbit."),
            ("30–45", "Button → color", "State clock, not useFrame."),
            ("45–60", "They add focus-visible", "Circulate."),
        ],
        cut="drei Html tour. Keep page HUD + pointer-events.",
        add="One pinned drei Html label, then say the cost.",
    )
    GOLD[(C, 4)] = dict(
        kernel="scroll 0–1 drives one camera or mix; reduced-motion path",
        success="they can map scroll progress to one rotation or dolly and name a non-scroll path",
        invariant="3D and DOM are two clocks",
        goal="one beat, not a locomotive theme park",
        board="""```
scroll  0 ──────── 1
          ↓
   camera / mix / rotation

prefers-reduced-motion  →  same content, no forced scroll
```""",
        slides=[],
        hook_say="Awwwards pages are often scroll → 3D. Students overbuild. One beat: progress 0–1 rotates a product. Capstone energy starts when there is a beat.",
        hook_ask="If the user cannot scroll, is the story gone? Wait. Want: no — a button or reduced-motion cut.",
        frame_say="useFrame reads progress, not setState of scroll every pixel. Do not lerp 100 meshes. Fluid images and viewport still apply from Web Tech.",
        frame_ask="Where does progress live — React state every pixel, or a ref the frame loop reads?",
        build=[
            "**Say:** Narrative is a shot, not a second scene graph.",
            "**Board:** 0–1 line. Camera or rotation only.",
            "**Say:** prefers-reduced-motion. Progress bar is honest UX.",
        ],
        ask_build="Why is locomotive + three scenes a week-4 fail?",
        they_build="Sketch stacked copy vs 3D beat; mark the reduced-motion path.",
        show_say="Scroll 0–1 dollies or spins a primitive. Plant setState on every scroll event. Move progress to a ref.",
        attempt_say="Bind progress to rotation.y. Eight minutes.",
        land_say="Lab: reduced-motion extra; progress bar. Homework: one-beat storyboard. Quiz: 0–1, two clocks, reduced-motion.",
        live=[
            ("0–15", "Progress 0–1", "Plant full locomotive."),
            ("15–40", "Drive one mesh", "Plant 100 lerps."),
            ("40–55", "Reduced-motion branch", "They feel the skip."),
            ("55–60", "They add a progress bar", "Circulate."),
        ],
        cut="Lenis/locomotive. Keep one beat.",
        add="Progress bar as DOM, not a 3D ticker.",
    )
    GOLD[(C, 5)] = dict(
        kernel="one motion library; CameraControls vs OrbitControls do not both own the camera",
        success="they can spring or lerp one part on click and say which control is makeDefault",
        invariant="3D and DOM are two clocks",
        goal="feel without fighting the camera",
        board="""```
pick one:  lerp    or    spring
do not: GSAP + spring + CSS on the same property

OrbitControls  vs  CameraControls
          makeDefault — one owner
```""",
        slides=[],
        hook_say="Product sites use springs. Games often lerp. Two owners of the camera is a bug, not a style.",
        hook_ask="If Orbit and CameraControls both run, who wins? Wait. Want: a fight — pick makeDefault.",
        frame_say="drei helpers are oracles. Cleanup: geometries created in effects must dispose, or use JSX geometries. We freeze one library today.",
        frame_ask="What must unmount dispose?",
        build=[
            "**Say:** Feel is a choice under constraint. One library.",
            "**Board:** two control names. Cross out dual ownership.",
            "**Say:** Mode toggle: orbit vs story camera. Story wins during the beat.",
        ],
        ask_build="lerp vs spring in one sentence?",
        they_build="On paper: click → spring position; orbit disabled while it runs.",
        show_say="Spring a part on click. Plant two controls. Fix makeDefault. Plant leaked geometry on hot reload.",
        attempt_say="One spring or lerp on click. Eight minutes.",
        land_say="Lab: orbit vs story toggle; dispose note. Homework: which control owns the camera. Quiz: makeDefault, one library, dispose.",
        live=[
            ("0–15", "Lerp or spring one part", "Plant three libraries."),
            ("15–40", "makeDefault", "Plant dual controls."),
            ("40–55", "Dispose / JSX geom", "Hot-reload leak."),
            ("55–60", "They add a mode toggle", "Circulate."),
        ],
        cut="Full CameraControls API. Keep one owner + one motion.",
        add="dispose note on a useLayoutEffect geometry.",
    )
    GOLD[(C, 6)] = dict(
        kernel="user-gesture AudioContext; analyser bins → instance scale; mute",
        success="they can start audio from a Play button and scale bars from an analyser without autoplay",
        invariant="3D and DOM are two clocks",
        goal="bars that work silent",
        board="""```
Play (gesture)  →  AudioContext
analyser.fftSize = 64
bins → instance scale     cap N

mute + still image     (not audio-only)
licensed loop only
```""",
        slides=[],
        hook_say="Browsers block autoplay. A surprise soundtrack is a fail. Audio is data for graphics — and a11y still needs a silent path.",
        hook_ask="Why did play() throw? Wait. Want: no user gesture.",
        frame_say="fftSize named. Map bins to instances, not 1024 meshes. Do not ship a copyrighted album as the asset. Captions/mute in the HUD.",
        frame_ask="If the speaker is off, is the viz still readable?",
        build=[
            "**Say:** Gesture first. Then analyser.",
            "**Board:** Play → context → bins → scale. Cap N.",
            "**Say:** Mute. Fallback still. Instances, not 32 Mesh objects if they already know Instances — else 32 is enough.",
        ],
        ask_build="What does fftSize change?",
        they_build="On paper: button, analyser, one bin → one bar.",
        show_say="Licensed short loop; 32 bars. Plant autoplay. Plant a full song file. Fix: button + tiny loop.",
        attempt_say="Play button starts context; one bar follows a bin. Eight minutes.",
        land_say="Lab: mute + still fallback. Homework: gesture paragraph. Quiz: autoplay, fftSize, why mute.",
        live=[
            ("0–15", "Play gesture", "Plant autoplay."),
            ("15–40", "Analyser → scale", "Plant 1024 meshes."),
            ("40–55", "Mute / silent still", "Audio-only plant."),
            ("55–60", "They cap N", "Circulate."),
        ],
        cut="Beat-matching DSP. Keep gesture + bins.",
        add="Fallback still image in the HUD.",
    )
    GOLD[(C, 7)] = dict(
        kernel="rapier/cannon-es is an oracle for collision, like Raycaster",
        success="they can drop a cube on a floor, reset, and write one sentence: we did not implement contact",
        invariant="3D and DOM are two clocks",
        goal="use physics; do not claim the algorithm",
        board="""```
oracle     rapier / cannon-es / Raycaster
kernel     our scene, HUD, reset, labels

<RigidBody>  falling box
reset →  origin

single player     no netcode
```""",
        slides=[],
        hook_say="Computational Geometry owns predicates. Today we use an engine and we say so. Claiming you implemented physics because a cube fell is an integrity fail.",
        hook_ask="Is a falling box a physics paper? Wait. Want: no — it is an oracle.",
        frame_say="Floor + dropping cubes + reset. Collider wireframe extra. Skip networking. 1000 convex hulls is not the lab.",
        frame_ask="What must the README say about rapier?",
        build=[
            "**Say:** Oracle vs kernel. Write both words.",
            "**Board:** RigidBody box; reset arrow.",
            "**Say:** Same honesty as Raycaster: we call it, we do not derive GJK.",
        ],
        ask_build="Why is 1000 hulls a cut?",
        they_build="One sentence: oracle vs kernel for this lab.",
        show_say="Floor + drop + reset. Plant 'we implemented physics' in a comment. Cross it out. Wireframe extra.",
        attempt_say="One falling box and a reset button. Eight minutes.",
        land_say="Lab: wireframe extra; oracle sentence. Homework: that sentence in README. Quiz: oracle, reset, no netcode. Next: midterm then Suspense.",
        live=[
            ("0–15", "Floor + gravity", "Plant algorithm claim."),
            ("15–40", "Drop cubes + reset", "Plant 1000 hulls."),
            ("40–55", "Oracle sentence on board", "They copy."),
            ("55–60", "They add reset", "Circulate."),
        ],
        cut="Networking. Keep floor + honesty.",
        add="Collider wireframe.",
    )
    GOLD[(C, 8)] = dict(
        kernel="midterm; then Suspense / useLoader with a fallback and a missing-file error",
        success="after the exam they can show a fallback while a glTF loads and a visible error if it 404s",
        invariant="3D and DOM are two clocks",
        goal="midterm, then loading UX",
        kind="midterm",
        midterm_topics="reconciler/Canvas; two clocks; HUD pointer-events; scroll 0–1; one motion library + camera owner; analyser gesture; physics as oracle.",
        board="""```
<Suspense fallback={placeholder}>
  <Model />
</Suspense>

missing glTF  →  visible error, not a black canvas
useProgress  =  name; % is measured, not invented
```""",
        slides=[],
        hook_say="This meeting is a **midterm**, then loading UX. No laptop for the exam. After: a black screen while a glTF loads is not mysterious — it is missing Suspense.",
        show_say="Suspense fallback while a glTF loads, or a fake delay. Plant a missing file and a silent hang. Fix: error + placeholder cube.",
        attempt_say="Fallback cube; error text if missing. Compress later (Blender).",
        land_say="Lab: missing-file error; progress name. Homework: midterm rewrite of one miss. Next: a11y. No quiz this week.",
        live=[
            ("0–15", "Suspense fallback", "Plant black canvas."),
            ("15–40", "Missing glTF error", "Plant silent 404."),
            ("40–60", "Placeholder cube", "They type. Circulate."),
        ],
        cut="drei useProgress UI kit. Keep fallback + error.",
        add="Timeout message name.",
    )
    GOLD[(C, 9)] = dict(
        kernel="keyboard cycle, HUD name, reduced-motion stops auto orbit",
        success="they can tab or press Next to select three parts and read the name without the mouse",
        invariant="3D and DOM are two clocks",
        goal="3D that a keyboard can use",
        board="""```
Next part   (button, focus visible)
HUD text    =  selected name
outline     +  label   (not color alone)

prefers-reduced-motion → stop auto orbit
no 3 Hz strobe
```""",
        slides=[],
        hook_say="Orbit is a mouse skill. A canvas with no keyboard story fails this course and XR later. Color-only selection fails.",
        hook_ask="Can you use this page with keyboard only? Wait. Then try.",
        frame_say="Reset camera. Cycle parts. HUD names them. Bloom caps. Empty alt only if decorative — the HUD is not decorative.",
        frame_ask="When is outline:none a fail?",
        build=[
            "**Say:** Hostile by default. Provide a path.",
            "**Board:** Next + HUD + outline. Reduced-motion stops spin.",
            "**Say:** Seizure: no 3 Hz strobe. We do not invent Lighthouse scores.",
        ],
        ask_build="Why is color-only selection a fail?",
        they_build="Tab the HUD; list what fails.",
        show_say="Keyboard cycles three parts; HUD names them. Plant canvas-only. Plant outline:none. Fix button + focus.",
        attempt_say="Next-part button + label. Eight minutes.",
        land_say="Lab: focus styles; reduced-motion kills auto orbit. Homework: keyboard path paragraph. Quiz: Next, not color-only, reduced-motion.",
        live=[
            ("0–15", "div-as-control", "Plant. Fix button."),
            ("15–40", "Cycle + HUD name", "Color-only plant."),
            ("40–55", "Reduced-motion", "Auto orbit plant."),
            ("55–60", "They add focus-visible", "Circulate."),
        ],
        cut="Full WCAG sermon. Keep keyboard + label.",
        add="Reset-camera button.",
    )
    GOLD[(C, 10)] = dict(
        kernel="shot list as data: {id, copy, cam}; three beats",
        success="they can run a 3-beat story from JSON without burying copy in JSX",
        invariant="3D and DOM are two clocks",
        goal="an experience, not a cube demo",
        board="""```
[{ id, copy, cam }]     ←  data, not JSX soup

beat 1  hero
beat 2  detail
beat 3  HUD / CTA

one light setup per beat or lerp; budget
```""",
        slides=[],
        hook_say="A cube is a demo. A beat is a shot. Capstone energy: visitors do something in time. Novels in tooltips fail.",
        hook_ask="If I delete your JSX copy, does the story still exist in data? Wait.",
        frame_say="JSON array. Camera per beat. Lights budgeted. Cinematic 4-minute take is a cut. Screenshot a contact sheet.",
        frame_ask="Why not bury strings only in JSX?",
        build=[
            "**Say:** Experience vs demo. Write three beats.",
            "**Board:** JSON row. cam as a triple.",
            "**Say:** One light rig or lerp. Do not add a film lighting course.",
        ],
        ask_build="What is a beat in one sentence?",
        they_build="On paper: three {id, copy, cam} rows.",
        show_say="Three beats on a product or museum object. Plant copy only in JSX. Move to JSON.",
        attempt_say="JSON-driven beat 1→2. Eight minutes.",
        land_say="Lab: JSON; contact sheet. Homework: shot list. Quiz: beat, data vs JSX, budgeted lights.",
        live=[
            ("0–15", "Three beats on paper", "Plant a novel."),
            ("15–40", "JSON → camera", "Plant JSX-only copy."),
            ("40–55", "Contact sheet", "They screenshot."),
            ("55–60", "They add beat 3", "Circulate."),
        ],
        cut="Film lighting. Keep three beats + JSON.",
        add="Contact sheet of the three cameras.",
    )
    GOLD[(C, 11)] = dict(
        kernel="instance lists; cap dpr; count draw calls; do not invent fps",
        success="they can replace a naive list of meshes with Instances and write a table without a fake fps number",
        invariant="3D and DOM are two clocks",
        goal="a budget table, not a vibes number",
        board="""```
each <mesh> is an object
1k trees  →  InstancedMesh / <Instances>

dpr 1 vs 2     (cap)
draw calls     (count)

measure on a named device     or omit fps
```""",
        slides=[],
        hook_say="A janky HUD over WebGL is last term. Today: R3F cost. Each mesh is an object. Invented fps still fail this program.",
        hook_ask="Is 200 <mesh> trees the same as 200 instances? Wait. Want: no.",
        frame_say="Textures still follow Blender budgets. Strict mode double-mount: do not panic; dispose. Dev vs prod named.",
        frame_ask="What do you write if you did not measure?",
        build=[
            "**Say:** Count meshes. Then instance.",
            "**Board:** naive vs Instances. dpr cap. empty fps cell if unmeasured.",
            "**Say:** One table: device, dpr, what you cut. No fantasy 200 fps.",
        ],
        ask_build="Why 500 MeshStandardMaterials hurt?",
        they_build="On paper: two-row table, fps column blank or measured.",
        show_say="200 trees naive vs instanced; log counts. Do not quote fps unless the profiler is on this machine. Plant invented 60.",
        attempt_say="Instances limit={200} or a smaller N they can count. Eight minutes.",
        land_say="Lab: dpr 1 vs 2; one table. Homework: budget paragraph. Quiz: Instances, dpr, do not invent fps.",
        live=[
            ("0–15", "Naive list", "Plant 500 materials."),
            ("15–40", "Instances", "Count draw calls."),
            ("40–55", "Table, no fake fps", "Plant 200 fps."),
            ("55–60", "They cap dpr", "Circulate."),
        ],
        cut="Renderer source dive. Keep instance + table.",
        add="One row: named device, dpr, cut.",
    )
    GOLD[(C, 12)] = dict(
        kernel="one seed, one palette, one motion; cite assets",
        success="they can type a seed and regenerate a small composition without fifty sliders",
        invariant="3D and DOM are two clocks",
        goal="choice under constraint",
        board="""```
seed  →  rand(i)  →  pose / color

palette of 5
one motion

cite:  models, HDRI, shaders, AI textures
leva is optional; it does not replace a story
```""",
        slides=[],
        hook_say="Creative coding is not 50 sliders. One seed, one palette, one motion. Unlicensed assets fail. AI textures: still cite — AI course later, same table.",
        hook_ask="If I change the seed, do I get the same piece? Wait. Want: a different piece, deterministically.",
        frame_say="Deterministic rand. PNG export extra. Integrity: shaders and models cited.",
        frame_ask="What belongs in the asset table this week?",
        build=[
            "**Say:** Constraint is the craft.",
            "**Board:** seed → rand → composition. Palette of 5.",
            "**Say:** leva is a tool. A story beat still wins.",
        ],
        ask_build="Why is an unseeded Math.random a problem for a report?",
        they_build="On paper: seed field + three parameters it drives.",
        show_say="Seed field regenerates a composition. Plant 50 sliders. Plant an unlicensed HDRI. Cite or cut.",
        attempt_say="Seed + palette of 5. Eight minutes.",
        land_say="Lab: palette; png extra. Homework: citations. Quiz: seed, palette, cite. Next: critique.",
        live=[
            ("0–15", "Seeded rand", "Plant Math.random soup."),
            ("15–40", "Palette of 5", "Plant 50 sliders."),
            ("40–55", "Cite the HDRI", "Unlicensed plant."),
            ("55–60", "They regenerate", "Circulate."),
        ],
        cut="Full generative-art syllabus. Keep seed + cite.",
        add="PNG export extra.",
    )
    GOLD[(C, 13)] = dict(
        kernel="Awwwards-style rubric: beat, HUD, motion, budget, keyboard, citations",
        success="they can score two works on the rubric and apply one fix to their own project",
        invariant="3D and DOM are two clocks",
        goal="critique on criteria, not vibes",
        board="""```
beat   HUD   motion   budget   keyboard   citations

specific · kind · next action
screenshot + date if public
do not clone their glTF
```""",
        slides=[("Optional: two dated screenshots of public sites", "photographs")],
        hook_say="Taste without a rubric is a vibe. We score story, HUD, motion, budget, keyboard, citations. Mocking peers is a fail. Clone-as-project is a fail.",
        hook_ask="If the HUD has no keyboard path, which cell is zero? Wait.",
        frame_say="Public sites: screenshot and date. Do not copy their glTF. Feedback: specific, kind, next action.",
        frame_ask="What is a next action vs a roast?",
        build=[
            "**Say:** Rubric on the board. Six cells.",
            "**Board:** fill one row together on a volunteer or a public still.",
            "**Say:** Apply one fix to your project this hour — not a rewrite.",
        ],
        ask_build="Why date the screenshot?",
        they_build="Score two sites or two classmates (names stripped) on paper.",
        show_say="Walk one public still against the six cells. Plant a roast. Rewrite as next action. Then they write 1 page × 2.",
        attempt_say="Fill the rubric; pick one fix. Eight minutes, then studio-like apply.",
        land_say="Lab: rubric table; before/after. Homework: one-page critique. Quiz: six cells, not a clone. Next: studio.",
        live=[
            ("0–15", "Rubric on board", "Plant vibes."),
            ("15–40", "Two critiques", "Plant mocking."),
            ("40–55", "One fix applied", "Clone plant."),
            ("55–60", "Before/after still", "Circulate."),
        ],
        cut="Awwwards brand lecture. Keep six cells + one fix.",
        add="Before/after screenshot.",
    )
    GOLD[(C, 14)] = dict(
        kernel="interactive experience: two clocks, HUD, keyboard, budget table, README",
        success="a TA can npm run dev, tab the HUD, and see a beat without a second tool",
        invariant="3D and DOM are two clocks",
        goal="studio — freeze, do not add a library",
        kind="studio",
        board="""```
Must: two clocks · HUD · keyboard · one beat · budget table
Cuts: extra scenes, extra physics, extra audio
README: npm run dev     no CDN
```""",
        slides=[],
        hook_say="This meeting is **studio**. An orbit-only cube fails. Cuts are allowed. Two clocks and a keyboard path beat a new drei helper.",
        hook_ask="If behind, what do you cut first — the beat or a second library?",
        frame_say="Desk review: useFrame vs setState, HUD pointer-events, Next-part or equivalent, table with no invented fps.",
        show_say="Volunteer against the board. Serve first.",
        attempt_say="Studio. npm run dev first.",
        land_say="Report + repo. Next week 12+5. Keyboard path in the demo.",
        live=[
            ("0–10", "Headings", "Photograph."),
            ("10–50", "Desk review", "Two clocks + HUD."),
            ("50–60", "60s rehearsal", "Stop."),
        ],
        cut="New libraries. Keep freeze.",
        add="One 60-second rehearsal in front of another team.",
    )
    GOLD[(C, 15)] = dict(
        kernel="12+5; demo the beat; point at two clocks and a HUD label",
        success="they stop at 12 and can show select-vs-spin and a labeled control",
        invariant="no new features today",
        goal="presentations — not a content lecture",
        kind="presentations",
        board="""```
12 + 5
Show: two clocks · HUD label · keyboard or reduced-motion
No new drei on stage
```""",
        slides=[("Timer", "not a slide of R3F docs")],
        hook_say="Presentations. 12+5. Repo. Stop at 12. If the only interface is orbit-drag, say what you cut.",
        show_say="None. Present.",
        attempt_say="Present.",
        land_say="The habit — two clocks, a HUD, a budget table — is the capstone experience, not a second scene graph.",
        live=[("0–60", "Talks", "Cut at 12.")],
        cut="Debugging on stage.",
        add="One question: where is useState vs useFrame?",
    )


def _xr(GOLD: dict) -> None:
    C = "Virtual and Augmented Reality"
    GOLD[(C, 1)] = dict(
        kernel="immersive-vr / immersive-ar vs inline; feature detect; lab fallback required",
        success="they can run isSessionSupported and screenshot an inline fallback — no headset lottery",
        invariant="comfort and tracking beat extra polygons",
        goal="detect + inline; headset is extra evidence",
        board="""```
inline          always the lab deliverable
immersive-vr    headset extra
immersive-ar    often missing on desktop

navigator.xr?.isSessionSupported('immersive-vr')
HTTPS / localhost     user gesture     no CDN
```""",
        slides=[],
        hook_say="This is interaction design + the WebXR API, not a Unity degree. If it cannot run inline in the lab, it is not the weekly deliverable. Headset is extra evidence — never a lottery for the grade.",
        hook_ask="If there is no Quest in the room, did you fail week 1? Wait. Want: no — inline + detect.",
        frame_say="Three.js XRButton wraps requestSession. Camera permission is AR later. Secure context: localhost or HTTPS. http:// LAN IP is a plant.",
        frame_ask="Who must grant the session — a script on load, or a user gesture?",
        build=[
            "**Say:** Session types. Draw three boxes: inline, vr, ar.",
            "**Board:** detect snippet. Circle fallback.",
            "**Say:** TA headset video is evidence, not a substitute for student session code.",
        ],
        ask_build="Why HTTPS?",
        they_build="On paper: detect + what you screenshot if xr is undefined.",
        show_say="Detect modes; inline Three scene; XRButton if available. Plant Quest-only homework. Plant http://. Demo XR/code/01-detect.html.",
        attempt_say="isSessionSupported + a fallback sentence on the page. Eight minutes.",
        land_say="Lab: HTTPS note; fallback screenshot. Homework: session types. Quiz: immersive-vr, HTTPS, gesture.",
        live=[
            ("0–10", "Detect xr", "Plant Quest-only."),
            ("10–30", "Inline scene", "Plant no fallback."),
            ("30–45", "Secure context", "Plant LAN http."),
            ("45–60", "They write the fallback line", "Circulate."),
        ],
        cut="Permissions deep-dive. Keep detect + fallback.",
        add="Fallback screenshot on the board as a checklist item.",
    )
    GOLD[(C, 2)] = dict(
        kernel="requestSession; local-floor; Three.js setAnimationLoop with XR",
        success="they can enable renderer.xr, request a session from a gesture, and end the session",
        invariant="comfort and tracking beat extra polygons",
        goal="a session that starts and ends",
        board="""```
viewer · local · local-floor · bounded-floor · unbounded

teaching: local-floor
renderer.xr.enabled = true
setAnimationLoop     pose from XRFrame

End session     (test exit)
```""",
        slides=[],
        hook_say="Spaces are not decoration. Unbounded as a week-2 requirement is a lottery. Standing origin this week; comfort is week 8 leftover + week 9.",
        hook_ask="Where is the floor — viewer space or local-floor? Wait.",
        frame_say="Three.js owns the XR loop; students still say the pose comes from the frame. Never testing exit is a plant. Inline still required.",
        frame_ask="What happens if we never call end?",
        build=[
            "**Say:** Names of spaces. Freeze local-floor.",
            "**Board:** enabled = true. Gesture → session. End button.",
            "**Say:** Headset or TA recording; students still write the code. Fallback: inline floor plane.",
        ],
        ask_build="Why not unbounded this week?",
        they_build="On paper: start/end arrows + local-floor origin.",
        show_say="Enter VR if hardware; else TA video + student code. Plant missing end. Floor plane in inline.",
        attempt_say="xr.enabled + end-session button (inline stub OK). Eight minutes.",
        land_say="Lab: end button; floor plane. Homework: space names. Quiz: local-floor, loop, why end.",
        live=[
            ("0–15", "Spaces on board", "Plant unbounded required."),
            ("15–40", "requestSession + loop", "Plant no gesture."),
            ("40–55", "End session", "Never-exit plant."),
            ("55–60", "They add a floor plane", "Circulate."),
        ],
        cut="Comfort vignette. Keep session + local-floor.",
        add="Floor plane in inline.",
    )
    GOLD[(C, 3)] = dict(
        kernel="XRInputSource; select is the click; debug the ray",
        success="they can select a cube along a controller or mouse-ray fallback and change its color",
        invariant="comfort and tracking beat extra polygons",
        goal="a ray you can see",
        board="""```
hands · controllers · gaze (last resort)
select  =  click
squeeze =  named extra

controller.addEventListener('select', …)
show the ray     or it is mouse-only theatre
```""",
        slides=[],
        hook_say="Mouse-only and calling it VR fails. Gaze is last resort. The ray must be visible in the lab fallback too.",
        hook_ask="If I cannot see the ray, how do I debug a miss? Wait.",
        frame_say="Three.js XRControllerModelFactory / Raycaster from controller. Haptics pulse named, not required. Inline: mouse ray analog.",
        frame_ask="What event is the click?",
        build=[
            "**Say:** Input sources. select vs squeeze.",
            "**Board:** select listener. Draw the ray.",
            "**Say:** Fallback: click-to-select on the inline cube. Same verb.",
        ],
        ask_build="Why is gaze last resort?",
        they_build="On paper: select → recolor. Fallback arrow.",
        show_say="Point and select to recolor. Plant mouse-only with no ray. Show the ray. Squeeze extra.",
        attempt_say="select listener + visible ray or mouse analog. Eight minutes.",
        land_say="Lab: show ray; squeeze extra. Homework: select vs squeeze. Quiz: XRInputSource, select, why debug ray.",
        live=[
            ("0–15", "select listener", "Plant mouse-only VR."),
            ("15–40", "Draw the ray", "Plant no debug."),
            ("40–55", "Inline click analog", "Headset lottery plant."),
            ("55–60", "They recolor a cube", "Circulate."),
        ],
        cut="Haptics API. Keep select + ray.",
        add="squeeze extra.",
    )
    GOLD[(C, 4)] = dict(
        kernel="teleport + snap turn as default policy; smooth optional behind a setting",
        success="they can teleport to a floor hit and snap 30°; smooth is not the only path",
        invariant="comfort and tracking beat extra polygons",
        goal="locomotion that does not assume a stomach",
        board="""```
default:  teleport  +  snap ~30°
optional: smooth     behind a setting
never:    fly by default

raycast floor → on select, move rig to hit
vignette named extra
```""",
        slides=[],
        hook_say="Vection makes people sick. Teleport + snap is the student policy unless they document otherwise. Smooth-only is a fail. Flying by default is a fail.",
        hook_ask="Who is the locomotion for — the demo reel or the person in the chair? Wait.",
        frame_say="A plane is enough; navmesh named. Blink fade extra. Inline: click-to-move on the plane. Comfort leftover in week 8.",
        frame_ask="Why hide smooth behind a setting?",
        build=[
            "**Say:** Comfort first. Policy on the board.",
            "**Board:** teleport vs smooth. Snap 30°.",
            "**Say:** Seated still works. No headset lottery for the lab.",
        ],
        ask_build="What is snap turn for?",
        they_build="Sketch floor hit → rig move; mark snap.",
        show_say="Teleport on select-hit; snap 30°. Plant smooth-only. Plant flying. Inline click-to-move.",
        attempt_say="Teleport to plane hit (or inline analog). Eight minutes.",
        land_say="Lab: disable smooth or hide it; vignette extra. Homework: policy paragraph. Quiz: default locomotion, snap, no fly.",
        live=[
            ("0–15", "Policy: teleport+snap", "Plant smooth-only."),
            ("15–40", "Floor hit → move", "Plant fly."),
            ("40–55", "Inline click-to-move", "Lottery plant."),
            ("55–60", "They add snap", "Circulate."),
        ],
        cut="Blink shader. Keep teleport + policy.",
        add="Vignette name extra.",
    )
    GOLD[(C, 5)] = dict(
        kernel="hit-test pose on a plane, or inline fake plane; ARKit-native is not the homework",
        success="they can place an object on a real hit-test or a documented fake plane",
        invariant="comfort and tracking beat extra polygons",
        goal="place on a plane without a headset lottery",
        board="""```
immersive-ar  +  hit-test source
desktop: often no AR  →  mouse-place on fake plane

requestHitTestSource({ space: viewerSpace })
document the device     camera permission
```""",
        slides=[],
        hook_say="AR is a pose on a detected plane. Desktop often has no AR. The lab is real hit-test or a fake plane — written in the README. Native ARKit as the homework is out of scope.",
        hook_ask="If Chrome on the lab laptop has no AR, what do you submit? Wait. Want: inline fake plane + the same place verb.",
        frame_say="Anchors persist next week. Privacy: camera. Policy in the syllabus. Remove-last extra.",
        frame_ask="What is a hit-test in one sentence?",
        build=[
            "**Say:** Plane detection idea. Pose, not a mesh of the room.",
            "**Board:** hit-test vs fake plane. Same place verb.",
            "**Say:** Document device. No lottery.",
        ],
        ask_build="Why is an ARKit app the wrong homework?",
        they_build="README two lines: device, fallback.",
        show_say="Place on plane or fake plane. Plant no fallback. Plant native-only. Remove-last extra.",
        attempt_say="Click-to-place on a plane (fake OK). Eight minutes.",
        land_say="Lab: document device; remove-last extra. Homework: fallback paragraph. Quiz: hit-test, fake plane, camera.",
        live=[
            ("0–15", "Hit-test name", "Plant ARKit homework."),
            ("15–40", "Place on plane / fake", "Plant no fallback."),
            ("40–55", "Document device", "Lottery plant."),
            ("55–60", "They place one object", "Circulate."),
        ],
        cut="Privacy law. Keep place + fallback.",
        add="Remove last extra.",
    )
    GOLD[(C, 6)] = dict(
        kernel="anchor = world-locked pose this session; honesty about 'forever'",
        success="they can place two anchored cubes that stay while walking, or say the inline analog",
        invariant="comfort and tracking beat extra polygons",
        goal="locked pose, not a floating bug",
        board="""```
createAnchor(pose, space)
this session  ≠  cloud forever

meters     a 10 m cube is a bug
unanchored HUD floats — call it out
```""",
        slides=[],
        hook_say="Anchors are a stable pose in the XR world. Cloud anchors as required work is a lottery and a product claim we do not make. Scale is meters — Blender habit.",
        hook_ask="If I walk around, why did the cube follow my head? Wait. Want: never anchored.",
        frame_say="UA-dependent. Student honesty: this session vs forever. Clear-all. 0.2 m object as a sanity check.",
        frame_ask="What do you write if persistence is not available?",
        build=[
            "**Say:** World-locked vs head-locked.",
            "**Board:** createAnchor. Session vs forever.",
            "**Say:** Scale. Furniture is not 10 m.",
        ],
        ask_build="Why is a cloud-anchor vendor the wrong required lab?",
        they_build="On paper: two poses, walk, they stay.",
        show_say="Two anchored cubes; walk. Plant unanchored floating UI. Plant cloud required. Inline: parent to world, not camera.",
        attempt_say="Two world-locked boxes (inline parent OK). Eight minutes.",
        land_say="Lab: clear all; 0.2 m scale. Homework: session vs forever. Quiz: anchor, meters, no cloud required.",
        live=[
            ("0–15", "Anchor vs float", "Plant head-locked cube."),
            ("15–40", "Two cubes stay", "Plant cloud required."),
            ("40–55", "Scale 0.2 m", "10 m plant."),
            ("55–60", "They clear all", "Circulate."),
        ],
        cut="Cloud maps. Keep session anchor + scale.",
        add="0.2 m object as a ruler.",
    )
    GOLD[(C, 7)] = dict(
        kernel="diegetic / world panel, large hits, waist height; not a 2D site at 1 m",
        success="they can laser-select three large world buttons and say why tiny text fails",
        invariant="comfort and tracking beat extra polygons",
        goal="XR UI you can hit while seated",
        board="""```
diegetic / world panel     vs     browser DOM only
arm's length     large hits     ~3–5° teaching target
waist / rest     not arms-up forever

sitting layout still works
```""",
        slides=[],
        hook_say="VR UI is not a website pasted at one meter. Prefer world panels, large targets, rest poses. Browser-DOM-only never in-world fails the week. Tiny text fails.",
        hook_ask="After two minutes arms-up, what happened to accuracy? Wait.",
        frame_say="Hover scale. Sitting layout extra. Feedback: highlight; sound/haptic optional. Inline: the same three buttons in a panel.",
        frame_ask="Diegetic vs HUD in one sentence?",
        build=[
            "**Say:** Affordances. Hits you can see.",
            "**Board:** three buttons, arm's length. Sitting mark.",
            "**Say:** Fatigue. Waist-level menus.",
        ],
        ask_build="Why not only DOM overlay this week?",
        they_build="Sketch a seated panel with three hits.",
        show_say="World panel, three large buttons, laser select. Plant tiny text. Plant DOM-only. Sitting layout extra.",
        attempt_say="Three world buttons (or inline panel analog). Eight minutes.",
        land_say="Lab: hover scale; sitting extra. Homework: diegetic vs HUD. Quiz: hit size, fatigue, sitting. Next: midterm then comfort.",
        live=[
            ("0–15", "World panel", "Plant DOM-only."),
            ("15–40", "Large hits + laser", "Plant tiny text."),
            ("40–55", "Sitting layout", "Arms-up plant."),
            ("55–60", "They add hover scale", "Circulate."),
        ],
        cut="Full UX paper. Keep panel + hits.",
        add="Sitting layout extra.",
    )
    GOLD[(C, 8)] = dict(
        kernel="midterm; then comfort: snap, vignette, seated, teleport vs optional smooth",
        success="after the exam they can toggle teleport vs smooth and name vignette as a comfort tool",
        invariant="comfort and tracking beat extra polygons",
        goal="midterm, then a settings panel",
        kind="midterm",
        midterm_topics="inline vs immersive; fallback; local-floor; select/ray; teleport+snap policy; hit-test or fake plane; session anchors; diegetic hits.",
        board="""```
settings:  teleport | smooth (optional)
           snap     | vignette
           seated height

dropped frames  →  sickness
measure or omit fps     no invented 90
```""",
        slides=[],
        hook_say="This meeting is a **midterm**, then comfort. No laptop for the exam. After: IPD is a headset fact we name; we do not diagnose. Vignette on move. Do not invent 90 fps.",
        show_say="Settings panel: teleport vs optional smooth; vignette toggle. Plant smooth-only. Plant invented 90 fps. Demo XR/code/02-safety.html if needed.",
        attempt_say="Two settings that change locomotion or vignette (inline analog OK).",
        land_say="Lab: seated height extra; fps only if measured. Homework: midterm rewrite. Next: fill rate. No quiz this week.",
        live=[
            ("0–15", "Settings panel", "Plant no options."),
            ("15–40", "Vignette + snap", "Plant 90 fps claim."),
            ("40–60", "Seated height", "They type. Circulate."),
        ],
        cut="IPD hardware lecture. Keep settings + policy.",
        add="Seated camera height extra.",
    )
    GOLD[(C, 9)] = dict(
        kernel="stereo cost; framebuffer scale factor; cut bloom in VR; do not invent fps",
        success="they can setFramebufferScaleFactor and write a table: device, scale, what they cut",
        invariant="comfort and tracking beat extra polygons",
        goal="a cheaper frame, honestly measured",
        board="""```
two eyes     MSAA expensive     overdraw hurts
renderer.xr.setFramebufferScaleFactor(0.8)

cut bloom in VR     shadow map 512

device | scale | cut     — fps only if measured
```""",
        slides=[],
        hook_say="Two eyes. Desktop bloom stacks in VR are a common fail. Invented fps still forbidden. Scale 1.0 vs 0.7 is a look-vs-cost experiment — on a headset or a TA video, plus the same code path inline.",
        hook_ask="Does stereo mean two draws? Wait. Want: often yes, or multiview as a name.",
        frame_say="Multiview named. Quest targets documented, not invented. Student table required.",
        frame_ask="What do you cut first — bloom or the verb?",
        build=[
            "**Say:** Fill rate. Overdraw. Two eyes.",
            "**Board:** setFramebufferScaleFactor. Empty fps if unmeasured.",
            "**Say:** Shadow 512. Bloom off in VR.",
        ],
        ask_build="Why is desktop bloom a VR trap?",
        they_build="Fill the three-column table on paper.",
        show_say="Scale 1.0 vs 0.7; note look vs cost. Do not quote fps unless measured here. Plant bloom-on. Plant 90.",
        attempt_say="setFramebufferScaleFactor and log it. Eight minutes.",
        land_say="Lab: cut bloom; shadow 512. Homework: table. Quiz: two eyes, scale factor, no invented fps.",
        live=[
            ("0–15", "Stereo cost", "Plant 90 fps."),
            ("15–40", "Scale factor", "Plant bloom stack."),
            ("40–55", "Table on a named device", "They write."),
            ("55–60", "They cut bloom", "Circulate."),
        ],
        cut="Foveation implementation. Keep scale + table.",
        add="Shadow map 512.",
    )
    GOLD[(C, 10)] = dict(
        kernel="one spatial menu pattern; obvious exit; do not ship a custom keyboard as the project",
        success="they can open a wrist or look-down menu with three actions and exit XR",
        invariant="comfort and tracking beat extra polygons",
        goal="three actions, a way out",
        board="""```
pick one:  wrist · belt · look-to-pin
3 actions
exit XR  obvious     (OS menu still exists)

text entry is painful — fewer strings
```""",
        slides=[],
        hook_say="Patterns: wrist, belt, look-to-pin. Pick one. A custom keyboard as the whole project fails. Trapping the user fails.",
        hook_ask="Where is Exit? Wait. Then find it.",
        frame_say="World-locked mode extra. Companion-phone HUD named extra. Inline: the same three actions in a panel.",
        frame_ask="Why is text entry a last resort?",
        build=[
            "**Say:** One pattern. Three actions.",
            "**Board:** wrist/belt/look. Exit circled.",
            "**Say:** System: they must reach the OS menu. We do not trap.",
        ],
        ask_build="What is look-to-pin for?",
        they_build="Sketch one menu + exit.",
        show_say="Wrist or look-down menu, three actions. Plant no exit. Plant custom keyboard as the week.",
        attempt_say="Three-action menu + exit. Eight minutes.",
        land_say="Lab: world-locked extra; exit obvious. Homework: pattern paragraph. Quiz: one pattern, exit, no keyboard-project.",
        live=[
            ("0–15", "Pick a pattern", "Plant all three at once."),
            ("15–40", "Three actions", "Plant keyboard project."),
            ("40–55", "Exit XR", "Trap plant."),
            ("55–60", "They place exit", "Circulate."),
        ],
        cut="System keyboard research. Keep menu + exit.",
        add="Exit control obvious in inline too.",
    )
    GOLD[(C, 11)] = dict(
        kernel="VRButton/ARButton as oracles; students explain session + input",
        success="they can strip a Three.js XR example to a short file they can explain and cite",
        invariant="comfort and tracking beat extra polygons",
        goal="helpers you can read",
        board="""```
VRButton.createButton(renderer)
examples folder  =  oracle
cite the example URL

XREstimatedLight  +  fallback dir light
hand tracking     name only
```""",
        slides=[],
        hook_say="Helpers are not a license to paste 400 lines. Full example dump they cannot explain fails. Citation required. No CDN — local three build.",
        hook_ask="If I delete VRButton, what must you still know? Wait. Want: requestSession + loop.",
        frame_say="AR light estimate named; fallback directional. Hands optional extra. Remove unused passes.",
        frame_ask="What is an oracle in this course?",
        build=[
            "**Say:** Button helper. Then the session it hides.",
            "**Board:** createButton. Cite URL.",
            "**Say:** Strip to ~80 lines they can narrate.",
        ],
        ask_build="Why cite the example?",
        they_build="On paper: session, loop, select — three lines the helper wraps.",
        show_say="Strip a Three.js XR example. Plant dump. Plant no citation. Fallback dir light.",
        attempt_say="VRButton + one cube they can explain. Eight minutes.",
        land_say="Lab: cite URL; remove unused passes. Homework: 80-line explain. Quiz: VRButton, oracle, citation.",
        live=[
            ("0–15", "VRButton", "Plant CDN."),
            ("15–40", "Strip the example", "Plant dump."),
            ("40–55", "Cite + fallback light", "No citation plant."),
            ("55–60", "They narrate 80 lines", "Circulate."),
        ],
        cut="Hand tracking impl. Keep button + explain.",
        add="Remove unused passes.",
    )
    GOLD[(C, 12)] = dict(
        kernel="guardian, seated option, no jumpscares as required, no secret recording",
        success="they can ship a safety README: space, seated, data, epilepsy note",
        invariant="comfort and tracking beat extra polygons",
        goal="a lab that does not hurt people",
        board="""```
clear the space     sitting demos OK
no required jumpscares
no recording classmates in AR without consent
epilepsy note     (no 3 Hz strobe)

we do not give medical advice
```""",
        slides=[],
        hook_say="Real rooms have tables. Forced standing-only as an exam is a fail. Secret recording is a fail. We name epilepsy risk; we do not practice medicine. Demo XR/code/02-safety.html.",
        hook_ask="If a student is seated, is the experience allowed to exist? Wait. Want: yes.",
        frame_say="Single-user ethics still: AR cameras catch faces. Multiplayer moderation named if they ever add it — not this week. Course: no horror jumpscares as required content.",
        frame_ask="What goes in the safety README?",
        build=[
            "**Say:** Boundaries. Guardian / play space.",
            "**Board:** seated · consent · epilepsy note · no medical claims.",
            "**Say:** Harassment: if social ever, moderation. Today: do not trap, do not record silently.",
        ],
        ask_build="Why is a jumpscare the wrong required content?",
        they_build="Draft the safety README headings.",
        show_say="Safety README: space, seated, data. Plant standing-only exam. Plant secret recording. Plant a medical claim — strike it.",
        attempt_say="Write the README section. Eight minutes.",
        land_say="Lab: epilepsy note; no recording without consent. Homework: safety page. Quiz: seated, consent, no medical advice. Next: one verb.",
        live=[
            ("0–15", "Play space", "Plant standing-only."),
            ("15–40", "README: seated + data", "Plant secret recording."),
            ("40–55", "No medical claims", "Strike the sentence."),
            ("55–60", "They add epilepsy note", "Circulate."),
        ],
        cut="Policy lecture. Keep README + seated.",
        add="Consent line for AR camera.",
    )
    GOLD[(C, 13)] = dict(
        kernel="one verb well: place, inspect, or teleport-museum; fallback required",
        success="they can complete the verb inline and, if hardware exists, in session — same README",
        invariant="comfort and tracking beat extra polygons",
        goal="one verb, two modes",
        board="""```
one verb:  place furniture | inspect product | teleport museum
session + inline fallback
safety README linked
cite: controllers, HDRI, models
```""",
        slides=[],
        hook_say="Open-world VR is a cut. One verb. Headset is extra evidence. The happy path on a lab machine is the project.",
        hook_ask="If the TA has no headset, can they still finish the verb? Wait. Want: yes.",
        frame_say="Working session + fallback. Screenshots of both modes. Citations. Comfort defaults from week 8.",
        frame_ask="What is the verb in one word?",
        build=[
            "**Say:** Verb on the board. Circle it.",
            "**Board:** two columns: inline / immersive. Same verb.",
            "**Say:** Cite assets. Safety README linked.",
        ],
        ask_build="Why is open-world a fail this week?",
        they_build="One-sentence verb + fallback.",
        show_say="Working session if any + fallback. Plant open-world. Plant headset-only.",
        attempt_say="Finish the verb inline. Eight minutes of tightening, not features.",
        land_say="Lab: safety README; both-mode screenshots. Homework: freeze verb. Quiz: one verb, fallback, cite. Next: studio.",
        live=[
            ("0–15", "Name the verb", "Plant open-world."),
            ("15–40", "Fallback path", "Headset-only plant."),
            ("40–55", "Cite + safety link", "They write."),
            ("55–60", "They screenshot both", "Circulate."),
        ],
        cut="Second verb. Keep one + fallback.",
        add="Screenshots of both modes.",
    )
    GOLD[(C, 14)] = dict(
        kernel="XR mini: one verb, comfort defaults, inline fallback, safety README",
        success="a TA can finish the verb without a headset and without a second tool",
        invariant="comfort and tracking beat extra polygons",
        goal="studio — fallback first",
        kind="studio",
        board="""```
Must: verb · fallback · comfort setting · safety README · cite
Cuts: second verb, custom keyboard, cloud anchors
README: how to run inline     no CDN
```""",
        slides=[],
        hook_say="This meeting is **studio**. Fallback first, then headset if any. A lottery at the desk fails.",
        hook_ask="If behind, do you cut the headset path or the verb?",
        frame_say="Desk review: inline happy path, exit, seated option, no invented fps.",
        show_say="Volunteer: TA runs inline only.",
        attempt_say="Studio. Fallback first.",
        land_say="Report + repo. Next week 12+5. Show both modes if you have them — inline is required.",
        live=[
            ("0–10", "Headings", "Photograph."),
            ("10–50", "Desk review", "Fallback first."),
            ("50–60", "60s rehearsal", "Stop."),
        ],
        cut="New libraries. Keep freeze.",
        add="One 60-second rehearsal of the verb.",
    )
    GOLD[(C, 15)] = dict(
        kernel="12+5; demo the verb inline; point at fallback and a comfort setting",
        success="they stop at 12; TA could have done the verb seated",
        invariant="no new features today",
        goal="presentations — not a content lecture",
        kind="presentations",
        board="""```
12 + 5
Show: verb · inline fallback · exit · comfort
No new locomotion on stage
```""",
        slides=[("Timer", "not a Quest ad")],
        hook_say="Presentations. 12+5. Repo. Stop at 12. Headset is extra evidence.",
        show_say="None. Present.",
        attempt_say="Present.",
        land_say="If it ran inline, it was a lab. That habit is the capstone XR slice.",
        live=[("0–60", "Talks", "Cut at 12.")],
        cut="Debugging on stage.",
        add="One question: what if there is no headset?",
    )


def _ai(GOLD: dict) -> None:
    C = "AI for Interactive Graphics"
    GOLD[(C, 1)] = dict(
        kernel="this is not training GPT; human in the loop; no medical/legal product claims",
        success="they can list three allowed and three forbidden uses and say exams stay human",
        invariant="no secrets in the frontend; cite the model",
        goal="scope the course before a key exists",
        board="""```
human  +  model  +  graphics app

NOT:  train GPT/CUDA ML
NOT:  medical or legal advice as a product
NOT:  keys in Three.js
NOT:  unlabeled gen as 'I modeled this'

.env is server-side
```""",
        slides=[],
        hook_say="APIs, images-as-textures, limits of 3D-gen, agents that drive a scene, latency, eval — not an ML degree and not a startup in 15 weeks. We do not train GPT. We do not ship medical or legal advice. Integrity from week 1.",
        hook_ask="Is a Midjourney albedo you did not label 'your model'? Wait. Want: no.",
        frame_say="Handbook: disclose tools; exams human. Harm: no CSAM, no non-consensual deepfakes, no medical advice as a claim. Keys never in the client — week 2 architecture, named today.",
        frame_ask="Where does a vendor key live?",
        build=[
            "**Say:** Generative vs classical graphics. Both can be in a scene; only one is a dice roll.",
            "**Board:** human + model + app. Strike train-GPT, strike medical/legal claims, strike VITE_SECRET.",
            "**Say:** Asset table starts empty — still a table. Demo 01-proxy-mock.html as the later shape.",
        ],
        ask_build="What is a forbidden product claim this term?",
        they_build="Three allowed / three forbidden uses on paper.",
        show_say="One-page ethics addendum for their future idea. Plant a key in client JS. Plant a medical chatbot. Strike both.",
        attempt_say="Allowed/forbidden list + 'no keys in frontend' line. Eight minutes.",
        land_say="Lab: list + API key policy. Homework: authorship policy. Quiz: frontend secrets, label gen, exam policy.",
        live=[
            ("0–10", "Scope: not training GPT", "Plant startup pitch."),
            ("10–30", "No medical/legal claims", "Plant diagnostic app."),
            ("30–45", "No VITE_SECRET", "Plant key in Three.js."),
            ("45–60", "They write three+three", "Circulate."),
        ],
        cut="Harm slideshow. Keep scope + key rule.",
        add="API key policy sentence in the addendum.",
    )
    GOLD[(C, 2)] = dict(
        kernel="browser → your proxy → vendor; mock is first-class; key never in the repo",
        success="they can fetch('/api/complete') against a mock or proxy and show .env is not in git",
        invariant="no secrets in the frontend; cite the model",
        goal="a proxy or an honest mock",
        board="""```
browser  →  POST /api/complete  →  proxy  →  vendor
                ↑
              mock JSON is a valid lab

key in GitHub  =  fail
unbounded spend  =  fail
ToS: student work, not resale
```""",
        slides=[],
        hook_say="The browser never sees the vendor key. Same as any production app. If there is no budget, a mock server is the lab — architecture still counts. Demo 01-proxy-mock.html.",
        hook_ask="Does a mock mean you skipped the course? Wait. Want: no — you still have a proxy shape.",
        frame_say="Error states and timeout. No CDN vendor SDK required. Read ToS at teaching level — we are not lawyers.",
        frame_ask="What happens on 401 from the proxy?",
        build=[
            "**Say:** Three boxes. Key lives in the middle box.",
            "**Board:** fetch POST. Mock returns canned JSON.",
            "**Say:** .gitignore .env. Unbounded student spend is a plant.",
        ],
        ask_build="Why not VITE_OPENAI_KEY?",
        they_build="On paper: the three boxes and where the key sits.",
        show_say="fetch('/api/complete') against mock. Plant key in the HTML. Plant infinite retries. Timeout.",
        attempt_say="Button → mock complete → show JSON. Eight minutes.",
        land_say="Lab: error states; timeout. Homework: why the key is not in the client. Quiz: proxy, mock OK, no GitHub key.",
        live=[
            ("0–15", "Three boxes", "Plant client key."),
            ("15–40", "Mock fetch", "Plant real key in repo."),
            ("40–55", "Timeout / error", "Unbounded spend plant."),
            ("55–60", "They hide .env", "Circulate."),
        ],
        cut="ToS law. Keep proxy + mock.",
        add="Timeout UI.",
    )
    GOLD[(C, 3)] = dict(
        kernel="prompt → image → Three map; human picks among retries; cite model+date",
        success="they can apply a generated or mock albedo and fill one asset-table row",
        invariant="no secrets in the frontend; cite the model",
        goal="look-dev with a dice roll, still PBR slots",
        board="""```
prompt → image → map (sRGB)
human picks among 4     not first-output-wins

| file | source | license | gen? | prompt/model | edits |

budget 1024     not 8k
one diffuse ≠ full PBR
```""",
        slides=[],
        hook_say="This is look-dev with a dice roll. They still know albedo vs roughness from RTR/Blender. Claiming PBR from one diffuse fails. Demo 02-asset-table.html.",
        hook_ask="If the map is 8k, what did we forget? Wait. Want: budget.",
        frame_say="colorSpace sRGB for albedo. Seed, size, retries. Cite prompt + model + date. Reject three images on purpose.",
        frame_ask="What column is required if generated? is yes?",
        build=[
            "**Say:** Pipeline. Then the table — even for a mock PNG.",
            "**Board:** asset table header. Circle gen? and prompt.",
            "**Say:** Second sphere handmade color for comparison.",
        ],
        ask_build="Why not first-output-wins in the report?",
        they_build="Fill one asset-table row for the lab map.",
        show_say="Mock or real albedo on a sphere; handmade neighbor. Plant 8k. Plant 'I modeled this'. Fill the table.",
        attempt_say="Apply map + one table row. Eight minutes.",
        land_say="Lab: reject 3; budget 1024. Homework: cite the model. Quiz: sRGB, table, not full PBR.",
        live=[
            ("0–15", "Image → map", "Plant client key again."),
            ("15–40", "Asset table row", "Plant unlabeled Midjourney."),
            ("40–55", "1024 budget", "8k plant."),
            ("55–60", "They compare handmade", "Circulate."),
        ],
        cut="Full material gen. Keep albedo + table.",
        add="Budget 1024 on the board.",
    )
    GOLD[(C, 4)] = dict(
        kernel="inspect image-to-3D: normals, holes, scale, legal question — cleanup is the skill",
        success="they can fill a table: gen mesh vs a crate (tris, UVs, scale) and not call the gen the homework",
        invariant="no secrets in the frontend; cite the model",
        goal="inspection, not one-click mesh",
        board="""```
gen mesh → Blender cleanup → glTF
inspect: normals  holes  scale  UVs

we mention IP lawsuits     we do not play lawyer
one-click mesh as the whole HW  =  fail
```""",
        slides=[("Wireframe of a gen mesh vs a crate", "photograph")],
        hook_say="Tools improve; the teaching point is inspection. One-click mesh as the whole homework fails. We mention training-data lawsuits; we do not give legal advice.",
        hook_ask="If UVs are missing, is the mesh done? Wait. Want: no.",
        frame_say="Survey is allowed if tools cost money. Cleanup in Blender extra. Screenshot wireframe. Scale is meters.",
        frame_ask="What do you write instead of a legal conclusion?",
        build=[
            "**Say:** Honesty. Limits of image-to-3D.",
            "**Board:** inspect list. IP: mention, don't advise.",
            "**Say:** Table: tris, UVs yes/no, scale vs student crate.",
        ],
        ask_build="Why is cleanup the course skill?",
        they_build="Empty table headers; they fill from a still or a file.",
        show_say="Gen vs crate table. Plant one-click as HW. Plant a legal claim — strike. Wireframe screenshot.",
        attempt_say="Fill the inspection table. Eight minutes.",
        land_say="Lab: cleanup extra; wireframe. Homework: limits paragraph. Quiz: inspect list, no legal advice, cleanup.",
        live=[
            ("0–15", "Inspect list", "Plant one-click HW."),
            ("15–40", "Table vs crate", "Plant no inspection."),
            ("40–55", "No legal claims", "Strike the sentence."),
            ("55–60", "They screenshot wireframe", "Circulate."),
        ],
        cut="IP seminar. Keep inspect + cleanup.",
        add="Wireframe screenshot.",
    )
    GOLD[(C, 5)] = dict(
        kernel="agent = loop + allowlisted tools (setColor, setCamera); no eval; log every action",
        success="they can run a mock agent that calls setColor and show the tool log",
        invariant="no secrets in the frontend; cite the model",
        goal="tools on a scene, not a generic chatbot",
        board="""```
thought → action → observe   (ReAct name)
tools = { setColor, resetCamera }   allowlist
max 4 steps
no eval     no shell
log every call
```""",
        slides=[],
        hook_say="A chatbot that calls setMetalness is more IGWT than a generic assistant. Unbounded agents with shell access fail. Hidden tool logs fail. Mock LLM is first-class.",
        hook_ask="If the model says eval('…'), what does our proxy do? Wait. Want: refuse — not in the allowlist.",
        frame_say="Confirm dialog extra. Max 4 steps. Keys still on the server. We are not training the model.",
        frame_ask="What is a tool in one sentence?",
        build=[
            "**Say:** Graphics agents. Tools are functions we wrote.",
            "**Board:** allowlist. Log. Max 4.",
            "**Say:** ReAct as a name. Teaching level.",
        ],
        ask_build="Why log tools?",
        they_build="On paper: two tools and one refused action.",
        show_say="Mock LLM calls setColor / resetCamera; log actions. Plant eval. Plant hidden log. Plant shell.",
        attempt_say="One tool call + log line. Eight minutes.",
        land_say="Lab: confirm extra; max 4. Homework: allowlist paragraph. Quiz: tools, no eval, log.",
        live=[
            ("0–15", "Allowlist", "Plant eval."),
            ("15–40", "setColor log", "Plant hidden log."),
            ("40–55", "Max 4 steps", "Unbounded plant."),
            ("55–60", "They refuse a bad tool", "Circulate."),
        ],
        cut="Full ReAct paper. Keep allowlist + log.",
        add="Max 4 steps on the board.",
    )
    GOLD[(C, 6)] = dict(
        kernel="retrieve then generate; keyword search over local captions is enough",
        success="they can show the retrieved chunk beside the answer and a miss case",
        invariant="no secrets in the frontend; cite the model",
        goal="your captions, not the model's memory",
        board="""```
query → retrieve chunk → generate (or mock)
cite filename

keyword filter is a valid lab
vector DB optional extra

wrong chunk → confident nonsense
```""",
        slides=[],
        hook_say="A museum app should answer from your captions. Embeddings as required infrastructure week 6 fail. Show a miss. Cite the file.",
        hook_ask="If retrieval misses, should the model still sound sure? Wait. Want: no — show the miss.",
        frame_say="Split a few markdown files. Mock the generate step. No frontend secrets if a real model is used.",
        frame_ask="What do you display besides the answer?",
        build=[
            "**Say:** Why RAG. Grounding.",
            "**Board:** retrieve then generate. Cite filename.",
            "**Say:** Failure: wrong chunk. They must see it.",
        ],
        ask_build="Why is a vector DB not required today?",
        they_build="Three local captions; one query that misses.",
        show_say="Query box over 3 captions; show chunk + mocked answer. Plant no citation. Plant embeddings-required. Show a miss.",
        attempt_say="Filter + display hit. Eight minutes.",
        land_say="Lab: miss case; cite filename. Homework: miss paragraph. Quiz: retrieve-then-generate, cite, miss.",
        live=[
            ("0–15", "Local captions", "Plant vector DB required."),
            ("15–40", "Show the chunk", "Plant no cite."),
            ("40–55", "A miss case", "Confident-nonsense plant."),
            ("55–60", "They cite the file", "Circulate."),
        ],
        cut="Embedding math. Keep retrieve + miss.",
        add="Cite filename on the HUD.",
    )
    GOLD[(C, 7)] = dict(
        kernel="asset table + prompt log; unlabeled gen is an integrity case",
        success="they can fill a table for a mini scene even if every file is handmade",
        invariant="no secrets in the frontend; cite the model",
        goal="a lab notebook for assets",
        board="""```
| file | source | license | generated? | prompt/model | human edits |

empty table because 'just a cube'  =  fail
labeled gen + human cleanup        =  OK
exams remain human
```""",
        slides=[],
        hook_say="Good students keep a prompt log like a lab notebook. Unlabeled gen is an integrity case. Labeled gen with cleanup is fine. TAs will spot-check one asset. Demo 02-asset-table.html.",
        hook_ask="If it was 'just a cube,' do you still have a row? Wait. Want: yes.",
        frame_say="Peer review of a stripped table. Template in the repo. Same rule as Teaching/12: disclose; explain.",
        frame_ask="What is the difference between labeled gen and a lie?",
        build=[
            "**Say:** Process. The table is the kernel.",
            "**Board:** six columns. Fill one handmade row.",
            "**Say:** Spot-check. Prompts recorded.",
        ],
        ask_build="Who is the table for — the model or the TA?",
        they_build="Fill three rows (handmade allowed).",
        show_say="Fill an asset table for a mini scene. Plant empty table. Plant missing prompts. Peer swap names stripped.",
        attempt_say="Three rows. Eight minutes.",
        land_say="Lab: peer review; template in repo. Homework: table in README. Quiz: columns, unlabeled = case, cube still has a row. Next: midterm then latency.",
        live=[
            ("0–15", "Columns", "Plant empty table."),
            ("15–40", "Fill handmade + gen", "Plant unlabeled."),
            ("40–55", "Peer review stripped", "They mark a miss."),
            ("55–60", "Template in repo", "Circulate."),
        ],
        cut="TA process lecture. Keep table + log.",
        add="Prompt log template file.",
    )
    GOLD[(C, 8)] = dict(
        kernel="midterm; then latency: stream or placeholder; 3D keeps orbiting; abort",
        success="after the exam they can orbit a cube while a mocked stream fills a HUD",
        invariant="no secrets in the frontend; cite the model",
        goal="midterm, then time-to-first-token as UX",
        kind="midterm",
        midterm_topics="not training GPT; no frontend secrets; proxy/mock; image→map + asset table; 3D-gen inspect; allowlisted tools; RAG retrieve-then-cite.",
        board="""```
time to first token     (name; measure later)
3D orbits while text streams
placeholder on textures
abort · timeout
retries cost $     cache mocks in dev
```""",
        slides=[],
        hook_say="This meeting is a **midterm**, then latency UX. No laptop for the exam. After: a frozen canvas waiting on a vendor is a fail. Placeholders. Abort. Do not invent milliseconds.",
        show_say="Orbit a cube while a mocked stream fills a HUD. Plant blocking fetch that freezes the canvas. Abort button.",
        attempt_say="Placeholder + abort. Two clocks: rAF vs await.",
        land_say="Lab: abort; timeout UI. Homework: midterm rewrite. Next: vision. No quiz this week.",
        live=[
            ("0–15", "Orbit during mock stream", "Plant frozen canvas."),
            ("15–40", "Placeholder texture", "Plant blocking await."),
            ("40–60", "Abort + timeout", "They type. Circulate."),
        ],
        cut="Vendor streaming protocol. Keep placeholder + abort.",
        add="Timeout UI.",
    )
    GOLD[(C, 9)] = dict(
        kernel="button-captured 256px snapshot to mock/real vision; never 30 fps of classmates",
        success="they can capture a downscaled canvas still, show a label, and state the privacy note",
        invariant="no secrets in the frontend; cite the model",
        goal="one shot, a label, not a webcam firehose",
        board="""```
button → canvas.toBlob jpeg q~0.7 → proxy/mock → HUD label
256px crop
not every frame
not webcam-to-vendor of classmates
throttle
```""",
        slides=[],
        hook_say="Vision is image in, labels out. Webcam 30 fps of the room to a vendor fails ethics and budget. One shot on a button. Privacy note. No medical diagnosis labels as a product.",
        hook_ask="Why not send every frame? Wait. Want: cost, latency, privacy.",
        frame_say="Use: describe a part, QR, a11y captions. Proxy still holds the key. Throttle.",
        frame_ask="What is the privacy sentence?",
        build=[
            "**Say:** Snapshot. Downscale.",
            "**Board:** button, 256px, label. Strike 30 fps class demo.",
            "**Say:** Harm: we do not claim a diagnostic.",
        ],
        ask_build="When is a mock label enough?",
        they_build="Privacy note + throttle on paper.",
        show_say="Capture 256px; show mock label. Plant 4k PNG. Plant classmate webcam stream. Plant medical label.",
        attempt_say="toBlob + mock label on HUD. Eight minutes.",
        land_say="Lab: privacy note; throttle. Homework: why not every frame. Quiz: 256px, button, no classmate firehose.",
        live=[
            ("0–15", "256px capture", "Plant 4k."),
            ("15–40", "Mock label HUD", "Plant every-frame."),
            ("40–55", "Privacy + no medical claim", "Webcam plant."),
            ("55–60", "They add throttle", "Circulate."),
        ],
        cut="Cost spreadsheets. Keep one-shot + privacy.",
        add="Throttle on the button.",
    )
    GOLD[(C, 10)] = dict(
        kernel="STT/TTS as names; captions required; push-to-talk; never always-on mic default",
        success="they can push-to-talk a mock transcript into a tool (color or camera) with captions on",
        invariant="no secrets in the frontend; cite the model",
        goal="voice as an input, captions as the product",
        board="""```
push-to-talk → STT (mock OK) → tool
TTS optional     captions always
mic indicator
Web Speech API named     vendor STT via proxy
```""",
        slides=[],
        hook_say="Captions are required even if TTS is the fun part. Always-on mic as default fails. TTS without captions fails. XR later: still captions on a panel. No medical dictation product.",
        hook_ask="If the speaker is muted, can they still use the feature? Wait. Want: yes — captions / HUD.",
        frame_say="Proxy for vendor STT. Mic indicator. Keys not in the client.",
        frame_ask="Why push-to-talk?",
        build=[
            "**Say:** a11y first. Captions.",
            "**Board:** PTT → transcript → setColor. Mic indicator.",
            "**Say:** Always-on is a plant.",
        ],
        ask_build="Where do captions live in XR?",
        they_build="PTT flow on paper plus captions.",
        show_say="PTT → mock transcript → set color or camera beat. Plant always-on. Plant TTS without captions.",
        attempt_say="Mock transcript applies one tool. Eight minutes.",
        land_say="Lab: captions on; mic indicator. Homework: PTT paragraph. Quiz: captions, PTT, no always-on.",
        live=[
            ("0–15", "Captions required", "Plant TTS-only."),
            ("15–40", "PTT → tool", "Plant always-on mic."),
            ("40–55", "Mic indicator", "They add it."),
            ("55–60", "They apply setColor", "Circulate."),
        ],
        cut="XR voice spatialization. Keep PTT + captions.",
        add="Mic indicator.",
    )
    GOLD[(C, 11)] = dict(
        kernel="AI as salesperson on enums: validate {part, finish}; undo; no freeform shaders",
        success="they can reject invalid JSON and apply a finish only from FINISHES",
        invariant="no secrets in the frontend; cite the model",
        goal="constrained generation",
        board="""```
FINISHES = ['oak','steel','matte']
if (!FINISHES.includes(data.finish)) throw

AI proposes     schema validates     user confirms
undo every apply
freeform 'gold-er' writing shaders  =  fail
```""",
        slides=[],
        hook_say="The configurator is structured. AI is a salesperson, not the CAD kernel. Freeform 'make it gold-er' that writes shaders fails. Validate. Confirm. Undo.",
        hook_ask="If the model returns finish: 'gold-er', what happens? Wait. Want: throw / reject, do not compile a shader.",
        frame_say="Three finishes. Mock or real via proxy. Invalid JSON handling. Keys still server-side.",
        frame_ask="Who is allowed to invent a new part?",
        build=[
            "**Say:** Enums. The 3D product already has parts.",
            "**Board:** includes check. Confirm. Undo.",
            "**Say:** Parse + validate. Never eval the payload.",
        ],
        ask_build="Why confirm before apply?",
        they_build="On paper: valid vs invalid payload.",
        show_say="Three finishes; model may only pick among them; apply on confirm. Plant freeform shader. Plant no validate. Undo.",
        attempt_say="Reject invalid finish. Eight minutes.",
        land_say="Lab: invalid JSON; undo. Homework: schema paragraph. Quiz: enums, validate, undo.",
        live=[
            ("0–15", "FINISHES enum", "Plant freeform."),
            ("15–40", "Validate + confirm", "Plant no check."),
            ("40–55", "Undo", "They apply twice."),
            ("55–60", "They handle bad JSON", "Circulate."),
        ],
        cut="Full CAD. Keep enums + undo.",
        add="Undo stack of one.",
    )
    GOLD[(C, 12)] = dict(
        kernel="eval table: task success, latency name, call count/$, harm, citation — not one lucky still",
        success="they can score five outputs and pick one for the scene with costs counted",
        invariant="no secrets in the frontend; cite the model",
        goal="a scored pick, not a vibe",
        board="""```
task success | latency (measured or blank) | calls/$ | harm | citation

one lucky screenshot  ≠  eval
mock: still count calls
no invented ms     no invented fps
```""",
        slides=[],
        hook_say="Graphics papers measure error. AI features need task measures: did the user finish configuring? Hidden costs fail. One lucky screenshot is not eval. Harm checklist — not a legal memo.",
        hook_ask="If you did not count calls, what do you write in the $ column? Wait. Want: unknown — not a fake number.",
        frame_say="Even mocks count calls. Latency: measure or omit. Harm: biased labels, unsafe images — a checklist, not a diagnosis.",
        frame_ask="What is task success for a configurator?",
        build=[
            "**Say:** Rubric. Five columns.",
            "**Board:** score 5. Pick 1. Count calls.",
            "**Say:** Harm note. Citation of model.",
        ],
        ask_build="Why count mock calls?",
        they_build="Empty table; they fill two rows.",
        show_say="Score 5 outputs; pick one. Plant lucky screenshot as eval. Plant hidden costs. Plant invented ms.",
        attempt_say="Fill five rows; circle the pick. Eight minutes.",
        land_say="Lab: cost column; one harm note. Homework: eval paragraph. Quiz: task success, count calls, no lucky still. Next: thin slice.",
        live=[
            ("0–15", "Rubric columns", "Plant lucky still."),
            ("15–40", "Score 5 / pick 1", "Plant hidden $."),
            ("40–55", "Harm checklist", "They write one note."),
            ("55–60", "They count calls", "Circulate."),
        ],
        cut="Harm seminar. Keep table + pick.",
        add="One harm note row.",
    )
    GOLD[(C, 13)] = dict(
        kernel="one AI-backed graphics feature: texture, copy, tool, or RAG caption — with logs",
        success="they can demo the slice, show the asset table, and name a key-leak threat",
        invariant="no secrets in the frontend; cite the model",
        goal="depth over a chatbot wrapper",
        board="""```
one feature in a scene
proxy/mock     asset table     eval row
README threats: key leak, ToS
cite model, date, prompts
wrapper chatbot with no 3D  =  fail
```""",
        slides=[],
        hook_say="Capstone energy. Mock the model, keep the architecture. A wrapper around a chatbot with no 3D fails. No medical/legal claims in the slice.",
        hook_ask="If the vendor is down, does the architecture still demo? Wait. Want: yes — mock.",
        frame_say="Working slice + logs. Cuts allowed. Cite. Screenshot.",
        frame_ask="What is the one feature?",
        build=[
            "**Say:** Slice. Depth.",
            "**Board:** feature · logs · table · threats.",
            "**Say:** Chatbot-only is a cut to fail.",
        ],
        ask_build="What threat goes in the README?",
        they_build="One-sentence feature + mock/real.",
        show_say="Working slice + logs. Plant chatbot wrapper. Plant key in client. Plant medical claim.",
        attempt_say="Tighten the slice; fill threats. Eight minutes.",
        land_say="Lab: README threats; screenshot. Homework: freeze feature. Quiz: one feature, table, no secrets. Next: studio.",
        live=[
            ("0–15", "Name the feature", "Plant chatbot wrapper."),
            ("15–40", "Logs + table", "Plant client key."),
            ("40–55", "Threats README", "Medical-claim plant."),
            ("55–60", "They screenshot", "Circulate."),
        ],
        cut="Second feature. Keep one + logs.",
        add="Screenshot of HUD + scene.",
    )
    GOLD[(C, 14)] = dict(
        kernel="AI + graphics mini: proxy/mock, asset table, scored eval, no frontend secrets",
        success="a TA can run the README, see .env not in git, and read the asset table",
        invariant="no secrets in the frontend; cite the model",
        goal="studio — architecture over a new model",
        kind="studio",
        board="""```
Must: proxy/mock · table · one feature · eval row · no keys in git
Cuts: second vendor, training a model, medical/legal claims
README: how to run with the mock
```""",
        slides=[],
        hook_say="This meeting is **studio**. .env not in git. Asset table. If the key is in the repo or the asset is unlabeled, the project fails before aesthetics.",
        hook_ask="If behind, do you cut the vendor or the table?",
        frame_say="Desk review: mock path, table, eval, no medical/legal claims.",
        show_say="Volunteer: grep the repo for sk- / API_KEY.",
        attempt_say="Studio. Mock first.",
        land_say="Report + repo. Next week 12+5. Be ready to show the table.",
        live=[
            ("0–10", "Headings", "Photograph."),
            ("10–50", "Desk review", ".env + table."),
            ("50–60", "60s rehearsal", "Stop."),
        ],
        cut="New vendors. Keep freeze.",
        add="One 60-second rehearsal of the feature.",
    )
    GOLD[(C, 15)] = dict(
        kernel="12+5; demo the feature; point at proxy, table, and a limit",
        success="they stop at 12 and can say where the key lives and what they did not train",
        invariant="no new features today",
        goal="presentations — not a content lecture",
        kind="presentations",
        board="""```
12 + 5
Show: proxy/mock · asset table · eval · a failure
We did not train GPT
```""",
        slides=[("Timer", "not a vendor keynote")],
        hook_say="Presentations. 12+5. Repo. Stop at 12. No keys on stage.",
        show_say="None. Present.",
        attempt_say="Present.",
        land_say="If the key stayed off the client and the asset was labeled, the graphics feature was real.",
        live=[("0–60", "Talks", "Cut at 12.")],
        cut="Debugging on stage.",
        add="One question: what did the mock stand in for?",
    )


def _acg(GOLD: dict) -> None:
    C = "Advanced Computer Graphics"
    GOLD[(C, 1)] = dict(
        kernel="direct = bounce 0; GI is the rest; IBL is not GI",
        success="they can point at the dark side of a cube and say what local PBR misses",
        invariant="local lighting is bounce 0; GI is the rest",
        goal="name the gap before a tracer",
        board="""```
lamp → cube face     =  direct (bounce 0)
wall → cube back     =  indirect (GI)

IBL  =  stand-in for the rest of the world
IBL  ≠  GI

albedo < 1     white room goes grey
```""",
        slides=[("Three.js local scene vs cited GI still", "photograph")],
        hook_say="RTR PBR is mostly local: lights + IBL as a stand-in. GI is light after leaving other surfaces. 'PBR already is GI' is the plant. We do not start with a production path tracer.",
        hook_ask="Does an HDRI mean the cube's shadow side received bounce from the wall? Wait. Want: no — that is IBL, not GI.",
        frame_say="Taxonomy named: radiosity, path tracing, photon mapping, irradiance volumes, SSGI, probes. This course implements teaching-scale radiosity idea + a tiny tracer. Energy: unbounded albedo 2.0 is a bug.",
        frame_ask="What is color bleeding?",
        build=[
            "**Say:** The gap. Draw lamp, wall, dark side.",
            "**Board:** bounce 0 vs rest. IBL ≠ GI.",
            "**Say:** Rendering equation as a name. L_out = emit + ∫ … We will not solve it in closed form today.",
        ],
        ask_build="Why does a white room go grey?",
        they_build="Table of 5 GI methods: realtime? teaching impl this term?",
        show_say="Diagram + cited GI still vs Three.js local. Plant 'PBR is GI'. Plant albedo 2.0. Demo 01-radiosity2.html as a teaser, not the week's kernel.",
        attempt_say="Five-method table + IBL vs GI sentence. Eight minutes.",
        land_say="Lab: table; albedo note. Homework: why IBL is not full GI. Quiz: indirect, bleeding, IBL vs GI.",
        live=[
            ("0–15", "Lamp / wall / dark side", "Plant PBR=GI."),
            ("15–40", "Taxonomy names", "Plant production tracer."),
            ("40–55", "Albedo < 1", "Albedo 2 plant."),
            ("55–60", "They write IBL ≠ GI", "Circulate."),
        ],
        cut="Energy proofs. Keep gap + IBL ≠ GI.",
        add="Albedo < 1 note.",
    )
    GOLD[(C, 2)] = dict(
        kernel="patches + form factors; iterate B_i = E_i + ρ_i Σ F_ij B_j on a tiny system",
        success="they can iterate a 2×2 made-up F and say radiosity is diffuse, view-independent",
        invariant="local lighting is bounce 0; GI is the rest",
        goal="color bleed on paper, not a hemicube coder",
        board="""```
B_i = E_i + ρ_i Σ_j F_ij B_j

2×2 F   made-up, honest
diffuse only     bad for mirrors

hemicube     named, not coded in full
lightmaps / probes     realtime cousins
```""",
        slides=[],
        hook_say="Goral et al. Classic interiors. Full hemicube as required lab fails. Radiosity on a mirror sphere fails the model. Demo 01-radiosity2.html.",
        hook_ask="Does F_ij depend on the camera? Wait. Want: no — view-independent.",
        frame_say="4-patch room or 2-quad bleed. Iterate gather. Blender bake as oracle extra. Plot convergence extra.",
        frame_ask="Why is a mirror a bad radiosity customer?",
        build=[
            "**Say:** Discretize. Patches.",
            "**Board:** the gather formula. 2×2 F.",
            "**Say:** Honesty: F from hemicube is a name.",
        ],
        ask_build="What is a form factor in one sentence?",
        they_build="One iteration on paper with made-up F.",
        show_say="Two-quad bleed with 2×2 F. Plant hemicube as required. Plant mirror radiosity. Plot a couple iterates.",
        attempt_say="One gather iteration in JS or on paper. Eight minutes.",
        land_say="Lab: bake extra as oracle; plot convergence. Homework: view-independent paragraph. Quiz: patches, F, diffuse-only.",
        live=[
            ("0–15", "Patches on a room", "Plant hemicube lab."),
            ("15–40", "Iterate 2×2", "Plant mirror."),
            ("40–55", "Convergence sketch", "They plot."),
            ("55–60", "They change ρ", "Circulate."),
        ],
        cut="Hemicube implementation. Keep 2×2 gather.",
        add="Plot B over iterations.",
    )
    GOLD[(C, 3)] = dict(
        kernel="Monte Carlo paths; cosine-weighted hemisphere; accumulate spp — teaching tracer, not production",
        success="they can accumulate a 2-sphere Lambert scene and say speckle is variance",
        invariant="local lighting is bounce 0; GI is the rest",
        goal="a tiny tracer that is theirs",
        board="""```
color += trace(ray);  n++;  display(color/n)

spp ↑  →  slower, cleaner     (measure spp, do not invent fps)
cosine hemisphere     NEE named
spheres + Lambert + one light  =  complete teaching tracer
```""",
        slides=[],
        hook_say="Average many random paths. One path is not a tracer. Copied GPUPathTracer unread fails. We do not start with a production path tracer. Demo 02-tracer.html.",
        hook_ask="What is the speckle? Wait. Want: variance, not a bug in the sphere.",
        frame_say="Next event estimation named. Gamma encode display. One more bounce extra. Cornell extra. spp slider they can explain.",
        frame_ask="Why cosine-weighted for diffuse?",
        build=[
            "**Say:** MC. Mean of paths.",
            "**Board:** accumulate / n. spp.",
            "**Say:** Scope freeze: spheres + Lambert + one area light.",
        ],
        ask_build="If n=1, what do you see?",
        they_build="On paper: ray, bounce, sample light or hemisphere.",
        show_say="2-sphere Lambert on Canvas; spp slider. Plant one path as done. Plant GPUPathTracer paste. Gamma encode.",
        attempt_say="Accumulate n samples on one pixel or a tiny buffer. Eight minutes.",
        land_say="Lab: gamma; extra bounce. Homework: variance paragraph. Quiz: MC, cosine, why not production tracer.",
        live=[
            ("0–15", "One path vs many", "Plant n=1 done."),
            ("15–40", "Accumulate spp", "Plant production tracer."),
            ("40–55", "Gamma display", "They see the lift."),
            ("55–60", "They move spp", "Circulate. No invented fps."),
        ],
        cut="Full Cornell. Keep spheres + accumulate.",
        add="One more bounce extra.",
    )
    GOLD[(C, 4)] = dict(
        kernel="mirror bounce; glass: refract + Schlick mix; max depth",
        success="they can reflect a mirror sphere and name ior 1.5 without unbounded recursion",
        invariant="local lighting is bounce 0; GI is the rest",
        goal="two materials in a teaching tracer",
        board="""```
mirror:  reflect(ω, n)
glass:   refract, ior 1.5, Schlick k
max depth     Russian roulette named

WebGLPathTracer = oracle after theirs looks like noise
dispersion not required
```""",
        slides=[],
        hook_say="BXDF teaching. Mirror is easy. Dispersion as required fails. Unbounded recursion fails. Production tracers remain oracles.",
        hook_ask="What stops a hall of mirrors? Wait. Want: max depth / roulette.",
        frame_say="Fake glass with reflect-only if refract slips. Lambert floor stays. ior slider extra. Depth 2 vs 5 extra. Microfacet optional extra — RTR already named it.",
        frame_ask="What is Schlick mixing?",
        build=[
            "**Say:** Mirror first. Then glass names.",
            "**Board:** reflect / refract / k. Max depth.",
            "**Say:** Oracle after their noise looks like a picture.",
        ],
        ask_build="Why not recurse forever?",
        they_build="Trace a mirror hit on paper: new direction.",
        show_say="Mirror sphere + glass or reflect-only glass; Lambert floor. Plant dispersion required. Plant depth ∞.",
        attempt_say="Mirror bounce in the tracer. Eight minutes.",
        land_say="Lab: ior extra; depth 2 vs 5. Homework: Schlick sentence. Quiz: mirror, ior, max depth.",
        live=[
            ("0–15", "Mirror bounce", "Plant unbounded recursion."),
            ("15–40", "Glass names / Schlick", "Plant dispersion lab."),
            ("40–55", "Depth 2 vs 5", "They compare stills."),
            ("55–60", "Oracle screenshot cited", "Circulate."),
        ],
        cut="Microfacet in-tracer. Keep mirror + depth.",
        add="Depth 2 vs 5 stills.",
    )
    GOLD[(C, 5)] = dict(
        kernel="homogeneous fog: Beer–Lambert T = exp(−σ t); emission/absorption/scatter named",
        success="they can march a homogeneous fog toward a sun disk and move a density slider",
        invariant="local lighting is bounce 0; GI is the rest",
        goal="transmittance along a ray",
        board="""```
emission · absorption · scatter
T = exp(−σ t)     Beer–Lambert

Henyey–Greenstein named
OpenVDB / 3D tex inhomogeneous  ≠  week 5 required
```""",
        slides=[],
        hook_say="Participating media: fog, smoke, clouds, SSS as a name. Homogeneous fog is the lab. OpenVDB as required fails. Inhomogeneous 3D tex as week 5 required fails.",
        hook_ask="If σ doubles, what happens to T? Wait. Want: it decays faster.",
        frame_say="Phase function named. Height fog / volumetric lighting as realtime names. Emission extra.",
        frame_ask="What is scatter vs absorb?",
        build=[
            "**Say:** Media. Three verbs.",
            "**Board:** Beer–Lambert. Sun disk through fog.",
            "**Say:** Homogeneous first. Heterogeneous next week.",
        ],
        ask_build="Why is OpenVDB a cut?",
        they_build="On paper: T at two σ values.",
        show_say="Ray march homogeneous fog toward a sun disk. Plant OpenVDB required. Density slider.",
        attempt_say="exp(-sigma*t) along a ray. Eight minutes.",
        land_say="Lab: density slider; emission extra. Homework: Beer–Lambert. Quiz: T, three verbs, homogeneous.",
        live=[
            ("0–15", "Three verbs", "Plant OpenVDB."),
            ("15–40", "Beer–Lambert march", "Plant inhomogeneous required."),
            ("40–55", "Density slider", "They move σ."),
            ("55–60", "Emission extra if time", "Circulate."),
        ],
        cut="HG phase impl. Keep homogeneous T.",
        add="Emission extra.",
    )
    GOLD[(C, 6)] = dict(
        kernel="heterogeneous regular tracking: step, sample density, accumulate; Woodcock named",
        success="they can march an fBm density ball and compare two step sizes with screenshots",
        invariant="local lighting is bounce 0; GI is the rest",
        goal="step size is a bias/cost choice",
        board="""```
for t=0..far step dt:
  d = density(p)
  acc += emit * d * dt * T
  T  *= exp(−d * dt)

dt=0 is a bug
Woodcock / delta tracking     named
```""",
        slides=[],
        hook_say="σ varies. Shadertoy clouds energy. Research cloud as the lab fails. Cost vs step size — measure stills, do not invent fps. Shadow in volume extra.",
        hook_ask="If dt is huge, what happens to the ball? Want: banding / missed density.",
        frame_say="Delta tracking unbiased for some media — name, optional code. Froxels / slice volumes named. Realtime names only.",
        frame_ask="What do you screenshot?",
        build=[
            "**Say:** Heterogeneous. Sample density.",
            "**Board:** the loop. Circle dt.",
            "**Say:** Two screenshots, two dt. Honesty about bias.",
        ],
        ask_build="What is Woodcock tracking in one sentence?",
        they_build="Loop in words; mark where T updates.",
        show_say="fBm density ball; cheap emission. Plant research cloud. Plant dt=0. Two step-size stills.",
        attempt_say="March with a dt they can name. Eight minutes.",
        land_say="Lab: two screenshots; shadow extra. Homework: dt paragraph. Quiz: regular tracking, dt, Woodcock name.",
        live=[
            ("0–15", "Density(p)", "Plant dt=0."),
            ("15–40", "Accumulate + T", "Plant research cloud."),
            ("40–55", "Two dt stills", "No invented fps."),
            ("55–60", "They compare", "Circulate."),
        ],
        cut="Realtime froxel impl. Keep march + two dt.",
        add="Shadow in volume extra.",
    )
    GOLD[(C, 7)] = dict(
        kernel="G-buffer review; CPU tile lists for N lights; heatmap of overlap",
        success="they can bin lights into screen tiles and say why 1000 Mesh helpers are not the algorithm",
        invariant="local lighting is bounce 0; GI is the rest",
        goal="many lights as a data structure",
        board="""```
forward dies at many lights
deferred: G-buffer, then lights
tiled: light indices per screen tile
clustered: 3D bins in the frustum (name)

heatmap overlay is a valid lab
```""",
        slides=[],
        hook_say="Deferred and clustered exist because forward dies. 1000 Mesh point-light helpers are not the algorithm. No debug view fails. We do not start a production deferred engine.",
        hook_ask="If two lights overlap a tile, what does the tile store? Wait. Want: two indices.",
        frame_say="Restate G-buffer from RTR. Clustered named. Cull by distance extra. Compare naive vs tiled count.",
        frame_ask="What lives in a G-buffer?",
        build=[
            "**Say:** Many lights. Why forward dies.",
            "**Board:** tiles. Light AABB → tiles.",
            "**Say:** Heatmap. Count, do not invent fps.",
        ],
        ask_build="Clustered vs tiled in one sentence?",
        they_build="On paper: 4 tiles, 3 lights, who overlaps.",
        show_say="N point lights; 2D heatmap of overlapping lights per tile. Plant Mesh helpers as the method. Plant no debug view.",
        attempt_say="Assign lights to tiles (JS). Eight minutes.",
        land_say="Lab: distance cull extra; naive vs tiled count. Homework: G-buffer restated. Quiz: tiles, G-buffer, not helpers. Next: midterm then shadow names.",
        live=[
            ("0–15", "G-buffer recap", "Plant production deferred."),
            ("15–40", "Tile lists", "Plant 1000 helpers."),
            ("40–55", "Heatmap", "No debug plant."),
            ("55–60", "They count overlaps", "Circulate."),
        ],
        cut="WebGL deferred impl. Keep CPU tiles + heatmap.",
        add="Naive vs tiled count.",
    )
    GOLD[(C, 8)] = dict(
        kernel="midterm; then VSM / CSM / PCSS as names: leak, seams, blocker search",
        success="after the exam they can fill a compare table and sketch cascade splits",
        invariant="local lighting is bounce 0; GI is the rest",
        goal="midterm, then shadow research names",
        kind="midterm",
        midterm_topics="direct vs indirect; IBL ≠ GI; radiosity gather; MC spp + cosine; mirror/glass depth; Beer–Lambert; tiled lights.",
        board="""```
VSM   mean+variance, Chebyshev     light leak
CSM   splits in view depth         seams
PCSS  blocker search               contact-ish

write 1 page comparing two
implement none or one extra
```""",
        slides=[],
        hook_say="This meeting is a **midterm**, then shadow names beyond PCF. No laptop for the exam. After: we name VSM leak, CSM seams, PCSS blockers. We do not ship a production shadow stack.",
        show_say="Written compare table. Optional tiny VSM extra. Draw cascade splits. Light-leak sketch.",
        attempt_say="Fill VSM vs CSM vs PCSS (one row each).",
        land_say="Lab: cascade splits; leak sketch. Homework: midterm rewrite or 1-page compare. Next: LOD names. No quiz this week.",
        live=[
            ("0–15", "Three names", "Plant implement-all."),
            ("15–40", "Table: leak / seams / blockers", "They write."),
            ("40–60", "Cascade sketch", "Circulate."),
        ],
        cut="Implement all three. Keep names + table.",
        add="Light-leak sketch.",
    )
    GOLD[(C, 9)] = dict(
        kernel="LOD swap by distance; Nanite is a visibility-buffer idea, not a glTF checkbox",
        success="they can switch three LOD meshes, log tri count, and refuse 'we used Nanite' on a glTF",
        invariant="local lighting is bounce 0; GI is the rest",
        goal="detail as a budget, named",
        board="""```
lod.addLevel(high, 0)
lod.addLevel(low, 20)

hysteresis named     popping without it
Nanite / vis buffer  cartoon-level name
'we used Nanite' on a glTF  =  fail
```""",
        slides=[],
        hook_say="Blender/RTR budgets meet algorithm names. UE5 Nanite is not a lab port. drei Detailed / Three.js LOD is the lab. Pixel-error sentence extra.",
        hook_ask="If you loaded one glTF, did you use Nanite? Wait. Want: no.",
        frame_say="Hysteresis extra. Tessellation named. Web: Three.LOD. Do not invent fps when they switch.",
        frame_ask="What do you log when LOD switches?",
        build=[
            "**Say:** Distance swap. Count tris.",
            "**Board:** addLevel. Nanite as idea, not a checkbox.",
            "**Say:** Popping. Hysteresis name.",
        ],
        ask_build="What is a visibility buffer in one cartoon sentence?",
        they_build="Three boxes as LODs; distances labeled.",
        show_say="Three LOD meshes or boxes; switch; log tris. Plant Nanite-on-glTF. Plant pop without talking hysteresis.",
        attempt_say="Two levels, log count. Eight minutes.",
        land_say="Lab: hysteresis extra; pixel-error sentence. Homework: Nanite-is-not-glTF. Quiz: LOD, popping, vis-buffer name.",
        live=[
            ("0–15", "Three LODs", "Plant Nanite checkbox."),
            ("15–40", "Log tris", "Plant no count."),
            ("40–55", "Hysteresis name", "Pop plant."),
            ("55–60", "They switch distances", "Circulate."),
        ],
        cut="Nanite impl. Keep LOD + honesty.",
        add="Pixel error sentence.",
    )
    GOLD[(C, 10)] = dict(
        kernel="profile → cut → measure on a named device; before row required",
        success="they can show a two-row table (before/after) without a fantasy fps",
        invariant="local lighting is bounce 0; GI is the rest",
        goal="optimization as a method",
        board="""```
before  |  device  |  spp or dt or lights  |  (fps only if measured)
after   |  same    |  the cut              |

algorithm cuts: BVH, roulette, tile cull
asset cuts:  resolution, instances
a cut that changes the image needs a screenshot
```""",
        slides=[],
        hook_say="Advanced CG is also engineering. Same rule as RTR: measure or omit. Optimizing without a before row fails. Fantasy 200 fps fails. Heavier scene: tracer spp, volume steps, or lights.",
        hook_ask="If you have no before row, did you optimize? Wait. Want: you guessed.",
        frame_say="Paper vs product: screenshot if the image changes. BVH from geometry course as a named cut.",
        frame_ask="What is an algorithm cut vs an asset cut?",
        build=[
            "**Say:** Method. Before first.",
            "**Board:** two-row table. Empty fps if unmeasured.",
            "**Say:** One algorithm cut or one asset cut today — named.",
        ],
        ask_build="Why screenshot a cut that changes the image?",
        they_build="Empty two-row table; they fill device + metric.",
        show_say="Two-row table on a named device. Plant no before. Plant 200 fps. One cut.",
        attempt_say="Fill before row for their scene. Eight minutes.",
        land_say="Lab: one algorithm cut; one asset cut. Homework: table. Quiz: before row, measure-or-omit, screenshot.",
        live=[
            ("0–15", "Before row", "Plant no baseline."),
            ("15–40", "One named cut", "Plant 200 fps."),
            ("40–55", "After still / number", "They write device."),
            ("55–60", "Screenshot if image changed", "Circulate."),
        ],
        cut="Paper vs product sermon. Keep two rows.",
        add="One asset cut.",
    )
    GOLD[(C, 11)] = dict(
        kernel="figures first; claim; limitation; IGWT connection; no ChatGPT summary as the note",
        success="they can write a 1-page note on a named paper they opened, with one figure redrawn",
        invariant="local lighting is bounce 0; GI is the rest",
        goal="read, do not summarize unseen",
        board="""```
1 claim
1 algorithm picture (drawn)
1 limitation / threat
1 IGWT connection
BibTeX later

AI summary without opening the PDF  =  fail
```""",
        slides=[],
        hook_say="Undergraduates drown in papers. Force: claim, picture, limit, connection. ChatGPT summary as the note fails. A paper they did not open fails. Skip proofs they cannot do; they must still say what is integrated.",
        hook_ask="If you cannot redraw figure 3, did you read it? Wait. Want: not yet.",
        frame_say="TOG/I3D/EGSR or a PBRT chapter. One question for the authors extra.",
        frame_ask="What is a threat to validity here?",
        build=[
            "**Say:** Figures first.",
            "**Board:** four lines of a reading note.",
            "**Say:** Name the paper on the parked strip.",
        ],
        ask_build="What may you skip, and what must you still say?",
        they_build="Redraw one figure from memory after a short look.",
        show_say="1-page note on a named paper. Plant AI summary. Plant unread paper. Draw their figure.",
        attempt_say="Four lines: claim, picture, limit, IGWT. Eight minutes.",
        land_say="Lab: draw the figure; one author question. Homework: full page. Quiz: four lines, no fake-read. Next: prepare talks.",
        live=[
            ("0–15", "Named paper", "Plant unread."),
            ("15–40", "Four-line note", "Plant ChatGPT note."),
            ("40–55", "Redraw a figure", "They draw."),
            ("55–60", "IGWT connection", "Circulate."),
        ],
        cut="Proof reconstruction. Keep four lines.",
        add="One question for the authors.",
    )
    GOLD[(C, 12)] = dict(
        kernel="prepare a 12 min teaching talk: one method, one figure, one limit, bibliography",
        success="they can rehearse 5 min with a claim sentence and a cited figure",
        invariant="local lighting is bounce 0; GI is the rest",
        goal="they can teach one name",
        board="""```
12 min  +  5 questions   (next meeting)
one method · one figure · one limit · bib

topics: photon mapping, DDGI, ReSTIR names, SSS, NeRF/3DGS as survey
NeRF: name, figure, limit (edit/dynamic) — not a required impl
Wikipedia-on-stage  =  fail
```""",
        slides=[],
        hook_say="Advanced course means they can teach. Next week is the talks. Today is content: structure, topics, what not to implement. Unattributed figures fail. Full NeRF training is skipped.",
        hook_ask="If you cannot state the limitation, what did you copy? Wait. Want: a demo.",
        frame_say="Photon mapping, DDGI, ReSTIR names, SSS, neural radiance fields as survey. 3DGS: name and limit. Slides or board photos. Bib required.",
        frame_ask="What is the one sentence of the talk?",
        build=[
            "**Say:** Why they teach. Capstone energy.",
            "**Board:** method / figure / limit / bib. Clock.",
            "**Say:** NeRF/3DGS survey only. No required impl.",
        ],
        ask_build="What must a cited figure include?",
        they_build="Talk outline: four bullets + bib key.",
        show_say="5 min rehearsal in lab; feedback. Plant Wikipedia. Plant unattributed figure. Plant NeRF impl as required.",
        attempt_say="Write the claim sentence and limitation. Eight minutes.",
        land_say="Lab: slides or board photos; bib. Homework: freeze the talk. Quiz: four parts of a talk, NeRF not required. Next: presentations.",
        live=[
            ("0–15", "Talk spine", "Plant Wikipedia."),
            ("15–40", "5 min rehearsal", "Plant no limit."),
            ("40–55", "Bib + figure credit", "Unattributed plant."),
            ("55–60", "They freeze the claim", "Circulate."),
        ],
        cut="Second topic. Keep one talk spine.",
        add="Bib entries on the outline.",
    )
    GOLD[(C, 13)] = dict(
        kernel="12+5 survey talks: claim, figure, limitation; no new impl on stage",
        success="they stop at 12 and can answer what they did not implement",
        invariant="no new features today",
        goal="survey presentations — not a content lecture",
        kind="presentations",
        board="""```
12 + 5
Show: claim · one figure · one limit · IGWT link
No production tracer on stage
Peer: one thing you learned
```""",
        slides=[("Timer", "not Wikipedia")],
        hook_say="Survey presentations. 12+5. I will cut you at the clock. If they cannot state the claim and the limitation, they copied a demo.",
        frame_ask="What did you not implement? What is the limitation?",
        show_say="None. Present talks.",
        attempt_say="Present.",
        land_say="Peer scores. One thing learned from a peer. Next: studio on one advanced piece.",
        live=[("0–60", "Talks", "Cut at 12.")],
        cut="Q&A. Keep the clock.",
        add="One extra question on a missed limitation.",
    )
    GOLD[(C, 14)] = dict(
        kernel="one advanced piece: teaching tracer, volume, tiles, or a measured cut — with a claim sentence",
        success="a TA can run the README and read the limitation paragraph",
        invariant="local lighting is bounce 0; GI is the rest",
        goal="studio — honesty over a film still",
        kind="studio",
        board="""```
Must: claim sentence · figure · limitation · spp/dt/device if relevant
Cuts: production path tracer, Nanite port, NeRF training
README: how to run     no CDN     no invented fps
```""",
        slides=[],
        hook_say="This meeting is **studio**. Pretty graphs with no tests or no limitation fail. We still do not start a production path tracer this week.",
        hook_ask="If behind, do you cut spp or the claim sentence?",
        frame_say="Desk review: claim + figure. Measure or omit.",
        show_say="Volunteer against the headings.",
        attempt_say="Studio. Claim first.",
        land_say="Report + repo. Next week 12+5. Be ready to derive or name one formula.",
        live=[
            ("0–10", "Headings", "Photograph."),
            ("10–50", "Desk review", "Claim + figure."),
            ("50–60", "60s rehearsal", "Stop."),
        ],
        cut="New methods. Keep freeze.",
        add="One 60-second rehearsal of the limitation.",
    )
    GOLD[(C, 15)] = dict(
        kernel="12+5; demo the piece; state claim and limitation",
        success="they stop at 12 and can say IBL ≠ GI or what bounce they simulated",
        invariant="no new math today",
        goal="presentations — not a content lecture",
        kind="presentations",
        board="""```
12 + 5
Questions: IBL vs GI? what did you not implement? measured spp/dt?
Habit: claim + limit
```""",
        slides=[("Timer", "not a SIGGRAPH trailer")],
        hook_say="Presentations. 12+5. Repo. Stop at 12.",
        show_say="None. Present.",
        attempt_say="Present.",
        land_say="If they stated the claim and the limitation, they did the course.",
        live=[("0–60", "Talks", "Cut at 12.")],
        cut="Debugging on stage.",
        add="One extra question on IBL vs GI.",
    )


def _cap(GOLD: dict) -> None:
    C = "Capstone Project"
    GOLD[(C, 1)] = dict(
        kernel="problem = users + job; tech list is not a problem; teams 2–4 or justified solo",
        success="they can write Problem | Users | Non-goals | Success look and create a repo",
        invariant="the problem is users, not a tech list",
        goal="who, why, users",
        board="""```
Problem | Users | Non-goals | Success look

'We will use R3F and AI'     ≠  a problem
'A visitor compares three bronzes on a phone'  =  a problem

roles: graphics · UI · assets · producer
medical viz OK     medical device claims not
```""",
        slides=[],
        hook_say="Fifteen weeks, one product. Configurator, viz, museum, game prototype, walkthrough, medical viz (not a device), creative demo. Five engines in week 1 fail. No users fail. Demo Capstone/code/01-moscow.html as the later spec shape.",
        hook_ask="Is 'we will use WebXR' a problem? Wait. Want: no — who must do what?",
        frame_say="Team contract. Git from day 1. Meeting time. Staff approve topics that fit the lab. We do not start in an engine before the problem statement.",
        frame_ask="What is a non-goal?",
        build=[
            "**Say:** Capstone is a complete interactive application — the happy path on a lab machine.",
            "**Board:** four boxes. Strike the tech list as problem.",
            "**Say:** Roles. Producer is a role, not leftover.",
        ],
        ask_build="Why is a medical device a skip?",
        they_build="Fill the four boxes for their idea.",
        show_say="Problem page + team contract. Plant five engines. Plant no users. Plant medical-device claim.",
        attempt_say="Four boxes + repo created. Eight minutes.",
        land_say="Lab: repo; meeting time. Homework: signed contract + problem page. Quiz: user, non-goal, tech list is not a problem.",
        live=[
            ("0–15", "Four boxes", "Plant tech-list problem."),
            ("15–40", "Team contract + roles", "Plant five engines."),
            ("40–55", "Repo", "Plant no git."),
            ("55–60", "They write users", "Circulate."),
        ],
        cut="Engine bake-off. Keep users + contract.",
        add="Meeting time on the contract.",
    )
    GOLD[(C, 2)] = dict(
        kernel="MoSCoW is the grading contract; lab laptop first; explicit skips",
        success="they can show Must/Should/Could/Won't plus five risks on one page",
        invariant="the problem is users, not a tech list",
        goal="a spec a TA can mark",
        board="""```
Must / Should / Could / Won't
Devices: lab laptop first     headset extra     phone extra
Skip: no multiplayer, no accounts, … (named)

risk table  5 rows
spec as a novel  =  fail
```""",
        slides=[],
        hook_say="TAs cannot mark a dream. The spec is the contract. Novel-length specs fail. No risks fail. Demo 01-moscow.html.",
        hook_ask="If Must cannot run on the lab laptop, whose problem is that? Wait. Want: the spec's — cut or change Must.",
        frame_say="Wireframe HUD extra. Asset list extra. Headset extra, not Must, unless staff said so.",
        frame_ask="What belongs in Won't?",
        build=[
            "**Say:** MoSCoW. Must is the slice.",
            "**Board:** four lists. Devices. Skips.",
            "**Say:** Five risks. Likelihood × impact teaching-level.",
        ],
        ask_build="Why list skips?",
        they_build="Must vs Won't for their team, five lines each max.",
        show_say="MoSCoW one page + 5-row risk table. Plant novel spec. Plant no risks. Plant headset as Must without staff.",
        attempt_say="Must list ≤ 7 bullets. Eight minutes.",
        land_say="Lab: HUD wireframe; asset list. Homework: spec page. Quiz: Must, skip, lab-laptop-first.",
        live=[
            ("0–15", "MoSCoW", "Plant novel."),
            ("15–40", "Devices + skips", "Plant headset Must."),
            ("40–55", "Five risks", "Plant no risks."),
            ("55–60", "They freeze Must", "Circulate."),
        ],
        cut="Skip-list philosophy. Keep MoSCoW + risks.",
        add="Asset list extra.",
    )
    GOLD[(C, 3)] = dict(
        kernel="named modules; labeled oracles; TA runs in three commands; no client secrets",
        success="they can draw DOM / 3D / loaders / optional proxy and paste npm run dev in README",
        invariant="the problem is users, not a tech list",
        goal="architecture as a one-pager",
        board="""```
ui/     scene/     assets/     (optional) proxy/

oracles: physics, Raycaster, PMREM, LLM — labeled
npm i && npm run dev
no CDN     no secrets in client
```""",
        slides=[],
        hook_say="Same as theses: modules with names. Rewriting architecture weekly with no diagram fails. Secrets in client fail. How a TA runs it is part of the architecture.",
        hook_ask="If the LLM is unlabeled, what is the integrity problem? Wait.",
        frame_say="Folder skeleton. Empty CI optional extra. Serve local. Three commands in README.",
        frame_ask="What is an oracle here?",
        build=[
            "**Say:** Boxes with names. Arrows are data.",
            "**Board:** ui / scene / assets / proxy. Oracles listed.",
            "**Say:** README run line. .env if AI — not in git.",
        ],
        ask_build="Why three commands, not a wiki?",
        they_build="Architecture one-pager sketch.",
        show_say="Architecture in README. Plant weekly rewrite with no diagram. Plant client key. Plant CDN Three.",
        attempt_say="Folders + run line. Eight minutes.",
        land_say="Lab: skeleton; CI extra. Homework: one-pager in README. Quiz: modules, oracles, no client secrets.",
        live=[
            ("0–15", "Module boxes", "Plant no diagram."),
            ("15–40", "Oracles labeled", "Plant secret in client."),
            ("40–55", "README run", "Plant CDN."),
            ("55–60", "They mkdir", "Circulate."),
        ],
        cut="CI theatre. Keep diagram + run line.",
        add="Empty CI extra optional.",
    )
    GOLD[(C, 4)] = dict(
        kernel="one happy path on the target device; placeholders beat waiting for art",
        success="a TA can complete the path without the team in the room",
        invariant="the problem is users, not a tech list",
        goal="a slice that exists",
        board="""```
happy path  =  the project
placeholders: boxes with labels
slideware without a path  =  fail
uncommitted assets  =  fail
30s recording extra
```""",
        slides=[],
        hook_say="If the slice is not there, the project is a wish. Graphics capstones die on loaders and cameras. Slideware fails. A TA completes the path alone.",
        hook_ask="If Blender is late, is the slice allowed to be boxes? Wait. Want: yes — labeled placeholders.",
        frame_say="5 min demo to class or TA. Bug list. 30s recording extra. Still the lab laptop.",
        frame_ask="What is the one path in one sentence?",
        build=[
            "**Say:** Slice. Load, see, do the verb.",
            "**Board:** path arrows. Placeholder box.",
            "**Say:** Commit the glTF or the box. Uncommitted is a fail.",
        ],
        ask_build="Why record 30s?",
        they_build="Happy-path steps numbered 1–5.",
        show_say="Happy path demo. Plant slideware. Plant uncommitted assets. Plant engine-not-problem.",
        attempt_say="Run the path from a cold serve. Eight minutes of fixing loaders, not features.",
        land_say="Lab: bug list; 30s extra. Homework: slice README. Quiz: path, placeholders, TA-alone. Next: sprints.",
        live=[
            ("0–15", "Name the path", "Plant slideware."),
            ("15–40", "Cold serve the slice", "Plant uncommitted."),
            ("40–55", "Bug list", "They write."),
            ("55–60", "Placeholder labels", "Circulate."),
        ],
        cut="Polish. Keep the path.",
        add="30s recording extra.",
    )
    GOLD[(C, 5)] = dict(
        kernel="budgeted glTF: still vs engine, license table, units/facing from Blender",
        success="a TA can open the viewer screenshot and the license table without a new engine",
        invariant="the problem is users, not a tech list",
        goal="studio — look under a budget",
        kind="studio",
        board="""```
budget:  tris · maps · draw calls   (count)
still vs engine
license table
Cuts: second hero mesh, 8k maps
no invented fps
```""",
        slides=[],
        hook_say="This meeting is **studio** (sprint: assets and look). Unlabeled dumps fail. Budget sheet + still vs engine. Demo Capstone/code/03-budget.html.",
        hook_ask="If behind, do you cut the 8k map or the verb?",
        frame_say="Desk review: glTF viewer screenshot, license rows, units. No new engine.",
        show_say="Volunteer: still vs in-engine. Count or omit fps.",
        attempt_say="Studio. Budget sheet first.",
        land_say="License table in repo. Next sprint is the verb. Do not replace the problem with a prettier mesh.",
        live=[
            ("0–10", "Budget headings", "Photograph."),
            ("10–50", "Desk review", "Still vs engine."),
            ("50–60", "License pass", "Unlabeled dump plant."),
        ],
        cut="New hero mesh. Keep budget + licenses.",
        add="One 60s still-vs-engine compare.",
    )
    GOLD[(C, 6)] = dict(
        kernel="the verb works on the slice; reset; keyboard; error state",
        success="a stranger can do the verb and reset without coaching",
        invariant="the problem is users, not a tech list",
        goal="studio — interaction sprint",
        kind="studio",
        board="""```
verb     (one sentence)
reset
keyboard path
error state     (load fail later; empty state now)
Cuts: second verb
```""",
        slides=[],
        hook_say="This meeting is **studio** (sprint: interaction). Orbit-only is not a verb. If the user cannot do the job from week 1, the tech list won.",
        hook_ask="What is the verb in one word?",
        frame_say="Desk review: happy path, reset, keyboard or documented exception, error if the mesh is missing.",
        show_say="Volunteer does another team's verb silently.",
        attempt_say="Studio. Verb first.",
        land_say="Reset + keyboard in the README. Next: measure and a11y. No invented fps.",
        live=[
            ("0–10", "Verb on the board", "Photograph."),
            ("10–50", "Desk review", "Stranger does the verb."),
            ("50–60", "Reset + keyboard", "Orbit-only plant."),
        ],
        cut="Second verb. Keep one + reset.",
        add="Empty-state message.",
    )
    GOLD[(C, 7)] = dict(
        kernel="measure on a named device; keyboard path; no invented fps",
        success="they can show a before/after row and tab to the verb",
        invariant="the problem is users, not a tech list",
        goal="studio — performance and a11y",
        kind="studio",
        board="""```
device | before | cut | after
fps only if measured
focus visible     keyboard does the verb
Cuts: bloom, extra instances, not the verb
```""",
        slides=[],
        hook_say="This meeting is **studio** (sprint: performance and a11y). Invented frame rates fail the budget section. Keyboard still required. Demo 03-budget.html.",
        hook_ask="If you did not measure, what do you write? Want: omit — not 60.",
        frame_say="Fill tables; fix the worst row. Focus visible. Reduced-motion if they animate.",
        show_say="Volunteer: tab the HUD, then show the table with a blank fps cell if unmeasured.",
        attempt_say="Studio. Worst row first.",
        land_say="Before/after in README. Next week is the midterm demo — public checkpoint, not a written exam.",
        live=[
            ("0–10", "Table headings", "Photograph."),
            ("10–50", "Desk review", "Measure or omit."),
            ("50–60", "Keyboard pass", "Invented-fps plant."),
        ],
        cut="New post stack. Keep table + keyboard.",
        add="Focus-visible pass.",
    )
    GOLD[(C, 8)] = dict(
        kernel="public checkpoint: 10+5 demo of the happy path; updated MoSCoW; remaining risks",
        success="the path runs for an audience; they can say what they cut; not a written exam",
        invariant="the problem is users, not a tech list",
        goal="studio — midterm demo",
        kind="studio",
        board="""```
10 + 5     public checkpoint
Show: users · verb · path on lab machine
updated MoSCoW     risks remaining
NOT a written exam
no new engine this hour
```""",
        slides=[("Timer", "not a pitch-deck template")],
        hook_say="This meeting is a **midterm demo** — a public checkpoint, not a written exam. The happy path on a lab machine is the project. Slideware without the path fails.",
        hook_ask="If the demo dies, what do you show — a video backup or a new feature?",
        frame_say="10+5. Circulate as audience. Updated MoSCoW. Risks remaining. Who did what.",
        show_say="First team: path only. Cut them at 10. Plant a tech-list opening — send them back to users.",
        attempt_say="Studio / remaining teams demo. Backup video if hardware fails.",
        land_say="MoSCoW + risks committed. Next sprints: content, robustness, docs. No surprise scope.",
        live=[
            ("0–10", "Rubric: users, verb, path", "Photograph."),
            ("10–50", "10+5 demos", "Tech-list opening plant."),
            ("50–60", "MoSCoW delta", "Stop."),
        ],
        cut="New features between talks. Keep the path.",
        add="One 60s rehearsal if a team has not gone.",
    )
    GOLD[(C, 9)] = dict(
        kernel="copy, data, beats: replace lorem; schema in /data; empty-data path",
        success="a TA can change a JSON/markdown string and see it in the product",
        invariant="the problem is users, not a tech list",
        goal="studio — content completeness",
        kind="studio",
        board="""```
/data     not JSX-only copy
beats complete     or cut the beat
empty data path
one citation pass
Cuts: new scene
```""",
        slides=[],
        hook_say="This meeting is **studio** (sprint: content). Lorem in a capstone is a user-problem fail. Data lives in files. Cite sources.",
        hook_ask="If I delete your JSX strings, does the product still have words?",
        frame_say="Replace lorem. Schema in /data. Empty data path. Citation pass.",
        show_say="Volunteer: edit a data file, reload, the HUD changes.",
        attempt_say="Studio. Kill lorem first.",
        land_say="Citation pass in the table. Next: robustness. Users still own the copy.",
        live=[
            ("0–10", "Lorem hunt", "Photograph."),
            ("10–50", "Desk review", "/data + empty path."),
            ("50–60", "Citation pass", "JSX-only copy plant."),
        ],
        cut="New beats. Keep completeness of Must.",
        add="Empty-data message.",
    )
    GOLD[(C, 10)] = dict(
        kernel="load fail, bad GLB, offline: user-visible errors; support matrix",
        success="they can demo three failures without a white screen",
        invariant="the problem is users, not a tech list",
        goal="studio — robustness",
        kind="studio",
        board="""```
missing file     bad GLB     offline
user-visible error
support matrix: laptop · (phone) · (headset extra)
Cuts: new features while the 404 is silent
```""",
        slides=[],
        hook_say="This meeting is **studio** (sprint: robustness). Silent 404 is a TA-fail. Offline is a labeled limit or a message — not a crash.",
        hook_ask="What does the user see if the glTF 404s?",
        frame_say="Three failure demos. Support matrix. Errors in the HUD, not only the console.",
        show_say="Rename a glTF; they must show a message. Plant console-only.",
        attempt_say="Studio. Three failures.",
        land_say="Support matrix in README. Next: documentation. The path still comes first.",
        live=[
            ("0–10", "Three failures listed", "Photograph."),
            ("10–50", "Desk review", "Visible errors."),
            ("50–60", "Support matrix", "Silent-404 plant."),
        ],
        cut="New features. Keep failure UX.",
        add="Offline sentence in README.",
    )
    GOLD[(C, 11)] = dict(
        kernel="README a TA can follow; video draft; report outline; labeled oracles",
        success="a TA runs from README alone and finds who-wrote-what",
        invariant="the problem is users, not a tech list",
        goal="studio — documentation",
        kind="studio",
        board="""```
README: problem, run, verb, oracles, budget, licenses
video draft
report outline
who wrote what
Demo: Capstone/code/02-readme.html
```""",
        slides=[],
        hook_say="This meeting is **studio** (sprint: documentation). A TA using only the README is the test. Demo 02-readme.html as a skeleton, not a CDN template.",
        hook_ask="If the TA cannot serve it in three commands, whose bug is it?",
        frame_say="README review with a TA hat. Video draft. Outline. Oracles labeled.",
        show_say="You run a volunteer README cold. Plant missing run line.",
        attempt_say="Studio. README first.",
        land_say="Video draft + outline committed. Next: rehearsal 12+5.",
        live=[
            ("0–10", "README headings", "Photograph."),
            ("10–50", "Cold TA run", "Missing-run plant."),
            ("50–60", "Who wrote what", "Stop."),
        ],
        cut="Report prose polish. Keep run + oracles.",
        add="Video draft even if rough.",
    )
    GOLD[(C, 12)] = dict(
        kernel="timed 12+5 rehearsal; cut wander; question bank; backup video",
        success="they can stop at 12 in rehearsal and answer two staff questions",
        invariant="the problem is users, not a tech list",
        goal="studio — rehearsal",
        kind="studio",
        board="""```
12 + 5 practice
open on users, not the stack
backup video
question bank: users, verb, cut, oracle, measure
```""",
        slides=[("Timer", "rehearsal clock")],
        hook_say="This meeting is **studio** (sprint: rehearsal). Opening on a tech list fails. Cut two slides or two seconds of wander. Backup video if the demo dies.",
        hook_ask="What is the first sentence — users or Three.js?",
        frame_say="Timed rehearsal. Question bank. Backup video. No new engine.",
        show_say="One team full 12+5. Cut at 12. Plant tech-list open.",
        attempt_say="Studio. Every team rehearses.",
        land_say="Question bank in the repo. Next: bugs only. Freeze is coming.",
        live=[
            ("0–10", "Clock + first sentence", "Photograph."),
            ("10–50", "Timed rehearsals", "Tech-list open plant."),
            ("50–60", "Backup video check", "Stop."),
        ],
        cut="New slides of architecture trivia. Keep users + path.",
        add="Question bank of five.",
    )
    GOLD[(C, 13)] = dict(
        kernel="bugs only; known issues list; contact sheet; no new scope",
        success="the triage list is in README and Must is not growing",
        invariant="the problem is users, not a tech list",
        goal="studio — polish freeze approaching",
        kind="studio",
        board="""```
bugs only
known issues
contact sheet of the path
Must is frozen     Could is already dead
```""",
        slides=[],
        hook_say="This meeting is **studio** (polish freeze approaching). New features this week become known issues or they slip the defense. Triage in README.",
        hook_ask="Is that a bug in Must or a Could in disguise?",
        frame_say="Triage meeting recorded in README. Contact sheet. Known issues. No new library.",
        show_say="Volunteer triage: bug vs Could. Plant a new verb.",
        attempt_say="Studio. Bugs only.",
        land_say="Known issues committed. Next week is freeze: tag, report, video.",
        live=[
            ("0–10", "Triage columns", "Photograph."),
            ("10–50", "Desk review", "Bugs only."),
            ("50–60", "Contact sheet", "New-verb plant."),
        ],
        cut="New features. Keep freeze of Must.",
        add="Known issues section.",
    )
    GOLD[(C, 14)] = dict(
        kernel="tag the freeze; report; video; TA run from README; typos only",
        success="a tagged commit that a TA can run; report submitted; no new engine",
        invariant="the problem is users, not a tech list",
        goal="studio — freeze week",
        kind="studio",
        board="""```
git tag freeze
report + video
TA run from README
typos only     no new engine in week 14
```""",
        slides=[],
        hook_say="This meeting is **studio** (freeze week). The happy path on a lab machine is the project. Everything else is a slide. No new engine.",
        hook_ask="If it is not tagged, is it frozen?",
        frame_say="TA run + tag. Report submit. Typos only. Video of the path.",
        show_say="Cold TA run of one team. Plant a last-minute engine.",
        attempt_say="Studio. Tag when the TA run works.",
        land_say="Tagged freeze. Next week is the defense 12+5 public. No new features.",
        live=[
            ("0–10", "Freeze checklist", "Photograph."),
            ("10–50", "TA runs + tags", "New-engine plant."),
            ("50–60", "Report submit", "Stop."),
        ],
        cut="Features. Keep tag + report.",
        add="Typo pass on README.",
    )
    GOLD[(C, 15)] = dict(
        kernel="defense 12+5: users, verb, measure, limits; who wrote what; no new features",
        success="they stop at 12; the path runs; they can answer as individuals",
        invariant="no new features today",
        goal="presentations — defense",
        kind="presentations",
        board="""```
12 + 5  public defense
Show: users · verb · path · budget/oracles · what you cut
who wrote what
individual questions
```""",
        slides=[("Timer", "not a startup pitch")],
        hook_say="Defense. 12+5 public. Same energy as Graduation Requirements. No new features. I will cut you at the clock. The deck is not the product.",
        frame_ask="Who is the user? What is the verb? What did you cut? Who wrote the loader? Where did you measure?",
        show_say="None. Defend.",
        attempt_say="Defend.",
        land_say="The happy path on a lab machine was the project. That is the course.",
        live=[("0–60", "Defenses", "Cut at 12. No debug on stage.")],
        cut="Q&A beyond the clock.",
        add="One extra individual question on an oracle or a cut.",
    )
