# Lecture 6 — Hierarchical models and scene graphs

**Week 6 of 15** · Computer Graphics I  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** world(node) = world(parent) * local(node); Node { local, children, mesh }  
**Success check:** moving the parent moves the child; rotating the child does not move the parent; axes draw

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Computer Graphics/code/06-vec3.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: a solar system / arm from a tree of transforms — how glTF and Three.js store scenes | Invariant: a picture is an array; putPixel lives in pixels`

## Board at the end (they photograph this)

```
M : object → world
columns of M = object axes + origin in world

world(node) = world(parent) * local(node)
world(root) = local(root)

Earth = worldSun * localEarth     (not T(orbit) alone)

n' = normalize( (M⁻¹)ᵀ n )   if non-uniform scale
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Last week T(c) R T(−c). Today that product lives on a tree. Three.js Object3D.matrix is this. Instancing is the same mesh, different M — do not clone vertex arrays.

**Ask:** world = ? * local  (column vectors). Wait. Want: parentWorld * local.

**Board:** parked strip. Then Sun–Earth–Moon as three nested frames.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *scene node `{ local, children }`, world matrix*.

**Do not:** `local * parent` (row-vector hangover).

### Minutes 10–12 — Frame

**Say:** DFS, pass parentWorld down. Cycles forbidden. Debug RGB axes at each node using world rotation; ignore huge scale. Normal matrix: name it now so the midterm can ask why; implement in Week 10.

**Ask:** Why does non-uniform scale break normals?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Model matrix is the object frame written in world coordinates.

**Board:** nested frames Sun–Earth–Moon. Tree with matrices on edges. RGB axes on a tilted cube.

**Say:** Robot arm shoulder*elbow*wrist is the midterm product.

**Ask:** Write the product for a 3-node leaf.

**They do:** On paper: expand worldMoon as named matrices. Instancing vs cloning vertices.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Sun/Earth/Moon, time t, orbit sliders, axes. Pause: Earth’s world is not T(orbit) if parented badly. Demo 09-scene-graph.html. Plant local*parent. Plant updating local from world every frame.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** draw(node, parentWorld). Eight minutes. One parent, one child.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: two-bone arm or turret; key A toggles axes. Homework: scene graph JSON or clean solar system. Quiz: what M does, world=parent*local, 3-node product, normal matrix name.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | One node M | Plant row-vector multiply. |
| 15–40 | Sun Earth Moon | Bad parenting: Earth inherits Sun spin. |
| 40–50 | Axes debug | Finds bad locals faster than a debugger. |
| 50–60 | They parent a moon | Circulate. |

Point them at `Computer Graphics/code/06-vec3.html` as the after-class check, not as the lecture.

---

## Lab

1. `Node { localMat4, mesh, children }`.
2. `function draw(node, parentWorld)`.
3. Two-bone arm **or** turret on a tank.
4. Key `A` toggles axes.

---

## Homework

1. Written: expand `worldMoon` as a product of named matrices.
2. Code: scene graph JSON loader (tiny: array of nodes with `parent` index) **or** hardcode the solar system cleanly.
3. Written: instancing vs cloning vertices.

---

## Quiz next meeting (they hear this now)

1. What does M do to a vertex? (2 pts)
2. `world = ? * local` (2 pts)
3. Draw a 3-node chain and write the product for the leaf. (4 pts)
4. Why a normal matrix? One sentence. (2 pts)


## Extra exercises

See [[Computer Graphics/exercises/Week 06]].

---

## Notes you may still need (from the outline)

**1. Model matrix (15 min).** M takes object-space vertices to world space. Its columns (column-vector convention) are the object’s x-axis, y-axis, z-axis, and origin, all in world coordinates.
A “mesh at the origin” plus M is how every engine stores placement. glTF nodes are this. Three.js `Object3D.matrix` is this.
---

**2. Hierarchy (25 min).** ```
world(node) = world(parent) * local(node)
world(root) = local(root)
```
**Solar system:** Sun local = spin. Earth local = orbit * spin. Moon local = smaller orbit * spin. Draw Earth with `worldSun * localEarth`.
**Robot arm:** shoulder * elbow * wrist. This is the product they will write on the midterm.
Traversal: depth-first, pass `parentWorld` down. Do not recompute from the root for every node if you already have the parent (O(n) vs O(n × depth) is worth one sentence).
Cycles in the graph: forbid them.
---

**3. Instancing and debug (15 min).** Same cube mesh, different M: instance. Do not clone vertex arrays.
**Debug:** at each node, draw the three axes (small RGB lines) using the world rotation, ignoring scale if scale is huge. This finds bad local matrices faster than any debugger.
---

**4. Normal matrix (10 min).** If M has non-uniform scale, `n' = normalize( (M⁻¹)ᵀ n )` on the 3×3. Uniform scale: `normalize(M_3×3 n)` is enough. Implement in Week 10; name it now so the midterm can ask “why.”
---

---

## Common mistakes

1. `local * parent` (row-vector hangover).
2. Updating local from world every frame and drifting (Euler integration of matrices).
3. Scaling the parent and wondering why the child’s offset explodes (it should).

## If we run long, cut

glTF loader. Keep parent×local + axes.

## If we run short, add

Key to pause time.
