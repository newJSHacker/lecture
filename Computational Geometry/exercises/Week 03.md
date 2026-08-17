# Extra exercises — Week 3 (convexity and polygons)

Lecture: [[Computational Geometry/Week 03 Convexity and Polygons]]  
Demo: [06-shoelace.html](../code/06-shoelace.html)

---

## Written

1. Define a convex set. Is the union of two disks convex? Their intersection?
2. Write a convex combination of three points that is the centroid. What are the λi?
3. Classify: convex hexagon, C-shape, bowtie, star polygon (self-touching). Simple? Convex?
4. A 6-gon has turns +, +, +, −, +, +. Assume simple. Classification?
5. Prove (short): a simple polygon is convex iff every turn has the same sign (ignoring collinear policy).
6. Why does the same-turn test **fail** on a bowtie? Compute the turn signs.
7. Shoelace of (0,0), (6,0), (6,2), (0,2). Signed area? Reverse the vertices.
8. Why do most algorithms this semester assume a **simple** polygon?
9. Interior angle 180° (collinear edge). Convex vertex or not under the course policy?
10. Give a simple concave polygon that has exactly one reflex vertex.

## Coding

11. `classifyPolygon` → `convex` | `simple-concave` | `self-intersecting` | `degenerate`. Skip adjacent edges when testing intersections.
12. Shoelace + a “force CCW” button that reverses vertices if signed area is negative.
13. Highlight reflex vertices (turn sign disagrees with overall orientation).

## Snippet — shoelace and class

```js
function shoelace(P) {
  let s = 0;
  for (let i = 0; i < P.length; i++) {
    const a = P[i], b = P[(i + 1) % P.length];
    s += a.x * b.y - a.y * b.x;
  }
  return 0.5 * s;
}

function allTurnsSame(P, eps = 1e-9) {
  let sign = 0;
  const n = P.length;
  for (let i = 0; i < n; i++) {
    const o = orient(P[i], P[(i + 1) % n], P[(i + 2) % n], eps);
    if (o === 0) continue;
    if (sign === 0) sign = o;
    else if (o !== sign) return false;
  }
  return true;
}

function classifyPolygon(P) {
  if (!P || P.length < 3) return "degenerate";
  if (hasProperSelfIntersection(P)) return "self-intersecting";
  if (allTurnsSame(P)) return "convex";
  return "simple-concave";
}
```

## Hidden fixtures

```js
assert(Math.abs(shoelace([{x:0,y:0},{x:2,y:0},{x:0,y:2}]) - 2) < 1e-9);
assert(classifyPolygon([{x:0,y:0},{x:1,y:0},{x:1,y:1},{x:0,y:1}]) === "convex");
assert(classifyPolygon([{x:0,y:0},{x:3,y:0},{x:3,y:3},{x:1,y:3},{x:1,y:1},{x:0,y:1}]) === "simple-concave");
assert(classifyPolygon([{x:0,y:0},{x:2,y:2},{x:0,y:2},{x:2,y:0}]) === "self-intersecting");
```
