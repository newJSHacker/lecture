# Lecture 7 — Cameras and the view transform

**Week 7 of 15** · Computer Graphics I  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** lookAt(eye, target, up); V = C⁻¹; after V the eye is at origin looking −Z  
**Success check:** V*eye ≈ 0; moving the camera left moves the scene right; degenerate up is not NaN

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Computer Graphics/code/07-mat4-order.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: the view matrix is the inverse of the camera’s world transform | Invariant: a picture is an array; putPixel lives in pixels`

## Board at the end (they photograph this)

```
w = normalize(eye − target)     // look −Z in view
u = normalize(cross(up, w))     // derive on the board
v = cross(w, u)

V = [ uᵀ  −u·eye ]
    [ vᵀ  −v·eye ]
    [ wᵀ  −w·eye ]
    [ 0    1     ]

eye (0,0,5), target origin, up (0,1,0)
  →  w = (0,0,1)   camera at +Z looking at origin
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** M put the cube in the world. Today V puts the world in the camera. Students get the (0,0,5) example wrong every year. Spend the time. Three.js orbit is a five-minute oracle, then close it — they still write lookAt.

**Ask:** After V, where is the eye? Wait. Want: origin.

**Board:** parked strip. Then camera axes u, v, w at the eye.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *`lookAt(eye, target, up)`*.

**Do not:** `cross(w, up)` vs `cross(up, w)` until it “looks okay” — pick the board order.

### Minutes 10–12 — Frame

**Say:** Camera looks −Z in view space. Standard lookAt: V*eye=0 and target on −Z. Duality: camera right = world left. Do not mix both in one frame without a story. FPS: move eye in u/w, recompute lookAt. Hand out the midterm topic list at the end: spaces, barycentric, matrix order, point vs vector, scene-graph product, lookAt. No P on the exam.

**Ask:** What if up is parallel to look?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Draw the camera at +Z looking at origin. Walk u,v,w.

**Board:** V as change to camera frame. Duality arrows.

**Say:** Match your u,v,w to the closed-form layout in live coding. Tests: V*vec4(eye,1)≈0.

**Ask:** Why −Z look in this course? Want: freeze with WebGL/Three.js later.

**They do:** On paper: V as inverse of C, 6–8 sentences. Degenerate up policy.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Implement lookAt. Fly around Week 6 solar system. Sliders eye x,y,z. Reset (0,2,8). Degenerate up → NaN then fallback. Optional 5 min Three.js orbit: camera.position is eye; engine builds V; close it. Demo 10-lookat.html. Plant cross(w,up) until it ‘looks okay.’

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** lookAt fixture: eye z=5, target origin. Eight minutes. No Three.js lookAt in the lab.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: lookAt tests, WASD or sliders, camera axes in world, look-at-origin button. Homework: three fixtures including tilted up. Quiz: eye/target/up, where is the eye, −Z, V*eye. Topic list for Week 8.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Numeric (0,0,5) example | They will swap w sign. Draw it. |
| 15–40 | lookAt + solar system | Plant V = I and moving the model. |
| 40–50 | Degenerate up | Fallback up. Show NaN first. |
| 50–60 | Oracle 5 min then close | Back to student lookAt. |

Point them at `Computer Graphics/code/07-mat4-order.html` as the after-class check, not as the lecture.

---

## Lab

1. `lookAt` with tests (eye at z=5, target origin).
2. WASD or sliders.
3. Draw camera axes in **world** (debug).
4. Do not call Three.js `lookAt` in the submitted lab.

---

## Homework

1. Code: `lookAt` + three fixtures (including a tilted up).
2. Written: V as inverse of C, 6–8 sentences.
3. Written: what if up is parallel to look?

---

## Quiz next meeting (they hear this now)

1. Name eye, target, up. (2 pts)
2. After V, where is the eye? (2 pts)
3. Why −Z look in this course? (2 pts)
4. `V * eye` should be …? (4 pts)


## Extra exercises

See [[Computer Graphics/exercises/Week 07]].

---

## Notes you may still need (from the outline)

**1. Camera basis (20 min).** ```
w = normalize(eye - target)     // +w points behind the camera if we look down −Z
// Alternative: f = normalize(target - eye), then w = -f
u = normalize(cross(up, w))     // depends on which w you chose — derive on the board
v = cross(w, u)
```
**This course:** camera looks down **−Z** in view space. After V, the target should be on −Z.
Walk one numeric example: eye `(0,0,5)`, target `(0,0,0)`, up `(0,1,0)`. Then w = `(0,0,1)`, looking toward −Z in world… wait: eye − target = (0,0,5), normalize (0,0,1). View space +Z points toward world +Z, so the origin is in front if we look along world −Z. **Draw the camera at +Z looking at origin.** Students get this wrong every year. Spend the time.
Standard `lookAt` (OpenGL-style) produces a V such that `V * eye = 0` and the target lands on the −

**2. View matrix (20 min).** Camera world matrix C has columns u, v, w, eye (if those are the camera’s x,y,z axes). Then `V = C⁻¹`.
Closed form: rotation that maps camera axes to canonical, then translate by −eye.
```
V = [ u.x  u.y  u.z  -dot(u,eye) ]
    [ v.x  v.y  v.z  -dot(v,eye) ]
    [ w.x  w.y  w.z  -dot(w,eye) ]
    [ 0    0    0     1          ]
```
Match **your** u,v,w to this layout in live coding. Tests: `V * vec4(eye,1) ≈ 0`.
---

**3. Duality (15 min).** Translating the camera right is the same (as a picture) as translating the world left. Students should not mix both in one frame without a story.
FPS: move eye in the u/w plane; recompute `lookAt` or update C and invert.
---

**4. Three.js oracle (5 min).** Open [[ThreeJS/]] orbit demo. Say: `camera.position` is eye; the engine builds V. Close it. Back to student `lookAt`.
---

---

## Common mistakes

1. `cross(w, up)` vs `cross(up, w)` until it “looks okay” — pick the board order.
2. Leaving V as identity and moving the model instead, then calling it a camera.
3. Up vector not normalized; then v is scaled and the picture shears.

## If we run long, cut

FPS collision. Keep lookAt + V*eye.

## If we run short, add

Draw camera axes in world.
