# Lecture 6 — Line segment intersection (sweep line)

**Time:** 75 min lecture + 60 min live coding  
**Algorithm this week:** Bentley–Ottmann at teaching level  
**Board first:** a vertical line moving right, active segments sorted along it

---


This file is a **session guide** ([[Teaching/24 Session Guides]]) plus the detailed notes. Run the 75 minutes as **moves** (Say / Ask / Board / Slide / They do). Detailed notes follow.

## Before you enter

- Demo: `Computational Geometry/code/06-shoelace.html` (local, no CDN). Serve the folder if ES modules fail.
- Backup: board first — a vertical line moving right, active segments sorted along it.
- Parked strip: `Lecture 6 | Line segment intersection (sweep line) | Invariant: predicates before constructions; degeneracy is the course`
- Quiz from last lecture (except Lecture 1 / midterm / presentations).

## Board at the end (they photograph this)

```
a vertical line moving right, active segments sorted along it
Sweep line, three active segments, T listed by y.
Event timeline: LEFT, LEFT, INTER, RIGHT, …
Two segments that cross, status before and after swap.
```

## Slides today (cap: 6)

Photograph, animation, or 20pt code only. If a slide has the argument in sentences, delete the sentences and write them on the board.

## How to run this meeting

Use the **Timing** or **Classroom moves** table below as the 75-minute spine. For each block: **Say** the question, **Board** the picture, **They do** a fragment, **Do not** skip the attempt. Then stand up for live coding (60 min).

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 5 |
| 10–20 | Naive O(n²) and why we can do better |
| 20–40 | Sweep line, events, status |
| 40–60 | Bentley–Ottmann, degeneracy |
| 60–75 | Graphics uses; what the lab will simplify |

---

## Learning goals

1. State the naive bound and when it is optimal (Θ(n²) intersections).
2. Describe a plane sweep: event queue + status.
3. List the event types: left endpoint, right endpoint, intersection.
4. Explain why only **adjacent** segments in the status can be the next intersection.
5. Implement a teaching sweep with a sorted list (n ≤ 200), not a red-black tree.

---

## 1. Naive algorithm (10 min)

```
for every pair of segments:
    if they intersect: report it
```

Time Θ(n²). Space O(1) extra besides the output.

If there are I = Θ(n²) intersections, **any** algorithm is Ω(n²) just to write them down. Sweep is interesting when I is smaller: maps, UI edges, CAD, almost-planar drawings.

Output-sensitive target: **O((n + I) log n)**.

---

## 2. The sweep idea (20 min)

Imagine a vertical line L moving from x = −∞ to +∞.

At a typical x, L hits a subset of segments. That subset is the **status**. Order the status by y-coordinate of the hit.

**Key lemma (teaching).**  
Two segments can intersect to the right of L only if they are **neighbors** in the status, or will become neighbors after some event. So we only test neighbors.

### Event queue Q

A priority queue of x-coordinates (then y as tie-break):

| Event | When | What we do |
| --- | --- | --- |
| LEFT | left endpoint of a segment | insert segment into status; test against its two new neighbors |
| RIGHT | right endpoint | delete segment; test the two neighbors that just became adjacent |
| INTER | crossing of two segments | report the point; **swap** the two segments in the status; test new neighbor pairs |

Store events so each geometric point is unique. If we discover an intersection, we insert an INTER event at that x, unless it is already in Q.

### Status T

Ideally a balanced BST ordered by the y-order along L.  
For the lab: a sorted array, O(n) insert/delete, fine for n ≤ 200.

### Invariant

All intersections with x less than the current event have been reported. The status is the set of segments stabbed by L, ordered by y.

---

## 3. Bentley–Ottmann, teaching version (20 min)

```
sweep(segments):
    Q = all LEFT and RIGHT endpoints
    T = empty status
    I = []
    while Q is not empty:
        e = pop min x
        if e is LEFT of s:
            insert s into T
            test(s, above(s)); test(s, below(s))
        else if e is RIGHT of s:
            a, b = above(s), below(s)
            delete s from T
            test(a, b)
        else: // INTER of s, t
            report e.point
            swap s and t in T
            test each with its new outer neighbor
    return I

test(s, t):
    if s, t exist and intersect at p with p.x >= current x:
        insert INTER(p, s, t) into Q if new
```

