"""Full-script GOLD for Computer Graphics I and Computational Geometry (15 meetings each)."""


def register(GOLD: dict) -> None:
    _register_cg(GOLD)
    _register_compgeo(GOLD)


def _register_cg(GOLD: dict) -> None:
    C = "Computer Graphics I"
    GOLD[(C, 1)] = dict(
        kernel="putPixel(x, y, rgb) on Canvas ImageData; six spaces; RH +Y look −Z; P*V*M; CCW",
        success="they can point at six boxes and say putPixel lives in pixels, not in clip",
        invariant="a picture is an array; putPixel lives in pixels",
        goal="see that graphics is geometry + sampling + shading, with no magic engine yet",
        board="""```
object → world → view → clip → NDC → pixels

geometry + camera + light + material  →  framebuffer

RH  +Y up  look −Z
p_clip = P * V * M * vec4(p,1)    CCW front

putPixel: index = (y * width + x) * 4
canvas (0,0) = top-left; world +Y is not canvas +Y
```""",
        slides=[("One pretty still of a cube", "do not lecture the pipeline from the still")],
        hook_say="A computer has no cube, only numbers. Today we freeze the pipeline and write a pixel. Computational geometry asks which triangle; we ask what color this pixel is. Three.js is not this week’s lab.",
        hook_ask="If the picture is an array, where does putPixel live — object space or pixels? Wait seven seconds.",
        frame_say="Rasterization loops triangles then pixels. Ray tracing loops pixels then rays — name only; we implement raster. Do not derive P today. Promise Week 8. Conventions freeze now: right-handed, +Y, camera looks −Z, column vectors P*V*M, CCW. Radians in code.",
        frame_ask="Which loop does WebGL run first — triangles or rays?",
        build=[
            "**Say:** Draw geometry + camera + light + material → framebuffer. That arrow is the semester.",
            "**Board:** six boxes, fill slowly. Object, world, view, clip (w matters), NDC, pixels. Who runs which later: CPU builds M,V,P; vertex shader object→clip; rasterizer fragments; fragment shader color.",
            "**Say:** Skip list on the board: shadows, deferred, PBR, Vulkan, glTF as the claim, Three.js as the weekly lab. Assessment: labs 25, hw 20, quizzes 10, midterm 15, project 30. Language: JS + ImageData. WebGL2 in Week 13 as a map, not the engine.",
        ],
        ask_build="P*V*M or M*V*P in this course? Want: P*V*M.",
        they_build="On paper: six boxes, one sentence each. Circle the box putPixel writes.",
        show_say="Canvas, backing store not 0×0, getImageData/putImageData. putPixel with integer coords and bounds checks. Vertical gradient. Print width, height, data.length === width*height*4. Demo Computer Graphics/code/01-putpixel.html. Plant fillRect as ‘the renderer.’ Plant CSS size without canvas.width.",
        attempt_say="Write putPixel with the index formula and a clip. Eight minutes. No fillRect.",
        land_say="Photograph the six boxes and the conventions. Lab: clear, checkerboard 16, clipped rectangle — do not wrap x%width. Homework: pipeline diagram; putPixel tests (corners, off-canvas, 1×1). Quiz: raster vs ray, six spaces, P*V*M, canvas (0,0).",
        live=[
            ("0–10", "Canvas + ImageData", "Plant CSS size, backing store 0×0. Black screen."),
            ("10–30", "putPixel + bounds", "Plant missing clip; wrap as a torus bug."),
            ("30–45", "Gradient; y down", "Say: world +Y flip is Week 9 viewport, not today."),
            ("45–60", "They write checkerboard cells", "Circulate. No Three.js."),
        ],
        cut="Who-runs-which GPU table. Keep six boxes + putPixel.",
        add="Alpha as a fourth byte name; blend is Week 2.",
    )
    GOLD[(C, 2)] = dict(
        kernel="over: out_rgb = src*src_a + dst*(1-src_a); index (y*width+x)*4; sRGB named not solved",
        success="they can write over in 0–1 and the byte index, and say byte 128 is not half the light",
        invariant="a picture is an array; putPixel lives in pixels",
        goal="stop treating 8-bit as linear light; composite two squares",
        board="""```
index = (y * width + x) * 4     RGBA uint8

over (straight, 0–1):
  out_rgb = src_rgb * src_a + dst_rgb * (1 - src_a)
  out_a   = src_a + dst_a * (1 - src_a)

Weeks 2–10: store 8-bit as-is
Weeks 11–12: linear in, pow(c, 1/2.2) out

letterbox  ≠  stretch
```""",
        slides=[("CSS-stretched circle becoming an ellipse", "photograph"), ("50% gray 128 vs a linear mid", "photograph")],
        hook_say="Last week a pixel. Today the pixel has alpha and a lie: averaging 8-bit sRGB is not averaging light. We name the lie. We do not invent a color-science course.",
        hook_ask="Is byte 128 half as much light as 255? Wait. Want: no.",
        frame_say="Pixel is a sample. Resolution is sample count; aspect is framebuffer width/height. ImageData is RGBA, unpadded. Premultiplied: name it; lab is straight over. Coverage vs transparency: name; no MSAA. Policy: weeks 2–10 as-is; 11–12 linear then gamma. Never ‘fix’ lighting with shininess.",
        frame_ask="What does width in the index formula mean — CSS pixels or canvas.width?",
        build=[
            "**Say:** Clear color is visible gray, never (0,0,0) while debugging a black cube later.",
            "**Board:** two overlapping squares; over in 0–1. They compute white 0.5 over black on paper.",
            "**Say:** Letterbox vs stretch. Match backing store to CSS * dPR (cap 2) or letterbox. That helper returns in Week 9 as the viewport.",
        ],
        ask_build="Write over for rgb, ignore output alpha. Work in 0–1.",
        they_build="On paper: index of pixel (2,1) in width-10. Then 16:9 in a 4:3 window — stretch or letterbox?",
        show_say="Two translucent rectangles, alpha slider. Side-by-side 128-gray vs labeled ‘not linear 0.5.’ Demo 03-alpha-over.html. Plant blending in uint8. Plant getContext alpha:false then debugging alpha.",
        attempt_say="overPixel on two boxes. Eight minutes. Convert to 0–1 first.",
        land_say="Lab: overPixel; eight boxes alpha 1/8…; CSS-stretch checkbox with a caption. Homework: over tests (opaque, invisible, 50% red on black); sRGB paragraph; letterbox. Quiz: index, over, CSS stretch, 128 vs light.",
        live=[
            ("0–10", "Index formula + visible clear", "Plant clear alpha 0; page shows through."),
            ("10–30", "over two squares", "Plant uint8 blend without /255."),
            ("30–45", "128 vs linear", "Do not derive the 2.4 piecewise sRGB."),
            ("45–60", "Letterbox helper sketch", "Plant stretch as the default."),
        ],
        cut="ICC / premultiplied GPU storage. Keep over + the sRGB name.",
        add="Coverage as cheap 50% alpha on an edge — name only.",
    )
    GOLD[(C, 3)] = dict(
        kernel="barycentric(p,a,b,c); fill if α,β,γ ≥ −eps and area ≠ 0; test pixel centers",
        success="they fill a triangle colored by αβγ and skip a collinear triple without crashing",
        invariant="a picture is an array; putPixel lives in pixels",
        goal="a filled triangle from three pixel coordinates — the heart of the course",
        board="""```
p = α a + β b + γ c
α+β+γ = 1
α,β,γ ≥ 0  ⇔  inside (boundary = policy)

α = area(pbc)/area(abc)     area = ½ cross(b−a, c−a)
if area ≈ 0: skip (degenerate)

test at (x+0.5, y+0.5)
bbox is a reject, not the triangle
```""",
        slides=[],
        hook_say="GPUs fill triangles. Today we do it with signed area — the same cross as Computational Geometry’s orient. A line is not a thin triangle.",
        hook_ask="Barycentric of a vertex a? Wait. Want: (1,0,0).",
        frame_say="DDA walks the long axis; Bresenham is named, not derived. Half-planes vs barycentric: we implement barycentric. Top-left fill rule: cracks otherwise. Course policy: α,β,γ ≥ −eps, or document double-draw and let z-buffer hide it in 3D. Same formula later for UV, n, z.",
        frame_ask="Why not loop the whole canvas for every triangle?",
        build=[
            "**Say:** Signed area. Unsigned area kills a CW triangle. Prefer signed + abs in the denominator, or skip if area ≈ 0.",
            "**Board:** triangle, a pixel, αβγ. Two triangles of a quad; shared edge. Pixel-center overlay.",
            "**Say:** Bounding box = AABB reject, like computational geometry. The box is not the triangle.",
        ],
        ask_build="Barycentric of the centroid? Want: (1/3,1/3,1/3).",
        they_build="On paper: relate orient / signed area to α. Why pixel centers, not integer corners.",
        show_say="Draggable 2D triangle; RGB = αβγ*255; dashed bbox; degenerate button. Demo 04-barycentric.html. Plant unsigned area. Plant α+β+γ === 1 without eps, rejecting everyone.",
        attempt_say="barycentric returning null if degenerate. Eight minutes. Tests: vertex, centroid, outside.",
        land_say="Lab: barycentric + fillTriangle + a quad. Homework: eight tests including on-edge and degenerate. Quiz: vertex, centroid, degenerate policy, why bbox is not enough.",
        live=[
            ("0–10", "DDA line stub", "Do not rasterize lines as triangles."),
            ("10–35", "Barycentric fill RGB=αβγ", "Plant integer-corner tests → holes."),
            ("35–50", "Drag through collinear", "Must not crash. Signed area sign flip."),
            ("50–60", "They fill a quad", "Shared edge. Circulate."),
        ],
        cut="Bresenham derivation. Keep barycentric + degenerate skip.",
        add="Strict γ > 0 as a toy top-left rule.",
    )
    GOLD[(C, 4)] = dict(
        kernel="vec3: dot, cross, normalize, add, sub, scale; point ≠ vector; 2D cross = signed area",
        success="they refuse p+q, get a vector from p−q, and rotate a 2D point with a 2×2 matrix",
        invariant="a picture is an array; putPixel lives in pixels",
        goal="the math they thought they knew, now tied to a renderer",
        board="""```
point  w=1   affine M
vector w=0   linear part (no t)
normal       (M⁻¹)ᵀ   (Week 6/10)

dot: |a||b|cosθ     Lambert will be n·l
cross 3D: RH perpendicular
2D cross: ax by − ay bx   =  orient’s kernel

normalize(0) → policy, not NaN
```""",
        slides=[],
        hook_say="Last week signed area filled a triangle. That was a 2D cross. Today points are not arrows. Adding two points is a type error until you meant a midpoint.",
        hook_ask="Point minus point is a …? Wait. Want: vector.",
        frame_say="A frame is origin plus axes. M’s columns (column vectors) are object axes and origin in world. Do not drown in abstract LA. One picture: a cube’s local x drawn in the world. slerp is not this week; lerp of points along a segment is homework.",
        frame_ask="Do normals transform with M? Want: no — normal matrix.",
        build=[
            "**Say:** orient(a,b,c) is sign(cross(b−a,c−a)). Same algebra as Comp Geo.",
            "**Board:** point vs vector. RH cross. Object axes in the world.",
            "**Say:** Zero vector: do not divide. Skip or return (0,1,0) and document it.",
        ],
        ask_build="2D cross of (2,0) and (0,3)? Want: 6.",
        they_build="On paper: why p+q is meaningless. RH rule for cross(i,j).",
        show_say="Orbit a point with cos/sin, then 2×2 matrix — same picture. Draw i,j after rotation. Console: dot orthogonal = 0, cross(i,j)=k. Demo 06-vec3.html. Plant left-handed cross ‘until it looks right.’",
        attempt_say="normalize and a test that (0,0,0) is not NaN. Eight minutes.",
        land_say="Lab: vec3.js tests + draggable vector. Homework: lerp of points; written p+q. Quiz: p−p, unit dot, 2D cross, normals vs M.",
        live=[
            ("0–15", "Point vs vector on the board", "Plant p+q as midpoint without ½."),
            ("15–40", "cos/sin then matrix", "Same picture or the matrix is wrong."),
            ("40–50", "cross(i,j)=k", "Plant swapped args."),
            ("50–60", "They write normalize", "Zero policy. Circulate."),
        ],
        cut="Normal-matrix derivation. Keep types + 2×2 rotate.",
        add="Orthonormal basis from look+up as a name — Week 7 lookAt.",
    )
    GOLD[(C, 5)] = dict(
        kernel="mat4 multiply; T, Rx/Ry/Rz, S; T(c) R T(−c) about a center; w=1 vs w=0",
        success="they can rotate a triangle about its centroid and say T R ≠ R T",
        invariant="a picture is an array; putPixel lives in pixels",
        goal="4×4 so translation and (later) projection share one multiply",
        board="""```
[ L  t ] [ x ]   [ Lx + t ]
[ 0  1 ] [ 1 ] = [   1    ]

column vectors: nearest matrix acts first
T * R * p     rotate about origin, then translate
R * T * p     translate, then orbit the origin

about c:  T(c) * R * T(−c) * p

T(t)⁻¹ = T(−t)    R⁻¹ = Rᵀ    S(s)⁻¹ = S(1/s)
```""",
        slides=[],
        hook_say="A 3×3 cannot translate. Homogeneous w=1 is a point; w=0 is a direction so t does not apply. Composition order is the whole of scene graphs next week.",
        hook_ask="Does T R equal R T? Wait. Want: no.",
        frame_say="Draw Ry on the board. Confirm with (1,0,0) at small +θ. If Three.js disagrees later, the matrix drifted — fix the matrix, do not flip θ in five places. Row-vector APIs reverse the product; we do not use them. Document m[col*4+row] vs row-major and pick one.",
        frame_ask="w for a direction?",
        build=[
            "**Say:** Affine = Lx + t. Homogeneous packs it.",
            "**Board:** T R vs R T on a stick figure. Homogeneous columns. Three arrows for rotate-about-c.",
            "**Say:** Inverse of a matrix with translation is not a transpose.",
        ],
        ask_build="How do you rotate about c?",
        they_build="By hand: 2×2 rotate (1,0) by 90°. Then T(1,0,0)*p for p=(0,0,0,1).",
        show_say="mul, mulVec. Triangle at origin, Ry slider. Offset it — swings around origin. Then T(c) R T(−c) about centroid. Print the matrix. Demo 07-mat4-order.html and 08-rotate-center.html. Plant translating after a fake P.",
        attempt_say="rotateY of a point. Eight minutes. Write the expected vector from the board into the test.",
        land_say="Lab: mat4 identity/mul/translate/rotateY/scale; rotate-about-center; A-vs-B button. Homework: rotateX/Z; why w=0. Quiz: write T, TR vs RT, about c, w.",
        live=[
            ("0–15", "T as last column", "Plant transposing a T to invert."),
            ("15–40", "T*R vs R*T animation", "They must see they differ."),
            ("40–55", "About centroid", "Clap when it works."),
            ("55–60", "They toggle order", "Circulate."),
        ],
        cut="Generic inverse derivation. Keep order + about-c.",
        add="A known T*R inverse test.",
    )
    GOLD[(C, 6)] = dict(
        kernel="world(node) = world(parent) * local(node); Node { local, children, mesh }",
        success="moving the parent moves the child; rotating the child does not move the parent; axes draw",
        invariant="a picture is an array; putPixel lives in pixels",
        goal="a solar system / arm from a tree of transforms — how glTF and Three.js store scenes",
        board="""```
M : object → world
columns of M = object axes + origin in world

world(node) = world(parent) * local(node)
world(root) = local(root)

Earth = worldSun * localEarth     (not T(orbit) alone)

n' = normalize( (M⁻¹)ᵀ n )   if non-uniform scale
```""",
        slides=[],
        hook_say="Last week T(c) R T(−c). Today that product lives on a tree. Three.js Object3D.matrix is this. Instancing is the same mesh, different M — do not clone vertex arrays.",
        hook_ask="world = ? * local  (column vectors). Wait. Want: parentWorld * local.",
        frame_say="DFS, pass parentWorld down. Cycles forbidden. Debug RGB axes at each node using world rotation; ignore huge scale. Normal matrix: name it now so the midterm can ask why; implement in Week 10.",
        frame_ask="Why does non-uniform scale break normals?",
        build=[
            "**Say:** Model matrix is the object frame written in world coordinates.",
            "**Board:** nested frames Sun–Earth–Moon. Tree with matrices on edges. RGB axes on a tilted cube.",
            "**Say:** Robot arm shoulder*elbow*wrist is the midterm product.",
        ],
        ask_build="Write the product for a 3-node leaf.",
        they_build="On paper: expand worldMoon as named matrices. Instancing vs cloning vertices.",
        show_say="Sun/Earth/Moon, time t, orbit sliders, axes. Pause: Earth’s world is not T(orbit) if parented badly. Demo 09-scene-graph.html. Plant local*parent. Plant updating local from world every frame.",
        attempt_say="draw(node, parentWorld). Eight minutes. One parent, one child.",
        land_say="Lab: two-bone arm or turret; key A toggles axes. Homework: scene graph JSON or clean solar system. Quiz: what M does, world=parent*local, 3-node product, normal matrix name.",
        live=[
            ("0–15", "One node M", "Plant row-vector multiply."),
            ("15–40", "Sun Earth Moon", "Bad parenting: Earth inherits Sun spin."),
            ("40–50", "Axes debug", "Finds bad locals faster than a debugger."),
            ("50–60", "They parent a moon", "Circulate."),
        ],
        cut="glTF loader. Keep parent×local + axes.",
        add="Key to pause time.",
    )
    GOLD[(C, 7)] = dict(
        kernel="lookAt(eye, target, up); V = C⁻¹; after V the eye is at origin looking −Z",
        success="V*eye ≈ 0; moving the camera left moves the scene right; degenerate up is not NaN",
        invariant="a picture is an array; putPixel lives in pixels",
        goal="the view matrix is the inverse of the camera’s world transform",
        board="""```
w = normalize(eye − target)     // look −Z in view
u = normalize(cross(up, w))     // derive on the board
v = cross(w, u)

V = [ uᵀ  −u·eye ]
    [ vᵀ  −v·eye ]
    [ wᵀ  −w·eye ]
    [ 0    1     ]

eye (0,0,5), target origin, up (0,1,0)
  →  w = (0,0,1)   camera at +Z looking at origin
```""",
        slides=[],
        hook_say="M put the cube in the world. Today V puts the world in the camera. Students get the (0,0,5) example wrong every year. Spend the time. Three.js orbit is a five-minute oracle, then close it — they still write lookAt.",
        hook_ask="After V, where is the eye? Wait. Want: origin.",
        frame_say="Camera looks −Z in view space. Standard lookAt: V*eye=0 and target on −Z. Duality: camera right = world left. Do not mix both in one frame without a story. FPS: move eye in u/w, recompute lookAt. Hand out the midterm topic list at the end: spaces, barycentric, matrix order, point vs vector, scene-graph product, lookAt. No P on the exam.",
        frame_ask="What if up is parallel to look?",
        build=[
            "**Say:** Draw the camera at +Z looking at origin. Walk u,v,w.",
            "**Board:** V as change to camera frame. Duality arrows.",
            "**Say:** Match your u,v,w to the closed-form layout in live coding. Tests: V*vec4(eye,1)≈0.",
        ],
        ask_build="Why −Z look in this course? Want: freeze with WebGL/Three.js later.",
        they_build="On paper: V as inverse of C, 6–8 sentences. Degenerate up policy.",
        show_say="Implement lookAt. Fly around Week 6 solar system. Sliders eye x,y,z. Reset (0,2,8). Degenerate up → NaN then fallback. Optional 5 min Three.js orbit: camera.position is eye; engine builds V; close it. Demo 10-lookat.html. Plant cross(w,up) until it ‘looks okay.’",
        attempt_say="lookAt fixture: eye z=5, target origin. Eight minutes. No Three.js lookAt in the lab.",
        land_say="Lab: lookAt tests, WASD or sliders, camera axes in world, look-at-origin button. Homework: three fixtures including tilted up. Quiz: eye/target/up, where is the eye, −Z, V*eye. Topic list for Week 8.",
        live=[
            ("0–15", "Numeric (0,0,5) example", "They will swap w sign. Draw it."),
            ("15–40", "lookAt + solar system", "Plant V = I and moving the model."),
            ("40–50", "Degenerate up", "Fallback up. Show NaN first."),
            ("50–60", "Oracle 5 min then close", "Back to student lookAt."),
        ],
        cut="FPS collision. Keep lookAt + V*eye.",
        add="Draw camera axes in world.",
    )
    GOLD[(C, 8)] = dict(
        kernel="perspective(fov, aspect, near, far); ortho; last row copies −z into w; near>0",
        success="after the exam they can toggle ortho/perspective on the cube and read clip.w; cube grows when fov shrinks",
        invariant="a picture is an array; putPixel lives in pixels",
        goal="midterm, then P — we promised not to derive P until now",
        kind="midterm",
        midterm_topics="six spaces; P*V*M; canvas vs world origin; over; barycentric centroid and pixel centers; point vs vector (w); T R vs R T; rotate about c; 2×2 rotation; scene-graph leaf product; lookAt; V*eye; degenerate up; normal matrix name only. No full P derivation on the paper.",
        board="""```
ortho: box → clip cube     no foreshorten
persp: frustum  fov (radians, vertical)  aspect  near  far

sy = 1/tan(fov/2)    sx = sy/aspect
P last row (0,0,−1,0)  copies −z into w

near > 0     far > near     near = 0 forbidden
Do not divide by w today — look at clip.w. Divide is Week 9.
```""",
        slides=[],
        hook_say="This meeting is a **midterm**, then perspective. No laptop. After: we finally write P. If the cube is behind the camera, V is wrong — do not ‘fix’ P.",
        show_say="perspective and ortho. Course cube, M=I, V=lookAt, P=perspective. Toggle ortho. Print p_clip for one vertex. Demo 11-perspective.html. Plant fov in degrees into tan. Plant aspect = height/width.",
        attempt_say="Slider fov. Cube must grow when fov shrinks. Aspect from canvas width/height.",
        land_say="Lab: perspective unit test (point on look axis, ndc.x≈0 after divide — divide in JS for the test is OK). Ortho toggle. Homework: why huge far/near hurts depth (tease Week 9). No quiz. Next quiz: camera + projection.",
        live=[
            ("0–15", "Write P once; test a center-line point", "Plant near=0."),
            ("15–40", "Cube foreshortens", "If behind camera, fix V not P."),
            ("40–60", "Ortho toggle", "Flat engineering drawing vs recede."),
        ],
        cut="Full a,b derivation from near/far if time is gone. Quote Shirley / Scratchapixel and test a point.",
        add="Print clip.w for a near vs far vertex.",
    )
    GOLD[(C, 9)] = dict(
        kernel="ndc = clip.xyz/clip.w; viewport with y-flip; z-buffer compare documented; never near=0",
        success="two overlapping triangles occlude correctly; disable depth shows painter’s-order bug; z as grayscale",
        invariant="a picture is an array; putPixel lives in pixels",
        goal="a correct 3D triangle rasterizer: transform, divide, viewport, depth",
        board="""```
p_clip = P V M p
ndc = clip.xyz / clip.w          [−1,1] if inside

sx = (ndc.x*0.5+0.5)*width
sy = (1 − (ndc.y*0.5+0.5))*height    // canvas y down

z01 = ndc.z*0.5+0.5     pick 0-near or 1-near; match compare
if z < depth[i]: depth[i]=z; putPixel

drop triangle if any w ≤ eps     (full clipper not required)
```""",
        slides=[],
        hook_say="P is built. Today we divide, flip y because canvas grows down, and keep a second image called depth. A correct z-buffer on a plain canvas beats a pretty wrong cube.",
        hook_ask="Why flip y for Canvas? Wait. Want: NDC +Y vs canvas +Y down.",
        frame_say="Clip volume −w≤x,y,z≤w. Straddle near → garbage divide; policy: drop if w≤eps or ndc out of range. Optional lerp-clip; no Sutherland–Hodgman. Affine z in NDC is acceptable if documented. Perspective-correct z is extra. Do not invent fps.",
        frame_ask="Who wins when two triangles overlap?",
        build=[
            "**Say:** Divide after P, not before.",
            "**Board:** clip cube → square NDC → canvas + y-flip. Z-buffer as a second image.",
            "**Say:** Z-fighting: near too small, far too large, coplanar. Push near out. Polygon offset: name only.",
        ],
        ask_build="Depth init value? Want: +∞ or 1.0 if using [0,1] far.",
        they_build="On paper: y-flip formula, one picture. Why near=0.0001 is a bad idea.",
        show_say="Full cube, 12 triangles, PVM, divide, viewport, screen-space barycentric, z-buffer. Color=gray(z). Without depth, back faces scribble. Demo 12-zbuffer.html. Plant sy without flip then negating Ry forever. Plant clearing color but not depth.",
        attempt_say="viewport(ndc,w,h) with a y-flip test. Eight minutes.",
        land_say="Lab: z-buffer cube; toggle depth; toggle z-visualize; a piercing triangle. Homework: init+compare documented. Quiz: NDC from clip, y-flip, depth init, who wins.",
        live=[
            ("0–15", "Divide + print ndc", "Plant dividing before P."),
            ("15–40", "Viewport y-flip", "Upside-down cube is this, not Ry."),
            ("40–55", "Z-buffer two triangles", "Disable depth = bug."),
            ("55–60", "They paint z grayscale", "Circulate."),
        ],
        cut="Perspective-correct z. Keep divide + y-flip + z-buffer.",
        add="Culling as optional if depth is correct — Week 10.",
    )
    GOLD[(C, 10)] = dict(
        kernel="Lambert: kd*max(0,n·l)+ka*ambient; face n=normalize(cross(b−a,c−a)); same space for n and l",
        success="rotating the light moves the terminator; debug n*0.5+0.5 is colorful; they can say culling ≠ black Lambert",
        invariant="a picture is an array; putPixel lives in pixels",
        goal="a lit cube that is not each face a random color",
        board="""```
n_face = normalize(cross(b−a, c−a))     CCW
n_world = normalize( (M⁻¹)ᵀ n_obj )

l = unit toward the light     (write it)
diff = kd * max(0, n·l)
color = ka*ambient + diff*lightColor

flat: one n per face
Gouraud: Lambert at vertices, interpolate color

cull: not drawn     n·l<0: drawn, dark
```""",
        slides=[],
        hook_say="Depth made a solid cube. Today it is not a random crayon. Freeze light space: world or view — pick one. Mixing world n with view l is the classic bug.",
        hook_ask="Why max(0, n·l)? Wait. Want: the back of the surface gets no light, not negative light.",
        frame_say="Vertex normals vs face normals. Sphere needs vertices; faceted cube can use faces. Point light: l=normalize(lightPos−p); extra, not required. Gouraud smears highlights — Phong-interpolate n in Week 11 if Gouraud works.",
        frame_ask="Same space for n and l — why?",
        build=[
            "**Say:** ka is a projector policy against pure black.",
            "**Board:** n and l, θ. Non-uniform scale wrong vs right normals. Gouraud colors at vertices.",
            "**Say:** Back-face culling is winding. A front face with n·l<0 is still drawn.",
        ],
        ask_build="Face normal formula from three vertices.",
        they_build="On paper: one picture of non-uniform scale on a circle. Why (M⁻¹)ᵀ.",
        show_say="Per-face Lambert, light-angle sliders, ambient slider, cull toggle (projected winding). Debug n*0.5+0.5. Demo 13-lambert.html. Plant l toward the surface → black cube. Plant lighting in object space while the camera moved.",
        attempt_say="lambert(n,l,kd,ka). Eight minutes.",
        land_say="Lab: face-Lambert cube; Gouraud; normalMatrix(M); normals debug. Homework: transformNormal. Quiz: face n, why max, same space, cull vs Lambert.",
        live=[
            ("0–15", "Face n + one light", "Plant unnormalized n."),
            ("15–40", "Move the light", "Terminator must move."),
            ("40–50", "Gouraud vs flat", "Cube with face n at vertices looks faceted — OK."),
            ("50–60", "Debug normals view", "Black = a bug."),
        ],
        cut="Point-light falloff. Keep directional Lambert + same space.",
        add="Toggle culling vs dark faces.",
    )
    GOLD[(C, 11)] = dict(
        kernel="Blinn: h=normalize(l+v); spec=(max(0,n·h))^shininess; linear light; pow(c,1/2.2) at the end",
        success="the highlight moves with the camera; gamma toggle is visible; two lights sum; they say this is not PBR",
        invariant="a picture is an array; putPixel lives in pixels",
        goal="specular and a gamma-aware output",
        board="""```
v = normalize(eye − p)          same space as n
Phong: r = reflect(−l, n)       spec = (max(0,r·v))^s
Blinn: h = normalize(l + v)     spec = (max(0,n·h))^s

if n·l ≤ 0: skip spec

light in linear
out: pow(linear, 1/2.2) then *255

not energy-conserving; PBR is Semester 4
```""",
        slides=[],
        hook_say="Lambert is the moon. Specular is the highlight that depends on v. If the highlight does not move when the camera moves, they used a constant v. Do not invent fps; do not raise shininess until it looks Instagram.",
        hook_ask="Half-vector formula? Wait. Want: normalize(l+v).",
        frame_say="Shininess 16–64 for a cube; 256 is a pin spark; 0.5 is not roughness. Sum lights then min(1,color) or float then encode once. HDR/bloom is Real-Time Rendering. Toggle wrong (light in sRGB) vs right — the wrong one often ‘looks contrasty’; the projector lies; the policy stands.",
        frame_ask="Where does gamma encode happen?",
        build=[
            "**Say:** Is Blinn-Phong PBR? No.",
            "**Board:** n,l,v,r,h. Linear add vs sRGB add. Two lights, two highlights.",
            "**Say:** Per-pixel: interpolate n, normalize, shade — if Gouraud from last week works.",
        ],
        ask_build="Why skip spec when n·l<0?",
        they_build="On paper: h vs r, one picture. Why lighting in sRGB is wrong, one paragraph.",
        show_say="Blinn-Phong cube, shininess slider, two lights, gamma toggle, specular-only (kd=0). Demo 14-blinn-phong.html. Plant v=(0,0,1) forever. Plant adding spec in sRGB then encoding again.",
        attempt_say="blinnPhong tests: n=l=v → spec>0; n opposite l → spec 0. Eight minutes.",
        land_say="Lab: two lights; gamma encode; debug keys N/L/S. Homework: shininess slider in README. Quiz: h, skip spec, where encode, not PBR.",
        live=[
            ("0–15", "h vs r on the board", "They copy."),
            ("15–40", "Highlight vs camera", "Must move. Constant v is the plant."),
            ("40–50", "Gamma toggle", "Do not invent a Lighthouse score."),
            ("50–60", "Two lights", "Clip uint8; mention it."),
        ],
        cut="Cook-Torrance. Keep Blinn + encode at the end.",
        add="Normals-as-color debug already from Week 10.",
    )
    GOLD[(C, 12)] = dict(
        kernel="UV interpolant; sampleNearest; albedo * Lambert; affine UV is wrong in perspective (picture)",
        success="a textured cube or floor; UV debug (u,v,0); they can say texture is not lighting",
        invariant="a picture is an array; putPixel lives in pixels",
        goal="UVs are just another interpolant",
        board="""```
UV in [0,1]    pick image origin (PNG top-left vs glTF bottom-left) and freeze
wrap: u − floor(u)     clamp: min(1,max(0,u))

nearest: floor(u*width), floor(v*height)

affine screen UV bows on a perspective quad
correct: interpolate u/z, v/z, 1/z     (picture; extra to implement)

albedo = sample     color = lambert * albedo
mipmaps: name; lab is nearest
```""",
        slides=[],
        hook_say="A texture is not a reason to skip normals. If it is upside-down, flip v=1−v once on the board — do not randomly swap four vertices. file:// may block image load: procedural checker is a valid lab.",
        hook_ask="Does texture replace lighting? Wait. Want: no.",
        frame_ask="Why affine UV fails in perspective?",
        frame_say="Mag: nearest vs bilinear (name; extra). Min: many texels per pixel → aliasing; mipmaps are the word games use. Spec often not multiplied by albedo — policy. Do not invent fps.",
        build=[
            "**Say:** Same barycentric as color and z.",
            "**Board:** UV square on a mesh. Nearest vs bilinear 2×2. Trapezoid road, affine vs correct.",
            "**Say:** Integer UV 0–width mixed with 0–1 is the classic smear.",
        ],
        ask_build="Nearest sample formula.",
        they_build="On paper: trapezoid road, affine vs correct. Mipmaps in three sentences.",
        show_say="Load PNG into ImageData or checker. Textured quad facing camera, then UVs on the cube. UV debug RGB=(u,v,0). Demo 15-texture.html. Plant one UV for the whole cube. Plant sampling v from the wrong origin then rotating the PNG.",
        attempt_say="sampleNearest(tex,u,v) with clamp. Eight minutes.",
        land_say="Lab: textured cube or perspective floor (to see affine bug); UV debug; checker fallback. Homework: clamp vs repeat. Quiz: UV not a position, nearest, affine fail, texture≠lighting.",
        live=[
            ("0–15", "UV on a quad", "Plant origin confusion; freeze v-flip."),
            ("15–40", "sampleNearest", "Plant u in 0–width."),
            ("40–50", "Perspective floor affine bug", "Describe 1/z; extra to code."),
            ("50–60", "Albedo * Lambert", "Unlit texture is a debug view, not the shader."),
        ],
        cut="Mipmap chain. Keep nearest + affine picture.",
        add="Bilinear four taps as extra.",
    )
    GOLD[(C, 13)] = dict(
        kernel="same cube: CPU putPixel/bary/z/PVM/Lambert/sample → GPU fragment/raster/DEPTH/gl_Position/texture(); Three.js is an oracle",
        success="they fill u_model, u_view, u_proj from their mat4 (or a mapping table if Three.js); software-only slice is complete if WebGL failed",
        invariant="a picture is an array; putPixel lives in pixels",
        goal="map their renderer onto WebGL2; do not abandon what they wrote",
        board="""```
CPU putPixel          →  fragment write
barycentric fill      →  rasterizer (fixed)
z-buffer              →  DEPTH_TEST
P * V * M             →  vertex gl_Position
Lambert / Blinn       →  fragment shader
sampleNearest         →  texture() + sampler

Three.js: projectionMatrix = P
          matrixWorldInverse = V
          mesh.matrixWorld = M
Raycaster = Comp Geo, not lighting
```""",
        slides=[],
        hook_say="Week 13 is the same scene on the GPU, not a new engine. Joint note with Computational Geometry: picking is ray vs triangle. A library is windowing and decode, not the student claim ‘I wrote a renderer.’",
        hook_ask="matrixWorldInverse is which matrix? Wait. Want: V.",
        frame_say="Students may copy WebGL boilerplate; they must fill uniforms from their math if they claim the math. Checkpoint: mesh, camera, one light, texture or debug UV/n, depth, README student-vs-library. Black-screen checklist: canvas size, camera, near, winding. Do not invent fps. Do not grow fov until the cube ‘shows up’ — fix V.",
        frame_ask="May Three.js Raycaster be the student picking algorithm? Want: no.",
        build=[
            "**Say:** Leave the GPU column empty; fill with the class.",
            "**Board:** payoff table. Vertex vs fragment boxes. Same cube, two windows.",
            "**Say:** Vertex shader is Weeks 5–9. Fragment is Weeks 10–12. enable DEPTH_TEST, CULL_FACE, CCW.",
        ],
        ask_build="Where does gl_Position sit in the space chain? Want: clip.",
        they_build="On paper: CPU function → GPU stage, one page. That table is homework in the repo.",
        show_say="Port the course cube to WebGL2: Lambert, one texture, same lookAt. Side-by-side software vs WebGL if possible. Use WebGL/demos/index.html (01–04, 06) if stuck on boilerplate. Demo 16-webgl-cube.html. When it mismatches: NDC y, winding, linear/sRGB, light space. Plant Three.js checkpoint with no mapping table.",
        attempt_say="Point at u_proj * u_view * u_model in the shader. Eight minutes.",
        land_say="Lab is the project checkpoint. Software-only is complete. WebGL-only is complete if they explain each uniform. Both is the A path. Homework: project + the table. Quiz: gl_Position, depth test, black-screen cause, matrixWorldInverse, Raycaster.",
        live=[
            ("0–15", "Fill the payoff table live", "They name GPU stages."),
            ("15–40", "WebGL2 cube uniforms from their mat4", "Plant sRGB texture vs CPU gamma."),
            ("40–50", "Three.js oracle: P, V, M hiding places", "Close it. Table still required."),
            ("50–60", "Picking sentence", "Ray vs triangle, not ‘the engine knows.’"),
        ],
        cut="Second shader pass. Keep one program + the table.",
        add="Print shader compile logs.",
    )
    GOLD[(C, 14)] = dict(
        kernel="running pipeline + one debug view (n / UV / depth) + README that serves; freeze: cube+Lambert+texture beats broken glTF",
        success="a TA can serve the folder, see more than an untransformed triangle, and hear where M,V,P are",
        invariant="a picture is an array; putPixel lives in pixels",
        goal="studio — not a content lecture",
        kind="studio",
        board="""```
Report: problem · weeks used · pipeline · hard case · kernel vs lib · results · limits · refs
Defense: M V P order?  divide by w?  debug view?  disable depth?  library vs you?
         affine UV?  where encode?  left-handed API?

Must: serve · debug view · who wrote which file
Cuts: glTF/PBR/shadows → cube+Lambert+texture
      dual CPU/GPU → one path + mapping table
      city graph → two nodes
Do not invent fps. If you did not measure, say so.
```""",
        slides=[],
        hook_say="This meeting is **studio**. No PBR lecture. If they are stuck on a matrix, debug the matrix. A correct z-buffer on canvas beats a broken gltf dump. Three people, one git author is a failure mode.",
        hook_ask="If behind, what do you cut first?",
        frame_say="Desk order: mat4/shaders, camera, rasterizer or depth test, report outline. Comment on the pipeline, not the CSS. Rehearse 12+5 once with a TA timer: 0–2 problem, 2–6 pipeline+limitation, 6–10 live debug view, 10–12 who did what.",
        show_say="Volunteer against the board. Pretty Three.js with no student matrix fails.",
        attempt_say="Studio. Serve first. One debug view. Recording draft.",
        land_say="Report draft + 30s recording due before Week 15. Next week 12+5. No quiz.",
        live=[
            ("0–10", "Eight headings + eight questions + clock", "Photograph."),
            ("10–50", "Desk review", "Kernel, then camera, then depth, then outline."),
            ("50–60", "60s rehearsal", "Hard stop."),
        ],
        cut="New libraries. Keep freeze.",
        add="Waiver only for a documented recovery plan on a single triangle.",
    )
    GOLD[(C, 15)] = dict(
        kernel="12+5; live demo of the student pipeline; point at M,V,P and a debug view",
        success="they stop at 12; if the demo dies, play the recording — do not debug five minutes on stage",
        invariant="no new features today",
        goal="presentations — not a content lecture",
        kind="presentations",
        board="""```
12 + 5
Show: M V P product · divide by w · one debug view
No new shaders on stage
Software rasterizers first, then WebGL ports
```""",
        slides=[("Timer", "not a slide of PBR")],
        hook_say="Presentations. 12+5. Repo, 6–8 page report, 30s recording. Order: software first, then GPU ports. Graphics in this program is naming the space, writing the product, looking at a debug view, only then switching on a library.",
        show_say="None. Present. Ask two from the Week 14 list plus one from their code.",
        attempt_say="Present.",
        land_say="That habit is WebGL, Three.js, Real-Time Rendering, and the capstone. Grades close when report and repo are in.",
        live=[("0–60", "Talks", "Cut at 12. Play recording if HDMI dies.")],
        cut="Debugging on stage.",
        add="One question: what would break in a left-handed API?",
    )


