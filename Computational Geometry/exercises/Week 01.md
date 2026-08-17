# Extra exercises — Week 1 (orientation)

Lecture: [[Computational Geometry/Week 01 What Computational Geometry Is]]  
Demo: [01-orient.html](../code/01-orient.html)

---

## Written

1. Compute `cross(A,B,C)` and `orient` for A=(0,0), B=(4,1), C=(1,3). LEFT, RIGHT, or COLLINEAR?
2. Same three points, translated by (1000, −50). What happens to `orient`? To `atan2(C-A)` vs `atan2(B-A)`?
3. Predicate or construction: (a) left of line, (b) intersection point, (c) circumcenter, (d) “segments overlap”?
4. Give four degenerate cases you expect in this course (not just “points coincide”).
5. Why is `orient(A,B,C)` not equal to `orient(B,A,C)`? One sentence and one picture.
6. Signed area of triangle ABC is `cross/2`. What is the signed area if you reverse the vertex order?
7. A student writes `if (cross === 0)`. Why is that a policy bug even when it “works” on the board examples?
8. Reduce “is P inside triangle ABC” to three orientation tests. State the boundary policy.
9. Why do we print the raw cross value in the visualizer, not only LEFT/RIGHT?
10. Name the four flagship problems of the course (hull, intersection, triangulation, proximity/search) and one graphics use each.

## Coding

11. Implement `orient` and eight tests (the homework list). Add two more: a 1e-12-height triangle, and C = B.
12. Implement `projectToLine(c, a, b)` that returns the closest point on the **line** AB (not the segment). Then clamp to the segment. Tests: C on the segment, C beyond B, C off the line.
13. Visualizer: button “nudge C by 1e-8 perpendicular to AB”. Watch `orient` flip or go collinear. Write one sentence on EPS.

## Snippet — kernel

```js
export function cross(a, b, c) {
  return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

export function orient(a, b, c, eps = 1e-9) {
  const v = cross(a, b, c);
  if (v > eps) return 1;   // LEFT / CCW
  if (v < -eps) return -1; // RIGHT / CW
  return 0;                // COLLINEAR
}

export function signedArea3(a, b, c) {
  return 0.5 * cross(a, b, c);
}
```

## Snippet — point in triangle (boundary = BOUNDARY)

```js
function pointInTriangle(q, a, b, c, eps = 1e-9) {
  if (onSegment(q, a, b) || onSegment(q, b, c) || onSegment(q, c, a)) return "BOUNDARY";
  const o1 = orient(a, b, q, eps);
  const o2 = orient(b, c, q, eps);
  const o3 = orient(c, a, q, eps);
  if (o1 === o2 && o2 === o3 && o1 !== 0) return "INSIDE";
  return "OUTSIDE";
}
```

## Hidden fixtures (paste into tests)

```js
assert(orient({x:0,y:0},{x:1,y:0},{x:1,y:1}) === 1);
assert(orient({x:0,y:0},{x:1,y:0},{x:1,y:-1}) === -1);
assert(orient({x:0,y:0},{x:2,y:0},{x:1,y:0}) === 0);
assert(orient({x:0,y:0},{x:2,y:0},{x:0,y:0}) === 0);
assert(orient({x:5,y:5},{x:7,y:5},{x:6,y:8}) === 1); // translation
```
