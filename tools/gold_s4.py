"""Full-script GOLD for Shader Programming, Real-Time Rendering, GPU Programming (15 meetings each)."""


def register(GOLD: dict) -> None:
    _shader(GOLD)
    _rtr(GOLD)
    _gpu(GOLD)


def _shader(GOLD: dict) -> None:
    C = "Shader Programming"
    GOLD[(C, 1)] = dict(
        kernel="VS writes a varying; GPU interpolates; FS reads it — v_uv as color",
        success="they can pass v_uv from VS to FS and say who interpolates",
        invariant="a shader is a program over pixels or vertices; a clip you cannot uniform is not the lab",
        goal="see interpolation as a program, not a filter",
        board="""```
VS  →  interpolate  →  FS

attribute  →  varying  →  gl_FragColor / out
uniform    (same for every vertex/pixel)

gl_Position is clip space
```""",
        slides=[],
        hook_say="IGWT shaders are programs you pause, uniform, and debug — not a Shadertoy tab left playing. Mesh shaders live in WebGL Programming; today the same GLSL in a fullscreen triangle. If you cannot read a compile log, you will later call a missing varying a GPU driver bug.",
        hook_ask="Who interpolates the color between three vertices — you, the VS, or the rasterizer? Wait seven seconds.",
        frame_say="Two homes: mesh VS/FS, and Shadertoy-style mainImage. We freeze WebGL2: #version 300 es and precision highp float in the fragment. Desktop GLSL paste without version is a fail.",
        frame_ask="Where does a uniform live — per vertex or once for the draw?",
        build=[
            "**Say:** Draw vertex → interpolate → fragment. The arrow in the middle is hardware. A step in the VS stays a step after interpolation if every vertex wrote the same edge; a step in the FS is per pixel.",
            "**Board:** varying vs uniform. Circle gl_Position: clip, not pixels.",
            "**Say:** Normals must be renormalized in the FS — interpolation shortens them. No CDN; serve the local shadertoy harness.",
        ],
        ask_build="Why highp in ES fragment shaders?",
        they_build="On paper: VS that outputs v_uv; FS that paints vec4(v_uv,0,1). Label who interpolates.",
        show_say="Demo WebGL/shadertoy/index.html. Pass v_uv as color. Plant a Shadertoy paste without #version — read the compile log out loud. Then a step() in VS vs the same step in FS.",
        attempt_say="Break interpolation: step in VS versus step in FS. Eight minutes.",
        land_say="Photograph the board. Lab: interpolation break + compile logs. Homework: varying vs uniform; uv-as-color. Quiz: who interpolates, gl_Position space, precision.",
        live=[
            ("0–10", "Fullscreen triangle + v_uv", "Plant Shadertoy paste without #version."),
            ("10–30", "uv as color", "Plant normalize only in VS."),
            ("30–45", "Compile log", "Read the error; do not hide it."),
            ("45–60", "They break interpolation", "Circulate. Pause time with a uniform if the harness has one."),
        ],
        cut="Precision sermon. Keep VS→FS + compile log.",
        add="One uniform float to freeze time — the course contract.",
    )
    GOLD[(C, 2)] = dict(
        kernel="pow(c, 2.2) decode; light in linear; encode for the monitor",
        success="they can decode sRGB, Lambert in linear, and say why lighting in sRGB looks wrong",
        invariant="lighting is linear; the monitor is sRGB; pow is a teaching approx, not a CMS",
        goal="stop lighting in display space",
        board="""```
sRGB texel  --pow 2.2-->  linear  --Lambert-->  linear
linear      --pow 1/2.2->  sRGB display

do not pow(normal)
```""",
        slides=[("Two gradients: encoded vs forgotten encode", "photograph; do not draw a color-managed UI")],
        hook_say="Computer Graphics I named gamma. Today it is three lines in GLSL. If they light in sRGB they will later call PBR 'grey' in Real-Time Rendering.",
        hook_ask="Do you pow the normal? Wait. Want: no.",
        frame_say="Decode albedo. Light. Encode. SRGB8_ALPHA8 and Three.js colorSpace are names. pow(c, 2.2) is the teaching curve.",
        frame_ask="If you skip encode, who looks wrong — the shader or the monitor?",
        build=[
            "**Say:** Two gradients on the board: linear ramp displayed raw vs encoded.",
            "**Board:** toLinear / toSRGB. Circle albedo, not n.",
            "**Say:** WebGL sRGB textures do the decode if you set the internal format — still write the helper once so they see it.",
        ],
        ask_build="Write toLinear in one line.",
        they_build="On paper: Lambert in linear for a white albedo 0.8 — do not pow n.",
        show_say="Gradient with and without encode; screenshot both. Plant pow on a normal. Toggle encode. Local files only.",
        attempt_say="Light a Lambert quad in linear; toggle encode. Eight minutes.",
        land_say="Lab: Lambert linear + toggle. Homework: why lighting in sRGB is wrong; encode helper. Quiz: decode formula, double gamma, albedo space.",
        live=[
            ("0–10", "Two gradients", "Plant skipped encode; blame the monitor."),
            ("10–30", "Lambert in linear", "Plant pow(normal)."),
            ("30–45", "Toggle encode", "They see the mid-greys move."),
            ("45–60", "They write the helpers", "Circulate."),
        ],
        cut="ICC profiles. Keep decode + Lambert + encode.",
        add="SRGB8_ALPHA8 as a name.",
    )
    GOLD[(C, 3)] = dict(
        kernel="st = fract(uv * n); polar (r, a); checker from step(fract)",
        success="they can make a checker from fract, not from a 4-pixel texture",
        invariant="a pattern is a function of uv (and time); a texture is optional",
        goal="UV as a plane you program",
        board="""```
st = fract(uv * n)

r = length(p)
a = atan(p.y, p.x)     // y, x  — not swapped

smoothstep / fwidth  on edges
```""",
        slides=[],
        hook_say="Procedural is the Shadertoy muscle. If they load a 4-pixel checker PNG they skipped the course. Pause time; the pattern must still be a function.",
        hook_ask="What does fract(uv.x * 8) do? Wait.",
        frame_say="Grid, polar, repeat. atan(y, x). Aliased step() is a teaching moment; smoothstep is the fix, not a style.",
        frame_ask="Why not texture2D of a tiny checker?",
        build=[
            "**Say:** UV plane. Scale, fract, step.",
            "**Board:** polar. Circle argument order of atan.",
            "**Say:** fwidth named. Brick is offset fract — they try after the checker.",
        ],
        ask_build="fract vs mod in one sentence?",
        they_build="On paper: checker from two step(fract) lines.",
        show_say="Fullscreen checker + spinning polar stripes. Plant atan(x,y) swapped. Serve local. No CDN.",
        attempt_say="Brick pattern or a smoothstep circle. Eight minutes.",
        land_say="Lab: brick + AA circle. Homework: fract vs mod; snippet in the repo. Quiz: fract, atan, why smoothstep.",
        live=[
            ("0–10", "fract checker", "Plant a 4px texture instead."),
            ("10–30", "Polar stripes", "Plant atan swapped."),
            ("30–45", "smoothstep edge", "Aliased step() first."),
            ("45–60", "They brick or AA", "Circulate. Uniform for n."),
        ],
        cut="Every IQ pattern. Keep fract + polar + one AA.",
        add="mod as a name next to fract.",
    )
    GOLD[(C, 4)] = dict(
        kernel="hash(lattice) then bilinear lerp — value noise, not Math.random",
        success="they can hash a lattice point and lerp the four corners",
        invariant="same uv → same noise; fireflies are a random() per frame",
        goal="deterministic noise you can pause",
        board="""```
i = floor(p)     f = fract(p)

a--b     hash(i+corner)
|  |     mix mix  (bilinear)
c--d

sin/dot hash  =  teaching, not crypto
```""",
        slides=[],
        hook_say="Fire, water, terrain, grain — all start here. If they call Math.random in the FS, the picture sparkles and they cannot debug a still.",
        hook_ask="Why not random() every frame? Wait. Want: not a function of uv.",
        frame_say="Value noise interpolates scalars. Perlin gradients are a name; fBm next week can use either. Hash artifacts exist — show them, do not hide.",
        frame_ask="What is bilinear here?",
        build=[
            "**Say:** Lattice. Four corners. Hash is a float in 0..1.",
            "**Board:** bilinear. Smoothstep on f as optional fade.",
            "**Say:** A 200-line noise library unread is a clip. Ten lines they can pause.",
        ],
        ask_build="Write hash(vec2) in one line (sin/dot is allowed).",
        they_build="On paper: four hashes and two mix calls.",
        show_say="Fullscreen value noise; slider for scale (a uniform). Plant true random per frame. Overlay the lattice.",
        attempt_say="Animate z as time extra, or freeze time and change scale. Eight minutes.",
        land_say="Lab: time or lattice overlay. Homework: why hash; noise(vec2). Quiz: why no Math.random, bilinear, artifact.",
        live=[
            ("0–10", "hash(vec2)", "Plant Math.random."),
            ("10–30", "Bilinear value noise", "Plant copying 200 unread lines."),
            ("30–45", "Scale uniform", "Pause time; debug a still."),
            ("45–60", "They add lattice overlay", "Circulate."),
        ],
        cut="Gradient noise proof. Keep hash + bilinear.",
        add="fade(t)=t*t*(3-2*t) name.",
    )
    GOLD[(C, 5)] = dict(
        kernel="fBm: sum a*noise(p); p*=2; a*=0.5 — 4–6 octaves",
        success="they can sum 4–6 octaves and name lacunarity and gain",
        invariant="fBm is a recipe; cranking octaves until the machine cries is not a measurement",
        goal="octaves as a stack you can turn down",
        board="""```
octave   freq     amp
  0       1       0.5
  1       2       0.25
  2       4       0.125

lacunarity ~ 2     gain ~ 0.5
do not unroll 20
```""",
        slides=[("1 octave vs 6, same uv", "photograph")],
        hook_say="Fractional Brownian motion is a recipe, not a proof. Terrain and marble later are this sum. If they unroll twenty octaves, we do not invent fps — we turn octaves down or we omit the speed claim.",
        hook_ask="What does gain 0.5 do to amplitude each octave? Wait.",
        frame_say="Parameters: octaves, lacunarity, gain. Warp `noise(p + noise(p))` once. fBm is not lighting.",
        frame_ask="Why not 20 octaves on a laptop?",
        build=[
            "**Say:** Stack amplitudes. Draw three sine-ish layers.",
            "**Board:** the table. Circle 5 as the lab default.",
            "**Say:** One sentence of cost: more octaves = more hash. Measure if you claim; otherwise omit.",
        ],
        ask_build="Lacunarity in one sentence?",
        they_build="On paper: the for-loop of fbm(vec2).",
        show_say="fBm slider for octaves; screenshot 1 vs 6. Plant 20 unrolled octaves. Warp extra after they have the sum.",
        attempt_say="Warp extra, or write the cost sentence. Eight minutes.",
        land_say="Lab: warp + cost sentence. Homework: one octave vs fBm; GLSL fbm. Quiz: lacunarity, gain 0.5, mobile octaves.",
        live=[
            ("0–10", "One octave", "They see value noise again."),
            ("10–30", "Octave slider", "Plant 20 octaves; no invented fps."),
            ("30–45", "Warp once", "marble = noise(p+noise(p))."),
            ("45–60", "They write fbm()", "Circulate. Uniform octaves."),
        ],
        cut="Domain warp catalog. Keep 5 octaves + names.",
        add="Measure one sentence if they insist on speed.",
    )
    GOLD[(C, 6)] = dict(
        kernel="sdCircle = length(p)-r; min=union, max=intersection; smoothmin name",
        success="they can write circle and box SDF and union two circles minus a box",
        invariant="signed distance is a number; a mesh of a 2D logo is the wrong tool this week",
        goal="a boolean logo from distances",
        board="""```
d = length(p) - r          // <0 inside

min(d1,d2)  union
max(d1,d2)  intersection
max(-d2,d1)  subtract

smoothmin  blends  (can break Lipschitz later)
```""",
        slides=[],
        hook_say="A function returns signed distance. Rendering is smoothstep on d, or sphere tracing in 3D later. IQ's tables are the encyclopedia — we implement three primitives, not fifty.",
        hook_ask="Is d negative inside the circle? Wait. Want: yes if signed.",
        frame_say="CSG: min/max. Onion is abs(d)-t. Unsigned-only cannot subtract cleanly.",
        frame_ask="Why signed, not only |d|?",
        build=[
            "**Say:** Circle. Then box as a named sdBox they copy from the board, not from a 200-line paste.",
            "**Board:** CSG tree for two circles minus a box.",
            "**Say:** fwidth AA on the edge. Pause time; the logo is a still you debug.",
        ],
        ask_build="Union in one operation?",
        they_build="On paper: d for a circle at origin radius 0.3.",
        show_say="Boolean logo: two circles minus a box. Plant unsigned distance only. AA with fwidth.",
        attempt_say="Onion (abs(d)-t) extra. Eight minutes.",
        land_say="Lab: onion + AA. Homework: why signed; sdCircle + sdBox. Quiz: union op, smoothmin idea, inside sign.",
        live=[
            ("0–10", "sdCircle", "Plant a triangle mesh logo."),
            ("10–30", "CSG logo", "Plant unsigned only."),
            ("30–45", "fwidth AA", "Aliased step(d)."),
            ("45–60", "They onion", "Circulate. Uniform r."),
        ],
        cut="Fifty IQ primitives. Keep circle, box, one CSG.",
        add="smoothmin as a name; warn Lipschitz.",
    )
    GOLD[(C, 7)] = dict(
        kernel="n = normalize(∇d) by central differences; Lambert n·ℓ",
        success="they can estimate a 2D normal with finite differences and light it",
        invariant="the normal is the gradient of the SDF; epsilon too big is a different shape",
        goal="light an SDF without an analytic n",
        board="""```
e = 0.001   (too big: 0.1 on a tiny shape)

n.x = d(p+ex) - d(p-ex)
n.y = d(p+ey) - d(p-ey)
n = normalize(n)

Lambert: max(dot(n,L), 0)
PBR is RTR — not this hour
```""",
        slides=[],
        hook_say="If they never compare analytic n to finite-difference n, they will trust a broken map() in week 9. Soft shadow is a name — week 9 marches. This week: N·L.",
        hook_ask="What happens if e=0.1 on a small circle? Wait.",
        frame_say="Gradient is ∇f. In 2D we fake a lit disk. Energy is still Lambert. Compare analytic (p/|p|) to FD once.",
        frame_ask="Why finite difference instead of only analytic?",
        build=[
            "**Say:** Central differences. Tetrahedral is a name for 3D later.",
            "**Board:** n from d. Circle e.",
            "**Say:** Two lights extra is two dots added — still not a named PBR pass.",
        ],
        ask_build="Write n.x in one line.",
        they_build="On paper: analytic n of a circle vs FD sketch.",
        show_say="Lit circle SDF; light-angle uniform. Plant e=0.1. Compare analytic vs FD on the board.",
        attempt_say="Two lights extra, or a Blinn specular extra. Eight minutes.",
        land_say="Lab: two lights or specular. Homework: why finite difference; normal2. Quiz: epsilon too big, n from d, Lambert. Midterm next week: gamma, uv, noise, fBm, SDF.",
        live=[
            ("0–10", "FD normal", "Plant e=0.1."),
            ("10–30", "Lambert slider", "Plant skipping analytic compare."),
            ("30–45", "Pause light angle", "Debug a still."),
            ("45–60", "They add a second light", "Circulate."),
        ],
        cut="Energy conservation speech. Keep FD + Lambert.",
        add="Blinn specular as extra, named.",
    )
    GOLD[(C, 8)] = dict(
        kernel="sphere trace: p += d * dir until hit or escape",
        success="after the exam they can step a ray by the SDF distance and color a hit",
        invariant="a true SDF lets you step by d; smoothmin can break that safety",
        goal="midterm, then one marching sphere",
        kind="midterm",
        midterm_topics="varying vs uniform; gamma decode/encode; fract/polar; hash+bilinear; fBm octaves; signed SDF + CSG.",
        board="""```
p = cam
for i in 0..maxSteps:
  d = map(p)
  if d < eps:  HIT
  p += d * dir
  if too far:  MISS

smoothmin  may  overstep
```""",
        slides=[],
        hook_say="This meeting is a **midterm**, then sphere tracing. No laptop for the exam. After: walk the ray by d. Do not start with eight nested SDFs.",
        show_say="March a sphere; Lambert on the hit. Plant a constant step size that skips the surface. Miss color as a debug uniform.",
        attempt_say="Miss color + max-steps slider (a uniform you can pause).",
        land_say="Lab: miss color + max steps. Homework: reflection + screenshot of a hit. No quiz this week.",
        live=[
            ("0–15", "p += d * dir", "Plant fixed 0.1 steps."),
            ("15–40", "Sphere + Lambert", "Plant eight nested SDFs."),
            ("40–60", "Miss color uniform", "They type. Circulate."),
        ],
        cut="Live coding if the exam ran long. Keep the leftover board.",
        add="Lipschitz / smoothmin warning in one sentence.",
    )
    GOLD[(C, 9)] = dict(
        kernel="secondary march toward L; soft = min(d/t); AO samples along n",
        success="they can march a shadow ray and toggle a cheap AO",
        invariant="if map hits before the light, it is shadowed; AO is a fake, named",
        goal="two rays: camera and light",
        board="""```
cam ray  →  hit p
shadow   →  march p → L
  blocked if d hits before light

soft: track min(d/t)
AO:  sample SDF along n   (not SSAO unless you say so)
```""",
        slides=[],
        hook_say="Last time: one ray. Today a second ray toward the light. Stencil shadows are a different course. SSAO is Real-Time Rendering — name the difference if it comes up.",
        hook_ask="If map(p) hits before L, is the point lit? Wait. Want: no.",
        frame_say="Hard shadow is a hit. Soft is IQ's min d/t. AO darkens crevices. Material id from map() return is extra.",
        frame_ask="Why a second march?",
        build=[
            "**Say:** Two arrows from p: to camera origin is the first ray already done; toward L is new.",
            "**Board:** shadow() stub. Circle blocked.",
            "**Say:** Pause time; debug the shadow with a still. Uniform for AO on/off.",
        ],
        ask_build="Soft shadow in one phrase?",
        they_build="On paper: steps of shadow() until blocked or arrived.",
        show_say="Sphere+plane, soft-ish shadow. Plant a stencil-shadow speech. AO toggle.",
        attempt_say="AO toggle. Eight minutes.",
        land_say="Lab: AO + material id extra. Homework: why second march; shadow(). Quiz: hit before light, soft idea, AO.",
        live=[
            ("0–10", "Shadow ray", "Plant stencil speech."),
            ("10–30", "Soft min(d/t)", "Plant AO called SSAO without saying."),
            ("30–45", "AO along n", "Toggle uniform."),
            ("45–60", "They add material id", "Circulate."),
        ],
        cut="Production IQ shadow. Keep second march + AO name.",
        add="Object id from map() as extra.",
    )
    GOLD[(C, 10)] = dict(
        kernel="domain warp uv; fBm as mask; study then shrink a catalog look",
        success="they ship a ~40-line fire/water/smoke with a citation and one original uniform",
        invariant="unread 400-line paste is a clip; a paused uniform is a program",
        goal="one look you can explain",
        board="""```
uv' = uv + k * noise(uv)

fire:  warp + fBm mask + palette
water: height fBm → n; fresnel name; sky gradient

cite what you copied
```""",
        slides=[],
        hook_say="Read the catalog, then shrink. Pasting aurora.glsl as homework fails integrity. Water: normals from height, fresnel as a name, reflection as a gradient sky — not a path tracer.",
        hook_ask="What do you write in the comment if you started from fire.glsl? Wait. Want: the source.",
        frame_say="Domain, lookup, noise. One parameter that is yours — a uniform they can pause. No CDN; local glsl.",
        frame_ask="Why a 40-line fire instead of 400?",
        build=[
            "**Say:** Warp the domain. Mask with fBm. Palette is a mix, not a 4K texture from the internet.",
            "**Board:** layers. Circle citation.",
            "**Say:** Ethics: comment the copy. Teaching/12.",
        ],
        ask_build="Fresnel in one sentence (name-level)?",
        they_build="On paper: three functions you will reuse, named.",
        show_say="A 40-line fire or water from WebGL/shadertoy; cite. Plant aurora.glsl paste. Pause time; one slider that is theirs.",
        attempt_say="One original uniform. Eight minutes.",
        land_say="Lab: your parameter + screenshot. Homework: three reused functions; your GLSL. Quiz: domain warp, why cite, fresnel name.",
        live=[
            ("0–10", "Warp uv", "Plant unread 400 lines."),
            ("10–30", "40-line fire/water", "Plant no citation."),
            ("30–45", "Pause + one slider", "Their parameter."),
            ("45–60", "They comment the source", "Circulate."),
        ],
        cut="Full Navier–Stokes. Keep warp + cite + one uniform.",
        add="Palette as mix of three colors.",
    )
    GOLD[(C, 11)] = dict(
        kernel="height = fBm(xz); march the heightfield; fog; LOD step named",
        success="they can set y = fbm(xz) and color a snow line without a DEM download",
        invariant="terrain this week is a function of xz, not a mesh pipeline",
        goal="one sun, fog, height color",
        board="""```
h = fbm(p.xz * scale)
map:  p.y - h

fog  =  mix(col, fogCol, 1 - exp(-k t))

LOD: step size may grow with t   (name; not required)
```""",
        slides=[],
        hook_say="The classic IQ hills. DEM downloads are next year's GIS course. Unlimited steps is a hang, not a look. Pause time; debug a still camera.",
        hook_ask="Where does height live — a texture from NASA, or fBm(xz)? Wait. Want: fBm today.",
        frame_say="One sun, height color, fog. Triplanar is a name, not required. Shadow extra if time — still a named second march.",
        frame_ask="What is LOD here?",
        build=[
            "**Say:** Slice of hills. Camera looks down the +z or along the ground — freeze one.",
            "**Board:** y = fbm(xz). Fog formula.",
            "**Say:** Cap max steps with a uniform. Do not invent fps; if the machine dies, lower octaves.",
        ],
        ask_build="Normal from height in one idea?",
        they_build="On paper: snow line if h > threshold.",
        show_say="Fullscreen terrain march; fog. Plant DEM as the week. Snow line extra.",
        attempt_say="Snow line extra. Eight minutes.",
        land_say="Lab: snow + shadow extra if time. Homework: height vs mesh terrain; GLSL. Quiz: height fBm, normal from height, fog.",
        live=[
            ("0–10", "h = fbm(xz)", "Plant DEM download."),
            ("10–30", "March + fog", "Plant unlimited steps."),
            ("30–45", "Max-steps uniform", "Pause camera."),
            ("45–60", "They add snow line", "Circulate."),
        ],
        cut="Triplanar textures. Keep height + fog + step cap.",
        add="LOD as a name on the board.",
    )
    GOLD[(C, 12)] = dict(
        kernel="pass 1: scene → FBO color; pass 2: fullscreen FS (vignette/grain)",
        success="they can name both passes and toggle the post without using it as lighting",
        invariant="post is an image filter on a named pass; it is not the light",
        goal="scene tex → FS",
        board="""```
PASS 1  scene (march or mesh)  →  color tex
PASS 2  fullscreen quad         →  vignette / grain

ping-pong  named for GPU course
FXAA       named for RTR
```""",
        slides=[],
        hook_say="Same FBO idea as WebGL week 11. Name every pass. A 4K FBO on integrated graphics is a hang — we do not invent timings; we shrink the target or omit the claim.",
        hook_ask="How many passes in vignette-on-a-cube? Wait. Want: two (at least).",
        frame_say="Kernel filters: blur/sharpen teaching. Separable blur is a name. Ping-pong is GPU Programming's week 2.",
        frame_ask="Why extra fill rate?",
        build=[
            "**Say:** Two boxes: scene, then quad. Label the texture.",
            "**Board:** two passes. Circle 'not lighting'.",
            "**Say:** Grain should be after tonemap in RTR; here it is a 2D teaching filter. Toggle with a uniform.",
        ],
        ask_build="What is pass 1 writing?",
        they_build="On paper: arrows FBO color → sampler2D in FS.",
        show_say="Vignette + grain on a marching scene or textured cube. Plant post as lighting. Toggle post.",
        attempt_say="Blur extra (separable name). Eight minutes.",
        land_say="Lab: blur name + toggle. Homework: why extra fill rate; two-pass code. Quiz: FBO, grain should be, 8 passes as a smell.",
        live=[
            ("0–10", "FBO scene", "Plant 4K target."),
            ("10–30", "Vignette FS", "Plant post as lighting."),
            ("30–45", "Toggle uniform", "Pause; debug still."),
            ("45–60", "They name separable blur", "Circulate."),
        ],
        cut="Eight Instagram passes. Keep two named passes.",
        add="Ping-pong as a name only.",
    )
    GOLD[(C, 13)] = dict(
        kernel="four looks: pattern, noise, SDF, march-or-post — each with pause + one slider",
        success="a contact sheet of four controlled stills, not four identical fBm screenshots",
        invariant="a gallery is uniforms you can pause; a random Shadertoy account is not a portfolio",
        goal="four looks you can defend",
        board="""```
1 pattern     fract / polar
2 noise       value / fBm
3 SDF         2D CSG
4 march|post  sphere or FBO filter

each:  pause time   +  one slider
cite copies
```""",
        slides=[],
        hook_say="Craft, not a dump of tabs. RTR will put these ideas on meshes with PBR. Today: pause, uniform, debug view. Four identical fBm shots fail.",
        hook_ask="If time is always running, how do you debug a look? Wait. Want: pause uniform.",
        frame_say="Gallery page linking four local HTML/GLSL files. Reuse the shadertoy harness. No CDN.",
        frame_ask="What is baked vs a uniform?",
        build=[
            "**Say:** Contact sheet on the board. Four boxes.",
            "**Board:** the four slots. Circle pause.",
            "**Say:** One original twist per look — a slider, not a new 400-line paste.",
        ],
        ask_build="Why pause?",
        they_build="On paper: which four files, and one uniform each.",
        show_say="Gallery page, four links, local serve. Plant four identical fBm. Pause time on one look live.",
        attempt_say="Pause time on their first look. Eight minutes.",
        land_say="Lab: pause + twist. Homework: one paragraph per look; repo. Quiz: uniform vs baked, why pause, citation. Next: studio.",
        live=[
            ("0–10", "Four slots", "Plant four identical fBm."),
            ("10–30", "Harness links", "Plant CDN."),
            ("30–45", "Pause + slider", "They feel debug."),
            ("45–60", "They cite", "Circulate."),
        ],
        cut="A fifth look. Keep four + pause.",
        add="Raw distance or uv debug key as a preview of studio.",
    )
    GOLD[(C, 14)] = dict(
        kernel="polish four looks; debug view (raw d or uv); freeze; cite",
        success="a TA can serve the folder, pause a look, and see a debug view without a second tool",
        invariant="README and freeze beat a fifth Shadertoy; tests are 'does it pause and serve'",
        goal="studio — not a content lecture",
        kind="studio",
        board="""```
Must:  4 looks · pause · 1 slider · cite · debug (d or uv)
Cuts:  drop terrain; keep SDF + noise + gamma
README: python -m http.server
```""",
        slides=[],
        hook_say="This meeting is **studio**. Four looks. Drop terrain if behind. A key that shows raw distance or normals is the debug contract.",
        hook_ask="If behind, what do you cut first?",
        frame_say="Desk review: debug view first, then pause, then citations, then README.",
        show_say="Volunteer: serve, pause, debug view. Plant a look that only works while time runs.",
        attempt_say="Studio. Serve first.",
        land_say="Report: screenshots, uniforms table, citations. Next week 12+5.",
        live=[
            ("0–10", "Headings + cut list", "Photograph."),
            ("10–50", "Desk review", "Debug view first."),
            ("50–60", "60s rehearsal", "Stop."),
        ],
        cut="New libraries. Keep freeze.",
        add="One 60-second rehearsal in front of another team.",
    )
    GOLD[(C, 15)] = dict(
        kernel="12+5; demo a paused look; point at a uniform and a citation",
        success="they stop at 12 and can say where gamma lives and whether map is a true SDF",
        invariant="no new features today",
        goal="presentations — not a content lecture",
        kind="presentations",
        board="""```
12 + 5
Show: pause · one slider · cite
Ask: where is gamma?  is map a true SDF?
No new GLSL on stage
```""",
        slides=[("Timer", "not a slide of GLSL")],
        hook_say="Presentations. 12+5. Repo. Stop at 12. I will ask where gamma is, and whether map is a true SDF.",
        show_say="None. Present.",
        attempt_say="Present.",
        land_say="A shader you can pause, uniform, and debug is the habit Real-Time Rendering will put on a named pass.",
        live=[("0–60", "Talks", "Cut at 12.")],
        cut="Debugging on stage.",
        add="One question on a citation or Lipschitz.",
    )


