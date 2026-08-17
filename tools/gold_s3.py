"""Full-script GOLD for WebGL Programming, Three.js Development, Blender (15 meetings each)."""


def register(GOLD: dict) -> None:
    _webgl(GOLD)
    _three(GOLD)
    _blender(GOLD)


def _webgl(GOLD: dict) -> None:
    C = "WebGL Programming"
    GOLD[(C, 1)] = dict(
        kernel="WebGL2 context; clip-space triangle; gl_Position is clip, not pixels",
        success="they get a red triangle from getContext('webgl2') with compile/link logs printed; they can say what gl_Position is",
        invariant="CPU fills buffers; GPU runs the shader; P*V*M; CCW",
        goal="a first triangle without Three.js",
        board="""```
CPU buffers → VS → raster → FS → framebuffer

gl_Position = clip (xyzw). GPU does the divide.
NDC after divide: xyz in [−1,1]

RH, Y-up, camera looks −Z
CCW front     column-major     P * V * M * vec4(p,1)

getContext('webgl2')   —  not Three.js
```""",
        slides=[],
        hook_say="If they cannot explain gl_Position, they are not allowed to hide in Three.js yet. Today is raw WebGL2. A black screen is a checklist, not a personality.",
        hook_ask="Is gl_Position in pixels? Wait seven seconds. Want: no — clip space; the GPU divides by w.",
        frame_say="Canvas, WebGL2 context, two shaders, one buffer, drawArrays TRIANGLES. Conventions freeze now: right-handed, Y-up, look −Z, CCW, column-major P*V*M. Week 1 triangle lives in clip with w=1 so it is already NDC. Matrices wait until week 7 — we still write the product on the board so the name exists.",
        frame_ask="Who fills the buffer — CPU or GPU?",
        build=[
            "**Say:** Pipeline every lecture: VBO → VS → raster → FS → FBO. Draw it. Three.js is next course.",
            "**Board:** gl_Position clip vs NDC vs pixels. Circle w. Do not divide in the VS.",
            "**Say:** Compile log and link log are different. Print both. Clear color you can see: 0.10, 0.10, 0.12.",
        ],
        ask_build="Why CCW? Want: OpenGL default front face.",
        they_build="On paper: pipeline boxes plus one line: gl_Position = vec4(a_position, 0, 1).",
        show_say="Typed triangle from WebGL/demos/01-triangle.html. Local _gl.js, no CDN. Plant getContext('webgl') then 'webgl2'. Plant a 0×0 canvas. Read the compile log out loud.",
        attempt_say="Clear color you can see, then the three clip verts. Eight minutes.",
        land_say="Photograph the board. Lab: visible clear + resize backing store. Homework: pipeline boxes; a triangle. Quiz: getContext webgl2, where logs, why not Three.js yet.",
        live=[
            ("0–10", "getContext('webgl2') + clear", "Plant webgl1 or Three.js. Fix: raw WebGL2."),
            ("10–30", "01-triangle.html typed", "Plant missing #version 300 es. Read the log."),
            ("30–45", "gl_Position on the board", "Plant pixels. Write clip → NDC."),
            ("45–60", "They type three verts", "Circulate. No CDN. Serve if file:// dies."),
        ],
        cut="P*V*M multiplication today. Keep clip triangle + logs.",
        add="Resize canvas backing store with devicePixelRatio named.",
    )
    GOLD[(C, 2)] = dict(
        kernel="ARRAY_BUFFER, vertexAttribPointer layout, ELEMENT_ARRAY_BUFFER",
        success="they can createBuffer, upload, enable the attrib, and draw an indexed quad",
        invariant="CPU arrays are dead until uploaded; layout is size/type/stride/offset",
        goal="layout you can debug",
        board="""```
bind ARRAY_BUFFER → bufferData → enableVertexAttribArray
vertexAttribPointer(loc, size, FLOAT, false, stride, offset)

stride 0  =  tightly packed
interleaved pos+color: stride 24, color offset 12

ELEMENT_ARRAY_BUFFER → drawElements
```""",
        slides=[],
        hook_say="Last time: a triangle that was already clip. Today the GPU must be told how bytes become a_position. A wrong stride is a Picasso, not a math bug.",
        hook_ask="What does stride 0 mean? Wait. Want: tightly packed; GPU infers from size*sizeof(type).",
        frame_say="createBuffer, bindBuffer, bufferData STATIC_DRAW. Location −1 means the name is unused or misspelled. Demo 02 colored triangle, 03 indexed quad.",
        frame_ask="Why enableVertexAttribArray?",
        build=[
            "**Say:** CPU Float32Array is not GPU memory until bufferData.",
            "**Board:** interleaved vs separate. Numbers: 3 floats pos + 3 color = 24 bytes.",
            "**Say:** Indexed quad: four verts, six indices. UNSIGNED_SHORT.",
        ],
        ask_build="bindBuffer — which target for indices?",
        they_build="On paper: pointer for interleaved pos+color. Two lines.",
        show_say="Interleaved pos+color from 02-colored-triangle.html then 03-indexed-quad.html. Plant never enabling the attrib. Plant WebGL1 attribute vs in mix.",
        attempt_say="Indexed quad. Then a wrong stride, then fix. Eight minutes.",
        land_say="Lab: indexed quad + stride bug. Homework: stride paragraph; indexed quad. Quiz: bindBuffer, stride 0, location −1.",
        live=[
            ("0–10", "createBuffer + bind", "Plant forgot bind."),
            ("10–30", "Interleaved pos+color; draw", "Plant stride 0 when data is interleaved."),
            ("30–45", "drawElements quad", "UNSIGNED_BYTE by accident."),
            ("45–60", "They index a quad", "Circulate."),
        ],
        cut="VAO theory dump. Keep pointer + indexed quad.",
        add="A wrong stride bug then fix, on purpose.",
    )
    GOLD[(C, 3)] = dict(
        kernel="#version 300 es first line; precision; in/out; outColor not gl_FragColor",
        success="they can break a shader, read the compile log, and ship a versioned VS/FS pair",
        invariant="the first line is the language; the log is the teacher",
        goal="GLSL ES 3.00 that compiles",
        board="""```
#version 300 es          ← first line, nothing before
precision highp float;
in  / out                not attribute / varying
out vec4 outColor;       not gl_FragColor
texture()                not texture2D

vec3  mat4  sampler2D
```""",
        slides=[],
        hook_say="A silent black screen is often a shader that did not compile. Today we make the log loud. WebGL1 vs 2 is a dialect, not a vibe.",
        hook_ask="Can #version 300 es sit on line 2 after a comment? Wait. Want: first line; even a blank can bite — freeze: first.",
        frame_say="in/out, layout(location=), outColor. precision highp float in FS. Types: vec3, mat4, sampler2D. Demo: break 01-triangle shaders.",
        frame_ask="Does WebGL2 have gl_FragColor?",
        build=[
            "**Say:** Language table on the board. WebGL1 names are banned in 300 es.",
            "**Board:** #version, precision, outColor.",
            "**Say:** Link error ≠ compile error. Check both.",
        ],
        ask_build="texture2D in 300 es — what happens?",
        they_build="On paper: the three first lines of a FS.",
        show_say="Break a shader; read the log; fix. Plant version after other lines. Plant texture2D. Plant gl_FragColor.",
        attempt_say="A second program that paints debug magenta. Eight minutes.",
        land_say="Lab: debug-color program + precision extra. Homework: WebGL1 vs 2 diffs; versioned pair. Quiz: first line, gl_FragColor?, precision.",
        live=[
            ("0–10", "#version first", "Plant it on line 2."),
            ("10–30", "Break / log / fix", "They must hear the log."),
            ("30–45", "outColor vs gl_FragColor", "Plant the old name."),
            ("45–60", "They write a second program", "Circulate."),
        ],
        cut="Every GLSL built-in. Keep version + logs.",
        add="precision extra on a second FS.",
    )
    GOLD[(C, 4)] = dict(
        kernel="uniforms: mat4, u_time, colors; getUniformLocation once",
        success="they spin a cube with u_time and can say uniform vs attribute",
        invariant="a uniform is constant for one draw; column-major matches kernel.js",
        goal="CPU values that reach the shader",
        board="""```
attribute  =  per vertex     (buffer)
uniform    =  per draw       (CPU sets)

gl.uniformMatrix4fv(loc, false, m);   // false = already column-major

u_time   u_color
location null → name unused or typo
```""",
        slides=[],
        hook_say="Last week the color was baked in the shader. Today the CPU talks. PVM is still a name — we rotate in the shader with u_time. Demo 04-rotating-cube.html.",
        hook_ask="Do you call getUniformLocation inside the fragment? Wait. Want: once after link, cache it.",
        frame_say="false in uniformMatrix4fv means the array is already column-major. Row-major by accident transposes the world. Missing name → location null, silent no-op.",
        frame_ask="Uniform vs attribute in one sentence?",
        build=[
            "**Say:** Constants for a draw. Change M next week per object; today one object.",
            "**Board:** u_time slider. CPU/GPU arrow.",
            "**Say:** Do not getUniformLocation every pixel. Cache.",
        ],
        ask_build="What does false mean in uniformMatrix4fv?",
        they_build="On paper: two uniforms you would set for a tinted spinner.",
        show_say="Spin with u_time; then a color uniform. Demo 04-rotating-cube.html. Plant row-major. Plant querying location in the rAF hot path.",
        attempt_say="Pause time with a flag. Eight minutes.",
        land_say="Lab: pause time; two objects different uniforms extra. Homework: uniform vs attribute; time. Quiz: vs attribute, column-major, missing name.",
        live=[
            ("0–10", "u_color uniform", "Plant forgot useProgram before set."),
            ("10–30", "u_time spin", "Plant row-major mat4."),
            ("30–45", "Cache locations", "Plant getUniformLocation in draw."),
            ("45–60", "They pause time", "Circulate."),
        ],
        cut="Full PVM today. Keep time + color + column-major.",
        add="Two objects, different color uniforms.",
    )
    GOLD[(C, 5)] = dict(
        kernel="indexed cube, DEPTH_TEST, CULL_FACE, CCW front",
        success="they enable depth, clear depth, and can toggle cull to see winding",
        invariant="hidden surfaces are a GPU test; winding is CCW; near is not 0",
        goal="a cube that is not painter-sorted by luck",
        board="""```
gl.enable(DEPTH_TEST)
gl.enable(CULL_FACE)     CCW front     cull BACK

clear COLOR | DEPTH      (forgot depth → flicker)

near 0.1   far 100       near=0 is illegal / fighting
```""",
        slides=[],
        hook_say="CG I z-buffer is now a GPU bit. Without depth a cube is a scribble. Winding: if it is inside-out, you mirrored scale or reversed CCW — not 'WebGL is broken.'",
        hook_ask="Do you need to clear depth every frame? Wait. Want: yes, COLOR | DEPTH.",
        frame_say="Indexed cube: 24 unique verts with normals later, or 8 verts if you accept shared normals. Today indices + depth. Demo 04-rotating-cube.html. Conventions: CCW.",
        frame_ask="What does CULL_FACE remove?",
        build=[
            "**Say:** Same as CG I hidden surfaces. Now enable the test.",
            "**Board:** DEPTH_TEST, clear mask, CCW.",
            "**Say:** Toggle depth off — painter bugs. Toggle cull — missing faces.",
        ],
        ask_build="Why is near=0 a problem?",
        they_build="On paper: the two enable lines plus the clear mask.",
        show_say="Cube with depth; toggle depth to show painter bugs. Plant no depth clear. Plant near=0.",
        attempt_say="cull toggle. See which faces vanish. Eight minutes.",
        land_say="Lab: cull toggle; wireframe extra. Homework: GPU depth vs CPU z-buffer; cube. Quiz: DEPTH_TEST, CCW, clear depth.",
        live=[
            ("0–10", "Indexed cube no depth", "It looks 'ok' from one angle. Plant."),
            ("10–30", "enable DEPTH_TEST + clear", "Plant forgot DEPTH bit."),
            ("30–45", "CULL_FACE CCW", "Plant CW verts. Inside-out."),
            ("45–60", "They toggle cull", "Circulate."),
        ],
        cut="Normal matrix. Keep cube + depth + cull.",
        add="Wireframe extra (LINES or barycentric name).",
    )
    GOLD[(C, 6)] = dict(
        kernel="texImage2D upload, UV, NEAREST vs LINEAR; uv as color debug",
        success="they sample a local image after onload and can debug UV as color",
        invariant="sampling before upload is black; UV is the map, not the mesh",
        goal="a textured quad you can debug",
        board="""```
img.onload → texImage2D → generateMipmap (named)
outColor = texture(u_tex, v_uv);

DEBUG: outColor = vec4(v_uv, 0, 1);

NEAREST vs LINEAR     REPEAT vs CLAMP_TO_EDGE
UNPACK_FLIP_Y_WEBGL
```""",
        slides=[],
        hook_say="A missing texture is an async bug until you prove UV. uv as color is the flashlight. Local file, no CDN. Demos 05-canvas-texture.html and 08-uv-debug.html.",
        hook_ask="If the quad is black, is it the shader or onload? Wait. Want: often onload — sampling before upload.",
        frame_say="Upload from Image or canvas. Premultiply named. Filtering: NEAREST vs LINEAR; mips named. flipY surprises PNG vs WebGL.",
        frame_ask="What does UV (0,0) mean on the image?",
        build=[
            "**Say:** Async. Draw a placeholder color until the texture is ready.",
            "**Board:** uv as color. Then texture().",
            "**Say:** wrap REPEAT vs CLAMP. One axis at a time.",
        ],
        ask_build="Why not fetch a texture from a CDN in this program?",
        they_build="On paper: the onload → texImage2D sequence.",
        show_say="Textured quad then cube. Plant sampling before upload. Plant wrong flipY. Demo 05-canvas-texture.html, 08-uv-debug.html.",
        attempt_say="uv debug as color, then sample. Eight minutes.",
        land_say="Lab: uv debug; wrap repeat vs clamp. Homework: flipY; sample. Quiz: texImage2D, uv debug, NEAREST.",
        live=[
            ("0–10", "Create texture + bind", "Plant TEXTURE0 vs uniform 1."),
            ("10–30", "Canvas texture 05", "Plant draw before onload."),
            ("30–45", "uv as color 08", "They see stretch."),
            ("45–60", "They sample", "Circulate. Local only."),
        ],
        cut="sRGB framebuffer details. Keep upload + uv debug.",
        add="wrap REPEAT vs CLAMP on one axis.",
    )
    GOLD[(C, 7)] = dict(
        kernel="gl_Position = P * V * M * vec4(pos,1); lookAt + perspective in JS",
        success="they upload P, V, M as column-major uniforms and orbit a cube without Three.js camera",
        invariant="clip is after P; view looks −Z; do not invert the product order",
        goal="the camera is three matrices",
        board="""```
object → world(M) → view(V) → clip(P) → NDC → pixels

gl_Position = u_p * u_v * u_m * vec4(a_pos, 1.0);

RH Y-up   look −Z   CCW   column-major
fov in radians     near 0.1
```""",
        slides=[("Optional: CG I lookAt diagram photograph", "photo, not a Three.js screenshot")],
        hook_say="Same math as Computer Graphics I weeks 7–9. Three.js later will hide these as camera.projectionMatrix and matrixWorldInverse. Today you write them. Demo 07-orbit-camera.html.",
        hook_ask="Is the product M*V*P or P*V*M for column vectors on the right? Wait. Want: P*V*M.",
        frame_say="lookAt + perspective from a JS mat4. Freeze: no THREE.PerspectiveCamera in the lab. Row-major P is the classic 'my cube vanished.'",
        frame_ask="What space is gl_Position?",
        build=[
            "**Say:** Spaces table from WebGL/01 Conventions. Circle clip.",
            "**Board:** the one GLSL line. Names u_p u_v u_m.",
            "**Say:** Orbit: move eye on a circle, lookAt origin. WASD is extra.",
        ],
        ask_build="Does the VS divide by w?",
        they_build="On paper: product order and what each matrix does.",
        show_say="lookAt + perspective; spin the cube. Demo 07-orbit-camera.html. Plant Three.js camera. Plant row-major P. Plant fov in degrees without conversion.",
        attempt_say="Orbit, or WASD extra if orbit already works. Eight minutes.",
        land_say="Lab: WASD extra; ortho toggle. Homework: CPU→uniform mapping table; orbit. Quiz: product order, lookAt, fov radians. Midterm next week on 1–7.",
        live=[
            ("0–10", "Identity PVM — clip cube", "They see last week's object."),
            ("10–30", "perspective + lookAt", "Plant degrees. Cube gone."),
            ("30–45", "Orbit mouse/drag", "Plant inverted V."),
            ("45–60", "They orbit", "Circulate. No Three.js."),
        ],
        cut="WASD full controller. Keep P*V*M + orbit.",
        add="Ortho toggle vs perspective.",
    )
    GOLD[(C, 8)] = dict(
        kernel="midterm; then Lambert in the fragment: n·l",
        success="after the exam they can pass a normal and shade Lambert without a specular term",
        invariant="lighting is a dot product after you normalize; n as color is the debug",
        goal="midterm, then diffuse",
        kind="midterm",
        midterm_topics="pipeline boxes; buffer layout/stride; #version 300 es; uniform vs attribute; DEPTH_TEST/CCW; texImage2D/UV debug; gl_Position = P*V*M and clip vs NDC.",
        board="""```
N, L normalized     L toward the light
ndotl = max(dot(N, L), 0.0)
color = albedo * (ambient + lightColor * ndotl)

DEBUG: outColor = vec4(N*0.5+0.5, 1);
```""",
        slides=[],
        hook_say="This meeting is a **midterm**, then Lambert in the FS. No laptop for the exam. After: CG I Lambert, now per fragment. Demo 06-phong-cube.html with spec off.",
        show_say="Lambert cube; light vector uniform. Plant unnormalized n. Plant lighting in the VS only and calling it per-pixel.",
        attempt_say="n as color debug. Then Lambert.",
        land_say="Lab: n as color; two-sided extra. Homework: VS vs FS lighting; reflection name. No quiz this week.",
        live=[
            ("0–15", "Pass normals as varying", "Plant not normalizing after interp."),
            ("15–40", "Lambert n·l", "Plant L away from the light."),
            ("40–60", "n as color", "They type. Circulate."),
        ],
        cut="Phong specular today. Keep Lambert + n-debug.",
        add="Two-sided extra: abs(dot) named, then why we usually don't.",
    )
    GOLD[(C, 9)] = dict(
        kernel="Blinn-Phong: H = normalize(L+V); normalize n in FS; gamma once",
        success="they can write the half vector, a shininess slider, and pow(c, 1/2.2) at the end only",
        invariant="interpolate then normalize; gamma twice is a bug; PBR is a later course",
        goal="a highlight you can explain",
        board="""```
H = normalize(L + V)
spec = pow(max(dot(N, H), 0), shininess)

gamma: pow(c, vec3(1.0/2.2))   once, at the end
normalize(v_n) in FS   (interpolation denormalizes)
```""",
        slides=[],
        hook_say="Same as CG I week 11, now GLSL. Phong reflect vs Blinn half vector — we prefer Blinn in class. Demo 06-phong-cube.html.",
        hook_ask="Why normalize n in the fragment if the VS already did? Wait. Want: interpolation.",
        frame_say="Varyings. Shininess 8–128. Gate spec with ndotl so the back face is dark. Gamma: linear lighting, encode at the end. Not twice. PBR name only — quiz trap.",
        frame_ask="H vs R — which is Blinn?",
        build=[
            "**Say:** Half vector on the board. Same N, L, V spaces.",
            "**Board:** H line + gamma once.",
            "**Say:** Two lights extra is add; energy not conserved — name it.",
        ],
        ask_build="Where does gamma live — VS, FS start, or FS end?",
        they_build="On paper: the H line and the spec pow.",
        show_say="Blinn cube; shininess slider. Plant gamma twice. Plant n not normalized. Demo 06-phong-cube.html.",
        attempt_say="gamma toggle. See the midtones. Eight minutes.",
        land_say="Lab: gamma toggle; two lights extra. Homework: why normalize n in FS; blinn. Quiz: half vector, gamma where, PBR? (name only).",
        live=[
            ("0–10", "Lambert still there", "Do not delete diffuse."),
            ("10–30", "H + shininess", "Plant Phong R if you want the contrast."),
            ("30–45", "gamma once", "Plant pow on inputs and output."),
            ("45–60", "They toggle gamma", "Circulate."),
        ],
        cut="Image-based lighting. Keep Blinn + gamma once.",
        add="Second light, additive.",
    )
    GOLD[(C, 10)] = dict(
        kernel="scene loop: for each mesh bind, set M, draw; one program",
        success="they draw three cubes with different M from one program and a mesh record",
        invariant="a Mesh is a draw call; compiling per cube is the anti-pattern Three.js will hide",
        goal="many objects, one pipeline",
        board="""```
for (const o of objects) {
  bind VAO
  uniform u_m = o.matrix     // world
  drawElements
}

ONE program     many M
parent:  M_child = M_parent * M_local
```""",
        slides=[],
        hook_say="Three.js Object3D is this loop with more. If they compile a program per cube they will not understand instancing next. Naive loop this week; demo 14 is next week.",
        hook_ask="What changes per object — the program or M? Wait. Want: M (and maybe material uniforms), not a new program.",
        frame_say="Mesh record: {vao, count, matrix}. Shared geometry: same vao, different M. State leaks: leftover binds. Parenting: multiply local onto parent.",
        frame_ask="Is a VAO per mesh or per layout?",
        build=[
            "**Say:** CPU loop. Bind, uniform, draw.",
            "**Board:** the for-each. Circle u_m.",
            "**Say:** Shared geometry for three cubes. New program per cube is the plant.",
        ],
        ask_build="Why one program?",
        they_build="On paper: fields of a mesh record.",
        show_say="Three cubes different M. Plant new program per cube. Plant leaking ELEMENT_ARRAY binds.",
        attempt_say="Parent a second cube (local offset). Eight minutes.",
        land_say="Lab: parented cube; shared geometry. Homework: why one program; loop. Quiz: what changes per object, compile per mesh?, VAO name.",
        live=[
            ("0–10", "Mesh record", "They copy fields."),
            ("10–30", "Three cubes", "Plant compile in the loop."),
            ("30–45", "Parent multiply", "Forgot update order."),
            ("45–60", "They parent", "Circulate."),
        ],
        cut="Instancing. Keep the naive loop.",
        add="Shared geometry, two materials via uniforms.",
    )
    GOLD[(C, 11)] = dict(
        kernel="FBO: render to texture, then a fullscreen second pass",
        success="they createFramebuffer, check COMPLETE, unbind to the canvas, and blit via a quad",
        invariant="the default framebuffer is the canvas; forget unbind and you draw into the texture forever",
        goal="offscreen, then on screen",
        board="""```
createTexture + renderbuffer(depth)
createFramebuffer → COLOR_ATTACHMENT0
check FRAMEBUFFER_COMPLETE
draw scene → tex
bindFramebuffer(null) → draw quad sampling tex

FBO size ≠ canvas size   (often)
```""",
        slides=[],
        hook_say="Post and GPGPU start here. Demo 13-framebuffer-post.html: cube to FBO, vignette on a fullscreen triangle. This is what EffectComposer hides next course.",
        hook_ask="After drawing to the FBO, where do you bind before the screen pass? Wait. Want: null / the canvas.",
        frame_say="Depth renderbuffer if 3D goes into the FBO. Incomplete FBO is a status, not a JS throw. Size: FBO can be smaller than the canvas.",
        frame_ask="Why might FRAMEBUFFER_COMPLETE fail?",
        build=[
            "**Say:** Offscreen color tex. Second program samples it.",
            "**Board:** two passes. Unbind.",
            "**Say:** Identity post shader is the debug. Invert extra.",
        ],
        ask_build="Do you need depth on a fullscreen post quad?",
        they_build="On paper: the bind sequence for pass 1 and pass 2.",
        show_say="Draw cube to FBO; display as a quad. Demo 13-framebuffer-post.html. Plant forgetting to unbind. Plant 3D into FBO with no depth.",
        attempt_say="Incomplete FBO debug: log the status. Then invert extra. Eight minutes.",
        land_say="Lab: incomplete debug; invert extra. Homework: why FBO; one offscreen pass. Quiz: COMPLETE, unbind, post.",
        live=[
            ("0–10", "Create FBO + tex", "Plant no COMPLETE check."),
            ("10–30", "Scene into FBO", "Plant no depth RB."),
            ("30–45", "Unbind + quad", "Plant still bound to FBO."),
            ("45–60", "They invert", "Circulate."),
        ],
        cut="Ping-pong GPGPU. Keep one offscreen pass.",
        add="Second-pass invert extra.",
    )
    GOLD[(C, 12)] = dict(
        kernel="vertexAttribDivisor(1); drawArraysInstanced — one draw, many M",
        success="they instance 100 cubes, color per instance, and compare to 100 draw calls by measuring on this machine",
        invariant="divisor 1 means the attrib advances per instance; do not invent fps",
        goal="one draw for a forest",
        board="""```
per-vertex attrib     divisor 0
per-instance attrib   divisor 1

gl.vertexAttribDivisor(loc, 1)
gl.drawArraysInstanced(..., instanceCount)

measure 100 draws vs 1   (this machine; no invented fps)
```""",
        slides=[],
        hook_say="Week 10 was a CPU loop. Today the GPU repeats. Forest, particles, bolts. Demo 14-instancing.html. If they do not measure, instancing is a religion.",
        hook_ask="Does divisor go on the position attrib of the cube? Wait. Want: no — on the instance offset/color.",
        frame_say="Still upload the instance buffer when it changes. Attribute slot limits named. n=3 on a quiz is 'three instances.'",
        frame_ask="When does instancing lose to a loop of three unique meshes?",
        build=[
            "**Say:** Same geometry, different instance attribs.",
            "**Board:** divisor 0 vs 1. drawInstanced.",
            "**Say:** Color per instance as the lab kernel.",
        ],
        ask_build="What does instanceCount mean in drawArraysInstanced?",
        they_build="On paper: which attribs get divisor 1.",
        show_say="100 cubes instanced vs 100 draw calls — log times or info, no invented fps. Demo 14-instancing.html. Plant divisor on the wrong attrib.",
        attempt_say="Color per instance. Eight minutes.",
        land_say="Lab: color per instance; measured table. Homework: when instancing wins; instanced. Quiz: divisor, drawInstanced, n=3.",
        live=[
            ("0–10", "Instance buffer of offsets", "Plant STATIC then never update."),
            ("10–30", "divisor 1 + instanced draw", "Plant divisor on a_pos."),
            ("30–45", "Measure loop vs instance", "No invented fps."),
            ("45–60", "They color instances", "Circulate."),
        ],
        cut="Indirect draw. Keep divisor + one draw + measure.",
        add="Measured table: loop vs instanced on this GPU.",
    )
    GOLD[(C, 13)] = dict(
        kernel="black-screen 10-point checklist; a 40-line renderer, not Engine.js",
        success="they can walk the checklist on a black screen and map Mesh → program/VAO/M/draw",
        invariant="abstraction after a cube; a 500-line engine with no cube is failure",
        goal="debug, then a mini engine",
        board="""```
1 canvas size   2 compile+link   3 camera looks
4 near plane    5 winding/cull   6 depth
7 attribs       8 texture ready  9 clear   10 uniforms

debug: n as color · uv as color · depth gray

Mesh → bind program, VAO, u_p u_v u_m, draw
```""",
        slides=[],
        hook_say="The 10-point list in WebGL/01 Conventions is the course. Mini engine: program, mesh, camera, light. Next course is Three.js — homework is a name map, not a rewrite.",
        hook_ask="Name one black-screen cause. Wait. Take three.",
        frame_say="Debug key modes: 1 n, 2 uv, 3 depth. README how to serve. Do not start the Three.js project tonight.",
        frame_ask="Three.js Mesh is which WebGL objects?",
        build=[
            "**Say:** Walk the checklist on a planted black screen.",
            "**Board:** ten items. Then Mesh → draw.",
            "**Say:** 40-line renderer drawing two meshes. Not 500 lines.",
        ],
        ask_build="Why is texture async on the checklist?",
        they_build="On paper: the ten items from memory.",
        show_say="A 40-line renderer, two meshes. Plant a 500-line Engine.js sketch. Plant 0×0 canvas. Read logs.",
        attempt_say="Debug-mode keys. README. Eight minutes.",
        land_say="Lab: debug keys; README. Homework: name map to Three.js; mini engine. Quiz: one black-screen cause, debug n, Mesh is?. Studio next.",
        live=[
            ("0–10", "Plant black screen", "Walk 1–10 out loud."),
            ("10–30", "40-line two meshes", "Keep it tiny."),
            ("30–45", "Debug n/uv/depth keys", "They toggle."),
            ("45–60", "They write README serve", "Circulate. No CDN."),
        ],
        cut="Full scene-graph editor. Keep checklist + 40 lines.",
        add="README: python -m http.server in WebGL/demos.",
    )
    GOLD[(C, 14)] = dict(
        kernel="mini WebGL engine: cube + orbit + Lambert + texture; README serves",
        success="a TA can serve the folder and see P*V*M in a shader without Three.js",
        invariant="freeze; drop FBO; tests are 'does it draw and can they name gl_Position'",
        goal="studio — not a content lecture",
        kind="studio",
        board="""```
Must: WebGL2 · P*V*M · CCW cube · Lambert · one texture
Cuts: drop FBO / instancing; keep orbit + logs
README: python -m http.server    no CDN    no Three.js
```""",
        slides=[],
        hook_say="This meeting is **studio**. Mini engine. Not a Three.js port.",
        hook_ask="If behind, what do you cut first? Want: FBO and instancing.",
        frame_say="Desk review: shaders and PVM first. Compile logs. Then texture onload. Report: pipeline figure, uniforms table.",
        show_say="Volunteer review against the board. Point at gl_Position.",
        attempt_say="Studio. Serve first.",
        land_say="Report + repo. Next week 12+5. They must answer gl_Position and depth.",
        live=[
            ("0–10", "Headings: pipeline, uniforms", "Photograph."),
            ("10–50", "Desk review", "Serve + logs + PVM."),
            ("50–60", "60s rehearsal", "Stop."),
        ],
        cut="New features. Keep freeze.",
        add="One 60-second rehearsal of the two oral questions.",
    )
    GOLD[(C, 15)] = dict(
        kernel="12+5; demo runs; gl_Position and depth",
        success="they stop at 12 and can point at gl_Position and DEPTH_TEST",
        invariant="no new features today",
        goal="presentations — not a content lecture",
        kind="presentations",
        board="""```
12 + 5
Show: gl_Position · depth · one uniform table
No Three.js on stage as a rewrite
```""",
        slides=[("Timer", "not a slide of GLSL")],
        hook_say="Presentations. 12+5. Repo. Stop at 12. I will ask where gl_Position is and how depth is enabled.",
        show_say="None. Present.",
        attempt_say="Present.",
        land_say="That habit — name the GPU object — is Three.js Development next.",
        live=[("0–60", "Talks", "Cut at 12.")],
        cut="Debugging on stage.",
        add="One question on winding/CCW.",
    )


