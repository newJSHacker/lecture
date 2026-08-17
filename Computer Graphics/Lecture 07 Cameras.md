# Lecture 7 — Cameras and the view transform

**Time:** 75 min lecture + 60 min live coding  
**Kernel this week:** `lookAt(eye, target, up)`  
**Board first:** camera axes u, v, w at the eye

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 6 |
| 10–30 | Eye, target, up; camera basis |
| 30–50 | View matrix as inverse of camera world |
| 50–65 | Move world vs move camera |
| 65–75 | Optional Three.js orbit **oracle** (5 min max) |

---

## Learning goals

1. Build a right-handed camera basis from eye, target, up.
2. Write V so that the camera sits at the origin looking down −Z.
3. Explain V as `inverse(cameraWorld)`.
4. Fly a camera around the Week 6 scene.
5. Handle degenerate up ∥ look.

---

## 1. Camera basis (20 min)

```
w = normalize(eye - target)     // +w points behind the camera if we look down −Z
// Alternative: f = normalize(target - eye), then w = -f
u = normalize(cross(up, w))     // depends on which w you chose — derive on the board
v = cross(w, u)
```

**This course:** camera looks down **−Z** in view space. After V, the target should be on −Z.

Walk one numeric example: eye `(0,0,5)`, target `(0,0,0)`, up `(0,1,0)`. Then w = `(0,0,1)`, looking toward −Z in world… wait: eye − target = (0,0,5), normalize (0,0,1). View space +Z points toward world +Z, so the origin is in front if we look along world −Z. **Draw the camera at +Z looking at origin.** Students get this wrong every year. Spend the time.

Standard `lookAt` (OpenGL-style) produces a V such that `V * eye = 0` and the target lands on the −Z axis.

---

## 2. View matrix (20 min)

Camera world matrix C has columns u, v, w, eye (if those are the camera’s x,y,z axes). Then `V = C⁻¹`.

Closed form: rotation that maps camera axes to canonical, then translate by −eye.

```
V = [ u.x  u.y  u.z  -dot(u,eye) ]
    [ v.x  v.y  v.z  -dot(v,eye) ]
    [ w.x  w.y  w.z  -dot(w,eye) ]
    [ 0    0    0     1          ]
```

Match **your** u,v,w to this layout in live coding. Tests: `V * vec4(eye,1) ≈ 0`.

---

## 3. Duality (15 min)

Translating the camera right is the same (as a picture) as translating the world left. Students should not mix both in one frame without a story.

FPS: move eye in the u/w plane; recompute `lookAt` or update C and invert.

---

## 4. Three.js oracle (5 min)

Open [[ThreeJS/]] orbit demo. Say: `camera.position` is eye; the engine builds V. Close it. Back to student `lookAt`.

---

## Live coding (60 min)

Implement `lookAt`. Solar system from Week 6. Sliders: eye x,y,z. Button: reset to `(0, 2, 8)`.

Degenerate: up parallel to look → show NaN, then fix with a fallback up.

---

## Lab

1. `lookAt` with tests (eye at z=5, target origin).
2. WASD or sliders.
3. Draw camera axes in **world** (debug).
4. Do not call Three.js `lookAt` in the submitted lab.

Done when moving the camera left moves the scene right, and the Sun stays the Sun.

---

## Homework

1. Code: `lookAt` + three fixtures (including a tilted up).
2. Written: V as inverse of C, 6–8 sentences.
3. Written: what if up is parallel to look?

---

## Quiz (10 min)

1. Name eye, target, up. (2 pts)
2. After V, where is the eye? (2 pts)
3. Why −Z look in this course? (2 pts)
4. `V * eye` should be …? (4 pts)

---

## Common mistakes

- `cross(w, up)` vs `cross(up, w)` until it “looks okay” — pick the board order.
- Leaving V as identity and moving the model instead, then calling it a camera.
- Up vector not normalized; then v is scaled and the picture shears.

---

## Board drawings

1. Camera at +Z, axes u,v,w.
2. V as “change to camera frame.”
3. Duality: camera right vs world left.
