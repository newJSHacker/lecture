# Lecture 6 — Hierarchical models and scene graphs

**Time:** 75 min lecture + 60 min live coding  
**Kernel this week:** scene node `{ local, children }`, world matrix  
**Board first:** Sun–Earth–Moon as three nested frames

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 5 |
| 10–25 | Model matrix as object → world |
| 25–50 | Parent × local; traversal |
| 50–65 | Instancing; debug axes |
| 65–75 | Normal matrix teaser |

---

## Learning goals

1. Define the model matrix M.
2. Compute world = parentWorld * local.
3. Traverse a tree and draw each mesh with its world matrix.
4. Draw local axes for debugging.
5. Name why non-uniform scale breaks normals.

---

## 1. Model matrix (15 min)

M takes object-space vertices to world space. Its columns (column-vector convention) are the object’s x-axis, y-axis, z-axis, and origin, all in world coordinates.

A “mesh at the origin” plus M is how every engine stores placement. glTF nodes are this. Three.js `Object3D.matrix` is this.

---

## 2. Hierarchy (25 min)

```
world(node) = world(parent) * local(node)
world(root) = local(root)
```

**Solar system:** Sun local = spin. Earth local = orbit * spin. Moon local = smaller orbit * spin. Draw Earth with `worldSun * localEarth`.

**Robot arm:** shoulder * elbow * wrist. This is the product they will write on the midterm.

Traversal: depth-first, pass `parentWorld` down. Do not recompute from the root for every node if you already have the parent (O(n) vs O(n × depth) is worth one sentence).

Cycles in the graph: forbid them.

---

## 3. Instancing and debug (15 min)

Same cube mesh, different M: instance. Do not clone vertex arrays.

**Debug:** at each node, draw the three axes (small RGB lines) using the world rotation, ignoring scale if scale is huge. This finds bad local matrices faster than any debugger.

---

## 4. Normal matrix (10 min)

If M has non-uniform scale, `n' = normalize( (M⁻¹)ᵀ n )` on the 3×3. Uniform scale: `normalize(M_3×3 n)` is enough. Implement in Week 10; name it now so the midterm can ask “why.”

---

## Live coding (60 min)

Sun / Earth / Moon with three cubes (or three colored triangles). Time `t`. Sliders: orbit speeds.

Draw axes. Pause: “Earth’s world matrix is not `T(orbit)` alone; it includes the Sun’s spin if I parented badly.” Fix parenting.

---

## Lab

1. `Node { localMat4, mesh, children }`.
2. `function draw(node, parentWorld)`.
3. Two-bone arm **or** turret on a tank.
4. Key `A` toggles axes.

Done when moving the parent moves the child, and rotating the child does not move the parent.

---

## Homework

1. Written: expand `worldMoon` as a product of named matrices.
2. Code: scene graph JSON loader (tiny: array of nodes with `parent` index) **or** hardcode the solar system cleanly.
3. Written: instancing vs cloning vertices.

---

## Quiz (10 min)

1. What does M do to a vertex? (2 pts)
2. `world = ? * local` (2 pts)
3. Draw a 3-node chain and write the product for the leaf. (4 pts)
4. Why a normal matrix? One sentence. (2 pts)

---

## Common mistakes

- `local * parent` (row-vector hangover).
- Updating local from world every frame and drifting (Euler integration of matrices).
- Scaling the parent and wondering why the child’s offset explodes (it should).

---

## Board drawings

1. Nested frames, Sun–Earth–Moon.
2. Tree with matrices on edges.
3. RGB axes on a tilted cube.
