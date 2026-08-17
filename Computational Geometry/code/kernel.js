/**
 * IGWT computational-geometry kernel (2D).
 * Teaching code: readable, not a production exact-arithmetic library.
 * Copy a function into a student starter rather than importing this forever.
 *
 * Policy:
 *   orient > 0  => LEFT (CCW)
 *   orient < 0  => RIGHT (CW)
 *   orient = 0  => COLLINEAR (abs(cross) <= EPS)
 *   hull: drop strictly intermediate collinear vertices
 *   polygons: closed; last edge vn-1 → v0
 */
(function (global) {
  "use strict";

  const EPS = 1e-9;
  const CG = { EPS };

  function hypot2(dx, dy) {
    return dx * dx + dy * dy;
  }

  function dist2(a, b) {
    return hypot2(a.x - b.x, a.y - b.y);
  }

  function dist(a, b) {
    return Math.hypot(a.x - b.x, a.y - b.y);
  }

  function midpoint(a, b) {
    return { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 };
  }

  function sub(a, b) {
    return { x: a.x - b.x, y: a.y - b.y };
  }

  function add(a, b) {
    return { x: a.x + b.x, y: a.y + b.y };
  }

  function scale(a, s) {
    return { x: a.x * s, y: a.y * s };
  }

  function eq(a, b, eps) {
    eps = eps == null ? EPS : eps;
    return dist2(a, b) <= eps * eps;
  }

  /** (B-A) × (C-A) */
  function cross(a, b, c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
  }

  function signedArea3(a, b, c) {
    return 0.5 * cross(a, b, c);
  }

  function orient(a, b, c, eps) {
    eps = eps == null ? EPS : eps;
    const v = cross(a, b, c);
    if (v > eps) return 1;
    if (v < -eps) return -1;
    return 0;
  }

  function onSegment(c, a, b, eps) {
    eps = eps == null ? EPS : eps;
    if (orient(a, b, c, eps) !== 0) return false;
    return (
      c.x >= Math.min(a.x, b.x) - eps &&
      c.x <= Math.max(a.x, b.x) + eps &&
      c.y >= Math.min(a.y, b.y) - eps &&
      c.y <= Math.max(a.y, b.y) + eps
    );
  }

  function aabb(points) {
    let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
    for (const p of points) {
      if (p.x < minX) minX = p.x;
      if (p.y < minY) minY = p.y;
      if (p.x > maxX) maxX = p.x;
      if (p.y > maxY) maxY = p.y;
    }
    return { minX, minY, maxX, maxY };
  }

  function aabbOverlap(A, B, eps) {
    eps = eps == null ? EPS : eps;
    return (
      A.minX <= B.maxX + eps &&
      B.minX <= A.maxX + eps &&
      A.minY <= B.maxY + eps &&
      B.minY <= A.maxY + eps
    );
  }

  function aabbContains(box, p, eps) {
    eps = eps == null ? EPS : eps;
    return (
      p.x >= box.minX - eps &&
      p.x <= box.maxX + eps &&
      p.y >= box.minY - eps &&
      p.y <= box.maxY + eps
    );
  }

  function intersectionPoint(a, b, c, d) {
    const dx1 = b.x - a.x, dy1 = b.y - a.y;
    const dx2 = d.x - c.x, dy2 = d.y - c.y;
    const den = dx1 * dy2 - dy1 * dx2;
    if (Math.abs(den) < EPS) return null;
    const t = ((c.x - a.x) * dy2 - (c.y - a.y) * dx2) / den;
    return { x: a.x + t * dx1, y: a.y + t * dy1 };
  }

  function uniqueTouchPoints(pts, eps) {
    const out = [];
    for (const p of pts) {
      if (!out.some((q) => eq(p, q, eps))) out.push(p);
    }
    return out;
  }

  /**
   * Classify AB ∩ CD.
   * type: "proper" | "touch" | "overlap" | "none"
   */
  function segmentsIntersect(a, b, c, d, eps) {
    eps = eps == null ? EPS : eps;
    const o1 = orient(a, b, c, eps);
    const o2 = orient(a, b, d, eps);
    const o3 = orient(c, d, a, eps);
    const o4 = orient(c, d, b, eps);

    if (eq(a, b, eps) || eq(c, d, eps)) {
      const p = eq(a, b, eps) ? a : c;
      const s0 = eq(a, b, eps) ? c : a;
      const s1 = eq(a, b, eps) ? d : b;
      if (onSegment(p, s0, s1, eps)) return { type: "touch", point: p };
      return { type: "none" };
    }

    if (o1 !== 0 && o2 !== 0 && o3 !== 0 && o4 !== 0 && o1 !== o2 && o3 !== o4) {
      return { type: "proper", point: intersectionPoint(a, b, c, d) };
    }

    const hits = [];
    if (onSegment(c, a, b, eps)) hits.push(c);
    if (onSegment(d, a, b, eps)) hits.push(d);
    if (onSegment(a, c, d, eps)) hits.push(a);
    if (onSegment(b, c, d, eps)) hits.push(b);
    const uniq = uniqueTouchPoints(hits, eps);
    if (uniq.length === 0) return { type: "none" };

    const collinear = o1 === 0 && o2 === 0;
    if (collinear && uniq.length >= 2) {
      return { type: "overlap", point: uniq[0], points: uniq };
    }
    return { type: "touch", point: uniq[0] };
  }

  function pointInTriangle(q, a, b, c, eps) {
    eps = eps == null ? EPS : eps;
    if (onSegment(q, a, b, eps) || onSegment(q, b, c, eps) || onSegment(q, c, a, eps)) {
      return "BOUNDARY";
    }
    const o1 = orient(a, b, q, eps);
    const o2 = orient(b, c, q, eps);
    const o3 = orient(c, a, q, eps);
    if (o1 === o2 && o2 === o3 && o1 !== 0) return "INSIDE";
    return "OUTSIDE";
  }

  /** Even–odd ray casting with half-open edges. Boundary first. */
  function pointInPolygon(q, P, eps) {
    eps = eps == null ? EPS : eps;
    const n = P.length;
    for (let i = 0; i < n; i++) {
      const a = P[i], b = P[(i + 1) % n];
      if (onSegment(q, a, b, eps)) return "BOUNDARY";
    }
    let inside = false;
    for (let i = 0; i < n; i++) {
      const a = P[i], b = P[(i + 1) % n];
      if ((a.y > q.y) !== (b.y > q.y)) {
        const xHit = a.x + ((q.y - a.y) * (b.x - a.x)) / (b.y - a.y);
        if (q.x < xHit) inside = !inside;
      }
    }
    return inside ? "INSIDE" : "OUTSIDE";
  }

  /** Signed area. Positive ⇒ CCW. */
  function shoelace(P) {
    let s = 0;
    for (let i = 0; i < P.length; i++) {
      const a = P[i], b = P[(i + 1) % P.length];
      s += a.x * b.y - a.y * b.x;
    }
    return 0.5 * s;
  }

  function isCCW(P) {
    return shoelace(P) > 0;
  }

  function allTurnsSame(P, eps) {
    eps = eps == null ? EPS : eps;
    let sign = 0;
    const n = P.length;
    for (let i = 0; i < n; i++) {
      const o = orient(P[i], P[(i + 1) % n], P[(i + 2) % n], eps);
      if (o === 0) continue;
      if (sign === 0) sign = o;
      else if (o !== sign) return false;
    }
    return sign !== 0 || n <= 2;
  }

  function hasProperSelfIntersection(P, eps) {
    const n = P.length;
    for (let i = 0; i < n; i++) {
      const a = P[i], b = P[(i + 1) % n];
      for (let j = i + 1; j < n; j++) {
        if (Math.abs(i - j) <= 1 || (i === 0 && j === n - 1) || (j === 0 && i === n - 1)) continue;
        const c = P[j], d = P[(j + 1) % n];
        const r = segmentsIntersect(a, b, c, d, eps);
        if (r.type === "proper") return true;
      }
    }
    return false;
  }

  /**
   * "convex" | "simple-concave" | "self-intersecting" | "degenerate"
   */
  function classifyPolygon(P, eps) {
    if (!P || P.length < 3) return "degenerate";
    if (hasProperSelfIntersection(P, eps)) return "self-intersecting";
    if (allTurnsSame(P, eps)) return "convex";
    return "simple-concave";
  }

  function uniquePoints(S, eps) {
    eps = eps == null ? EPS : eps;
    const out = [];
    for (const p of S) {
      if (!out.some((q) => eq(p, q, eps))) out.push({ x: p.x, y: p.y });
    }
    return out;
  }

  function lowestThenLeftmost(S) {
    let best = S[0];
    for (const p of S) {
      if (p.y < best.y || (p.y === best.y && p.x < best.x)) best = p;
    }
    return best;
  }

  function jarvis(S, eps) {
    const P = uniquePoints(S, eps);
    if (P.length <= 2) return P.slice();
    const start = lowestThenLeftmost(P);
    const hull = [];
    let p = start;
    do {
      hull.push(p);
      let q = P[0] === p ? P[1] : P[0];
      for (const r of P) {
        if (r === p) continue;
        const o = orient(p, q, r, eps);
        if (o < 0) q = r;
        else if (o === 0 && dist2(p, r) > dist2(p, q)) q = r;
      }
      p = q;
      if (hull.length > P.length + 2) break;
    } while (p !== start);
    return hull;
  }

  function andrew(S, eps) {
    eps = eps == null ? EPS : eps;
    const P = uniquePoints(S, eps).sort((u, v) => u.x - v.x || u.y - v.y);
    if (P.length <= 2) return P.slice();

    function build(seq) {
      const h = [];
      for (const p of seq) {
        while (h.length >= 2 && orient(h[h.length - 2], h[h.length - 1], p, eps) <= 0) {
          h.pop();
        }
        h.push(p);
      }
      return h;
    }

    const lower = build(P);
    const upper = build(P.slice().reverse());
    lower.pop();
    upper.pop();
    return lower.concat(upper);
  }

  function naiveSegmentIntersections(segments, eps) {
    const hits = [];
    for (let i = 0; i < segments.length; i++) {
      for (let j = i + 1; j < segments.length; j++) {
        const r = segmentsIntersect(segments[i].a, segments[i].b, segments[j].a, segments[j].b, eps);
        if (r.type !== "none") hits.push({ i, j, type: r.type, point: r.point });
      }
    }
    return hits;
  }

  /** Teaching sweep: event list + array status. Fine for n ≤ 200. */
  function teachingSweep(segments, eps) {
    eps = eps == null ? EPS : eps;
    const segs = segments.map((s, i) => {
      let a = s.a, b = s.b;
      if (a.x > b.x || (Math.abs(a.x - b.x) < eps && a.y > b.y)) {
        a = s.b;
        b = s.a;
      }
      return { i, a, b };
    });
    const Q = [];
    segs.forEach((s) => {
      Q.push({ kind: "LEFT", x: s.a.x, y: s.a.y, s });
      Q.push({ kind: "RIGHT", x: s.b.x, y: s.b.y, s });
    });
    const hits = [];
    const seen = new Set();
    const T = [];

    function yAt(s, x) {
      const dx = s.b.x - s.a.x;
      if (Math.abs(dx) < eps) return s.a.y;
      const t = (x - s.a.x) / dx;
      return s.a.y + t * (s.b.y - s.a.y);
    }

    function sortStatus(x) {
      T.sort((u, v) => yAt(u, x) - yAt(v, x) || u.i - v.i);
    }

    function testPair(u, v, xNow) {
      if (!u || !v) return;
      const key = u.i < v.i ? u.i + "," + v.i : v.i + "," + u.i;
      if (seen.has(key)) return;
      const r = segmentsIntersect(u.a, u.b, v.a, v.b, eps);
      if (r.type === "none" || !r.point) return;
      if (r.point.x + eps < xNow) return;
      seen.add(key);
      hits.push({ i: u.i, j: v.i, type: r.type, point: r.point });
      Q.push({ kind: "INTER", x: r.point.x, y: r.point.y, u, v });
    }

    while (Q.length) {
      Q.sort((e, f) => e.x - f.x || e.y - f.y);
      const e = Q.shift();
      if (e.kind === "LEFT") {
        T.push(e.s);
        sortStatus(e.x);
        const k = T.indexOf(e.s);
        testPair(T[k - 1], e.s, e.x);
        testPair(e.s, T[k + 1], e.x);
      } else if (e.kind === "RIGHT") {
        const k = T.indexOf(e.s);
        const above = T[k - 1], below = T[k + 1];
        T.splice(k, 1);
        testPair(above, below, e.x);
      } else if (e.kind === "INTER") {
        const iu = T.indexOf(e.u), iv = T.indexOf(e.v);
        if (iu < 0 || iv < 0) continue;
        T[iu] = e.v;
        T[iv] = e.u;
        sortStatus(e.x + 1e-6);
        const a = T.indexOf(e.u), b = T.indexOf(e.v);
        testPair(T[a - 1], T[a], e.x);
        testPair(T[a], T[a + 1], e.x);
        testPair(T[b - 1], T[b], e.x);
        testPair(T[b], T[b + 1], e.x);
      }
    }
    return hits;
  }

  function isConvexVertex(P, i, ccw, eps) {
    const n = P.length;
    const o = orient(P[(i + n - 1) % n], P[i], P[(i + 1) % n], eps);
    if (o === 0) return false;
    return ccw ? o > 0 : o < 0;
  }

  function isEar(P, i, ccw, eps) {
    if (!isConvexVertex(P, i, ccw, eps)) return false;
    const n = P.length;
    const a = P[(i + n - 1) % n], b = P[i], c = P[(i + 1) % n];
    for (let j = 0; j < n; j++) {
      if (j === (i + n - 1) % n || j === i || j === (i + 1) % n) continue;
      const loc = pointInTriangle(P[j], a, b, c, eps);
      if (loc !== "OUTSIDE") return false;
    }
    return true;
  }

  function earClip(P, eps) {
    const poly = P.map((p) => ({ x: p.x, y: p.y }));
    if (poly.length < 3) return [];
    const ccw = shoelace(poly) >= 0;
    const V = poly.slice();
    const T = [];
    let guard = 0;
    while (V.length > 3 && guard++ < poly.length * poly.length) {
      let found = false;
      for (let i = 0; i < V.length; i++) {
        if (isEar(V, i, ccw, eps)) {
          const n = V.length;
          T.push([V[(i + n - 1) % n], V[i], V[(i + 1) % n]]);
          V.splice(i, 1);
          found = true;
          break;
        }
      }
      if (!found) break;
    }
    if (V.length === 3) T.push([V[0], V[1], V[2]]);
    return T;
  }

  function buildKd(points, depth) {
    if (!points.length) return null;
    if (points.length === 1) return { leaf: true, p: points[0], box: aabb(points) };
    const axis = depth % 2;
    const sorted = points.slice().sort((u, v) => (axis === 0 ? u.x - v.x : u.y - v.y));
    const mid = Math.floor(sorted.length / 2);
    const node = {
      leaf: false,
      axis,
      p: sorted[mid],
      left: buildKd(sorted.slice(0, mid), depth + 1),
      right: buildKd(sorted.slice(mid + 1), depth + 1),
      box: aabb(points),
    };
    return node;
  }

  function rangeQuery(node, R, out) {
    if (!node) return;
    if (!aabbOverlap(node.box, R)) return;
    if (aabbContains(R, node.p)) out.push(node.p);
    if (node.leaf) return;
    rangeQuery(node.left, R, out);
    rangeQuery(node.right, R, out);
  }

  function nearestSite(p, sites) {
    let best = sites[0], bestD = dist2(p, sites[0]);
    for (let i = 1; i < sites.length; i++) {
      const d = dist2(p, sites[i]);
      if (d < bestD) {
        bestD = d;
        best = sites[i];
      }
    }
    return best;
  }

  function circumcenter(a, b, c) {
    const d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y));
    if (Math.abs(d) < EPS) return null;
    const a2 = a.x * a.x + a.y * a.y;
    const b2 = b.x * b.x + b.y * b.y;
    const c2 = c.x * c.x + c.y * c.y;
    const x = (a2 * (b.y - c.y) + b2 * (c.y - a.y) + c2 * (a.y - b.y)) / d;
    const y = (a2 * (c.x - b.x) + b2 * (a.x - c.x) + c2 * (b.x - a.x)) / d;
    return { x, y };
  }

  /**
   * Incircle predicate. abc should be CCW.
   * > 0 ⇒ d inside circumcircle; < 0 outside; 0 cocircular.
   */
  function incircle(a, b, c, d) {
    const adx = a.x - d.x, ady = a.y - d.y;
    const bdx = b.x - d.x, bdy = b.y - d.y;
    const cdx = c.x - d.x, cdy = c.y - d.y;
    const det =
      (adx * adx + ady * ady) * (bdx * cdy - cdx * bdy) -
      (bdx * bdx + bdy * bdy) * (adx * cdy - cdx * ady) +
      (cdx * cdx + cdy * cdy) * (adx * bdy - bdx * ady);
    const o = orient(a, b, c);
    return o < 0 ? -det : det;
  }

  function pointInCircumcircle(p, a, b, c, eps) {
    eps = eps == null ? 1e-7 : eps;
    return incircle(a, b, c, p) > eps;
  }

  function edgeKey(u, v) {
    return u.x < v.x || (u.x === v.x && u.y < v.y)
      ? u.x + "," + u.y + "|" + v.x + "," + v.y
      : v.x + "," + v.y + "|" + u.x + "," + u.y;
  }

  function bowyerWatson(points, eps) {
    const P = uniquePoints(points, eps);
    if (P.length < 3) return [];
    const box = aabb(P);
    const dx = Math.max(box.maxX - box.minX, 1);
    const dy = Math.max(box.maxY - box.minY, 1);
    const d = Math.max(dx, dy) * 20;
    const mid = { x: (box.minX + box.maxX) / 2, y: (box.minY + box.maxY) / 2 };
    const s1 = { x: mid.x - d, y: mid.y - d, super: true };
    const s2 = { x: mid.x + d, y: mid.y - d, super: true };
    const s3 = { x: mid.x, y: mid.y + d, super: true };
    let triangles = [{ a: s1, b: s2, c: s3 }];

    for (const p of P) {
      const bad = [];
      const good = [];
      for (const t of triangles) {
        if (pointInCircumcircle(p, t.a, t.b, t.c, eps)) bad.push(t);
        else good.push(t);
      }
      const count = new Map();
      function bump(u, v) {
        const k = edgeKey(u, v);
        const rec = count.get(k) || { u, v, n: 0 };
        rec.n++;
        count.set(k, rec);
      }
      for (const t of bad) {
        bump(t.a, t.b);
        bump(t.b, t.c);
        bump(t.c, t.a);
      }
      const hole = [];
      count.forEach((rec) => {
        if (rec.n === 1) hole.push(rec);
      });
      triangles = good;
      for (const e of hole) triangles.push({ a: e.u, b: e.v, c: p });
    }

    return triangles.filter(
      (t) => !t.a.super && !t.b.super && !t.c.super
    );
  }

  function bruteClosestPair(P) {
    let best = { dist: Infinity, a: P[0], b: P[1] };
    for (let i = 0; i < P.length; i++) {
      for (let j = i + 1; j < P.length; j++) {
        const d = dist(P[i], P[j]);
        if (d < best.dist) best = { dist: d, a: P[i], b: P[j] };
      }
    }
    return best;
  }

  function closestPairRec(Px, Py) {
    const n = Px.length;
    if (n <= 3) return bruteClosestPair(Px);
    const mid = Math.floor(n / 2);
    const midX = Px[mid].x;
    const Lset = new Set(Px.slice(0, mid));
    const PxL = Px.slice(0, mid);
    const PxR = Px.slice(mid);
    const PyL = Py.filter((p) => Lset.has(p));
    const PyR = Py.filter((p) => !Lset.has(p));
    const left = closestPairRec(PxL, PyL);
    const right = closestPairRec(PxR, PyR);
    let best = left.dist < right.dist ? left : right;
    const strip = Py.filter((p) => Math.abs(p.x - midX) < best.dist);
    for (let i = 0; i < strip.length; i++) {
      for (let j = i + 1; j < strip.length && j <= i + 7; j++) {
        if (strip[j].y - strip[i].y >= best.dist) break;
        const d = dist(strip[i], strip[j]);
        if (d < best.dist) best = { dist: d, a: strip[i], b: strip[j] };
      }
    }
    return best;
  }

  function closestPair(points) {
    const P = uniquePoints(points);
    if (P.length < 2) return null;
    const Px = P.slice().sort((u, v) => u.x - v.x || u.y - v.y);
    const Py = P.slice().sort((u, v) => u.y - v.y || u.x - v.x);
    return closestPairRec(Px, Py);
  }

  function triangleAABB(t) {
    return aabb([t.a, t.b, t.c]);
  }

  function buildBVH(triangles) {
    const items = triangles.map((t, i) => ({ t, i, box: triangleAABB(t) }));
    function rec(list, depth) {
      if (list.length === 1) return { leaf: true, item: list[0], box: list[0].box };
      const axis = depth % 2;
      list.sort((u, v) => {
        const cu = axis === 0 ? (u.box.minX + u.box.maxX) / 2 : (u.box.minY + u.box.maxY) / 2;
        const cv = axis === 0 ? (v.box.minX + v.box.maxX) / 2 : (v.box.minY + v.box.maxY) / 2;
        return cu - cv;
      });
      const mid = Math.floor(list.length / 2);
      const left = rec(list.slice(0, mid), depth + 1);
      const right = rec(list.slice(mid), depth + 1);
      const box = {
        minX: Math.min(left.box.minX, right.box.minX),
        minY: Math.min(left.box.minY, right.box.minY),
        maxX: Math.max(left.box.maxX, right.box.maxX),
        maxY: Math.max(left.box.maxY, right.box.maxY),
      };
      return { leaf: false, left, right, box };
    }
    return rec(items, 0);
  }

  function pickBVH(node, q, hits) {
    if (!aabbContains(node.box, q)) return;
    if (node.leaf) {
      const t = node.item.t;
      if (pointInTriangle(q, t.a, t.b, t.c) !== "OUTSIDE") hits.push(node.item);
      return;
    }
    pickBVH(node.left, q, hits);
    pickBVH(node.right, q, hits);
  }

  /** Minimal half-edge from a triangle list. Faces are the triangles + unbounded unused. */
  function trianglesToDCEL(triangles) {
    const verts = [];
    function vid(p) {
      const i = verts.findIndex((q) => eq(p, q));
      if (i >= 0) return i;
      verts.push({ x: p.x, y: p.y, incident: -1 });
      return verts.length - 1;
    }
    const half = [];
    const edgeMap = new Map();
    triangles.forEach((t, fi) => {
      const ids = [vid(t.a), vid(t.b), vid(t.c)];
      const start = half.length;
      for (let k = 0; k < 3; k++) {
        const he = {
          origin: ids[k],
          twin: -1,
          next: start + ((k + 1) % 3),
          prev: start + ((k + 2) % 3),
          face: fi,
        };
        half.push(he);
        if (verts[ids[k]].incident < 0) verts[ids[k]].incident = start + k;
        edgeMap.set(ids[k] + "→" + ids[(k + 1) % 3], start + k);
      }
    });
    half.forEach((he, i) => {
      const dest = half[he.next].origin;
      const twin = edgeMap.get(dest + "→" + he.origin);
      if (twin != null) he.twin = twin;
    });
    return { verts, half, nFaces: triangles.length };
  }

  function walkFace(dcel, faceIndex) {
    const start = dcel.half.findIndex((h) => h.face === faceIndex);
    if (start < 0) return [];
    const ids = [];
    let e = start;
    do {
      ids.push(dcel.half[e].origin);
      e = dcel.half[e].next;
    } while (e !== start && ids.length < 64);
    return ids.map((i) => dcel.verts[i]);
  }

  CG.dist = dist;
  CG.dist2 = dist2;
  CG.midpoint = midpoint;
  CG.sub = sub;
  CG.add = add;
  CG.scale = scale;
  CG.eq = eq;
  CG.cross = cross;
  CG.signedArea3 = signedArea3;
  CG.orient = orient;
  CG.onSegment = onSegment;
  CG.aabb = aabb;
  CG.aabbOverlap = aabbOverlap;
  CG.aabbContains = aabbContains;
  CG.intersectionPoint = intersectionPoint;
  CG.segmentsIntersect = segmentsIntersect;
  CG.pointInTriangle = pointInTriangle;
  CG.pointInPolygon = pointInPolygon;
  CG.shoelace = shoelace;
  CG.isCCW = isCCW;
  CG.allTurnsSame = allTurnsSame;
  CG.hasProperSelfIntersection = hasProperSelfIntersection;
  CG.classifyPolygon = classifyPolygon;
  CG.uniquePoints = uniquePoints;
  CG.lowestThenLeftmost = lowestThenLeftmost;
  CG.jarvis = jarvis;
  CG.andrew = andrew;
  CG.naiveSegmentIntersections = naiveSegmentIntersections;
  CG.teachingSweep = teachingSweep;
  CG.isEar = isEar;
  CG.earClip = earClip;
  CG.buildKd = buildKd;
  CG.rangeQuery = rangeQuery;
  CG.nearestSite = nearestSite;
  CG.circumcenter = circumcenter;
  CG.incircle = incircle;
  CG.pointInCircumcircle = pointInCircumcircle;
  CG.bowyerWatson = bowyerWatson;
  CG.bruteClosestPair = bruteClosestPair;
  CG.closestPair = closestPair;
  CG.buildBVH = buildBVH;
  CG.pickBVH = pickBVH;
  CG.trianglesToDCEL = trianglesToDCEL;
  CG.walkFace = walkFace;

  global.CG = CG;
})(typeof window !== "undefined" ? window : globalThis);