def _register_compgeo(GOLD: dict) -> None:
    C = "Computational Geometry"
    GOLD[(C, 1)] = dict(
        kernel="orient(a,b,c) = sign of cross(b−a, c−a); LEFT / RIGHT / COLLINEAR; atan2 is the wrong primitive",
        success="they can color a triangle left/right/collinear, print the raw cross, and say why not atan2",
        invariant="predicates before constructions; degeneracy is the course",
        goal="see that graphics already is computational geometry; freeze predicates, degeneracy, visualization",
        board="""```
cross(b−a, c−a) = (bx−ax)(cy−ay) − (by−ay)(cx−ax)
>0 LEFT of directed ab (CCW)    =0 COLLINEAR    <0 RIGHT
area = cross / 2

predicate: discrete answer     construction: new geometry
atan2: slow, wraps ±π, branch cut     cross: four sub, two mul

degenerate: collinear hull · T-junction · overlap · duplicate verts
1e20 can swallow a 1 in IEEE — detect; do not hope
```""",
        slides=[],
        hook_say="Does this click hit the polygon? Do these walls cross? That is this course. 2D first; 3D is the same idea with one extra coordinate. A construction inherits the predicate’s errors — implement predicates first.",
        hook_ask="Is the intersection point of two lines a predicate or a construction? Wait. Want: construction.",
        frame_say="Four flagships: closest pair, hull, segment intersection, point in polygon. Fifth family named: proximity and search. Course policy: detect degeneracy, write a policy, write a test, never ==0 on a float without saying EPS. EPS does not solve everything — Week 13 robustness. We will not implement full Fortune, Kirkpatrick, 3D Delaunay, CGAL kernels; we name them. JS + Canvas. Labs 25, hw 20, quizzes 10, midterm 15, project 30.",
        frame_ask="Why is sorting polar angles a bad replacement for orient?",
        build=[
            "**Say:** AB is directed. orient(a,b,c) is not orient(b,a,c).",
            "**Board:** triangle ABC, arrow on AB, +/− on C. Four flagship thumbnails. 15-week map: primitives, hulls, sweep/tri, proximity/search, project.",
            "**Say:** I subtract A first so the test is translation-invariant. I print the raw value so near-zero is visible. I do not call Math.atan2.",
        ],
        ask_build="cross for A=(0,0), B=(2,0), C=(1,3) — left/right?",
        they_build="On paper: why cross beats polar angles for left-of-line, half page. One fragile float input (explain the risk).",
        show_say="Visualizer from zero: click add, drag, reset, coordinates. Three points: segment AB, fill green/red/gray by orient, print LEFT/RIGHT/COLLINEAR and raw cross. Demo Computational Geometry/code/01-orient.html. Plant atan2. Plant cross===0 as ‘exact.’",
        attempt_say="orient with eps. Eight minutes. Four console tests: left, right, collinear-between, collinear-beyond.",
        land_say="Lab: distance, midpoint, signed area, ‘make C collinear’ button. Homework: 8 tests including C=A, tiny triangle, translated copy. Quiz: cross, predicate vs construction, two degeneracies, why not atan2.",
        live=[
            ("0–10", "Click / drag visualizer", "A visualizer that cannot move points cannot show degeneracy."),
            ("10–35", "orient + raw cross", "Plant atan2. Print v."),
            ("35–50", "Drag to collinear", "Gray + near-zero."),
            ("50–60", "They add signed area", "Circulate."),
        ],
        cut="Shewchuk details. Keep orient + degeneracy pictures.",
        add="Reduce point-in-triangle to three orient tests — name the boundary policy.",
    )
    GOLD[(C, 2)] = dict(
        kernel="onSegment = collinear + AABB; segmentsIntersect → proper|touch|overlap|none; then construct the point",
        success="they classify four pictures live and get BOUNDARY on a vertex, not a flicker",
        invariant="predicates before constructions; degeneracy is the course",
        goal="a correct kernel — everything later depends on this week",
        board="""```
onSegment(c,a,b): orient=0 AND c in AABB(ab)

proper: opposite-sign orients, zeros not opposite
touch:  endpoint on the other (T) or shared vertex
overlap: collinear 1D intervals overlap
none:   including AABB-overlap but miss

PIP even–odd: half-open edges
  (a.y>q.y) != (b.y>q.y)
onSegment first → BOUNDARY

AABB is a reject, not the answer
```""",
        slides=[],
        hook_say="Last week’s sign is this week’s intersection classifier. Classify with predicates; divide for the point only if proper or touch. The denominator is cross(B−A,D−C); near zero means parallel — do not divide.",
        hook_ask="Two AABBs overlap. Must the segments intersect? Wait. Want: no.",
        frame_say="Point, vector, segment t∈[0,1], ray t≥0, line ℝ, closed polygon. Winding number named; even–odd is enough for simple polygons. Treating touch as none breaks later DCEL and map overlay. Zero-length segment is a test, not a surprise.",
        frame_ask="Why is collinear not enough for onSegment?",
        build=[
            "**Say:** Four pictures: X, T, collinear overlap, disjoint boxes that overlap.",
            "**Board:** four types. Ray through a vertex, then the half-open rule. AABB counterexample.",
            "**Say:** Return type includes point for proper and touch.",
        ],
        ask_build="A=(0,0),B=(4,0),C=(2,2),D=(2,−2). Type?",
        they_build="On paper: why classify before dividing. Half-open edge rule, one paragraph.",
        show_say="Two segments, four draggable ends. Color green/orange/purple/gray. Draw the point. Overlay AABBs. Script all four cases. Pause on boxes-overlap/no-hit: ‘the box is not the algorithm.’ Demo 03-segments.html. Plant ==0. Plant counting both edges on a vertex hit.",
        attempt_say="onSegment then proper-only intersect. Eight minutes.",
        land_say="Lab: pointInPolygon even–odd on a concave polygon; vertex, edge, ray-hits-vertex. Homework: four-way segmentsIntersect + identical and zero-length. Quiz: type, onSegment, vertex-hit drawing, AABB converse.",
        live=[
            ("0–10", "Five objects", "Polygon is closed: last→first."),
            ("10–35", "Four intersection types live", "Plant dividing while parallel."),
            ("35–50", "AABB overlap, miss", "Dashed boxes."),
            ("50–60", "Ray through vertex plant", "Then half-open."),
        ],
        cut="Full winding-number holes. Keep four types + PIP vertex bug.",
        add="Shared endpoint as touch.",
    )
    GOLD[(C, 3)] = dict(
        kernel="classify: SELF_INTERSECTING | SIMPLE_CONCAVE | CONVEX via same-turn + non-adjacent proper intersects; shoelace signed area",
        success="a bowtie is not convex; a C-shape is simple concave; reflex vertices light up; signed area gives CW/CCW",
        invariant="predicates before constructions; degeneracy is the course",
        goal="say whether a polygon is convex, simple, or neither, and why algorithms care",
        board="""```
convex set: segment pq stays inside
convex polygon: simple AND interior convex
reflex: interior >180°  ⇔  turn disagrees with sign(A)

simple + all turns same sign  ⇔  convex
bowtie: consistent turns on each lobe, not a convex polygon
        (simplicity required)

2A = Σ (xi yi+1 − xi+1 yi)     sign(A) = orientation
```""",
        slides=[],
        hook_say="A UI blob or a font outline that self-intersects triangulates into garbage. We reject self-intersection rather than guess. Interior angles in degrees are the wrong primitive — use orient.",
        hook_ask="Is a star polygon simple? Convex? Wait. Want: usually neither (not simple).",
        frame_say="Hull of vertices always exists. Ear clipping and even–odd assume simple. SAT needs convex pieces. Adjacent edges share a vertex — do not mark them proper. FLAT vertices: document; allowed in convex by policy. Table stays up all semester: which algorithms need simple / convex.",
        frame_ask="Why does the same-turn test need simplicity?",
        build=[
            "**Say:** Convex combination; hull is all convex combinations — Week 4 will reuse that sentence.",
            "**Board:** segment stays inside. Four-polygon taxonomy. Reflex vertex. Shoelace as signed triangles from the origin.",
            "**Say:** (⇒) interior ≤180°. (⇐) local convexity; without simplicity the bowtie is the counterexample. Do not pretend a full proof.",
        ],
        ask_build="Shoelace of (0,0),(2,0),(0,2). Signed area?",
        they_build="1-page proof sketch: simple ⇔ same-turn for convexity; draw the bowtie.",
        show_say="Click polygon, Enter to close. Signed area, CW/CCW. Vertices green/orange/gray. Label CONVEX / SIMPLE_CONCAVE / SELF_INTERSECTING. Drag a hexagon until reflex; then cross non-adjacent edges. Demo 06-shoelace.html. Plant testing adjacent edges as proper. Plant |A| only, losing CW/CCW.",
        attempt_say="shoelace. Eight minutes. Hand: (0,0),(4,0),(4,3),(0,3).",
        land_say="Lab: classify + reflex highlight; fixtures convex, C, bowtie, flat. Homework: six fixtures including n=3 and duplicate-vertex square. Quiz: convex set, star, mixed turns, shoelace, why simplicity.",
        live=[
            ("0–15", "Convex set pictures", "Union of convex is not always convex."),
            ("15–40", "Classifier live", "Bowtie must not be CONVEX."),
            ("40–50", "Shoelace sign", "Reverse vertices → flip sign."),
            ("50–60", "They close a C-shape", "Circulate."),
        ],
        cut="Weakly-simple. Keep taxonomy + same-turn + shoelace.",
        add="Intersection of two convex sets is convex — one picture.",
    )
    GOLD[(C, 4)] = dict(
        kernel="Jarvis: start lowest-then-leftmost; next = all-left supporting; collinear take farthest; Θ(n h)",
        success="they can wrap 8 points by hand; circle n is slower than a cloud with h=3; no atan2",
        invariant="predicates before constructions; degeneracy is the course",
        goal="the hull as extreme points before a famous O(n log n) algorithm",
        board="""```
CH(S) = smallest convex set containing S
extreme = hull vertex = supporting line through p, S on one side

policy: unique points; drop strictly intermediate collinear

start = lowest then leftmost
o < 0: r is right of p→q → q = r
o = 0 and farther: q = r

time Θ(n h)     circle: h=n → Θ(n²)
Ω(n log n): points (xi, xi²); hull visits sorted x
```""",
        slides=[],
        hook_say="Rubber band around nails. Jarvis is output-sensitive: great when h is tiny, quadratic when points already sit on a circle. Polar angles wrap — we use orient.",
        hook_ask="Jarvis time in n and h? Wait. Want: Θ(n h).",
        frame_say="Incremental hull: idea only (tangents, O(n²) naive). 3D incremental is the later mental model. Lower bound is algebraic decision-tree teaching level: if hull were o(n log n), sorting would be too. Measure cloud vs circle; do not invent milliseconds.",
        frame_ask="Why start at lowest-then-leftmost?",
        build=[
            "**Say:** Interior points are not extreme. Collinear middles are not hull vertices under our policy.",
            "**Board:** rubber band. One full wrap on 8 points with the candidate ray. Parabola (xi,xi²) and the lower hull.",
            "**Say:** Invariant: polyline so far is a hull prefix; supporting ray has S on its left if we wrap CCW.",
        ],
        ask_build="Is Jarvis optimal for points in convex position? Why not?",
        they_build="Written: h=3 input and h=n input with Θ. Parabola reduction 6–8 sentences + 5 points.",
        show_say="Step mode: N one comparison, E one edge, Space finish. Current p/q/r colored. Time n=2000 cloud vs n=400 circle. Demo 07-jarvis.html. Plant starting at a random interior point. Plant nearest collinear (cuts the edge short). Plant duplicates infinite loop.",
        attempt_say="One wrap step: given p and candidates, pick next q. Eight minutes.",
        land_say="Lab: Jarvis; buttons cloud/circle/triangle+cloud; print n,h,elapsed; table 100/1k/10k. Homework: collinear policy + duplicate removal. Quiz: extreme point, Θ(nh), start, convex-position, sorting reduction.",
        live=[
            ("0–15", "Definitions + policy", "Drop middle collinear."),
            ("15–40", "Step-mode wrap", "q jumps when a righter point appears."),
            ("40–50", "Circle vs cloud timing", "Measure; do not invent ms."),
            ("50–60", "They implement the inner for-r", "Circulate. No atan2."),
        ],
        cut="Incremental code. Keep Jarvis + parabola.",
        add="Expected Gaussian h = O(log n) as a name.",
    )
    GOLD[(C, 5)] = dict(
        kernel="Andrew: sort (x,y); lower/upper stacks; while orient(h[-2],h[-1],p)≤0 pop; O(n log n); no atan2",
        success="all-collinear returns two endpoints; Andrew on a circle is not Θ(n²); join does not duplicate endpoints",
        invariant="predicates before constructions; degeneracy is the course",
        goal="the hull algorithm they will actually use",
        board="""```
Graham: p0 lowest-left; sort by orient(p0,a,b) not atan2; stack, pop non-left
Andrew (required):
  unique sort (x,y)
  lower L→R; upper reverse
  ≤0 pops collinear middles
  pop duplicated endpoints; concatenate

scan O(n): each point pushed/popped ≤ once per chain
Jarvis when h tiny; Andrew default

AABB is cheap and loose; hull is tight (diagonal stick)
```""",
        slides=[],
        hook_say="Graham’s danger is polar sort. Andrew never asks for an angle. 3D hull is a mesh of triangles, not a polygon — gift wrap / incremental named, not coded.",
        hook_ask="What is the sort key in Andrew? Wait. Want: (x,y).",
        frame_say="To keep collinear hull points, use <0 only. Forgetting unique-sort: consecutive duplicates are collinear with anything and ≤0 pops the world. Graphics: AABB, OBB, broad phase, silhouette = supporting line = one Jarvis step.",
        frame_ask="What does orient≤0 do to collinear hull points?",
        build=[
            "**Say:** Why the while-loop is O(n) after sorting: each index pushed/popped ≤ once.",
            "**Board:** Graham polar around p0. Andrew sorted list, two stacks, join. AABB vs hull on a diagonal stick.",
            "**Say:** Table Jarvis / Graham / Andrew. Default = Andrew.",
        ],
        ask_build="Give one case where Jarvis beats Andrew.",
        they_build="Prove the scan is O(n). One paragraph AABB vs hull as collision proxy.",
        show_say="Andrew with stacks drawn: sorted indices, lower blue, upper red, pops flash. Same 10k cloud and 2k circle as Week 4 — Andrew does not care that h=n. Demo 08-andrew.html. Plant concatenating without popping endpoints. Plant both chains L→R with the same orient test.",
        attempt_say="lower-hull while-condition on paper then in code. Eight minutes.",
        land_say="Lab: Andrew; compare Jarvis; toggle drop vs keep collinear; tests n=0,1,2, triangle, all-collinear, square+interior. Homework: document collinear policy. Quiz: sort key, O(n) while, ≤0, when Jarvis, one 3D strategy.",
        live=[
            ("0–15", "Graham without atan2", "orient(p0,a,b); nearer-first pops middles."),
            ("15–40", "Andrew step mode", "Join off-by-one is the plant."),
            ("40–50", "Circle n vs Jarvis", "Andrew stays O(n log n)."),
            ("50–60", "They unique-sort first", "Circulate."),
        ],
        cut="Conflict-graph 3D. Keep Andrew + collinear policy.",
        add="Oracle: Andrew vertex set equals Jarvis vertex set.",
    )
    GOLD[(C, 6)] = dict(
        kernel="sweep: Q events LEFT/RIGHT/INTER; T = y-order along L; test only neighbors; swap at INTER",
        success="oracle (all pairs) matches sweep on 80 segments; they can say why endpoint-y order is wrong",
        invariant="predicates before constructions; degeneracy is the course",
        goal="the sweep-line pattern, not only the intersection formula",
        board="""```
naive Θ(n²)     if I=Θ(n²) any algo is Ω(n²) to write
target O((n+I) log n)     lab list: O((n+I) n), n≤200

LEFT:  insert; test two neighbors
RIGHT: delete; test the two that meet
INTER: report; SWAP in T; test new outer neighbors

status = order along L at current x, not left-endpoint y
verticals: reject or tiny tilt, document
overlap ≠ INTER point     touch: report, do not split until Week 8
```""",
        slides=[],
        hook_say="Week 2 classified one pair. Today n segments. Drawing a vertical line and still testing every pair is not a sweep. Only neighbors in the status can be the next crossing.",
        hook_ask="After INTER, what happens in T? Wait. Want: swap.",
        frame_say="No red-black tree in the lab. Sorted list is enough. Several segments at one point: bundle reverse-order. Do not invent timings; the story is neighbor tests vs n² pairs.",
        frame_ask="If I=n²/4, is sweep asymptotically better than naive?",
        build=[
            "**Say:** Invariant: all intersections to the left of L reported; T is stabbed segments ordered by y.",
            "**Board:** sweep line, three active, T by y. Event timeline LEFT LEFT INTER RIGHT. Cross, status before/after swap.",
            "**Say:** Graphics: overlay, CAD, clip, UI strokes, mesh-repair outlines.",
        ],
        ask_build="Name the three event types.",
        they_build="1 page: why only neighbors. Counterexample: status by endpoint y misses a later cross.",
        show_say="Scrub a vertical line; status listed top to bottom; events as ticks. Script: two-cross + swap; three segments only two tests while non-adjacent; T-junction touch; AABB overlap no event. Demo 10-sweep.html (naive 09 as oracle). Plant not swapping. Plant inserting the same INTER twice and looping. Plant verticals crashing x-order.",
        attempt_say="test(s,t): if proper/touch at p with p.x≥current, insert INTER if new. Eight minutes.",
        land_say="Lab: teaching sweep + brute oracle, n≤200; document vertical policy. Homework: neighbor lemma + endpoint-y counterexample. Quiz: times, events, swap, I=n²/4, why a list is OK.",
        live=[
            ("0–10", "Naive pairs as oracle", "Correct, not the algorithm."),
            ("10–35", "Event loop + list T", "Plant testing every pair ‘because a line is drawn.’"),
            ("35–50", "Swap at INTER", "Order flips. Leave the picture up."),
            ("50–60", "They match oracle on 16 segments", "Circulate."),
        ],
        cut="BST complexity proof. Keep events + swap + neighbor lemma.",
        add="Touch as a reported event, not none.",
    )
    GOLD[(C, 7)] = dict(
        kernel="ear: convex tip + no other vertex in triangle(v−1,v,v+1); clip → n−2 triangles, O(n²); fail on bowtie",
        success="a C-shape yields n−2 triangles that fill; a bowtie throws; they have the midterm list",
        invariant="predicates before constructions; degeneracy is the course",
        goal="triangulate a simple polygon because GPUs want triangles",
        board="""```
simple n-gon: n−2 triangles, n−3 diagonals
ear tip: convex AND no other vertex in the ear triangle
Meisters: n≥4 ⇒ at least two ears

isEar: orient convex (not reflex); point-in-TRIANGLE not PIP
holes: not handled     Chazelle O(n): name only

ear clip ≠ Delaunay     CDT: name; Week 11

split vs merge vertex: label on a drawing (midterm)
```""",
        slides=[],
        hook_say="Induction: a diagonal splits; triangles add to n−2. A reflex vertex is never an ear tip — the diagonal would lie outside. Hand out the midterm list today: no Voronoi, no kd-tree, no DCEL on the paper.",
        hook_ask="How many triangles in a simple 10-gon? Wait. Want: 8. Diagonals: 7.",
        frame_say="y-monotone: two chains, O(n) after sort. Full pipeline: monotone split O(n log n) then linear — picture of start/end/split/merge/regular; do not require the sweep. Same point set can be a skinny ear-clip or a Delaunay preview.",
        frame_ask="Does ear clipping as taught handle holes?",
        build=[
            "**Say:** Existence of a diagonal from an ear — draw it; write-up is homework.",
            "**Board:** induction split. Ear with an interior point that invalidates it. Split/merge sketches. Skinny vs Delaunay.",
            "**Say:** Midterm topics 1–11 on a handout. Degeneracy will appear.",
        ],
        ask_build="Define ear tip.",
        they_build="Induction n−2. A concave quad has two ears (not a convex n-gon).",
        show_say="Step-mode ears: candidate highlighted; green legal / red point inside; faint clipped ears. C-shape: reflex refused, then accepted after a neighbor clips. Bowtie: clear error, not an infinite loop. Demo 11-ear-clip.html. Plant isEar without the convex-turn test. Plant PIP on whole P instead of the ear triangle.",
        attempt_say="isEar for one index. Eight minutes.",
        land_say="Lab: earClip; number triangles; convex, C, 12-vertex room; bowtie throws. Homework: study the list. Quiz: counts, ear, O(n²), holes, vs Delaunay. Next week exam.",
        live=[
            ("0–15", "n−2 on the board", "They count a hexagon."),
            ("15–40", "Clip a C", "Reflex refused."),
            ("40–50", "Fail a bowtie", "No infinite loop."),
            ("50–60", "Issue midterm list", "Photograph. No DCEL on it."),
        ],
        cut="Monotone sweep implementation. Keep ears + n−2 + the list.",
        add="Label one split vertex on a drawing.",
    )
    GOLD[(C, 8)] = dict(
        kernel="DCEL: half-edge origin/twin/next/face; walkFace = next loop; walkVertex = twin.next; face on the left",
        success="after the exam they walk two bounded faces of a pentagon-with-diagonal and twin.twin==e",
        invariant="predicates before constructions; degeneracy is the course",
        goal="midterm, then a mesh structure — arrays of vertices fail as soon as there are faces",
        kind="midterm",
        midterm_topics="orient and degeneracy; proper/touch/overlap/none; PIP vertex-hit; convex vs simple vs bowtie; same-turn ⇔ convex for simple (short proof); Jarvis Θ(nh); Andrew sort+≤0+O(n log n); parabola lower bound; sweep events and neighbors; ear + n−2; one degeneracy. No Voronoi, kd-tree, or DCEL on the paper.",
        board="""```
Vertex: x,y, incidentEdge
Half: origin, twin, next, face (left, CCW outer)
Face: outer, inners

e.twin.origin == e.next.origin
e.twin.twin == e

walkFace: e = e.next
walkVertex: e = e.twin.next

two triangles share an edge:
  4 verts, 10 half-edges, 3 faces (2 bounded + unbounded)

Three.js BufferGeometry is triangle soup, not a DCEL
```""",
        slides=[],
        hook_say="This meeting is a **midterm**, then DCEL. No laptop. After: half-edges are how you walk a face and split an edge after Week 6 intersections. Grading: a correct picture with a wrong name gets partial; O(n log n) on Jarvis without h gets zero.",
        show_say="Hardcoded DCEL for two triangles. Log walkFace and walkVertex on the shared verts. Demo 12-dcel-walk.html. Plant storing one directed edge per segment. Plant forgetting the unbounded face.",
        attempt_say="walkFace(edgeId) → vertex ids. Every twin.twin is itself.",
        land_say="Lab: JSON DCELs — triangle, two triangles, pentagon+diagonal. Homework: none except optional de Berg DCEL chapter. No quiz.",
        live=[
            ("0–15", "Count a triangle DCEL with the class", "3+3 halves, 2 faces."),
            ("15–40", "Two triangles, label every half", "Counts mismatch ⇒ the DCEL is wrong."),
            ("40–60", "walkFace / walkVertex", "They type the loops."),
        ],
        cut="Edge-split coding. Keep records + two walks.",
        add="Euler check: include the unbounded face.",
    )
    GOLD[(C, 9)] = dict(
        kernel="kd-tree: alternate x/y median; range query prune if cell disjoint, take if cell ⊂ R; closed range",
        success="oracle matches; at least one query prunes ≥40% of 5000 points; they draw 8 points and a pruned subtree",
        invariant="predicates before constructions; degeneracy is the course",
        goal="which face contains q, and which points are in this rectangle — not ‘test every face’",
        board="""```
point location: slabs O(log n) query, O(n²) space — too fat
Kirkpatrick: name, O(n) space; we do not code it
ship: BVH / kd on boxes + point-in-triangle

kd build: axis = depth%2; median; cells
query: disjoint → prune; contained → report all; else both
worst O(√n + k)     thin query stabs many cells

quadtree splits space; range tree: name O(log² n + k)
BVH: tree of object AABBs (Week 13 pick)
```""",
        slides=[],
        hook_say="Midterms back briefly; no quiz. Point location is not test every face. Practical substitute: a BVH plus last month’s inside test. Today we implement the kd-tree because the prune is visible.",
        hook_ask="When do we prune a node? Wait. Want: cell disjoint from R.",
        frame_say="Include boundary (R closed). Split always on x is a fail. Forgetting the point at an internal node is a fail. Quadtree ≠ kd-tree in the report. Do not invent milliseconds; visited vs brute is the story.",
        frame_ask="Which axis at depth 3? Want: y (if depth 0 is x).",
        build=[
            "**Say:** Slab method as the obvious structure; space explodes.",
            "**Board:** slabs. kd splits on 8 points. Query vs cell: disjoint / contained / overlap. BVH of three triangles.",
            "**Say:** kd vs BVH table: points vs objects; orthogonal range vs ray/frustum; GIS vs three-mesh-bvh.",
        ],
        ask_build="BVH stores what at each node?",
        they_build="Hand-draw kd for (2,3),(5,4),(9,6),(4,7),(8,1),(7,2),(6,3),(3,6); query [3,7]×[2,5]. O(√n+k) paragraph. One Three.js BVH use.",
        show_say="Clickable points, drag rectangle, x-splits blue y red, visited orange, pruned gray, reported green. Counters vs brute on 5000. Demo 13-kd-range.html. Plant always splitting on x. Plant pruning with the child’s cell.",
        attempt_say="rangeQuery prune test. Eight minutes.",
        land_say="Lab: build+query, oracle, 20 random rects, README figure of 8 points. Homework: that figure is required. Quiz: slabs, axis, prune, range-tree vs kd, BVH box.",
        live=[
            ("0–15", "Slabs then ‘we will not ship that’", "Kirkpatrick name."),
            ("15–40", "Build 8 points on the board then in code", "Median x first."),
            ("40–50", "A query that greys a whole subtree", "The story."),
            ("50–60", "BVH sentence", "Week 13 will pick with it."),
        ],
        cut="Range-tree code. Keep kd prune + BVH name.",
        add="Closed-range boundary policy in the README.",
    )
    GOLD[(C, 10)] = dict(
        kernel="V(si)={p: dist(p,si)≤dist(p,sj) ∀j}; vertex = empty-circumcircle center; discrete Voronoi; no Fortune code",
        success="dragging a site recolors the canvas; query point shows nearest site; they can state empty-circle and unbounded ⇔ hull",
        invariant="predicates before constructions; degeneracy is the course",
        goal="proximity: who is closest to this site?",
        board="""```
cell V(si)     edge ⊂ perpendicular bisector
vertex = circumcenter of 3 sites
empty circle: no site in the interior

unbounded cell  ⇔  site on CH(S)
complexity O(n) vertices/edges in 2D

Fortune (intuition only):
  beach = parabolic arcs
  site event: new arc     circle event: vertex born
DO NOT IMPLEMENT

discrete: argmin dist per pixel     tie: smaller index
dual teaser: Delaunay next week
```""",
        slides=[],
        hook_say="Nearest neighbor is a cell membership test. We will not spend the week debugging Fortune — that is why we forbid it. Drawing Delaunay and calling it Voronoi is the other fail: they are dual; edges are not the same.",
        hook_ask="A cell is unbounded iff the site is …? Wait. Want: on the convex hull.",
        frame_say="General position: no four cocircular, no three collinear — then say what fails. Every pair of sites does not produce a Voronoi edge, only neighbors. Jump-flood / cone shaders: name for IGWT, not required. Do not invent fps.",
        frame_ask="Site event vs circle event?",
        build=[
            "**Say:** Empty-circle is the homework proof and the bridge to Delaunay.",
            "**Board:** three sites, three bisectors, one vertex, empty circle. Hull sites with unbounded rays. Beach line: two parabolas, a site punching an arc. Dual teaser.",
            "**Say:** Applications: territory, coverage, stipple, Thiessen, city blocks.",
        ],
        ask_build="A Voronoi vertex is the _____ of three sites.",
        they_build="Proof: circumcircle of abc at a Voronoi vertex contains no other site. Fortune two events, three sentences each. No Fortune code.",
        show_say="Click sites, color pixels (or coarse grid), overlay dots, draggable q to nearest site. Optional messy all-bisectors to motivate a better algorithm. Do not start Fortune. Demo 14-voronoi-discrete.html. Plant == on distances.",
        attempt_say="nearestSite(p, sites) with a tie-break. Eight minutes.",
        land_say="Lab: discrete Voronoi, add/remove/drag, query highlight, screenshot of a 3-color meeting, README why a vertex is a circumcenter. Quiz: V(si), circumcenter, empty circle, events, unbounded.",
        live=[
            ("0–15", "Three sites by hand", "Empty circle."),
            ("15–35", "Beach-line cartoons only", "Stop. No heap of arcs."),
            ("35–50", "Discrete color + query", "Dragging updates live."),
            ("50–60", "Dual sentence", "Connect sites whose cells share an edge."),
        ],
        cut="Any Fortune attempt. Keep definition + discrete + empty circle.",
        add="Overlay a library Voronoi as a teaser if you already have one.",
    )
    GOLD[(C, 11)] = dict(
        kernel="Delaunay: empty circumcircle; illegal edge ⇔ incircle; flip; insert+legalize (n≤80); not minimum-weight",
        success="a known 6-point example matches the reference; they can flip an illegal diagonal and not flip a hull edge",
        invariant="predicates before constructions; degeneracy is the course",
        goal="the mesh they will actually use in terrain and interpolation",
        board="""```
DT ⇔ every triangle circumcircle empty of sites
dual: DT edge ↔ VD edge     DT triangle ↔ VD vertex

illegal: opposite vertex in circumcircle
         (angle sum >180° opposite the shared edge)
flip ad → bc     then legalize recursively
hull edges: never flip

incircle: force CCW or the sign flips
Delaunay maximizes min angle     shorter ≠ Delaunay
CDT: keep given edges; ear-clip can sliver
```""",
        slides=[],
        hook_say="Week 10’s empty circle at a Voronoi vertex is this week’s empty circumcircle. Ear clipping can produce slivers; show the same polygon, ear vs CDT. Do not claim minimum-weight.",
        hook_ask="Does Delaunay always minimize total edge length? Wait. Want: no.",
        frame_say="Locate triangle: n≤80 brute point-in-triangle; walk toward p is nicer. Super-triangle: clip from the display. Bowyer–Watson cavity: delete triangles whose circle contains p, star-shaped hole, connect p — equivalent to split+legalize. Naive lab O(n²) is fine.",
        frame_ask="When is a shared edge illegal?",
        build=[
            "**Say:** A triangulation is Delaunay iff every interior edge is legal. Flips terminate (min angle increases).",
            "**Board:** VD dashed, DT solid, one circle. Illegal edge + both circumcircles. Insert p, cavity. Skinny ear vs flipped pair.",
            "**Say:** Graphics: terrain, remesh, cloth, lightmaps, cities.",
        ],
        ask_build="A Delaunay edge corresponds to what in VD?",
        they_build="Connect Week 10 proof to today. Honest paragraph: shorter ≠ Delaunay. CDT vs ear clip for a navmesh.",
        show_say="n≤40 click-insert. Circumcircle under mouse. Illegal edges red. Animate a flip. Script: four points one keypress flip; fifth point three legalize calls; class shouts ‘illegal’ when a point sits in a circle. Demos 15-incircle.html, 16-delaunay.html. Plant flipping a hull edge. Plant leaving the super-triangle in the terrain mesh. Plant calling ear clipping Delaunay.",
        attempt_say="incircle (or angle-sum) on one quad. Eight minutes. Force CCW.",
        land_say="Lab: flip+legalize a JSON triangulation; incremental n≤80; clip super-triangle; match a reference screenshot. Homework: edge flip. Quiz: empty circle, dual, illegal, what flip replaces, not min-weight.",
        live=[
            ("0–15", "Dual on last week’s three sites", "Same circle."),
            ("15–40", "One illegal, one flip", "Both circumcircles drawn."),
            ("40–50", "Insert inside a triangle", "Three new edges, legalize."),
            ("50–60", "They legalize a fixture", "Circulate."),
        ],
        cut="Full Bowyer–Watson robustness. Keep incircle + flip + insert.",
        add="Show ear-clip slivers vs DT on one polygon.",
    )
    GOLD[(C, 12)] = dict(
        kernel="closest pair: presort Px,Py; T(n)=2T(n/2)+O(n); strip |x−mid|<δ; O(1) y-neighbors (packing)",
        success="oracle matches; strip scan is visibly not n²; they can draw the δ×2δ packing",
        invariant="predicates before constructions; degeneracy is the course",
        goal="one more classic algorithm, then a map of names we will not fully teach",
        board="""```
naive Θ(n²)
δ = min(δL, δR)
strip: |x−mid|<δ from already-sorted Py
for each p, only q with Δy<δ  (≤ ~7 by packing δ/2 disks)

T(n)=2T(n/2)+O(n)=O(n log n)
do not sort inside every recursive call

survey (picture + use, no lab code):
  arrangement Θ(n²)     zone O(n)
  A ⊕ B  C-obstacle     SAT cousin
  visibility graph      hug corners; Voronoi roadmap stays away
```""",
        slides=[],
        hook_say="Closest pair is the implemented topic. Arrangements, Minkowski, visibility: one picture each. A visibility graph is a project, not this lab. Project menu points at Weeks 14–15.",
        hook_ask="Why is the strip 2δ wide? Wait. Want: any closer pair must straddle the median, each within δ.",
        frame_say="Presort; build strip in linear time from Py. Ties: any closest pair. Duplicates: dist 0, not this week. Checking all pairs in the strip is correct but not the algorithm. Do not invent timings; n=2000 vs brute should diverge because of the strip, not because you quote fps.",
        frame_ask="A ⊕ B is used for what in robotics?",
        build=[
            "**Say:** Draw the packing. Do not handwave ‘we only check 7’ without the box.",
            "**Board:** split, two recursive pairs, δ, strip. δ/2 disks in the neighborhood. Minkowski square⊕disk. Start, goal, a few visibility edges.",
            "**Say:** Leave the field-map table up through the project (Fortune no, Kirkpatrick no, 3D Delaunay no, exact kernels Week 13).",
        ],
        ask_build="Visibility-graph edge exists when?",
        they_build="Trace 12 points; recurrence. Packing 1 page. Minkowski collision and visibility path, 4–6 sentences each, no code.",
        show_say="Median line, yellow strip, thin candidate pairs, thick best. Step the merge scan: 1–3 neighbors, not everyone. Demo 17-closest-pair.html. Plant sorting every call. Plant all-pairs in the strip. Plant implementing a visibility graph ‘for the lab.’",
        attempt_say="Build the strip from Py in linear time. Eight minutes.",
        land_say="Lab: O(n log n) closest pair, oracle n≤800, times at 2k/5k, 12-point README trace. Homework: packing + two survey paragraphs. Quiz: time, strip width, O(1) inner, Minkowski, visibility edge. Next: graphics systems.",
        live=[
            ("0–20", "Recursion + strip on the board", "Packing disks."),
            ("20–40", "Step the strip scan", "Most points compare to 1–3."),
            ("40–50", "Survey three pictures", "No code."),
            ("50–60", "Project menu", "Main algorithm must be theirs."),
        ],
        cut="Arrangement construction. Keep closest pair + three names.",
        add="n=3 brute base case written carefully.",
    )
    GOLD[(C, 13)] = dict(
        kernel="click → ray → BVH AABB prune → triangle (orient / barycentric); EPS is a policy; Shewchuk named; Three.js Raycaster is an oracle",
        success="a vertical slice runs; they name the predicate that would break it; visited boxes vs hit triangle are visible",
        invariant="predicates before constructions; degeneracy is the course",
        goal="connect the course to IGWT; picking is geometry, not ‘the engine knows’",
        board="""```
configurator: click → ray → BVH → triangle → barycentric → part
orient → back-face, clip side, ears
EPS = thick line, not exact     inconsistent signs possible
Shewchuk: adaptive; call a library for thesis meshes
3D orient = signed tetra volume

libraries hide: three-mesh-bvh, earcut, Delaunator, Recast
course rule: main algorithm is student code
```""",
        slides=[],
        hook_say="Joint with Computer Graphics I: the GPU picture does not replace the predicate. Growing EPS until Delaunay looks fine is forbidden. Starting the project from zero this week is what the checkpoint exists to prevent.",
        hook_ask="Why is EPS not exact? Wait. Want: it makes a band of COLLINEAR; predicates can still disagree around a cycle.",
        frame_say="Payoff table slowly, one course sentence + one IGWT sentence. Practical rules: snap UI, unique within EPS, one kernel file, do not grow EPS to pass tests. Ray–triangle: t,u,v barycentric, t≥0, u,v≥0, u+v≤1. Mesh repair is DCEL + Week 6 intersections — academic ‘Repair in Blender.’",
        frame_ask="3D analog of orient(a,b,c)?",
        build=[
            "**Say:** Leave one payoff column empty; fill with the class.",
            "**Board:** payoff table. Three points, three disagreeing epsilon signs. Ray vs AABB vs triangle. Miss the parent box, never see the children.",
            "**Say:** Terrain: Delaunay → normals → BufferGeometry. Collision: hull/AABB then SAT/segments.",
        ],
        ask_build="Which course algorithm does click-to-pick use?",
        they_build="README: build, degeneracy list, 6-bullet report outline. Project only.",
        show_say="20–80 triangles. Top-down BVH, longest-axis median. On click: orange visited boxes, gray pruned, green hit, print id and u,v. ‘Week 9 prune plus Week 2 inside-triangle, in 3D clothing.’ Demo 18-bvh-pick.html. Plant using Raycaster as the implementation. Plant five copies of orient with five epsilons.",
        attempt_say="Miss-parent-box early out. Eight minutes.",
        land_say="Lab: 10-minute vertical slice — algorithm theirs, something moves, one degeneracy discussed, repo runs, they know the weeks. Checkpoint complete/incomplete + advice. Quiz: pick pipeline, EPS, Shewchuk, 3D orient, one BVH library.",
        live=[
            ("0–15", "Fill the payoff table", "Configurator row last."),
            ("15–35", "Inconsistent epsilon picture", "One kernel file."),
            ("35–50", "BVH pick live", "Count box tests vs triangle tests on a far miss."),
            ("50–60", "Checkpoint roster", "Advice, not grade shock."),
        ],
        cut="Exact CGAL kernel. Keep mapping + BVH pick + EPS policy.",
        add="Black-screen / miss: the ray never hit the parent box.",
    )
    GOLD[(C, 14)] = dict(
        kernel="core algorithm on a non-toy input + one degeneracy handled or shown + README that runs on a lab machine",
        success="a TA can serve the folder, see the invariant (stack/strip/illegal/sweep), and hear where orient lives",
        invariant="predicates before constructions; degeneracy is the course",
        goal="studio — not a content lecture",
        kind="studio",
        board="""```
Report: problem · weeks · algorithm+complexity · degeneracy · kernel · results · limits · refs
Defense: predicate?  complexity and n measured?  degenerate input?
         naive vs yours?  3D break?  construction vs predicate?
         test if orient flips?  library vs you?

Cuts: Fortune → discrete Voronoi + DT dual
      map editor → intersect + DCEL walk
      3D physics → 2D hull + SAT
      shaders → unlit canvas + correct kernel
Do not invent timings.
```""",
        slides=[],
        hook_say="This meeting is **studio**. No third Delaunay lecture. If they are stuck on a predicate, debug the predicate. A correct O(n log n) on a plain canvas beats a broken Three.js scene. Pretty UI with no tests fails.",
        hook_ask="If behind, what do you cut first?",
        frame_say="Desk order: kernel (orient/intersect/incircle), visualizer, tests, report outline. Comment on the algorithm, not the CSS. Rehearse 12+5: 0–2 problem, 2–6 invariant+complexity, 6–10 live ugly input, 10–12 limits and who did what.",
        show_say="Volunteer against the board. Library-Delaunay + student draw fails.",
        attempt_say="Studio. Serve first. Freeze a degenerate input as reset state.",
        land_say="Report draft + 30s recording before Week 15. Next week 12+5. Always ask where orient is. No quiz.",
        live=[
            ("0–10", "Eight headings + eight questions + clock", "Photograph."),
            ("10–50", "Desk review", "Kernel, then viz, then tests, then outline."),
            ("50–60", "60s rehearsal with ugly input", "Hard stop."),
        ],
        cut="New algorithms. Keep freeze.",
        add="Point to the test that fails if orient flips sign.",
    )
    GOLD[(C, 15)] = dict(
        kernel="12+5; live demo of the student algorithm; where is orient (or incircle); one ugly input",
        success="they stop at 12; they can answer the predicate question; recording plays if HDMI dies",
        invariant="no new features today",
        goal="presentations — not a content lecture",
        kind="presentations",
        board="""```
12 + 5
Show: predicate · invariant in the viewer · one degenerate input
Always: where is orient (or incircle) in the repo?
No new algorithms on stage
```""",
        slides=[("Timer", "not a slide of Fortune")],
        hook_say="Presentations. 12+5. Repo, 6–8 page report, 30s recording. Computational geometry in this program is naming the predicate, drawing the invariant, testing the degenerate case, only then putting the result on a GPU.",
        frame_ask="Where is orient (or incircle)? What happens on your degenerate input? What did a library do?",
        show_say="None. Present. Two from the Week 14 list plus one from their code (T-junction split? reflex not an ear? empty circle? prune?).",
        attempt_say="Present.",
        land_say="That habit is Computer Graphics I, WebGL, and the capstone. Grades close when report and repo are in.",
        live=[("0–60", "Talks", "Cut at 12. Play recording if the demo dies.")],
        cut="Debugging on stage.",
        add="One question: what would break in 3D?",
    )