def _rtr(GOLD: dict) -> None:
    C = "Real-Time Rendering"
    GOLD[(C, 1)] = dict(
        kernel="forward: one geometry pass; lights add in the FS",
        success="they can draw the forward path and count draw calls without inventing fps",
        invariant="a frame is a named pass plus a budget; unnamed lights are not a path",
        goal="name the forward pass",
        board="""```
PASS: forward shade
  for each object:
    for each light:  add in FS

HDR leftover energy  →  later tonemap pass
do not invent fps
```""",
        slides=[],
        hook_say="CG I and WebGL already light a cube. This course is production looks: PBR, HDR, shadows, a post stack you can name, and numbers you measured. A look without a stack graph is a screenshot.",
        hook_ask="Is deferred this week? Wait. Want: no.",
        frame_say="Forward: each object, for each light, add. Simple. Dies with many lights — clustered/deferred later. Lambert+Blinn can exceed 1; that is why HDR exists, not because we quote 60 fps.",
        frame_ask="Where do the lights run — CPU draw per light, or a loop in the FS?",
        build=[
            "**Say:** One pass box. Lights live in the FS this week — two is enough.",
            "**Board:** for-each-light add. Circle 'name the pass'.",
            "**Say:** Saturated LDR vs a fake HDR multiply. No CDN. Three.js is an oracle after the picture, not instead of it.",
        ],
        ask_build="Why can Lambert+Blinn exceed 1?",
        they_build="On paper: draw-call count for 1 cube, 2 lights, forward FS loop.",
        show_say="WebGL or Three.js cube, two lights. Saturated LDR vs HDR multiply. Plant ten lights on day one. Do not quote fps.",
        attempt_say="Draw-call count. Light loop in shader vs CPU. Eight minutes.",
        land_say="Lab: draw calls + loop place. Homework: forward vs another Mesh; clip vs no clip screenshot. Quiz: forward path, why HDR, deferred this week?",
        live=[
            ("0–10", "Name the forward pass", "Plant ten lights."),
            ("10–30", "Two lights in FS", "Plant '60 fps' with no table."),
            ("30–45", "LDR clip vs HDR", "They see >1 energy."),
            ("45–60", "They count draw calls", "Circulate."),
        ],
        cut="Energy conservation proof. Keep named forward pass + two lights.",
        add="Light loop in FS vs extra draws — still no invented timings.",
    )
    GOLD[(C, 2)] = dict(
        kernel="Cook-Torrance names: D spread, F fresnel, G shadowing; metal-rough split",
        success="they can name D, F, G and set F0 = mix(0.04, albedo, metallic)",
        invariant="metalness 0.5 'for look' is not a material; roughness is not a grey albedo",
        goal="name the shade BRDF",
        board="""```
PASS: forward PBR shade

D  microfacet distribution   (rough → spread)
F  fresnel                   F0 = mix(0.04, albedo, metal)
G  geometry / shadowing

dielectric: diffuse + spec
metal:      no dielectric diffuse; F0 = albedo
```""",
        slides=[],
        hook_say="Microfacets. Students write a tiny GGX or use a 30-line kernel. MeshStandardMaterial is the oracle after they can name D, F, G — not the lab substitute in the first hour.",
        hook_ask="What is F0 of plastic, roughly? Wait. Want: ~0.04.",
        frame_say="Rough = more spread. Maps from Blender later. We do not invent how many ms GGX costs.",
        frame_ask="What does roughness do to D?",
        build=[
            "**Say:** Cartoon of microfacets: mirror vs sandpaper.",
            "**Board:** D F G + F0 mix. Circle metal 0 or 1 for the lab.",
            "**Say:** Compare to Standard after the picture is drawn.",
        ],
        ask_build="Write the F0 mix line.",
        they_build="On paper: metal vs dielectric in four bullets.",
        show_say="Two spheres: gold-ish metal vs plastic; roughness slider. Plant metalness 0.5 for look. Local glTF/maps only — no CDN.",
        attempt_say="Compare to MeshStandardMaterial extra, or an F0 chart. Eight minutes.",
        land_say="Lab: oracle compare + F0 chart. Homework: metal vs dielectric in 8 sentences; shader. Quiz: F0 plastic, roughness, D F G.",
        live=[
            ("0–10", "D F G names", "Plant roughness as grey albedo."),
            ("10–30", "Metal vs plastic", "Plant metalness 0.5."),
            ("30–45", "Roughness uniform", "Still one shade pass."),
            ("45–60", "They chart F0", "Circulate."),
        ],
        cut="Full Karis listing. Keep D F G + F0.",
        add="Blender pack as a name.",
    )
    GOLD[(C, 3)] = dict(
        kernel="IBL: irradiance (diffuse) + prefiltered spec; mip LOD ≈ roughness",
        success="they can treat a blurred env as diffuse IBL and roughness as mip, and toggle background vs lighting",
        invariant="the environment is a named light; a 500MB HDR is not a lab asset",
        goal="env as the other light",
        board="""```
PASS: IBL lookup  (after or with direct shade)

diffuse  ←  irradiance (blurred env)
spec     ←  prefiltered cubemap, lod = roughness

split-sum  Karis  (name)
HDR env  —  IBL without HDR is a lie
```""",
        slides=[],
        hook_say="A studio product has environment lighting. A single dir light is a lecture, not a catalog shot. Cubemap size is a budget — we do not invent fps; we pick a small local env.",
        hook_ask="Is the background the same texture as the lighting? Wait. Want: often related, not always the same pass.",
        frame_say="Split-sum named. Implementation can be env + mip. PMREM is the Three.js name after the picture. Cost: cubemap resolution, especially mobile.",
        frame_ask="What does a higher mip mean for roughness?",
        build=[
            "**Say:** Cubemap + sphere. Two arrows: irradiance, spec.",
            "**Board:** lod = roughness. Circle HDR.",
            "**Say:** Intensity slider is a uniform on this lookup pass.",
        ],
        ask_build="Irradiance in one sentence?",
        they_build="On paper: IBL vs dir light — two bullets.",
        show_say="Metallic sphere in a local env; roughness 0 vs 1. Plant 500MB HDR. Background vs lighting toggle.",
        attempt_say="Intensity slider. Eight minutes.",
        land_say="Lab: intensity + background/lighting toggle. Homework: IBL vs dir; screenshot pair. Quiz: irradiance, mip as roughness, PMREM name.",
        live=[
            ("0–10", "Name IBL lookups", "Plant IBL without HDR."),
            ("10–30", "Roughness 0 vs 1", "Plant huge HDR."),
            ("30–45", "Background vs lighting", "Two toggles."),
            ("45–60", "They write the intensity uniform", "Circulate."),
        ],
        cut="Convolve an env from scratch. Keep names + small local env.",
        add="PMREM as oracle name.",
    )
    GOLD[(C, 4)] = dict(
        kernel="HDR shade → tonemap pass (Reinhard or ACES name) → then sRGB encode",
        success="they can store HDR, expose, Reinhard, and say why not clamp and why not tonemap per light",
        invariant="tonemap is a named display pass; per-light tonemap is a bug",
        goal="map HDR to the monitor without inventing scores",
        board="""```
PASS 1  shade in HDR     (sun >> 1)
PASS 2  tonemap          Reinhard: x/(1+x)   or ACES name
PASS 3  encode sRGB

order:  tonemap then encode
do not tonemap per light
```""",
        slides=[],
        hook_say="Sun is >> 1. Bloom next week needs leftover energy. Clamp-to-1 throws the look away. We pick one operator and document it — we do not invent how many ms ACES costs.",
        hook_ask="Tonemap each light then add? Wait. Want: no.",
        frame_say="Reinhard, filmic, ACES — names. Exposure is a uniform before the operator. Gamma backwards (encode then tonemap) is a plant.",
        frame_ask="Why not clamp?",
        build=[
            "**Say:** HDR bar on the board: 0, 1, 10.",
            "**Board:** three passes. Circle order vs gamma.",
            "**Say:** False-color extra is a debug view of this buffer, not a fps claim.",
        ],
        ask_build="Write Reinhard in one line.",
        they_build="On paper: order shade → tonemap → encode.",
        show_say="Overbright cube; exposure; Reinhard. Plant tonemap per light. ACES as a comment name.",
        attempt_say="ACES name in comments, or false-color HDR extra. Eight minutes.",
        land_say="Lab: ACES name + false-color. Homework: why not clamp; reinhard(). Quiz: Reinhard, exposure, order vs gamma.",
        live=[
            ("0–10", "HDR buffer", "Plant clamp."),
            ("10–30", "Reinhard + exposure", "Plant per-light tonemap."),
            ("30–45", "Then encode", "Plant gamma first."),
            ("45–60", "They false-color", "Circulate. No invented fps."),
        ],
        cut="Full ACES fit. Keep Reinhard + named order.",
        add="ACES as a documented name.",
    )
    GOLD[(C, 5)] = dict(
        kernel="bloom: bright-pass → blur pass(es) → add; on HDR, named",
        success="they can extract highlights, blur, combine, and toggle the three passes",
        invariant="bloom is leftover HDR energy, not a substitute for lighting",
        goal="three named bloom passes",
        board="""```
PASS  bright    max(c - t, 0)   on HDR
PASS  blur      separable H then V   (not naive 12×12)
PASS  add       combine  (policy: before or after tonemap — freeze one)

half-res  is a budget  (measure if you claim)
```""",
        slides=[],
        hook_say="Same FBO idea as WebGL post. Draw the boxes before UnrealBloomPass. Fireflies and a huge kernel are artifacts. We do not invent fps; half-res is a named cut.",
        hook_ask="Which pass extracts the sun? Wait. Want: bright / threshold.",
        frame_say="Threshold on HDR. Separable blur. Combine policy frozen in README. Three.js UnrealBloomPass is the oracle after the boxes.",
        frame_ask="Why HDR before bloom?",
        build=[
            "**Say:** Three FBO boxes. Label each pass.",
            "**Board:** threshold → blur → add. Circle separable.",
            "**Say:** Threshold slider is a uniform. Toggle the add pass.",
        ],
        ask_build="Why not a naive 2D 12-tap?",
        they_build="On paper: the three pass names in order.",
        show_say="Bloom a bright sphere; toggle. Plant bloom as lighting. Half-res extra — if they claim speed, they measure on this machine.",
        attempt_say="Threshold slider. Eight minutes.",
        land_say="Lab: threshold + half-res extra. Homework: three passes written; on/off screenshots. Quiz: bright pass, separable, why HDR first.",
        live=[
            ("0–10", "Name bright pass", "Plant bloom as lighting."),
            ("10–30", "Separable blur", "Plant naive 12×12."),
            ("30–45", "Add + toggle", "Freeze combine policy."),
            ("45–60", "Half-res if time", "Measure or omit fps."),
        ],
        cut="UnrealBloomPass internals. Keep three named passes.",
        add="Half-res as a documented budget.",
    )
    GOLD[(C, 6)] = dict(
        kernel="shadow-map pass: depth from light; shade pass: compare z",
        success="they can render a depth map from the light, compare, and show the map as grayscale",
        invariant="a camera at the light is a named pass; CSM without one map is a speech",
        goal="two cameras: eye and light",
        board="""```
PASS 1  light camera  →  depth tex     (ortho if directional)
PASS 2  eye shade     →  compare zLight vs mapZ + bias

bias 0.1 is huge
mapSize: measure 512 vs 2048 on this device, or omit
```""",
        slides=[],
        hook_say="Algorithm: store depth from the light. If the main pixel is farther than the map, it is in shadow. WebGL DEPTH_COMPONENT. Three.js does this — they still draw the light frustum.",
        hook_ask="Who renders the shadow map — the eye or the light? Wait. Want: the light.",
        frame_say="Ortho for directional, perspective for spot. Frustum too tight → acne, too loose → jaggy. Bias is a uniform they will plant wrong.",
        frame_ask="Why ortho for a directional light?",
        build=[
            "**Say:** Two cameras. Two frustums.",
            "**Board:** light P V → depth → compare. Circle bias.",
            "**Say:** Show the map as grayscale extra. mapSize change is a measurement row, not a claimed fps.",
        ],
        ask_build="Write the compare in one line (teaching).",
        they_build="On paper: pass 1 vs pass 2.",
        show_say="Plane + cube; directional shadow; bias slider. Plant CSM speech. Plant bias 0.1. Grayscale map.",
        attempt_say="Show shadow map as grayscale. Eight minutes.",
        land_say="Lab: grayscale + mapSize 512 vs 2048 measured. Homework: compare function; bias paragraph. Quiz: who renders the map, bias, ortho why.",
        live=[
            ("0–10", "Light-depth pass", "Plant CSM without a map."),
            ("10–30", "Compare + bias", "Plant bias 0.1."),
            ("30–45", "Grayscale debug", "Named extra view."),
            ("45–60", "512 vs 2048 table", "Device + resolution; no invented fps."),
        ],
        cut="Cascades. Keep one directional map + named passes.",
        add="Spot perspective as a name.",
    )
    GOLD[(C, 7)] = dict(
        kernel="PCF: average binary depth compares in a 3×3 kernel — still the shadow pass",
        success="they can 3×3 PCF, count taps, and say why blurring the depth texture is not PCF",
        invariant="PCF averages tests, not the depth values",
        goal="soft-looking edges on a 2D map",
        board="""```
PASS: shadow compare  (same map as week 6)

3×3:  9 binary tests  →  average
not:  blur(depthTex) then compare once

VSM / PCSS  names only
sampler2DShadow  name
```""",
        slides=[("Hard vs 3×3 edge crop", "photograph")],
        hook_say="Percentage closer filtering: average the tests. Blurring depth and calling it PCF is the classic fail. PCSS is not the required lab. We do not invent how many ms nine taps cost.",
        hook_ask="If I blur the depth texture first, is that PCF? Wait. Want: no.",
        frame_say="Soft-looking edges, still a 2D map. Acne can remain — say why. API: compare mode names.",
        frame_ask="How many taps in 3×3?",
        build=[
            "**Say:** Nine samples around uv. Average 0/1.",
            "**Board:** 3×3. Circle 'tests, not blur depth'.",
            "**Say:** Count taps in comments. Toggle hard vs PCF.",
        ],
        ask_build="Why can acne survive PCF?",
        they_build="On paper: one tap vs nine — what is averaged?",
        show_say="Toggle hard vs 3×3; screenshot. Plant blur-the-depth. Do not quote fps.",
        attempt_say="Count taps in comments. Eight minutes.",
        land_say="Lab: tap count + acne sentence. Homework: PCF vs blur depth; code. Quiz: PCF, why not blur depth, tap count. Midterm next week.",
        live=[
            ("0–10", "Hard compare", "They still have week 6."),
            ("10–30", "3×3 PCF", "Plant blur depth."),
            ("30–45", "Toggle + screenshot", "No invented timings."),
            ("45–60", "They comment 9 taps", "Circulate."),
        ],
        cut="PCSS lab. Keep 9 taps + the wrong blur.",
        add="sampler2DShadow as a name.",
    )
    GOLD[(C, 8)] = dict(
        kernel="SSAO as a post pass: sample neighbors in view-space depth",
        success="after the exam they can name AO as a fake post and toggle it",
        invariant="SSAO is not a true GI pass; it is a named post on depth",
        goal="midterm, then AO as post",
        kind="midterm",
        midterm_topics="forward path; D F G and F0; IBL names; HDR/tonemap order; bloom's three passes; shadow map + PCF.",
        board="""```
PASS: SSAO post
  sample hemisphere in view space
  darken if depth neighbors occlude

fake · noisy · dark rims · skip sky
HBAO  name only
```""",
        slides=[],
        hook_say="This meeting is a **midterm**, then SSAO as a post. No laptop. After: sample neighbors in depth. Do not require production HBAO.",
        show_say="Two planes in a corner; cheap SSAO or a Three.js SAO pass explained after the boxes. Plant SSAO as GI. Radius slider. No invented fps.",
        attempt_say="Toggle + radius uniform.",
        land_say="Lab: toggle + radius. Homework: reflection + AO screenshot. No quiz this week.",
        live=[
            ("0–15", "Name the AO post", "Plant SSAO as GI."),
            ("15–40", "Hemisphere samples", "Plant missing sky skip."),
            ("40–60", "Toggle + radius", "They type. Circulate."),
        ],
        cut="Live coding if the exam ran long. Keep the leftover board.",
        add="Noise / dark-rim artifacts named.",
    )
    GOLD[(C, 9)] = dict(
        kernel="deferred: G-buffer pass (albedo, n, depth, metal-rough) then light pass",
        success="they can name G channels and show three debug panes without deferred-on-one-cube",
        invariant="many lights, few G writes; a single cube does not earn deferred",
        goal="name G then lights",
        board="""```
PASS 1  G-buffer   albedo | n | depth | metal-rough
PASS 2  lights     read G, add

MRT  name
debug panes  are  required
when not:  one cube, forward is enough
```""",
        slides=[],
        hook_say="Why: many lights, objects write G once. Light pass reads G. WebGL MRT is a name. Students can fake G with extra textures. We do not invent how many lights 'hurt' — they count, or they omit.",
        hook_ask="Does deferred help one cube and one light? Wait. Want: no.",
        frame_say="Packed G. Debug view of n and albedo. Transparency and MSAA are later reasons to stay forward.",
        frame_ask="What goes in G?",
        build=[
            "**Say:** Four panes. Label channels.",
            "**Board:** G then light pass. Circle MRT.",
            "**Say:** Written G layout is the lab if code time is short.",
        ],
        ask_build="When do you not deferred?",
        they_build="On paper: G layout (four rows).",
        show_say="Debug view: albedo | normals | depth. Plant deferred for a single cube. Count lights that would hurt forward — as a count, not an fps.",
        attempt_say="Count lights / written G layout. Eight minutes.",
        land_say="Lab: light count + G layout. Homework: when deferred wins; debug screenshot. Quiz: G channels, MRT, when not.",
        live=[
            ("0–10", "Name G pass", "Plant one-cube deferred."),
            ("10–30", "Three debug panes", "Plant no debug views."),
            ("30–45", "Light pass idea", "Read G, add."),
            ("45–60", "They write the layout", "Circulate."),
        ],
        cut="A full MRT engine. Keep named G + debug panes.",
        add="Transparency as a reason to stay forward.",
    )
    GOLD[(C, 10)] = dict(
        kernel="freeze a stack: shade HDR → shadow → bloom → tonemap → sRGB → grain/LUT",
        success="they can write the order, toggle three passes, and document it in README",
        invariant="a product shot is a named stack, not eight Instagram filters",
        goal="order of operations on the board",
        board="""```
shade(HDR) + shadow compare
  → bloom (HDR)
  → tonemap
  → sRGB encode
  → grain
  → LUT   (last or before grain — pick)

kill switch per pass
```""",
        slides=[],
        hook_say="Order matters. Bloom on HDR. Tonemap before 8-bit. Grain after. LUT last or before grain — pick and freeze. Undocumented order is a grading zero for the stack graph.",
        hook_ask="Bloom after tonemap — what did you lose? Wait. Want: leftover HDR energy.",
        frame_say="Look-dev is a stack. Kill switches for grading and for perf. If they claim a pass is cheap, they measure next week — not today with a fantasy number.",
        frame_ask="What is a kill switch for?",
        build=[
            "**Say:** Graph top to bottom. One box per pass.",
            "**Board:** the frozen order. Circle bloom vs tonemap.",
            "**Say:** Three toggles live: bloom, grain, vignette.",
        ],
        ask_build="LUT in one sentence?",
        they_build="On paper: their order and one why.",
        show_say="Three toggles; freeze order in README. Plant eight Instagram filters. Tiny LUT extra (16³ or 2D strip) — local file.",
        attempt_say="One LUT extra or a screenshot matrix of toggles. Eight minutes.",
        land_say="Lab: LUT or screenshot matrix. Homework: order and why; graph figure. Quiz: tonemap vs bloom order, LUT, kill switch.",
        live=[
            ("0–10", "Draw the graph", "Plant undocumented order."),
            ("10–30", "Three kill switches", "Plant Instagram soup."),
            ("30–45", "README freeze", "One policy."),
            ("45–60", "They screenshot the matrix", "Circulate. No fps."),
        ],
        cut="Color-grade product. Keep named order + toggles.",
        add="Vignette as an extra named pass.",
    )
    GOLD[(C, 11)] = dict(
        kernel="name MSAA (edge samples), FXAA (post), TAA (history) — table, not a homework TAA",
        success="they can fill where / cost-idea / blur and choose AA for a product viewer in words",
        invariant="AA is a named technique; 8× supersample on a laptop is not the lab; do not invent fps",
        goal="a table you can defend",
        board="""```
        where           blur risk
MSAA    geometry edge   low      (hates deferred)
FXAA    post            some
TAA     history         ghosting

alpha-to-coverage  name
TAA not required homework
```""",
        slides=[("Same edge: off vs renderer AA vs cheap blur", "photograph")],
        hook_say="Aliasing: edges, specular sparkle, thin geo, alpha test. MSAA hates deferred — that is a reason for FXAA/TAA. We screenshot; we do not invent milliseconds.",
        hook_ask="Why is TAA not the required homework? Wait. Want: ghosting, history, too much for a week.",
        frame_say="Forward antialias: true is MSAA-ish. FXAA is a post pass. Hair is hard. Alpha-to-coverage named.",
        frame_ask="What is TAA's main artifact?",
        build=[
            "**Say:** Table: where / cost-idea / blur. Cost-idea is 'samples' or 'history', not a fake ms.",
            "**Board:** the table. Circle deferred vs MSAA.",
            "**Say:** Ghosting description from a video still extra.",
        ],
        ask_build="MSAA in one sentence?",
        they_build="On paper: fill the three-row table.",
        show_say="Same edge: AA off vs renderer antialias vs cheap FXAA-ish blur. Plant TAA as required HW. Plant 8× SS as the lab.",
        attempt_say="Written table. Eight minutes.",
        land_say="Lab: table + ghosting extra. Homework: choose AA for a product viewer; screenshots. Quiz: MSAA idea, TAA risk, FXAA.",
        live=[
            ("0–10", "Why aliasing", "They list edges."),
            ("10–30", "Three screenshots", "Plant invented fps."),
            ("30–45", "Deferred vs MSAA", "Name the conflict."),
            ("45–60", "They fill the table", "Circulate."),
        ],
        cut="Implement TAA. Keep names + screenshots.",
        add="Alpha-to-coverage as a name.",
    )
    GOLD[(C, 12)] = dict(
        kernel="CPU vs GPU clocks; table: device, resolution, what changed, ms — measure or omit",
        success="they can record two rows after one change and never say 'it's 60' without numbers",
        invariant="invented frame rates are a grading zero; a budget is a measured table",
        goal="two rows on a named device",
        board="""```
CPU: JS, draw calls
GPU: fill, bandwidth, shader

table:
  device | res | change | ms or info.render

Spector.js / renderer.info / Chrome GPU  names
overdraw viz: additive white extra
```""",
        slides=[],
        hook_say="Two clocks. Student rule: device, resolution, what changed, ms. Spector.js, RenderDoc, three.js info, timestamp queries — names. 'It's 60 on my machine' with no numbers fails.",
        hook_ask="If you did not measure, what do you write? Wait. Want: omit.",
        frame_say="One change: shadow map size or pixel ratio. Two rows. Overdraw viz extra. Cut one pass extra. Do not optimize 8k textures last if they are the problem — still measure.",
        frame_ask="CPU bound vs GPU bound in one idea?",
        build=[
            "**Say:** Empty table on the board. Fill it live from this machine.",
            "**Board:** the columns. Circle omit.",
            "**Say:** console.table(renderer.info.render) as a snippet, not a fps fantasy.",
        ],
        ask_build="What four columns?",
        they_build="On paper: one hypothesized bottleneck — then they must measure or strike it.",
        show_say="Profile: one change; two rows on the named device. Plant 'it's 60'. No CDN tools that require a login wall — Spector as optional local.",
        attempt_say="Overdraw viz extra, or cut one pass. Eight minutes.",
        land_say="Lab: overdraw or cut pass. Homework: budget for *your* project device; measured table. Quiz: CPU vs GPU bound, overdraw, why measure.",
        live=[
            ("0–10", "Two clocks", "Plant '60 fps'."),
            ("10–30", "One change, two rows", "Fill device + res."),
            ("30–45", "info.render", "Read the numbers out loud."),
            ("45–60", "They cut one pass", "Circulate. Omit if unmeasured."),
        ],
        cut="RenderDoc deep dive. Keep the table + one change.",
        add="Timestamp query as a name.",
    )
    GOLD[(C, 13)] = dict(
        kernel="look-dev: one asset; dir + IBL + shadow + tonemap named; toggle stack",
        success="they can load a glb or primitives, match a reference crop in words, and say what they configured vs wrote",
        invariant="honesty: if PMREM or GGX is Three.js, say so; Unreal stills are not the lab",
        goal="one asset, full named stack",
        board="""```
dir light + IBL lookup + shadow compare + tonemap
(+ bloom if earned)

cuts: drop SSAO; keep metal-rough + shadow + tonemap
reference crop  |  yours
```""",
        slides=[],
        hook_say="Look-dev is a job: reference, then stack, then budget. Cinema from Unreal as 'the lab' fails. Local glb. No CDN HDR.",
        hook_ask="If IBL is Three.js PMREM, what do you write in the README? Wait. Want: that sentence.",
        frame_say="Toggle the stack. Device from last week's table. Cuts: drop SSAO.",
        frame_ask="What do you skip first?",
        build=[
            "**Say:** Reference pair. Three differences they will have to name.",
            "**Board:** dir + IBL + shadow + tonemap. Circle honesty.",
            "**Say:** README: configured vs wrote.",
        ],
        ask_build="Name today's required passes.",
        they_build="On paper: skip list.",
        show_say="A still that matches a reference crop (local photo). Plant Unreal as the lab. Toggle stack.",
        attempt_say="Toggle stack + README bullets. Eight minutes.",
        land_say="Lab: toggles + README. Homework: three differences vs reference; repo. Quiz: configured vs wrote, skip list, device. Next: studio.",
        live=[
            ("0–10", "Name the stack", "Plant Unreal screenshot."),
            ("10–30", "Load glb/primitives", "Plant CDN env."),
            ("30–45", "Toggles", "Honesty line in README."),
            ("45–60", "They write three diffs", "Circulate. No invented fps."),
        ],
        cut="SSAO on the look. Keep metal-rough + shadow + tonemap.",
        add="Bloom only if leftover HDR is visible.",
    )
    GOLD[(C, 14)] = dict(
        kernel="real-time look: named stack graph + measured table on a named device",
        success="a TA can serve the folder, read the graph, and see two measured rows without Unreal",
        invariant="freeze; drop deferred if behind; keep PBR+shadow+tonemap",
        goal="studio — not a content lecture",
        kind="studio",
        board="""```
Must: stack graph · PBR · shadow · tonemap · measured table
Cuts: drop deferred / SSAO / TAA
README: serve + device + what you did not write
```""",
        slides=[],
        hook_say="This meeting is **studio**. Product shot, small interior, or shader-ball. Cuts are allowed. Invented fps still fail.",
        hook_ask="If behind, what do you cut first?",
        frame_say="Desk review: stack graph on the board, then the measured table, then citations.",
        show_say="Volunteer graph vs running demo. Plant a missing pass name.",
        attempt_say="Studio. Serve first.",
        land_say="Report: stack graph, budgets, citations. Next week 12+5.",
        live=[
            ("0–10", "Headings + cut list", "Photograph."),
            ("10–50", "Desk review", "Graph + table."),
            ("50–60", "60s rehearsal", "Stop."),
        ],
        cut="New libraries. Keep freeze.",
        add="One 60-second rehearsal in front of another team.",
    )
    GOLD[(C, 15)] = dict(
        kernel="12+5; demo the stack; point at HDR and the shadow compare",
        success="they stop at 12 and can say where HDR lives and why acne happens",
        invariant="no new features today; no invented fps on stage",
        goal="presentations — not a content lecture",
        kind="presentations",
        board="""```
12 + 5
Show: named stack · one measured row
Ask: where is HDR?  why acne?
No new passes on stage
```""",
        slides=[("Timer", "not a slide of PBR")],
        hook_say="Presentations. 12+5. I will ask where HDR is, and why acne. If you did not measure, omit the number.",
        show_say="None. Present.",
        attempt_say="Present.",
        land_say="A look with a stack graph and a measurement is real-time rendering; a screenshot is not.",
        live=[("0–60", "Talks", "Cut at 12.")],
        cut="Debugging on stage.",
        add="One question on a pass they configured vs wrote.",
    )