def _three(GOLD: dict) -> None:
    C = "Three.js Development"
    GOLD[(C, 1)] = dict(
        kernel="Scene, PerspectiveCamera, WebGLRenderer; Mesh is a draw call",
        success="they boot 01-hello-cube.html from ThreeJS/vendor/three.module.js and can map Mesh to program+VAO+draw",
        invariant="Three.js is an engine, not the algorithm",
        goal="the three objects, mapped to WebGL",
        board="""```
Scene     = graph of Object3D
Camera    = P and V     (projectionMatrix, matrixWorldInverse)
Renderer  = clear, bind programs, draw

Mesh(geometry, material)  →  one draw call
(WebGL: VAO + program + uniforms + drawArrays/elements)

import from '../vendor/three.module.js'    no CDN
```""",
        slides=[],
        hook_say="You already wrote gl_Position = P*V*M. Today the engine hides it. If they cannot map Mesh to a draw call, they are using a magic box. Local vendor only — ThreeJS/vendor/three.module.js. Serve the ThreeJS/ folder.",
        hook_ask="What WebGL call is renderer.render? Wait. Want: clear, bind program, set uniforms, draw — for each mesh.",
        frame_say="Demo 01-hello-cube.html. Standard material needs a light. Resize: setSize false, aspect, updateProjectionMatrix. pixelRatio capped at 2. outputColorSpace SRGBColorSpace.",
        frame_ask="Why did we do WebGL first?",
        build=[
            "**Say:** Three boxes: scene, camera, renderer. Mesh is not the GPU.",
            "**Board:** mapping table from ThreeJS/01 Scene Camera Renderer.",
            "**Say:** import map to vendor/. file:// will fail — python -m http.server.",
        ],
        ask_build="What is camera.projectionMatrix in the shader you wrote?",
        they_build="On paper: Scene / Camera / Renderer / Mesh → GL names.",
        show_say="Cube from 01-hello-cube.html, then orbit from 02-orbit.html. Plant CDN script tag. Plant unbounded pixelRatio. Plant no light on Standard.",
        attempt_say="resize handler + updateProjectionMatrix. Eight minutes.",
        land_say="Lab: resize; color background. Homework: Scene vs WebGL program; cube. Quiz: three objects, domElement, why WebGL first.",
        live=[
            ("0–10", "import vendor three.module.js", "Plant CDN. Delete it."),
            ("10–30", "01-hello-cube", "Plant Standard without light."),
            ("30–45", "resize + aspect", "Plant forgot updateProjectionMatrix."),
            ("45–60", "They resize", "Circulate. Serve ThreeJS/."),
        ],
        cut="OrbitControls internals. Keep three objects + Mesh→draw.",
        add="scene.background color.",
    )
    GOLD[(C, 2)] = dict(
        kernel="Object3D: position, quaternion/euler, scale; parent.add(child); matrixWorld is M",
        success="they parent a cube, spin the parent, and can say matrixWorld is the model matrix",
        invariant="the graph multiplies M; scale −1 is a winding bug unless you mean it",
        goal="a tree of transforms",
        board="""```
local  position  rotation  scale
world  matrixWorld  =  parent.matrixWorld * local

parent.add(child)
AxesHelper     Euler.order     gimbal named

scale −1 'to flip'  →  winding / normals talk
```""",
        slides=[],
        hook_say="CG I scene graph with a nicer API. Demo 06-solar-system.html. matrixWorld is the M they uploaded last semester.",
        hook_ask="If the parent spins, does the child's position vector in local space change? Wait. Want: no — world does.",
        frame_say="Euler order property. Quaternion under the hood. lookAt extra. Units: 1 = 1 meter if the Blender course did its job.",
        frame_ask="What is matrixWorld in WebGL?",
        build=[
            "**Say:** Graph. Local vs world.",
            "**Board:** matrixWorld product. AxesHelper.",
            "**Say:** Plant scale −1. Faces invert. CCW from WebGL still applies.",
        ],
        ask_build="Why AxesHelper this week?",
        they_build="On paper: parent/child boxes and one product.",
        show_say="Parent a cube to another; spin parent. Demo 06-solar-system.html. Plant scale −1 to flip.",
        attempt_say="AxesHelper on parent and child. Eight minutes.",
        land_say="Lab: axesHelper; lookAt extra. Homework: matrixWorld is M; parent. Quiz: position units, matrixWorld, euler order.",
        live=[
            ("0–10", "position.set meters", "Plant 100-unit cube."),
            ("10–30", "parent.add + spin", "They see the orbit."),
            ("30–45", "scale −1 plant", "Winding talk."),
            ("45–60", "They add AxesHelper", "Circulate."),
        ],
        cut="Full quaternion SLERP lecture. Keep graph + matrixWorld.",
        add="lookAt extra on a child.",
    )
    GOLD[(C, 3)] = dict(
        kernel="BoxGeometry / Sphere / Plane; MeshBasicMaterial vs MeshStandardMaterial",
        success="they can say Basic is unlit, Standard needs lights, and dispose geometry they recreate in a loop",
        invariant="geometry is the VBO; material is the program + uniforms; leaking geo is a VRAM leak",
        goal="three meshes, two lighting models",
        board="""```
Geometry  →  attributes (position, normal, uv)
Material  →  program + uniforms
Mesh      →  draw call

Basic     unlit / debug
Standard  PBR-ish  (needs light + later env)

geo.dispose()  if you replace it in a loop
```""",
        slides=[],
        hook_say="Last week the cube was a Mesh. Today we split geometry and material. Demo 04-materials.html. ShaderMaterial is the shader course — name only.",
        hook_ask="Why is a Standard cube black? Wait. Want: no light (or metal+no env, later).",
        frame_say="Share one BoxGeometry across meshes. Wireframe toggle. Standard metalness/roughness knobs. Do not leak new BoxGeometry every frame.",
        frame_ask="Is Standard physically correct PBR?",
        build=[
            "**Say:** Basic = unlit debug. Standard = lit.",
            "**Board:** three meshes, three materials.",
            "**Say:** dispose. Custom ShaderMaterial parked.",
        ],
        ask_build="What GPU object is Geometry?",
        they_build="On paper: Basic vs Standard one sentence each.",
        show_say="Three meshes, three materials. Demo 04-materials.html. Plant new Geometry in rAF. Plant Standard with no light.",
        attempt_say="wireframe toggle. Eight minutes.",
        land_say="Lab: wireframe; shared geometry. Homework: Basic vs Standard; trio. Quiz: unlit material, dispose, Standard is PBR?.",
        live=[
            ("0–10", "Box Sphere Plane", "Same scene."),
            ("10–30", "Basic vs Standard", "Plant no light."),
            ("30–45", "dispose plant", "Loop leak."),
            ("45–60", "They share geometry", "Circulate."),
        ],
        cut="ShaderMaterial. Keep Basic vs Standard.",
        add="Shared geometry, two materials.",
    )
    GOLD[(C, 4)] = dict(
        kernel="Ambient + Directional + Point named; shadowMap.enabled; castShadow / receiveShadow",
        success="they light a cube on a plane, toggle a shadow, and do not spawn ten point lights",
        invariant="a light is uniforms plus optional shadow FBO; acne is bias, not 'broken PBR'",
        goal="one key light, then a shadow you can see",
        board="""```
Ambient     =  cheap fill (no direction)
Directional =  sun     Point = omni     Spot named

renderer.shadowMap.enabled = true
mesh.castShadow / plane.receiveShadow
light.castShadow = true
mapSize 512 vs 2048   (measure; not 8192)
```""",
        slides=[],
        hook_say="Energy: too many lights is a later clustered topic. Demo 03-lights-shadows.html. Shadow mapping internals live in Real-Time Rendering — here we enable and see acne.",
        hook_ask="Does AmbientLight cast a shadow? Wait. Want: no.",
        frame_say="Helpers: DirectionalLightHelper. mapSize 8192 on integrated GPU is a freeze violation. Contact-shadow demo 20 is later.",
        frame_ask="What WebGL object is a shadow map?",
        build=[
            "**Say:** Three types. One key directional.",
            "**Board:** enable shadowMap + flags.",
            "**Say:** Acne name. Bias next week deeper.",
        ],
        ask_build="Why a ground plane this week?",
        they_build="On paper: flags needed for a cube to shadow a plane.",
        show_say="Lit cube + plane; toggle shadow. Demo 03-lights-shadows.html. Plant 10 point lights. Plant mapSize 8192.",
        attempt_say="Light helper on. Eight minutes.",
        land_say="Lab: helper; mapSize 512 vs 2048 extra measure. Homework: acne; shadows. Quiz: castShadow, ambient purpose, mapSize.",
        live=[
            ("0–10", "Hemisphere or ambient + dir", "Plant only ambient."),
            ("10–30", "shadowMap + flags", "Plant forgot receiveShadow."),
            ("30–45", "mapSize measure", "No invented fps."),
            ("45–60", "They add helper", "Circulate."),
        ],
        cut="PCFSoft internals. Keep enable + one shadow.",
        add="mapSize 512 vs 2048 measured on this machine.",
    )
    GOLD[(C, 5)] = dict(
        kernel="Clock.getDelta(); mixer is a name for glTF clips later",
        success="they rotate with dt, can pause, and do not write rotation = t on a variable refresh display",
        invariant="time is dt; AnimationMixer is clips, not the rAF loop",
        goal="motion that does not depend on fps",
        board="""```
const dt = clock.getDelta();
mesh.rotation.y += speed * dt;

pause: skip the integrate, still render

AnimationMixer   (name)  —  glTF clips week 6
GSAP can tween Object3D; still one rAF
```""",
        slides=[],
        hook_say="Same as Interactive Web: rAF is the clock. rotation = elapsed without dt lies on 30 Hz vs 144 Hz. We do not invent fps — we integrate dt.",
        hook_ask="If the tab throttles, does rotation += 0.01 still mean the same angle per second? Wait. Want: no.",
        frame_say="Clock. Mixer named so week 6 has a word. GSAP optional name; still one rAF. Pause is a boolean around the integrate.",
        frame_ask="Mixer vs rAF rotate — which plays a glTF clip?",
        build=[
            "**Say:** dt from getDelta. Speed in rad/s.",
            "**Board:** pause still renders.",
            "**Say:** Bounce with sin(time) is ok if time is accumulated dt.",
        ],
        ask_build="What does getDelta return the first frame?",
        they_build="On paper: the integrate line with dt.",
        show_say="Spin + bounce with dt. Plant rotation = t. Demo 01 or 06. No fps brag.",
        attempt_say="Pause flag. Eight minutes.",
        land_say="Lab: pause; mixer extra if a clip exists. Homework: mixer vs rAF; dt. Quiz: getDelta, mixer, pause.",
        live=[
            ("0–10", "Clock.getDelta", "Plant Date.now()/16."),
            ("10–30", "spin with dt", "Plant += 0.01."),
            ("30–45", "pause", "Still render."),
            ("45–60", "They pause", "Circulate."),
        ],
        cut="GSAP timeline. Keep dt + pause.",
        add="mixer extra only if a clip is already in the scene.",
    )
    GOLD[(C, 6)] = dict(
        kernel="GLTFLoader from vendor/jsm; traverse for shadows; scale; DRACO as a name",
        success="they load a local glb (or the 10-gltf-pattern stand-in), traverse castShadow, and show an error UI on failure",
        invariant="gltf.scene is a Group; load once, not in rAF; no Sketchfab hotlink without credit",
        goal="a model that is a graph",
        board="""```
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js'
// addons → ThreeJS/vendor/jsm/     no CDN

loader.load('m.glb', (g) => scene.add(g.scene))
traverse: if (o.isMesh) o.castShadow = true
Box3.setFromObject → center / scale

DRACO   (name)   file:// fails → serve
```""",
        slides=[],
        hook_say="Blender exports this. Demo 10-gltf-pattern.html uses local vendor. If the glTF viewer is wrong, the engine is not the bug — that sentence is the Blender course; today we still check scale.",
        hook_ask="Do you loader.load inside the animation loop? Wait. Want: no.",
        frame_say="Loading manager + placeholder cube. Error UI. DRACO name, not a lab install. License on any third-party glb.",
        frame_ask="Who is gltf.scene — a Mesh or a Group?",
        build=[
            "**Say:** Format. One glb vs gltf+bin+png.",
            "**Board:** load, add g.scene, traverse.",
            "**Say:** Box3 center. Shadows need traverse.",
        ],
        ask_build="Why traverse for castShadow?",
        they_build="On paper: the load callback three lines.",
        show_say="Load pattern from 10-gltf-pattern.html. Plant CDN GLTFLoader. Plant load in rAF. Plant huge Sketchfab without credit.",
        attempt_say="Error UI on 404 glb. Eight minutes.",
        land_say="Lab: error UI; box3 center. Homework: why glTF; load. Quiz: who is scene, traverse, load in rAF?.",
        live=[
            ("0–10", "importmap vendor + addons", "Plant CDN."),
            ("10–30", "load + add scene", "Plant adding gltf not gltf.scene."),
            ("30–45", "traverse shadows", "Forgot isMesh."),
            ("45–60", "They error-UI", "Circulate. Serve."),
        ],
        cut="DRACO decode internals. Keep load + traverse + serve.",
        add="Box3 center / scale to meters.",
    )
    GOLD[(C, 7)] = dict(
        kernel="TextureLoader; albedo SRGBColorSpace; data maps stay linear",
        success="they put a local map on a sphere and can say which maps are sRGB",
        invariant="wrong colorSpace is a lighting bug; sRGB normals are a bug",
        goal="maps that match the shader",
        board="""```
albedo / color map     SRGBColorSpace
normal, roughness, metal     linear / NoColorSpace

tex.colorSpace = THREE.SRGBColorSpace   // albedo only
tex.wrapS = RepeatWrapping; tex.repeat.set(4,4)

renderer.outputColorSpace = SRGBColorSpace
```""",
        slides=[],
        hook_say="CG I gamma, WebGL week 9 pow(1/2.2). three r152+ colorSpace. Demo 05-canvas-texture.html. Uncapped anisotropy is not the lab.",
        hook_ask="Should a normal map be SRGBColorSpace? Wait. Want: no.",
        frame_say="Maps: albedo vs normal vs roughness. Repeat 4. Canvas texture is a CPU map — still local.",
        frame_ask="Which maps are sRGB?",
        build=[
            "**Say:** Color management. outputColorSpace on renderer.",
            "**Board:** sRGB vs linear table.",
            "**Say:** Plant sRGB on normals. The lighting goes muddy.",
        ],
        ask_build="Why repeat wrapping on a floor?",
        they_build="On paper: three map types and their colorSpace.",
        show_say="Albedo on a sphere; wrong colorSpace toggle. Demo 05-canvas-texture.html. Plant sRGB normals.",
        attempt_say="repeat 4. Eight minutes.",
        land_say="Lab: repeat 4; normal extra. Homework: which maps are sRGB; texture. Quiz: albedo space, normal sRGB?, repeat. Midterm next week on 1–7.",
        live=[
            ("0–10", "TextureLoader local", "Plant CDN image host."),
            ("10–30", "albedo SRGB", "Plant default wrong on a PNG."),
            ("30–45", "normal linear", "Plant SRGB on normal."),
            ("45–60", "They repeat 4", "Circulate."),
        ],
        cut="Anisotropy race. Keep colorSpace table.",
        add="normalMap extra on Standard.",
    )
    GOLD[(C, 8)] = dict(
        kernel="midterm; then Raycaster as an oracle — NDC mouse, not a BVH you write",
        success="after the exam they can convert a pointer to NDC, intersectObjects, and say the engine is not the algorithm",
        invariant="picking is a ray vs bounds the engine owns; y is flipped in NDC",
        goal="midterm, then a pick",
        kind="midterm",
        midterm_topics="Scene/camera/renderer and Mesh→draw; matrixWorld as M; Basic vs Standard; lights/shadow flags; dt vs fps; GLTFLoader/traverse; albedo sRGB vs linear data maps.",
        board="""```
pointer NDC: x = (cx/w)*2-1     y = −(cy/h)*2+1
raycaster.setFromCamera(pointer, camera)
hits = raycaster.intersectObjects(pickables, recursive)

oracle  ≠  you implemented a BVH
```""",
        slides=[],
        hook_say="This meeting is a **midterm**, then picking. No laptop for the exam. After: Raycaster is an oracle. Computational Geometry owns the algorithm. Demo 07-raycaster.html.",
        show_say="Click to highlight a mesh. Plant forgot minus on y. Plant intersect the whole scene including helpers.",
        attempt_say="Highlight on hit. Layer extra if time.",
        land_say="Lab: layer extra. Homework: oracle vs algorithm; pick. No quiz this week.",
        live=[
            ("0–15", "NDC mapping", "Plant +y. Picks the floor."),
            ("15–40", "intersectObjects", "Plant recursive false on a Group."),
            ("40–60", "They highlight", "Circulate."),
        ],
        cut="Octree. Keep NDC + oracle sentence.",
        add="layers extra: camera.layers vs raycaster.layers.",
    )
    GOLD[(C, 9)] = dict(
        kernel="scene.environment; PMREM name; background vs env",
        success="they put a small local env on a metallic sphere and can toggle background vs environment",
        invariant="Standard looks like clay without an env; 500MB HDR is not a lab",
        goal="IBL as a taste, not a thesis",
        board="""```
scene.environment = envTex     // lighting
scene.background  = envTex     // picture (optional)

PMREM  (name)  —  prefilter for IBL
RGBE / EXR     (names)

budget: tiny HDR or a PMREM from a cube
```""",
        slides=[],
        hook_say="Standard needs an env to look 'PBR'. Demo 13-environment.html. Real-Time Rendering owns the integrals. Today: the knob and the cost.",
        hook_ask="Is scene.background the same as scene.environment? Wait. Want: no — one is the picture, one is the lighting.",
        frame_say="RGBELoader name. PMREMGenerator name. Intensity. Do not download a 500MB HDR. Local vendor.",
        frame_ask="Why is a metal sphere black in a black scene?",
        build=[
            "**Say:** Environment lights Standard. Background is optional wallpaper.",
            "**Board:** two assignments. PMREM name.",
            "**Say:** Cost: big HDR. Budget sentence, no invented fps.",
        ],
        ask_build="What does PMREM stand for as a teaching expansion?",
        they_build="On paper: background vs environment one line each.",
        show_say="Metallic sphere in an env. Demo 13-environment.html. Plant 500MB HDR. Plant only background, no environment.",
        attempt_say="Toggle background vs env. Eight minutes.",
        land_say="Lab: toggle; intensity. Homework: env vs background; env. Quiz: environment, PMREM, budget.",
        live=[
            ("0–10", "metal roughness 0.1", "Black. Plant."),
            ("10–30", "environment = tex", "It wakes up."),
            ("30–45", "background off", "They see the split."),
            ("45–60", "They toggle", "Circulate. Tiny HDR."),
        ],
        cut="Write a split-sum IBL. Keep env knob + budget.",
        add="envMapIntensity slider.",
    )
    GOLD[(C, 10)] = dict(
        kernel="shadow types named (PCF); bias / normalBias; CameraHelper on shadow.camera",
        success="they tune bias on a character-scale cube and can name PCF without claiming a fps win",
        invariant="bias too large deletes shadows; one directional should not cover the earth",
        goal="acne you can fix",
        board="""```
PCF / PCFSoft   (names)
light.shadow.bias = −0.0001
light.shadow.normalBias   (named)

CameraHelper(light.shadow.camera)
frustum too big → acne + peter-panning

CSM   (name only)
```""",
        slides=[],
        hook_say="Week 4 enabled shadows. Today knobs. Demo 03-lights-shadows.html and 20-shadow-contact.html knobs. Full maps in RTR. Do not set bias 0.1.",
        hook_ask="If the shadow pulls away from the feet, is that acne or peter-panning? Wait. Want: panning — bias too negative / frustum.",
        frame_say="Helpers on the shadow camera. mapSize experiment measured. CSM name, skip implementation.",
        frame_ask="What is PCF in one sentence?",
        build=[
            "**Say:** Acne vs panning on the board.",
            "**Board:** bias line + helper.",
            "**Say:** One directional, tight frustum.",
        ],
        ask_build="Why not bias = 0.1?",
        they_build="On paper: two symptoms and which knob.",
        show_say="Tune bias on a character-scale cube. Plant bias 0.1. Plant one huge directional covering the earth.",
        attempt_say="CameraHelper on shadow.camera. Eight minutes.",
        land_say="Lab: helper on; mapSize experiment measured. Homework: acne vs panning; bias. Quiz: bias, PCF, helper.",
        live=[
            ("0–10", "Acne plant", "bias 0."),
            ("10–30", "tune −0.0001", "Plant 0.1."),
            ("30–45", "helper frustum", "Too big."),
            ("45–60", "They measure mapSize", "No invented fps."),
        ],
        cut="CSM implementation. Keep bias + helper.",
        add="mapSize experiment measured.",
    )
    GOLD[(C, 11)] = dict(
        kernel="EffectComposer = FBO plumbing; RenderPass then a cheap pass",
        success="they can toggle composer vs renderer.render and say this is week-11 WebGL FBO",
        invariant="composer without understanding framebuffer is a filter pack; extra passes cost fill rate",
        goal="post as a pipeline, not a bloom preset dump",
        board="""```
renderer.render     →  canvas
composer:  scene FBO → pass → pass → screen

RenderPass(scene, camera)
OutputPass / gamma     color space

WebGL FBO week 11   =   this plumbing
```""",
        slides=[],
        hook_say="Bloom/HDR labs live in Real-Time Rendering. Demo 18-bloom.html is a name. Today: RenderPass + toggle vs raw render. Local jsm, no CDN.",
        hook_ask="If you never unbind an FBO in raw WebGL, what is the Three analog of forgetting composer.setSize? Wait. Want: resize / ping-pong size.",
        frame_say="sRGB output pass. Why not 8 passes. Cost sentence — measure or omit, no invented fps.",
        frame_ask="What is RenderPass?",
        build=[
            "**Say:** Two paths: raw render vs composer.",
            "**Board:** render → pass → screen.",
            "**Say:** Cheap pass or identity. Bloom is optional show.",
        ],
        ask_build="Why not eight UnrealBloomPasses?",
        they_build="On paper: composer vs renderer.render.",
        show_say="Composer with a cheap pass or gamma output. Demo 18-bloom.html as optional. Plant composer without FBO talk. Plant CDN examples/js.",
        attempt_say="Toggle composer vs raw render. Eight minutes.",
        land_say="Lab: toggle; cost sentence. Homework: extra fill rate; composer. Quiz: RenderPass, why not 8 passes, output color.",
        live=[
            ("0–10", "Map to FBO", "Draw last semester."),
            ("10–30", "RenderPass + output", "Plant forgot setSize."),
            ("30–45", "toggle raw", "They see the difference."),
            ("45–60", "They write cost sentence", "No invented fps."),
        ],
        cut="Full bloom tuning. Keep plumbing + toggle.",
        add="Cost sentence: extra full-screen passes.",
    )
    GOLD[(C, 12)] = dict(
        kernel="draw calls; InstancedMesh; LOD name; renderer.info.render",
        success="they log info.render on 200 meshes vs InstancedMesh and cap pixelRatio; they do not invent fps",
        invariant="a Mesh is a draw; measure on this machine; 8k on a cube is a budget fail",
        goal="count, then cut",
        board="""```
console.log(renderer.info.render)   // calls, triangles

200 Mesh     =  200 draws
1 InstancedMesh(n=200)  =  1 draw

LOD.addLevel(high, 0) / (mid, 8) / (low, 18)
pixelRatio 1 vs min(dpr, 2)

measure or omit     no invented fps
```""",
        slides=[],
        hook_say="Blender course polycounts meet the engine. Demos 08-instancing.html and 15-lod.html. WebGL week 12 in engine form.",
        hook_ask="If info.render.calls is 200, what did you probably create? Wait. Want: 200 Mesh, not InstancedMesh.",
        frame_say="Frustum culling named. pixelRatio 1 vs 2 is a fill-rate lab. Stats.js optional. 8k textures on a cube forbidden.",
        frame_ask="What is a draw call in one sentence?",
        build=[
            "**Say:** Count first. Then instance or LOD.",
            "**Board:** info.render. InstancedMesh.",
            "**Say:** LOD name. Distances are teaching numbers, not a promise.",
        ],
        ask_build="Why cap pixelRatio at 2?",
        they_build="On paper: budget table headers: draws, tris, maps — fill later by measuring.",
        show_say="200 meshes vs InstancedMesh; log info.render. Demos 08-instancing.html, 15-lod.html. Plant invented 60 fps. Plant 8k on a cube.",
        attempt_say="pixelRatio 1 vs 2. Log calls. Eight minutes.",
        land_say="Lab: pixelRatio; stats. Homework: budget table measured; instanced. Quiz: draw call, InstancedMesh, info.render. R3F teaser next.",
        live=[
            ("0–10", "info.render on a cube", "1 call."),
            ("10–30", "200 Mesh vs InstancedMesh", "Log calls. No fps speech."),
            ("30–45", "LOD name + demo 15", "Distances as names."),
            ("45–60", "They cap pixelRatio", "Circulate."),
        ],
        cut="GPU profiler internals. Keep calls + instance + measure.",
        add="stats overlay or info.render dump.",
    )
    GOLD[(C, 13)] = dict(
        kernel="R3F is declarative Three; same scene graph; not this course's project",
        success="they can map <mesh> to Mesh/draw call and say useFrame is rAF; they do not abandon the vanilla project",
        invariant="JSX does not replace WebGL; wait for Interactive Experience",
        goal="a map, not a rewrite",
        board="""```
<Canvas>                 WebGLRenderer + rAF
  <mesh>                 Mesh  →  draw call
    <boxGeometry />      BoxGeometry
    <meshStandardMaterial />

useFrame  ≈  the rAF callback
position={[x,y,z]}  ≈  object.position

Semester 5 · Interactive Experience
```""",
        slides=[("Optional 20-line R3F cube if a bundler exists", "otherwise the board is the demo")],
        hook_say="Semester 5 will do this for real. Today: the map so they are not frightened later. Do not npm-install a new stack into the week-14 project.",
        hook_ask="Does <mesh> skip the draw call? Wait. Want: no — it still is one.",
        frame_say="Same graph. If the lab has no bundler, stay on the board. No full app.",
        frame_ask="What is useFrame?",
        build=[
            "**Say:** Declarative = same objects, different syntax.",
            "**Board:** Canvas > mesh > geometry/material.",
            "**Say:** Table: R3F prop → Object3D.",
        ],
        ask_build="Why wait until semester 5?",
        they_build="On paper: five-row map R3F → Three → WebGL.",
        show_say="Optional 20-line R3F cube if a bundler exists; else board mapping. Plant abandoning the Three.js project overnight. No CDN.",
        attempt_say="Table: R3F prop → Object3D. No full app. Eight minutes.",
        land_say="Lab: the table; no full app. Homework: when R3F. Quiz: R3F sits on, useFrame is, why wait. Studio next.",
        live=[
            ("0–10", "Map Mesh → draw again", "They still know it."),
            ("10–30", "JSX tree on the board", "No install required."),
            ("30–45", "useFrame = rAF", "dt still exists."),
            ("45–60", "They fill the table", "Circulate. Freeze vanilla project."),
        ],
        cut="drei helpers tour. Keep the map.",
        add="No full app — write that on the parked strip.",
    )
    GOLD[(C, 14)] = dict(
        kernel="interactive 3D scene: camera, light, local glTF or mesh, one pick or animate; vendor only",
        success="a TA can serve ThreeJS/ (or the project folder) and hear Mesh → draw call",
        invariant="drop composer; keep camera+light+model; no CDN",
        goal="studio — not a content lecture",
        kind="studio",
        board="""```
Must: vendor three.module.js · light · camera · one interaction
Cuts: drop composer / IBL; keep shadows optional
README: serve folder · import map · what Three hid vs what you set
```""",
        slides=[],
        hook_say="This meeting is **studio**. Product shot, small world, or viewer. Honesty: what Three.js did vs what you configured.",
        hook_ask="If behind, what do you cut first? Want: composer and extra HDR.",
        frame_say="Desk review: mapping table + scene. Serve first. One teammate map Mesh → draw.",
        show_say="Volunteer: point at a Mesh and say the draw call.",
        attempt_say="Studio. Serve first.",
        land_say="Report + repo. Next week 12+5. Questions: where is V? Raycaster oracle?",
        live=[
            ("0–10", "Headings: map, scene, README", "Photograph."),
            ("10–50", "Desk review", "Serve + vendor + one pick."),
            ("50–60", "60s rehearsal", "Stop."),
        ],
        cut="New libraries. Keep freeze.",
        add="One 60-second Mesh→draw rehearsal.",
    )
    GOLD[(C, 15)] = dict(
        kernel="12+5; demo from local vendor; Mesh → draw call",
        success="they stop at 12 and can map one Mesh to a draw call and name V",
        invariant="no new features today",
        goal="presentations — not a content lecture",
        kind="presentations",
        board="""```
12 + 5
Show: vendor import · Mesh → draw · where is V
No CDN · no new npm on stage
```""",
        slides=[("Timer", "not a slide of drei")],
        hook_say="Presentations. 12+5. I will ask where V is and whether Raycaster is an oracle.",
        show_say="None. Present.",
        attempt_say="Present.",
        land_say="That mapping habit is how they stay honest in Interactive Experience.",
        live=[("0–60", "Talks", "Cut at 12.")],
        cut="Debugging on stage.",
        add="One question on colorSpace.",
    )


