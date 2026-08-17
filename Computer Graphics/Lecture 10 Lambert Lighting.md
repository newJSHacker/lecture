# Lecture 10 — Lighting I (Lambert)

**Week 10 of 15** · Computer Graphics I  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Lambert: kd*max(0,n·l)+ka*ambient; face n=normalize(cross(b−a,c−a)); same space for n and l  
**Success check:** rotating the light moves the terminator; debug n*0.5+0.5 is colorful; they can say culling ≠ black Lambert

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Computer Graphics/code/10-lookat.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: a lit cube that is not each face a random color | Invariant: a picture is an array; putPixel lives in pixels`

## Board at the end (they photograph this)

```
n_face = normalize(cross(b−a, c−a))     CCW
n_world = normalize( (M⁻¹)ᵀ n_obj )

l = unit toward the light     (write it)
diff = kd * max(0, n·l)
color = ka*ambient + diff*lightColor

flat: one n per face
Gouraud: Lambert at vertices, interpolate color

cull: not drawn     n·l<0: drawn, dark
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Depth made a solid cube. Today it is not a random crayon. Freeze light space: world or view — pick one. Mixing world n with view l is the classic bug.

**Ask:** Why max(0, n·l)? Wait. Want: the back of the surface gets no light, not negative light.

**Board:** parked strip. Then `n·l` on a cube face, light arrow, clamped at 0.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Lambert, face and vertex normals, normal matrix*.

**Do not:** Lighting in object space while the camera moved.

### Minutes 10–12 — Frame

**Say:** Vertex normals vs face normals. Sphere needs vertices; faceted cube can use faces. Point light: l=normalize(lightPos−p); extra, not required. Gouraud smears highlights — Phong-interpolate n in Week 11 if Gouraud works.

**Ask:** Same space for n and l — why?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** ka is a projector policy against pure black.

**Board:** n and l, θ. Non-uniform scale wrong vs right normals. Gouraud colors at vertices.

**Say:** Back-face culling is winding. A front face with n·l<0 is still drawn.

**Ask:** Face normal formula from three vertices.

**They do:** On paper: one picture of non-uniform scale on a circle. Why (M⁻¹)ᵀ.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Per-face Lambert, light-angle sliders, ambient slider, cull toggle (projected winding). Debug n*0.5+0.5. Demo 13-lambert.html. Plant l toward the surface → black cube. Plant lighting in object space while the camera moved.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** lambert(n,l,kd,ka). Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: face-Lambert cube; Gouraud; normalMatrix(M); normals debug. Homework: transformNormal. Quiz: face n, why max, same space, cull vs Lambert.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Face n + one light | Plant unnormalized n. |
| 15–40 | Move the light | Terminator must move. |
| 40–50 | Gouraud vs flat | Cube with face n at vertices looks faceted — OK. |
| 50–60 | Debug normals view | Black = a bug. |

Point them at `Computer Graphics/code/10-lookat.html` as the after-class check, not as the lecture.

---

## Lab

1. Face-Lambert cube.
2. Gouraud with vertex normals (cube can reuse face normals at vertices — it will look faceted; that is OK).
3. `normalMatrix(M)`.
4. Debug normals view.

---

## Homework

1. Written: derive why `(M⁻¹)ᵀ` for normals (short; Shirley). Or: one picture of non-uniform scale on a circle.
2. Code: `lambert(n, l, kd, ka)`.
3. Point light extra: falloff optional, not required.

---

## Quiz next meeting (they hear this now)

1. Face normal formula. (2 pts)
2. `max(0, n·l)` — why max? (2 pts)
3. Same space for n and l. Why? (3 pts)
4. Culling vs negative Lambert. (3 pts)


## Extra exercises

See [[Computer Graphics/exercises/Week 10]].

---

## Notes you may still need (from the outline)

**1. Normals (15 min).** Face normal: `normalize(cross(b-a, c-a))` with CCW vertices.
Vertex normals: average adjacent faces, or from the mesh file. A sphere needs vertex normals; a faceted cube can use face normals.
Transform: `n_world = normalize(normalMat * n_obj)` with `normalMat = transpose(inverse(M_3×3))`.
---

**2. Lambert (25 min).** Directional light: `l` is a unit vector **toward** the light (or from the surface — pick and write it on the board).
```
diff = kd * max(0, dot(n, l))
color = ka * ambient + diff * lightColor
```
`ka` is a policy so unlit faces are not pitch black on a projector.
**Space:** transform n and l into the same space. Mixing world n with view l is the classic bug.
Point lights: `l = normalize(lightPos - p)`. Need a position p at the vertex or (later) in the fragment. This week: directional is enough; point light is the lab extra.
---

**3. Interpolation (15 min).** **Flat:** one n per triangle, one color, fill.
**Gouraud:** Lambert at vertices, barycentric-interpolate **color**. Fast; highlights smear (Week 11).
**Phong interpolation:** interpolate **normals**, normalize, shade per pixel. Better; do this in Week 11 if Gouraud is already working.
---

**4. Culling (10 min).** Back-face: `dot(n_view, viewDir)` or screen-space winding. Culled faces are not drawn. A front face with `n·l < 0` is still drawn, just dark. Students conflate these.
---

---

## Common mistakes

1. Lighting in object space while the camera moved.
2. Not normalizing n after interpolation (Week 11) or after the normal matrix.
3. `l` pointing toward the surface, then wondering why the cube is black.

## If we run long, cut

Point-light falloff. Keep directional Lambert + same space.

## If we run short, add

Toggle culling vs dark faces.