Use Week 2’s `segmentsIntersect`. Only `proper` (and, by policy, `touch`) generate INTER events.

### Complexity

Each event costs O(log n) with a heap + BST.  
Number of events ≤ 2n + I.  
**O((n + I) log n).**

With a list, **O((n + I) n)**, acceptable in lab.

### Degeneracy (spend time here)

1. **Vertical segments.** A vertical segment has left = right. Treat it as a special event: insert and delete at the same x, or perturb. Simplest lab policy: reject verticals, or store them with a tiny x-tilt documented in the README.
2. **Several segments meet at one point.** One INTER event with a bundle. Swap the whole bundle reverse-order.
3. **Overlapping collinear segments.** Not a point intersection. Report `overlap` separately; do not put a single INTER in Q.
4. **Endpoint lying on another segment.** `touch`. Decide: report as intersection, split the segment (needed later for DCEL), or ignore. Course default: **report touch, do not split** until Week 8.

---

## 4. Why the status order is “along L,” not “by endpoint y” (10 min)

Two segments can have left-endpoint y in one order and, after they cross, the opposite order. The status must be the order **at the current x**. After an INTER, we swap.

If a student sorts T by the y of left endpoints and never swaps, they will miss later intersections.

Draw this counterexample and leave it up.

---

## 5. Graphics (5 min)

- Map overlay (two road networks)
- CAD edge intersections
- Clipping a polyline against a window
- UI: do these two strokes meet?
- Mesh repair: self-intersecting outlines (Week 13 / project)

---

## Live coding (60 min)

Do **not** write a red-black tree.

Visualizer:

- n segments, draggable endpoints
- a vertical sweep line the professor can scrub
- status listed at the right, top to bottom
- events drawn as ticks on the x-axis
- intersections as dots

Script:

1. Two crossing segments — one INTER, a swap, status order flips.
2. Three segments, only two intersections — show that the third pair is never tested while non-adjacent.
3. T-junction — `touch`.
4. AABB-overlap, no intersection — no event.

Implement the list-based sweep live if time; otherwise scrub a prepared demo and implement the event loop together.

---

## Lab

1. Input: list of segments. Output: all `proper` and `touch` points, drawn.
2. Use a sorted list for T and a binary heap or sorted array for Q.
3. n ≤ 200. Brute-force pairs as an oracle: the two outputs must match (as sets of points, with an epsilon).
4. Reject or specially handle verticals; document the choice.

Done when the oracle and the sweep agree on a random 80-segment instance.

---

## Homework

1. Written: why only neighbors in T need to be tested. 1 page, with the “cross only if they become adjacent” picture.
2. Written: why status order is the y-order along L, not endpoint y. Use the crossing-pair counterexample.
3. Code: teaching sweep + oracle test.

---

## Quiz (10 min)

1. Naive time? Sweep time in n and I (BST version)? (2 pts)
2. Name the three event types. (2 pts)
3. After an INTER, what happens in T? (2 pts)
4. If I = n²/4, is sweep asymptotically better than naive? (2 pts)
5. Why can a list replace a BST in the lab? (2 pts)

---

## Common mistakes

- Testing every pair still, and calling it a sweep because a line is drawn.
- Not swapping at INTER.
- Inserting the same intersection twice and looping.
- Using `touch` as `none`.
- Vertical segments crashing the x-order.

---

## Board drawings

1. Sweep line, three active segments, T listed by y.
2. Event timeline: LEFT, LEFT, INTER, RIGHT, …
3. Two segments that cross, status before and after swap.

---

## Extra exercises and snippets

Sheet: [[Computational Geometry/exercises/Week 06]] · Demos: [09-naive](code/09-naive-intersect.html), [10-sweep](code/10-sweep.html)

1. Three event types and one action each.
2. If I = n²/4, is sweep better than naive?
3. Status is y-order along L, not endpoint y. Counterexample picture.
4. Naive vs `teachingSweep` hit-pair sets must match on 16 random segments.

```js
for (let i = 0; i < n; i++)
  for (let j = i + 1; j < n; j++)
    report(segmentsIntersect(S[i].a, S[i].b, S[j].a, S[j].b));
```