def _gpu(GOLD: dict) -> None:
    C = "GPU Programming"
    GOLD[(C, 1)] = dict(
        kernel="GPU as throughput: one FS kernel over a grid; readback is slow",
        success="they can contrast CPU latency vs GPU throughput and say why this is a kernel, not a triangle demo",
        invariant="data lives where the kernel runs; CUDA slides without a browser path are the wrong degree",
        goal="see a fullscreen kernel",
        board="""```
CPU:  one thread, low latency
GPU:  many lanes, high throughput

FS kernel:  one texel / pixel  (no pointers)

readPixels every frame  =  stall
this program: WebGL then WebGPU — not CUDA-only
```""",
        slides=[],
        hook_say="Particles, fluids teasers, image filters, then an honest WebGPU intro. Graphics students already write FS kernels; GPGPU is the same hardware with fewer triangles. Teaching only CUDA in a web degree fails the course contract.",
        hook_ask="Is CUDA required this term? Wait. Want: no.",
        frame_say="Web vs native: CUDA/OpenCL exist. IGWT ships in the browser: FBO ping-pong, TF as a name, then WebGPU. Limits: no pointers in FS, fixed output size, readback is slow.",
        frame_ask="Why is readPixels every frame a problem?",
        build=[
            "**Say:** Throughput bars vs a latency needle. Same silicon, different job.",
            "**Board:** data-parallel vs graphics. Circle no CUDA-only path.",
            "**Say:** A gradient 'simulation' into a texture is already a kernel. Time is a uniform you can pause.",
        ],
        ask_build="Where does the state live this week?",
        they_build="On paper: CPU vs GPU, four bullets, no CUDA-only line.",
        show_say="Fullscreen FS writes a gradient into a texture (static). Demo GPU Programming/code/01-pong.html when it helps. Plant CUDA-only slides. Plant readPixels every frame. Local serve, no CDN.",
        attempt_say="Time uniform. Why this is a kernel, in a sentence. Eight minutes.",
        land_say="Lab: time uniform + kernel sentence. Homework: CPU vs GPU one page; screenshot. Quiz: throughput, readback, CUDA this program?",
        live=[
            ("0–10", "Throughput vs latency", "Plant CUDA-only path."),
            ("10–30", "FS as kernel", "Plant readPixels every frame."),
            ("30–45", "u_time pause", "Debug a still."),
            ("45–60", "They write the kernel sentence", "Circulate."),
        ],
        cut="OpenCL history. Keep kernel + no CUDA-only.",
        add="Fixed output size as a limit on the board.",
    )
    GOLD[(C, 2)] = dict(
        kernel="ping-pong: read A, write B, swap — two FLOAT textures",
        success="they can draw two FBOs, swap, and debug A vs B without sampling the texture they are writing",
        invariant="a shader cannot safely read the texel it is writing; RGBA8 positions are a trap",
        goal="A→B→A you can pause",
        board="""```
frame n:    sample A  →  write B
swap:       [A,B] = [B,A]

A  FLOAT RGBA     B  FLOAT RGBA
   (sim res)         (sim res)

sim resolution  ≠  canvas resolution
```""",
        slides=[],
        hook_say="Ping-pong is game-of-life, blur, and particle positions. One texture in/out is a race. Unsigned byte positions die. This is still WebGL — WebGPU compute comes after the midterm.",
        hook_ask="Why two textures? Wait. Want: cannot read what you write.",
        frame_say="HALF_FLOAT / FLOAT for state. Sim res ≠ canvas. Pause the swap to debug A and B as color.",
        frame_ask="What is wrong with RGBA8 for positions?",
        build=[
            "**Say:** Two rectangles on the board. Arrows read/write.",
            "**Board:** the swap line. Circle FLOAT.",
            "**Say:** Plant same-texture, then fix. Local 01-pong.html.",
        ],
        ask_build="Write the swap in one JS line.",
        they_build="On paper: memory layout of A and B.",
        show_say="Game of life or blur ping-pong; pause. Plant one texture in/out. Plant RGBA8 positions. Show A and B debug views.",
        attempt_say="Show A and B debug. Eight minutes.",
        land_say="Lab: debug views + same-texture bug then fix. Homework: why two textures; code. Quiz: feedback loop, float tex, sim vs canvas.",
        live=[
            ("0–10", "Draw A and B", "Plant one texture in/out."),
            ("10–30", "Swap each frame", "Plant RGBA8 state."),
            ("30–45", "Pause; show A vs B", "They see the layout."),
            ("45–60", "They fix same-texture", "Circulate."),
        ],
        cut="Precision formats catalog. Keep two FLOAT textures + swap.",
        add="Sim res as a uniform they can shrink — measure if they claim speed.",
    )
    GOLD[(C, 3)] = dict(
        kernel="one texel = one particle; RG=pos, BA=vel; VS fetches by VertexID",
        success="they can pack pos/vel into a FLOAT texture and draw points without 50k Mesh objects",
        invariant="neighbor texels are not spatial neighbors unless you build a grid",
        goal="SoA on the GPU you can draw",
        board="""```
state tex  (W×H FLOAT)
  texel (i,j):  RG = pos.xy    BA = vel.xy

vertex i:  u = i % W;  v = i / W
           texelFetch(state, ivec2(u,v), 0)

CPU loop of 50k Mesh  =  not this course
```""",
        slides=[],
        hook_say="Structure of arrays on the GPU. Render: VS fetches by gl_VertexID. WebGL2 integer fetch. Instancing is a name from WebGL week 12. Invented particle counts are not measurements.",
        hook_ask="Why not one Mesh per particle? Wait. Want: draw-call / CPU death.",
        frame_say="N=64² is a teaching count they can see in the layout (64×64 texels). Points need a depth policy. Mouse force extra is a uniform.",
        frame_ask="How do you map VertexID to a texel?",
        build=[
            "**Say:** Grid of texels. One particle per cell. Draw the RG/BA split.",
            "**Board:** packing. Circle fetch.",
            "**Say:** Reset button rewrites the texture from JS once — not every frame.",
        ],
        ask_build="What is in BA?",
        they_build="On paper: packing diagram for one particle.",
        show_say="N=64² falling with wrap; points. Plant 50k Mesh. Mouse force extra. Pause to inspect one texel as color.",
        attempt_say="Mouse force extra. Eight minutes.",
        land_say="Lab: mouse force + reset. Homework: packing paragraph; demo. Quiz: why not one mesh, RG pos, ID mapping.",
        live=[
            ("0–10", "Packing RG/BA", "Plant 50k Mesh."),
            ("10–30", "texelFetch by ID", "Plant wrong % W."),
            ("30–45", "Points + wrap", "Depth policy."),
            ("45–60", "Reset button", "Circulate. Pause time."),
        ],
        cut="Spatial hash grid. Keep packing + fetch + points.",
        add="Two textures if pos and vel split — still draw the layout.",
    )
    GOLD[(C, 4)] = dict(
        kernel="transform feedback name: VS writes varyings into a buffer; rasterizer discard",
        success="they can name TF vs FBO ping-pong and keep particles working even if TF is diagram-only",
        invariant="TF is the graphics pipeline as compute; ping-pong remains the teaching path until WebGPU",
        goal="name VS→buffer",
        board="""```
TF:   VS varyings  →  GL buffer   (optional rasterizer discard)
FBO:  FS           →  texture     (week 2 — still valid)

WebGPU compute  will replace a lot of TF
no CUDA path
```""",
        slides=[],
        hook_say="Particles as vertices: VS updates pos. Rasterizer discard named. FS ping-pong is often easier in WebGL teaching. Skipping particles entirely fails. Claiming TF without a buffer fails.",
        hook_ask="What does TF capture — FS color, or VS outputs? Wait. Want: VS.",
        frame_say="Diagram required. Tiny TF optional. A README that says 'we use ping-pong instead' plus a working FS sim is honest. WebGPU compute later makes TF less necessary — still teach the name.",
        frame_ask="When would you keep FBO ping-pong?",
        build=[
            "**Say:** VS to buffer arrow. Discard the triangles.",
            "**Board:** TF vs FBO table. Circle discard.",
            "**Say:** transformFeedbackVaryings as a 20pt name, not a CUDA port.",
        ],
        ask_build="WebGPU's replacement in one word?",
        they_build="On paper: TF vs FBO, one sentence each.",
        show_say="Diagram + optional tiny TF, or ping-pong README with working FS sim. Plant skip particles. Plant TF with no buffer.",
        attempt_say="Rasterizer discard name + compare sentence. Eight minutes.",
        land_say="Lab: discard name + compare. Homework: TF vs FBO; week-3 particles OK. Quiz: TF captures, discard, WebGPU replacement.",
        live=[
            ("0–10", "Name TF", "Plant skip particles."),
            ("10–30", "Diagram VS→buffer", "Plant TF without a buffer."),
            ("30–45", "Ping-pong still runs", "Honesty in README."),
            ("45–60", "They write the compare", "Circulate."),
        ],
        cut="A full TF engine. Keep the name + honest ping-pong.",
        add="SEPARATE_ATTRIBS as a name.",
    )
    GOLD[(C, 5)] = dict(
        kernel="semi-implicit Euler in the update kernel: v+=a dt; p+=v dt; clamp dt and speed",
        success="they can explode with huge dt, then cap, in the same packing as week 3",
        invariant="integration runs where the state lives; CPU physics + GPU draw is not GPGPU",
        goal="stable steps you can pause",
        board="""```
in the update kernel (FS or TF):
  v += a * dt
  p += v * dt          // semi-implicit: v first
  v = clamp(v, ±vmax)
  dt = min(dt, dtMax)

state layout still: RG pos, BA vel
```""",
        slides=[],
        hook_say="Same as Interactive Web physics-lite, all particles in parallel. Variable uncapped dt explodes. CPU physics then upload is not this course. Pause; inspect one texel.",
        hook_ask="Why v before p? Wait. Want: semi-implicit Euler.",
        frame_say="Stability: dt too big → explode. Clamp speed. Forces: gravity, attractor; curl noise extra. Box collide extra writes p and v in the same layout.",
        frame_ask="What causes the explode?",
        build=[
            "**Say:** One particle on the board: numbers, then the same in a texel.",
            "**Board:** Euler + clamp. Circle dtMax.",
            "**Say:** Attractor as a uniform. Plant uncapped rAF dt.",
        ],
        ask_build="Write the two Euler lines.",
        they_build="On paper: where dt is clamped.",
        show_say="Attractor + gravity; explode then cap dt. Plant variable dt uncapped. Plant CPU physics + GPU draw labeled GPGPU.",
        attempt_say="Box collide extra. Eight minutes.",
        land_say="Lab: box collide + curl extra. Homework: why cap dt; demo. Quiz: Euler, explode cause, clamp.",
        live=[
            ("0–10", "Euler in the kernel", "Plant CPU physics as GPGPU."),
            ("10–30", "Explode then dtMax", "Plant uncapped dt."),
            ("30–45", "Clamp speed", "Same RG/BA layout."),
            ("45–60", "They add a box", "Circulate. Pause."),
        ],
        cut="RK4. Keep Euler + clamp + layout.",
        add="Curl noise as extra force.",
    )
    GOLD[(C, 6)] = dict(
        kernel="stable-fluids names: advect → diffuse → project; dye and velocity textures",
        success="they can advect a dye by a velocity field and say why project (incompressible)",
        invariant="a swirling dye is the lab; 3D Navier–Stokes is a thesis; Unity VFX is not the homework",
        goal="divergence-free as a name, dye as a picture",
        board="""```
vel tex   RG = velocity
dye tex   RGB = color     (ping-pong each)

advect  →  diffuse  →  project (Jacobi name)
  dye samples uv - dt * vel

3D NS  not this week
cite Stam / GPU Gems
```""",
        slides=[],
        hook_say="Velocity field in a texture. Pressure solve makes it incompressible — Jacobi iteration named. A dye blob that swirls is the lab. Unstable huge dt fails. Cite.",
        hook_ask="Is 3D fluid the week? Wait. Want: no.",
        frame_say="Scope: 2D dye, mouse or vortex velocity. One Jacobi extra or a note why skipped. Dissipation extra. Still ping-pong — WebGPU later.",
        frame_ask="Why project?",
        build=[
            "**Say:** Two layouts: vel and dye. Ping-pong both.",
            "**Board:** advect → diffuse → project. Circle incompressible.",
            "**Say:** Backtrace uv - dt*vel. Pause to see a still swirl.",
        ],
        ask_build="Write the advect sample line.",
        they_build="On paper: memory layout of vel vs dye.",
        show_say="2D dye advected by mouse velocity or a vortex. Plant Unity VFX as homework. Plant huge dt. Local only.",
        attempt_say="One Jacobi extra or a skip note. Eight minutes.",
        land_say="Lab: Jacobi note + dissipation. Homework: why project; screenshot. Quiz: advect, incompressible, 3D this week?",
        live=[
            ("0–10", "Vel + dye layout", "Plant Unity VFX homework."),
            ("10–30", "Advect dye", "Plant huge dt."),
            ("30–45", "Project name", "Jacobi optional."),
            ("45–60", "They add dissipation", "Circulate. Cite Stam."),
        ],
        cut="Full pressure solver. Keep advect + named project + layouts.",
        add="Dissipation on dye.",
    )
    GOLD[(C, 7)] = dict(
        kernel="reduce: mip chain as average; histogram named; no getImageData 1080p loop",
        success="they can treat generateMipmap (or blit down) as a reduce and avoid readPixels every frame",
        invariant="WebGL FS has almost no atomics; a CPU histogram of the canvas is not GPGPU",
        goal="a pyramid, not a readback",
        board="""```
scene tex
  → mip 1
  → mip 2
  → …  1×1  ≈  mean luminance

atomics:  WebGL2 FS ≈ none;  WebGPU compute has them
readback: async pack name; stall if you wait
```""",
        slides=[],
        hook_say="Average luminance for auto-exposure is a mip chain. Teaching: generateMips or blit down. CPU loop over getImageData at 1080p is the plant. Atomics in a WebGL1 blog post do not port.",
        hook_ask="Does generateMipmap reduce? Wait. Want: yes, as a teaching reduce.",
        frame_say="Show mip debug. Auto-exposure-ish: log average, feed exposure — still a named pass. Do not readPixels every frame. WebGPU atomics are a reason to move after the midterm.",
        frame_ask="Why almost no atomics in WebGL FS?",
        build=[
            "**Say:** Pyramid on the board. 1×1 is the reduce.",
            "**Board:** mip as reduce. Circle no getImageData.",
            "**Say:** Histogram is a name; mip is the lab.",
        ],
        ask_build="What stalls a frame?",
        they_build="On paper: the pyramid sizes (power of two sketch).",
        show_say="Downsample a scene tex; log average; feed exposure. Plant getImageData 1080p. Plant readPixels every frame. Mip debug view.",
        attempt_say="Show mip debug. Eight minutes.",
        land_say="Lab: mip debug + don't readPixels every frame. Homework: reduce paragraph; demo. Quiz: mip reduce, why atomics, stall. Midterm next week.",
        live=[
            ("0–10", "Mip pyramid", "Plant getImageData loop."),
            ("10–30", "1×1 as mean", "Plant readPixels every frame."),
            ("30–45", "Exposure feed", "Named, not a fps claim."),
            ("45–60", "They debug mips", "Circulate."),
        ],
        cut="A real histogram SSBO. Keep mip reduce + no stall.",
        add="Async pixel pack as a name.",
    )
    GOLD[(C, 8)] = dict(
        kernel="WebGPU: adapter → device → queue; feature detect; WGSL later",
        success="after the exam they can request adapter/device or show a documented WebGL fallback",
        invariant="WebGPU is after ping-pong; no Safari-only lab without a fallback; no CUDA",
        goal="midterm, then device/queue",
        kind="midterm",
        midterm_topics="throughput vs latency; ping-pong A/B; RG/BA packing; TF name; Euler+clamp; fluids names; mip reduce.",
        board="""```
navigator.gpu.requestAdapter()
  → device
  → queue.submit(...)

WebGL program  ≈  pipeline
uniform        ≈  bind group
FBO            ≈  texture view

feature detect  or  WebGL triangle + WGSL reading
```""",
        slides=[],
        hook_say="This meeting is a **midterm**, then WebGPU intro. No laptop. After: adapter/device/queue. Do not port the whole particle system this week. Chrome. Not a Safari-only lab without a fallback.",
        show_say="Hello triangle in WebGPU **or** documented fallback WebGL triangle plus a WGSL reading. Plant no feature detect. Plant CUDA as the leftover.",
        attempt_say="Feature detect + error popup.",
        land_say="Lab: detect + popup. Homework: reflection + adapter-name screenshot. No quiz this week.",
        live=[
            ("0–15", "adapter → device → queue", "Plant skip detect."),
            ("15–40", "Hello triangle or fallback", "Plant CUDA leftover."),
            ("40–60", "Error popup", "They type. Circulate."),
        ],
        cut="Live coding if the exam ran long. Keep the leftover board.",
        add="Mental map WebGL ≈ pipeline on the board.",
    )
    GOLD[(C, 9)] = dict(
        kernel="WGSL vs/fs: @builtin(vertex_index) → clip position; bind group for time",
        success="they can read a WGSL pair, resize, and table six GLSL vs WGSL rows",
        invariant="Three.js WebGPURenderer without reading WGSL is not the lab; validation errors are loud on purpose",
        goal="a triangle you wrote",
        board="""```
@vertex   fn vs(@builtin(vertex_index) i: u32)
          -> @builtin(position) vec4f

@fragment fn fs(...) -> @location(0) vec4f

clip z  0..1  (not GLSL's -1..1)   — freeze and say it
bind group  ≈  uniforms
```""",
        slides=[],
        hook_say="WGSL is typed. @location. No GLSL preprocessor soup. navigator.gpu.requestAdapter then configure the canvas. Copying a full sample unread fails. Still no CUDA.",
        hook_ask="Who supplies vertex_index — a VBO, or the draw? Wait. Want: the draw (builtin).",
        frame_say="Colored triangle; resize. Uniform time extra. Compare GLSL side by side. Clip Z convention named.",
        frame_ask="What is a bind group?",
        build=[
            "**Say:** Three vertices from an index. No buffer required for the hello.",
            "**Board:** @vertex @fragment. Circle clip z.",
            "**Say:** Validation is loud — read it like a GLSL compile log.",
        ],
        ask_build="Write the vs signature in one line.",
        they_build="On paper: GLSL vs WGSL, three rows to start the homework table.",
        show_say="Colored triangle WGSL; resize. Plant WebGPURenderer as the only lab. Plant unread sample paste. Local, no CDN.",
        attempt_say="Uniform time extra. Eight minutes.",
        land_say="Lab: time uniform + GLSL side by side. Homework: 6-row table; code. Quiz: @builtin(position), bind group, clip z.",
        live=[
            ("0–10", "requestAdapter + configure", "Plant no detect."),
            ("10–30", "WGSL triangle", "Plant Three.js-only lab."),
            ("30–45", "Resize + validation error", "Read it out loud."),
            ("45–60", "They add time bind group", "Circulate."),
        ],
        cut="A mesh loader. Keep triangle + bind group + table.",
        add="Clip z 0..1 on the parked strip.",
    )
    GOLD[(C, 10)] = dict(
        kernel="compute pass: dispatch workgroups; write storage texture/buffer; then blit",
        success="they can fill a texture from @compute @workgroup_size(8,8) without a triangle-per-particle",
        invariant="compute has no raster; races if you write without sync; this replaces some ping-pong FS hacks",
        goal="a grid of threads",
        board="""```
dispatch(x, y, 1)

@compute @workgroup_size(8,8)
fn cs(@builtin(global_invocation_id) id: vec3u)

storage buffer  vs  storage texture
  (draw the bytes:  width×height×channels)

no triangle per particle
```""",
        slides=[],
        hook_say="No raster. Threads in a grid. Perfect for particles and blur. Unbounded loops in WGSL are a hang. Fallback: if WebGPU is missing, they still have ping-pong from week 2 — say so.",
        hook_ask="Does a compute shader need a triangle? Wait. Want: no.",
        frame_say="Memory: storage buffers vs textures. Map: replaces some FS ping-pong. Workgroup 8×8 is the lab size. Particle integrate extra if time — still in a buffer they draw.",
        frame_ask="Why workgroups?",
        build=[
            "**Say:** Grid of threads over the texture. id.xy is the texel.",
            "**Board:** dispatch + workgroup_size. Circle storage.",
            "**Say:** Blit to the canvas is a separate render pass — name both.",
        ],
        ask_build="What does dispatch(x,y,z) mean?",
        they_build="On paper: compute pass then render/blit pass.",
        show_say="Compute a gradient or noise into a texture; blit. Plant compute that still rasterizes a triangle per particle. Plant unbounded loop.",
        attempt_say="Workgroup 8×8, or particle integrate extra. Eight minutes.",
        land_say="Lab: 8×8 + integrate extra if time. Homework: workgroup paragraph; WGSL compute. Quiz: dispatch, storage, why not FS.",
        live=[
            ("0–10", "Name compute pass", "Plant triangle-per-particle."),
            ("10–30", "8×8 fill + blit", "Plant unbounded loop."),
            ("30–45", "Storage layout", "Draw the bytes."),
            ("45–60", "They dispatch", "Circulate. Feature detect."),
        ],
        cut="Shared-memory prefix sum. Keep dispatch + storage + blit.",
        add="Race/sync as a one-line warning.",
    )
    GOLD[(C, 11)] = dict(
        kernel="Particle struct in a storage buffer; compute update pass then render points",
        success="they can keep pos/vel on the GPU and write a WebGL fallback note — no 100k JS uploads",
        invariant="the buffer is the source of truth; Safari-old or a textured cube may stay WebGL",
        goal="two named passes, one struct layout",
        board="""```
struct P { pos: vec2f, vel: vec2f }   // draw stride

PASS 1  compute  update P
PASS 2  render   draw points

do not upload 100k pos from JS each frame
fallback: week-2 ping-pong  (README)
```""",
        slides=[],
        hook_say="Two passes: physics compute, then draw. Buffer sizes and workgroup limits named. Honesty: if the audience is old Safari, WebGL ping-pong is enough. Invented N is not a measurement.",
        hook_ask="Where is the source of truth — JS array, or the GPU buffer? Wait. Want: GPU buffer.",
        frame_say="dt uniform. WebGL fallback note is the attempt if compute is blocked. Feature detect from week 8.",
        frame_ask="When would you not use WebGPU?",
        build=[
            "**Say:** Struct bytes on the board: pos.xy vel.xy, alignment.",
            "**Board:** compute then draw. Circle no JS upload.",
            "**Say:** N is a constant they can count in the buffer — not a fantasy million.",
        ],
        ask_build="Write struct P.",
        they_build="On paper: stride of one particle in bytes (teaching: 16).",
        show_say="N particles in WGSL compute; draw as points. Plant 100k JS uploads. Plant no fallback story. dt uniform.",
        attempt_say="WebGL fallback note. Eight minutes.",
        land_say="Lab: fallback note + dt. Homework: when not WebGPU; demo. Quiz: source of truth, two passes, Safari.",
        live=[
            ("0–10", "Struct layout", "Plant JS upload each frame."),
            ("10–30", "Compute then draw", "Name both passes."),
            ("30–45", "dt uniform", "Pause."),
            ("45–60", "Fallback README", "Circulate. Detect."),
        ],
        cut="Indirect draw. Keep struct + two passes + fallback sentence.",
        add="Workgroup / buffer limits as names.",
    )
    GOLD[(C, 12)] = dict(
        kernel="decision table: feature → WebGL2 ping-pong or WebGPU compute; detect; pick one API for the final",
        success="they can feature-detect, screenshot support, and write a one-page memo without rewriting the semester in three APIs",
        invariant="IGWT is web; WebGL2 still ships; WebGPU is taught without stranding labs; no CUDA",
        goal="a decision you can freeze",
        board="""```
need              stay WebGL2           move WebGPU
particles teach   FBO ping-pong         storage + compute
atomics / reduce  mip hack              compute atomics
lab browsers      always                detect + fallback

project: pick ONE api unless you demo both
```""",
        slides=[],
        hook_say="Decision, not a rewrite. Porting shaders is work. Pipelines are verbose. Gain: compute, less driver magic. canIuse is a screenshot they take, not a CDN widget in the product.",
        hook_ask="Must the final be both APIs? Wait. Want: no — pick one unless you explicitly demo both.",
        frame_say="One-page decision for a capstone-shaped idea. Risk list. Still JS in the browser.",
        frame_ask="One reason to stay on WebGL?",
        build=[
            "**Say:** Table feature → API. Fill three rows live.",
            "**Board:** the decision tree. Circle detect.",
            "**Say:** Risk list: Safari, validation, time to port.",
        ],
        ask_build="One reason to move to WebGPU?",
        they_build="On paper: their project row in the table.",
        show_say="A one-page decision for their idea. Plant rewriting the semester in three APIs. Plant CUDA as a third column.",
        attempt_say="canIuse screenshot + risk list. Eight minutes.",
        land_say="Lab: screenshot + risks. Homework: decision memo 1 page. Quiz: one reason WebGL, one WebGPU, detect. Next: choose a sim.",
        live=[
            ("0–10", "Fill the table", "Plant three-API rewrite."),
            ("10–30", "Detect in a stub page", "Plant CUDA column."),
            ("30–45", "Risk list", "Safari / time."),
            ("45–60", "They freeze one API", "Circulate."),
        ],
        cut="Vulkan. Keep the table + detect + one API.",
        add="Shader rewrite cost as a bullet.",
    )
    GOLD[(C, 13)] = dict(
        kernel="choose ping-pong FS or WebGPU compute; freeze packing, dt, debug view of state",
        success="they can run a small sim with a packing diagram, stable dt, and no readback every frame",
        invariant="if they cannot draw the memory layout, they are running a sample",
        goal="one architecture, visible state",
        board="""```
state  →  update kernel  →  draw

pick:  FBO A/B   or   storage buffer + compute
debug: show state as color
cuts:  drop fluids; keep particles + dt cap
cite:  Stam / IQ / samples
```""",
        slides=[],
        hook_say="This week you choose. Quality: stable dt, debug view of the state tex or buffer, no readback. Fluids drop if behind. Cite. Feature detect if WebGPU.",
        hook_ask="If you cannot draw the layout, what are you running? Wait. Want: a sample.",
        frame_say="N slider only if safe — a counted N, not a fantasy. Screenshot the debug view. README: packing + API.",
        frame_ask="What do you cut first?",
        build=[
            "**Say:** State machine: state → update → draw.",
            "**Board:** two columns, ping-pong vs compute. They circle one.",
            "**Say:** Debug view is mandatory. Pause.",
        ],
        ask_build="Where does pos live in your pick?",
        they_build="On paper: packing diagram for their pick.",
        show_say="Working sim + debug view (theirs or a volunteer). Plant missing layout. Plant readPixels every frame.",
        attempt_say="Draw the packing; screenshot debug. Eight minutes.",
        land_say="Lab: N slider if safe + screenshot. Homework: packing + API; repo. No quiz. Next: project studio.",
        live=[
            ("0–10", "Circle one API", "Plant both unfinished."),
            ("10–30", "Packing on the board", "Plant missing debug view."),
            ("30–45", "Pause + dt cap", "No readback."),
            ("45–60", "They screenshot state", "Circulate."),
        ],
        cut="A new fluid solver. Keep one architecture + layout.",
        add="60s rehearsal of the packing diagram.",
    )
    GOLD[(C, 14)] = dict(
        kernel="GPGPU or WebGPU mini: packing diagram, dispatch or ping-pong, named device",
        success="a TA can serve the folder, see the layout, and run with feature detect or WebGL",
        invariant="WGSL triangle + compute gradient is a valid cut; CUDA is not a path",
        goal="studio — not a content lecture",
        kind="studio",
        board="""```
Must: packing diagram · pause · detect or WebGL · README serve
Cuts: fluids; full TF; million particles
Valid cut: WGSL triangle + compute gradient
Report: memory layout, dispatch, device
```""",
        slides=[],
        hook_say="This meeting is **studio**. Particles, life, blur chain, or compute noise. Desk review: packing diagram first.",
        hook_ask="If behind, what do you cut first?",
        frame_say="Desk review: layout, then detect, then dt cap, then citations.",
        show_say="Volunteer packing vs running demo. Plant CUDA as the story. Plant invented N.",
        attempt_say="Studio. Serve first.",
        land_say="Report: memory layout, dispatch, device. Next week 12+5.",
        live=[
            ("0–10", "Headings + cut list", "Photograph."),
            ("10–50", "Desk review", "Packing first."),
            ("50–60", "60s rehearsal", "Stop."),
        ],
        cut="New APIs. Keep freeze.",
        add="One 60-second rehearsal in front of another team.",
    )
    GOLD[(C, 15)] = dict(
        kernel="12+5; demo the layout; point at two textures or a struct",
        success="they stop at 12 and can say why two textures and why WebGPU or why they stayed on WebGL",
        invariant="no new features today; no CUDA-only story",
        goal="presentations — not a content lecture",
        kind="presentations",
        board="""```
12 + 5
Show: packing · pause · detect
Ask: why two textures?  why WebGPU (or why not)?
No new kernels on stage
```""",
        slides=[("Timer", "not a slide of WGSL")],
        hook_say="Presentations. 12+5. I will ask why two textures, and why WebGPU — or why you stayed on WebGL. Invented particle counts are not measurements.",
        show_say="None. Present.",
        attempt_say="Present.",
        land_say="If they can draw the memory layout, they programmed a GPU; if not, they ran a sample.",
        live=[("0–60", "Talks", "Cut at 12.")],
        cut="Debugging on stage.",
        add="One question on feature detect or readback.",
    )


# Keys this module registers: ("Shader Programming"|"Real-Time Rendering"|"GPU Programming", 1..15)