def _blender(GOLD: dict) -> None:
    C = "Blender for Real-Time Graphics"
    GOLD[(C, 1)] = dict(
        kernel="viewport navigation; scene unit = meter; save .blend; apply scale as a name",
        success="they can orbit the viewport, set metric 1.0, and say a 100 m mug will fail in Three.js",
        invariant="units, facing, and budget travel with the asset",
        goal="meters before modeling",
        board="""```
Scene unit = 1 meter
character ~1.7 m     mug in centimeters (0.08 m)

Object vs Edit     Outliner     N-panel     numpad views

Ctrl+A Rotation & Scale   (name this week; do it before export)
Face orientation overlay     Statistics: triangles
```""",
        slides=[],
        hook_say="This course supplies assets that survive in a real-time engine — not a Cycles feature film. Wrong scale is the #1 Three.js import bug. Checklist: Blender/code/01-units.html.",
        hook_ask="If a mug is 100 units tall in Blender, what happens in a Y-up meter world? Wait. Want: it is a building.",
        frame_say="Metric, unit scale 1.0. Outliner names. Delete the default cube only after duplicating a backup. Never model at 'looks good' scale.",
        frame_ask="Object mode vs Edit mode — which moves the origin?",
        build=[
            "**Say:** Why Blender in IGWT: topology, UVs, Principled, glTF.",
            "**Board:** meters. 1.7 m human. Outliner.",
            "**Say:** Face orientation and statistics overlays on day one so they exist.",
        ],
        ask_build="Why apply scale later?",
        they_build="On paper: three objects with intended sizes in meters.",
        show_say="Set units; scale a cube to 1.7 m; screenshot outliner. Demo 01-units.html as the checklist. Plant modeling at unknown scale.",
        attempt_say="Rename objects in the outliner. Duplicate cube before delete. Eight minutes.",
        land_say="Lab: rename; backup cube. Homework: why meters; numbered outliner screenshot. Quiz: default unit, Object vs Edit, 100 m mug.",
        live=[
            ("0–10", "Orbit / numpad / outliner", "Plant only watching YouTube."),
            ("10–30", "Metric 1.0 + 1.7 m cube", "Plant 'looks good' scale."),
            ("30–45", "Face orientation overlay", "Red faces named."),
            ("45–60", "They rename + save", "Circulate. 01-units.html."),
        ],
        cut="Every keymap. Keep units + outliner.",
        add="Delete default cube only after duplicating a backup.",
    )
    GOLD[(C, 2)] = dict(
        kernel="verts, edges, faces; extrude / inset / loop cut; face orientation",
        success="they can extrude a crate and turn on face orientation; they do not sculpt a hero",
        invariant="real-time cares about triangle count and facing; inverted normals ship as inside-out in the engine",
        goal="a crate, not a film character",
        board="""```
E extrude   I inset   Ctrl+R loop cut   G/S/R
Merge by distance

Face orientation: blue front / red back
Statistics: tris     (glTF stores triangles)

ngons OK on flat caps; dangerous on curves
```""",
        slides=[],
        hook_say="Film cares about subdivision beauty. We care about tris and deformation. Inverted normals shipped to Three.js are a facing bug — the engine is not the bug.",
        hook_ask="Why turn on face orientation this week? Wait. Want: red faces will be inside-out in glTF.",
        frame_say="Quads on deforming surfaces; triangles are what glTF stores anyway. Ngons named. Statistics overlay. No hero sculpt as homework.",
        frame_ask="Quad vs tri in real-time — who triangulates?",
        build=[
            "**Say:** Operators. Overlay on.",
            "**Board:** E I Ctrl+R. Blue/red.",
            "**Say:** A table with four legs — separate objects or one mesh, they justify.",
        ],
        ask_build="What does red mean on face orientation?",
        they_build="On paper: a crate in 8–12 boxes (faces).",
        show_say="Block a crate; overlay; statistics. Plant sculpting a hero. Plant inverted faces.",
        attempt_say="Extrude a crate. Screenshot statistics. Eight minutes.",
        land_say="Lab: table with 4 legs; statistics screenshot. Homework: quad vs tri; blend + triangle count. Quiz: extrude, why face orientation, n-gon risk.",
        live=[
            ("0–10", "Face orientation on", "Plant skipped overlay."),
            ("10–30", "Extrude crate", "Plant ngons on a curve."),
            ("30–45", "Statistics tris", "They read the number."),
            ("45–60", "They merge by distance", "Circulate."),
        ],
        cut="Sculpt. Keep crate + facing + count.",
        add="Screenshot statistics on the crate.",
    )
    GOLD[(C, 3)] = dict(
        kernel="Mirror with clipping; Array; Bevel; stack order; apply vs live",
        success="they can mirror a crate with clipping and say glTF export applies mesh modifiers",
        invariant="modifiers are functions; order matters; applying every five minutes is not safety",
        goal="non-destructive until export needs it",
        board="""```
Mirror  +  clipping     (do not duplicate by hand)
Array   after the piece is right
Bevel   usually after Mirror

live while iterating
glTF export applies mesh modifiers

Boolean: blocking only; cleanup before animation
```""",
        slides=[],
        hook_say="Modifiers are the functions of modeling. Reverse the stack and you get double bevels. Demo checklist 03-budget.html is not this week's kernel — still glance at tris.",
        hook_ask="If Mirror sits after Bevel, what goes wrong? Wait. Want: you bevel a half then mirror a seam, or double bevel — show it.",
        frame_say="Keep live. Apply before some exports if the engine cannot see them — glTF applies mesh modifiers. Boolean named, not soup.",
        frame_ask="Apply vs live — when must it apply?",
        build=[
            "**Say:** Mirror clipping so the center welds.",
            "**Board:** stack order. Array. Bevel.",
            "**Say:** Plant applying every modifier to be safe every five minutes.",
        ],
        ask_build="Does the engine see an unapplied Mirror if you forget export-apply?",
        they_build="On paper: a three-modifier stack for a crate.",
        show_say="Mirror crate; reverse stack once. Plant apply-all. Plant boolean soup.",
        attempt_say="Toggle modifier visibility. Eight minutes.",
        land_say="Lab: toggle visibility; one boolean hole extra. Homework: apply vs live; stack screenshot. Quiz: clipping, why order, export applies?.",
        live=[
            ("0–10", "Mirror + clipping", "Plant duplicate-by-hand."),
            ("10–30", "Bevel after mirror", "Plant reverse stack."),
            ("30–45", "Array a bolt", "They instance in Blender."),
            ("45–60", "They toggle visibility", "Circulate."),
        ],
        cut="Geometry Nodes as the course. Keep mirror/array/bevel.",
        add="One boolean hole, then cleanup extra.",
    )
    GOLD[(C, 4)] = dict(
        kernel="seams, islands, texel density; checker grid as the judge",
        success="they mark seams on a crate, unwrap, pack with margin, and can read stretch on a checker",
        invariant="UVs are the fragment-shader map; stretch is blur; Smart UV is not a character pipeline",
        goal="islands a texture can use",
        board="""```
seam  =  cut where the island splits
island  =  connected UV chart
checker: even squares = good; skinny = stretch

pack + margin     overlap = shared texels
texel density: same pixel size on crate faces
```""",
        slides=[],
        hook_say="The fragment shader samples a 2D image. That is why this week exists. Lightmaps hate overlap; albedo sometimes shares trim. Do not Smart-UV a character as the only method.",
        hook_ask="If the checker is long rectangles, is that a 4k texture problem? Wait. Want: no — stretch in the unwrap.",
        frame_say="Cylinders: one side seam + caps. Pack with margin. Tiny islands / giant waste is a packing bug.",
        frame_ask="What is an island?",
        build=[
            "**Say:** Why UVs. Seams where they hide.",
            "**Board:** checker judgment.",
            "**Say:** One overlap bug then fix.",
        ],
        ask_build="Why a margin when packing?",
        they_build="Sketch seams on a crate (six faces).",
        show_say="Mark seams; unwrap; checker. Plant Smart UV as the only method. Plant tiny islands.",
        attempt_say="Pack with a margin. Eight minutes.",
        land_say="Lab: pack + margin; overlap bug then fix. Homework: what a seam is; UV screenshot. Quiz: island, stretch symptom, why checker.",
        live=[
            ("0–10", "Checker material", "Plant judging in solid view."),
            ("10–30", "Seams on crate", "Plant seam on the hero face."),
            ("30–45", "Pack margin", "Bleed named."),
            ("45–60", "They fix overlap", "Circulate."),
        ],
        cut="UDIM speeches. Keep crate seams + checker.",
        add="One overlap bug then fix.",
    )
    GOLD[(C, 5)] = dict(
        kernel="Principled: Base Color, Metallic 0 or 1, Roughness; maps to MeshStandardMaterial",
        success="they assign Principled and can say painted wood is metalness 0; they do not judge in solid view",
        invariant="same knobs as Standard; metalness 0.4 'because it looked nice' is usually wrong",
        goal="PBR knobs that survive glTF",
        board="""```
BaseColor     Metallic 0|1     Roughness     Normal
=  MeshStandardMaterial  map / metalness / roughness / normalMap

dielectric 0     metal 1
Material Preview + HDRI     not Solid

specular workflow  =  legacy
```""",
        slides=[],
        hook_say="Same knobs as Three.js Standard and later RTR. Students judge metal under gray clay and think PBR is broken. Preview with an HDRI.",
        hook_ask="Metalness of painted wood? Wait. Want: 0.",
        frame_say="Two materials on a crate ok. Emission as a tiny LED extra. Do not set 0.5 on everything.",
        frame_ask="Three.js name for Base Color?",
        build=[
            "**Say:** Principled slots. Write the Three.js names beside them.",
            "**Board:** 0 or 1 metal. Roughness meaning.",
            "**Say:** Solid view plant. Switch to Material Preview.",
        ],
        ask_build="Why is metalness 0.5 usually wrong?",
        they_build="On paper: crate wood vs crate metal strip — two values.",
        show_say="Assign Principled; HDRI preview; map names to Standard. Plant metalness 0.5. Plant judging in solid.",
        attempt_say="Crate with two materials. Eight minutes.",
        land_say="Lab: two materials; LED extra. Homework: map to MeshStandardMaterial; blend + screenshot. Quiz: painted wood, roughness meaning, three.js names.",
        live=[
            ("0–10", "Principled on crate", "Plant Solid view."),
            ("10–30", "metal 0 vs 1", "Plant 0.5."),
            ("30–45", "roughness slider", "They see the highlight."),
            ("45–60", "They add a second material", "Circulate."),
        ],
        cut="Clearcoat / sheen tour. Keep three knobs + preview.",
        add="Emission as a tiny LED extra.",
    )
    GOLD[(C, 6)] = dict(
        kernel="Sun ≈ directional; Area vs Point; one key light; camera FOV → PerspectiveCamera",
        success="they add Sun and Area, can disable extras, and map sun to DirectionalLight",
        invariant="preview in Eevee / Material Preview; Cycles caustics are not the goal; no invented exposure numbers as fps",
        goal="lights that have engine names",
        board="""```
Sun    ≈  DirectionalLight
Point  ≈  PointLight
Spot   ≈  SpotLight
Area   ≈  RectAreaLight (name)

one key light     disable extras to debug

camera 35–50 mm product     →  PerspectiveCamera.fov
```""",
        slides=[],
        hook_say="Real-time vs Cycles: we preview what a game-ish engine can do. Lighting with emission meshes only is not PBR. ISO 6400 noise is not a style goal.",
        hook_ask="Sun in Blender maps to which Three.js light? Wait. Want: DirectionalLight.",
        frame_say="Why one key light. FOV vs dolly extra. Turntable screenshot for homework. Exposure named; do not invent device fps.",
        frame_ask="Why one key light when debugging a material?",
        build=[
            "**Say:** Light type table. Same names in Three.js.",
            "**Board:** sun vs point. Camera mm → fov.",
            "**Say:** Disable extras. The material becomes readable.",
        ],
        ask_build="Does an Area light become a directional in glTF punctual lights?",
        they_build="On paper: three light types and Three.js names.",
        show_say="Sun + Area on the crate; disable extras. Plant emission-only lighting. Plant ISO-as-style.",
        attempt_say="Disable extra lights. Eight minutes.",
        land_say="Lab: disable extras; FOV vs dolly extra. Homework: sun vs point in Three.js; turntable screenshot. Quiz: sun maps to, why one key, fov.",
        live=[
            ("0–10", "Sun as key", "Plant 8 area lights."),
            ("10–30", "Area fill", "They see softness as a name."),
            ("30–45", "Camera 50 mm", "Plant 8 mm cartoon."),
            ("45–60", "They disable extras", "Circulate."),
        ],
        cut="Cycles caustics. Keep type table + one key.",
        add="FOV vs dolly extra.",
    )
    GOLD[(C, 7)] = dict(
        kernel="I-key loc/rot; Graph Editor bezier vs linear vs constant; clip idea",
        success="they insert loc/rot keys on a spinning logo and can say a F-curve is what the mixer will play",
        invariant="engines see glTF clips; auto-key garbage is not animation; object transforms this week, bones next",
        goal="a clip an engine can play",
        board="""```
I  →  Location / Rotation
Graph Editor:  bezier (default bounce you did not want)
               linear
               constant (stepped)

glTF clip  →  Three.js AnimationMixer
24 fps is a project setting, not a runtime promise
```""",
        slides=[],
        hook_say="A spinning logo is enough. Three.js mixer plays clips. Default bezier makes a bounce they did not want. Do not auto-key 400 garbage keys. Do not invent runtime fps from the timeline.",
        hook_ask="Does 24 fps in Blender mean 24 fps in the browser? Wait. Want: no — it is the clip's time base; the mixer uses dt.",
        frame_say="Object vs bone: bones next week. Will this export as a clip? Constant for stepped. Midterm next week on 1–7.",
        frame_ask="What is a F-curve?",
        build=[
            "**Say:** Insert loc/rot. Open the graph.",
            "**Board:** three interpolation names.",
            "**Say:** Plant auto-key. Plant animating verts in edit mode for a rigid lid.",
        ],
        ask_build="Mixer vs rAF rotate — which needs a clip?",
        they_build="On paper: three keys for a 360° Y spin.",
        show_say="Spin a logo; show bezier bounce; switch linear. Plant auto-key. Plant edit-mode vert anim for a lid.",
        attempt_say="Looping rotation. Eight minutes.",
        land_say="Lab: looping rotation; export thought. Homework: what a F-curve is; 24-frame viewport capture (not a fps claim). Quiz: insert key, linear vs bezier, mixer later.",
        live=[
            ("0–10", "I-key loc/rot", "Plant auto-key on."),
            ("10–30", "Graph bezier → linear", "Unwanted bounce."),
            ("30–45", "clip name", "Mixer later."),
            ("45–60", "They loop the spin", "Circulate. No fps brag."),
        ],
        cut="NLA strips. Keep I-key + graph + clip name.",
        add="Will this be a clip on export — write yes/no.",
    )
    GOLD[(C, 8)] = dict(
        kernel="midterm; then armature idea: a bone is a transform, weights skin the mesh",
        success="after the exam they can add an armature, parent with automatic weights on a bar, and name rest pose",
        invariant="real-time keeps bone count modest; automatic weights leak — that is the leftover lab",
        goal="midterm, then a bone",
        kind="midterm",
        midterm_topics="meters/apply-scale name; topology and face orientation; modifier order; seams/checker; Principled metal 0|1; sun→directional; I-key and F-curves (not runtime fps).",
        board="""```
armature  =  bones (transforms)
skin      =  weights per vertex
parent with automatic weights   (on a bar / simple arm)

Pose mode ≠ Edit bones
rest pose  =  what you export as bind
```""",
        slides=[],
        hook_say="This meeting is a **midterm**, then rigging start. No laptop for the exam. After: a bone is a transform. Weight paint names only. Modest bone count.",
        show_say="Add armature; parent automatic weights on a simple mesh. Plant posing in object mode. Plant 40 bones on a crate.",
        attempt_say="Pose the bar. Rest pose named.",
        land_say="Lab: weight leak extra; rest pose. Homework: midterm reflection + armature file. No quiz this week.",
        live=[
            ("0–15", "Add armature + bone", "Plant 40 bones."),
            ("15–40", "Automatic weights on a bar", "Leak into the other bone."),
            ("40–60", "Pose vs rest", "They type. Circulate."),
        ],
        cut="IK chains. Keep one bone + weights name.",
        add="Fix a weight leaking into the other bone extra.",
    )
    GOLD[(C, 9)] = dict(
        kernel="apply rotation & scale; rest pose; Z-up Blender vs Y-up glTF; no negative scale mirror",
        success="they apply rotation/scale on the mesh before parenting, document rest pose, and check axes in a viewer later",
        invariant="unapplied scale is tiny/huge in Three.js; exporter converts Z-up but they still check",
        goal="a bind pose that survives export",
        board="""```
Ctrl+A Rotation & Scale   on the mesh   (backup first)
Do not apply location if it wrecks the scene

Blender Z-up     glTF / Three.js Y-up
exporter converts — still verify in a viewer

negative scale 'to mirror'  →  facing bug
IK named, optional; FK enough
```""",
        slides=[],
        hook_say="Unapplied scale is the classic tiny model in Three.js. Face orientation from week 2 still applies. If it is wrong in a glTF viewer, the engine is not the bug.",
        hook_ask="Why apply scale before parenting to a bone? Wait. Want: the bone inherits a 100× scale and the mesh becomes a building or a speck.",
        frame_say="Bone axes overlay. Document rest pose in README. Negative scale to mirror is forbidden. IK name only.",
        frame_ask="Who is responsible for Y-up — Blender, exporter, or Three.js?",
        build=[
            "**Say:** Apply rot/scale with a backup.",
            "**Board:** Z vs Y. Rest pose.",
            "**Say:** Plant applying location and losing the scene.",
        ],
        ask_build="What is rest pose in one sentence?",
        they_build="On paper: checklist before export parenting.",
        show_say="Apply scale; parent; pose. Plant negative scale mirror. Plant apply location.",
        attempt_say="Bone axes overlay. Eight minutes.",
        land_say="Lab: axes overlay; rest pose in README. Homework: Z-up vs Y-up; checklist screenshot. Quiz: apply scale why, Z vs Y, rest pose.",
        live=[
            ("0–10", "Unapplied scale plant", "Cube is 100 m."),
            ("10–30", "Ctrl+A rot/scale", "Backup first."),
            ("30–45", "Y-up talk", "Viewer later."),
            ("45–60", "They document rest pose", "Circulate."),
        ],
        cut="Full IK. Keep apply + rest + axes.",
        add="Document rest pose in README.",
    )
    GOLD[(C, 10)] = dict(
        kernel="normal map stores offset to N; AO named; BaseColor sRGB, data maps non-color",
        success="they know what a normal map stores and do not bake 8k or sRGB normals",
        invariant="512–1k for student crates; 4k is a budget lecture not a flex; same colorSpace as Three.js week 7",
        goal="maps an engine can sample",
        board="""```
BaseColor     sRGB
Normal / Roughness / Metal     non-color (linear)

normal map = tangent-space offset to N
AO = cheap cavity / contact (name)

bake: high bevelled cube → low cube
512–1024     not 8k
```""",
        slides=[],
        hook_say="Same as Three.js colorSpace week. Baking every map at 8k is a fail. Substance is optional, not required. A subdivided bevelled cube onto a low cube is enough.",
        hook_ask="Is a 4k normal map on a mug a quality win? Wait. Want: usually a budget fail; texel density and distance matter.",
        frame_say="Cage, ray distance named. Color space check. Map list in README.",
        frame_ask="What do the channels of a normal map mean at teaching level?",
        build=[
            "**Say:** What a normal map stores. AO name.",
            "**Board:** sRGB vs non-color.",
            "**Say:** Plant sRGB normals. Plant 8k.",
        ],
        ask_build="Why non-color on roughness?",
        they_build="On paper: four slots and colorSpace.",
        show_say="Bake a bevelled high onto a low cube; assign. Plant 8k. Plant sRGB normals.",
        attempt_say="Color space check on the maps. Eight minutes.",
        land_say="Lab: normal on a flat plane extra; color space check. Homework: which maps are sRGB; map list in README. Quiz: normal channels, AO, 4k on a mug?.",
        live=[
            ("0–10", "High bevel / low cube", "Enough."),
            ("10–30", "Bake normal", "Plant 8k."),
            ("30–45", "non-color vs sRGB", "Plant sRGB normal."),
            ("45–60", "They list maps in README", "Circulate."),
        ],
        cut="Substance Painter. Keep bake + colorSpace.",
        add="Normal on a flat plane from a high bevel extra.",
    )
    GOLD[(C, 11)] = dict(
        kernel="glTF 2.0 Binary .glb; +Y Up; apply modifiers; viewer BEFORE Three.js",
        success="they export a .glb and open it in a glTF viewer (or 10-gltf-pattern.html with local vendor) before blaming Three.js",
        invariant="if it is wrong in a glTF viewer, the engine is not the bug",
        goal="a file the web can load",
        board="""```
glTF 2.0 Binary (.glb)     not .blend     not 'FBX because Unity'

+Y Up     Apply modifiers     UVs + normals
unused materials off     punctual lights optional

Open in a glTF viewer BEFORE Three.js
ThreeJS/demos/10-gltf-pattern.html  +  vendor/   no CDN
```""",
        slides=[],
        hook_say="Khronos standard. One file (glb) vs json+bin+png. Checklist Blender/code/02-export.html. Validate: if the viewer is wrong, do not debug the renderer.",
        hook_ask="You export .blend to the web — what happens? Wait. Want: browsers do not load .blend.",
        frame_say="Draco extra named. Log triangle count vs blend. FBX is not the pipeline in this course.",
        frame_ask="glb vs gltf in one sentence?",
        build=[
            "**Say:** Why glTF. Settings from 02-export.html.",
            "**Board:** viewer before Three.js.",
            "**Say:** Plant FBX-only. Plant skipping the viewer.",
        ],
        ask_build="Why apply modifiers on export?",
        they_build="On paper: export checklist five boxes.",
        show_say="Export crate.glb; open viewer; then 10-gltf-pattern.html with ThreeJS/vendor/. Plant .blend upload. Plant CDN loader.",
        attempt_say="Export; write triangle count vs blend. Eight minutes.",
        land_say="Lab: with/without Draco extra; log tris. Homework: glb vs gltf; the .glb in the repo (small). Quiz: glb vs gltf, apply modifiers, why viewer first.",
        live=[
            ("0–10", "Export settings +Y", "Plant Z-up leftover."),
            ("10–30", "Viewer first", "Plant jumping to Three.js."),
            ("30–45", "10-gltf-pattern local vendor", "No CDN."),
            ("45–60", "They log tris vs blend", "Circulate."),
        ],
        cut="Every glTF extension. Keep glb + viewer-first.",
        add="Log triangle count vs blend.",
    )
    GOLD[(C, 12)] = dict(
        kernel="budget sheet: tris, batches/materials, map size; measure; no invented fps",
        success="they fill Blender/code/03-budget.html with measured counts for their asset and can say why 40 materials are 40 draws",
        invariant="a frame is a budget; Nanite speeches on a crate are off-topic; never invent 60 fps",
        goal="numbers you measured",
        board="""```
tris        materials/batches        maps (1024²)        device
fill with measured numbers

each material can be a draw
atlas when you can     don't 40 materials for 40 bolts

LOD / instancing  —  Three.js / WebGL courses
no invented fps
```""",
        slides=[],
        hook_say="A student product viewer: tens of thousands of tris is plenty. Invented '60 fps' without a device is a fail. Nanite speech on a crate is a fail. Sheet: 03-budget.html.",
        hook_ask="If you have 40 unique materials on 40 bolts, what happens at draw-call time? Wait. Want: up to 40 draws.",
        frame_say="Mobile vs desktop as a column, not a fps. Decimate extra and compare measured tris. renderer.info is next week in Three — this week the written sheet.",
        frame_ask="Why atlas?",
        build=[
            "**Say:** Budget columns. Device named (their laptop).",
            "**Board:** the table from 03-budget.html.",
            "**Say:** Plant invented 60 fps. Plant Nanite.",
        ],
        ask_build="What do you write if you have not measured?",
        they_build="Fill the table headers; leave numbers blank until they count.",
        show_say="Count tris on the crate; count materials; map sizes. Demo 03-budget.html. Plant 60 fps. Plant Nanite.",
        attempt_say="Decimate extra and compare measured tris. Eight minutes.",
        land_say="Lab: decimate compare; one atlas vs three materials. Homework: budget table measured; what you cut. Quiz: draw call, why atlas, LOD name. Three.js import next.",
        live=[
            ("0–10", "Statistics tris", "Write the number."),
            ("10–30", "Materials = batches", "Plant 40 bolt mats."),
            ("30–45", "map 1024 vs 4k", "Budget, not flex."),
            ("45–60", "They fill 03-budget.html", "No invented fps."),
        ],
        cut="City-scale LOD design. Keep their asset's sheet.",
        add="One atlas vs three materials.",
    )
    GOLD[(C, 13)] = dict(
        kernel="load the glb with local GLTFLoader; scale, shadows, env; viewer already passed",
        success="they load in the Three.js pattern, traverse shadows, and fix black metal with env not MeshBasicMaterial",
        invariant="if the viewer was wrong, stop; if Three is black, check metal+rough+env, scale 0.01, inverted N",
        goal="the handshake",
        board="""```
Blender → .glb → viewer OK → ThreeJS/vendor GLTFLoader

scale 0.01          black metal (metal+rough, no env)
inverted normals    missing UVs     clip not exported

AxesHelper to check size
Unlit to 'fix' black  =  forbidden
```""",
        slides=[],
        hook_say="This week is why the course exists. Asset → [[18 Three.js Development]] loader. Local vendor. No CDN. Do not re-export 20 times without the viewer step.",
        hook_ask="Black metallic crate in Three, fine in Blender preview — first hypothesis? Wait. Want: no environment on Standard.",
        frame_say="traverse castShadow. Y-up check. file:// vs serve. AxesHelper. Unlit as a 'fix' is a plant.",
        frame_ask="What does traverse do here?",
        build=[
            "**Say:** Handshake. Viewer already green.",
            "**Board:** bug list. Env.",
            "**Say:** Shadow on a plane.",
        ],
        ask_build="Why might the model be 100× too small?",
        they_build="On paper: five import bugs and the fix.",
        show_say="Load crate.glb with vendor GLTFLoader (10-gltf-pattern.html pattern). Plant unlit fix. Plant re-export without viewer. Plant CDN.",
        attempt_say="AxesHelper to check size. Eight minutes.",
        land_say="Lab: shadow on a plane; AxesHelper. Homework: bug you hit and the fix; URL or file:// note. Quiz: traverse, black metal cause, Y-up. Studio next.",
        live=[
            ("0–10", "Viewer still OK?", "If not, stop."),
            ("10–30", "GLTFLoader vendor", "Plant CDN."),
            ("30–45", "black metal → env", "Plant MeshBasic."),
            ("45–60", "They add AxesHelper", "Circulate. Serve."),
        ],
        cut="Animation mixer deep dive. Keep load + env + scale.",
        add="AxesHelper to check size.",
    )
    GOLD[(C, 14)] = dict(
        kernel="one pack, one viewer: UVs + Principled + glb + Three.js load; README units/rest/maps/budget",
        success="a TA can open the README, serve the viewer, and see measured tris — not a cinematic short",
        invariant="drop armature if behind; keep UVs + Principled + glb + load; no invented fps",
        goal="studio — not a content lecture",
        kind="studio",
        board="""```
Must: meters · facing · UVs · Principled · .glb · viewer then Three
Cuts: drop armature / bake extras; keep the handshake
README: units, rest pose, map list, budget (measured), how to serve
```""",
        slides=[],
        hook_say="This meeting is **studio**. Product, prop, or simple arm. Not a cinematic short.",
        hook_ask="If behind, what do you cut first? Want: armature and extra bakes.",
        frame_say="Desk review: viewer first, then Three.js load with vendor. Budget sheet filled. Pipeline figures for the report.",
        show_say="Volunteer: open the glTF viewer, then the local Three page.",
        attempt_say="Studio. Viewer first.",
        land_say="Report 6–8 pages: pipeline figures. Next week 12+5. Questions: units, why viewer first.",
        live=[
            ("0–10", "Headings: units, maps, budget", "Photograph."),
            ("10–50", "Desk review", "Viewer then vendor load."),
            ("50–60", "60s rehearsal", "Stop."),
        ],
        cut="New tools. Keep freeze.",
        add="One 60-second viewer-then-engine rehearsal.",
    )
    GOLD[(C, 15)] = dict(
        kernel="12+5; glb in a viewer; then Three.js; units and facing",
        success="they stop at 12 and can say why a viewer bug is not an engine bug",
        invariant="no new features today",
        goal="presentations — not a content lecture",
        kind="presentations",
        board="""```
12 + 5
Show: meters · viewer · Three vendor load · budget numbers you measured
No invented fps · no CDN
```""",
        slides=[("Timer", "not a reel of Cycles")],
        hook_say="Presentations. 12+5. I will ask units and why the glTF viewer comes before Three.js.",
        show_say="None. Present.",
        attempt_say="Present.",
        land_say="If it is wrong in a glTF viewer, the engine is not the bug. That sentence is the course.",
        live=[("0–60", "Talks", "Cut at 12.")],
        cut="Debugging on stage.",
        add="One question on metalness 0 vs 1.",
    )
