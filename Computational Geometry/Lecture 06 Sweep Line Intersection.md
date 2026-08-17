# Lecture 6 — Line segment intersection (sweep line)

**Week 6 of 15** · Computational Geometry  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** sweep: Q events LEFT/RIGHT/INTER; T = y-order along L; test only neighbors; swap at INTER  
**Success check:** oracle (all pairs) matches sweep on 80 segments; they can say why endpoint-y order is wrong

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Computational Geometry/code/06-shoelace.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: the sweep-line pattern, not only the intersection formula | Invariant: predicates before constructions; degeneracy is the course`

## Board at the end (they photograph this)

```
naive Θ(n²)     if I=Θ(n²) any algo is Ω(n²) to write
target O((n+I) log n)     lab list: O((n+I) n), n≤200

LEFT:  insert; test two neighbors
RIGHT: delete; test the two that meet
INTER: report; SWAP in T; test new outer neighbors

status = order along L at current x, not left-endpoint y
verticals: reject or tiny tilt, document
overlap ≠ INTER point     touch: report, do not split until Week 8
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Week 2 classified one pair. Today n segments. Drawing a vertical line and still testing every pair is not a sweep. Only neighbors in the status can be the next crossing.

**Ask:** After INTER, what happens in T? Wait. Want: swap.

**Board:** parked strip. Then a vertical line moving right, active segments sorted along it.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Line segment intersection (sweep line)*.

**Do not:** Testing every pair still, and calling it a sweep because a line is drawn.

### Minutes 10–12 — Frame

**Say:** No red-black tree in the lab. Sorted list is enough. Several segments at one point: bundle reverse-order. Do not invent timings; the story is neighbor tests vs n² pairs.

**Ask:** If I=n²/4, is sweep asymptotically better than naive?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Invariant: all intersections to the left of L reported; T is stabbed segments ordered by y.

**Board:** sweep line, three active, T by y. Event timeline LEFT LEFT INTER RIGHT. Cross, status before/after swap.

**Say:** Graphics: overlay, CAD, clip, UI strokes, mesh-repair outlines.

**Ask:** Name the three event types.

**They do:** 1 page: why only neighbors. Counterexample: status by endpoint y misses a later cross.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Scrub a vertical line; status listed top to bottom; events as ticks. Script: two-cross + swap; three segments only two tests while non-adjacent; T-junction touch; AABB overlap no event. Demo 10-sweep.html (naive 09 as oracle). Plant not swapping. Plant inserting the same INTER twice and looping. Plant verticals crashing x-order.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** test(s,t): if proper/touch at p with p.x≥current, insert INTER if new. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: teaching sweep + brute oracle, n≤200; document vertical policy. Homework: neighbor lemma + endpoint-y counterexample. Quiz: times, events, swap, I=n²/4, why a list is OK.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Naive pairs as oracle | Correct, not the algorithm. |
| 10–35 | Event loop + list T | Plant testing every pair ‘because a line is drawn.’ |
| 35–50 | Swap at INTER | Order flips. Leave the picture up. |
| 50–60 | They match oracle on 16 segments | Circulate. |

Point them at `Computational Geometry/code/06-shoelace.html` as the after-class check, not as the lecture.

---

## Lab

1. Input: list of segments. Output: all `proper` and `touch` points, drawn.
2. Use a sorted list for T and a binary heap or sorted array for Q.
3. n ≤ 200. Brute-force pairs as an oracle: the two outputs must match (as sets of points, with an epsilon).
4. Reject or specially handle verticals; document the choice.

---

## Homework

1. Written: why only neighbors in T need to be tested. 1 page, with the “cross only if they become adjacent” picture.
2. Written: why status order is the y-order along L, not endpoint y. Use the crossing-pair counterexample.
3. Code: teaching sweep + oracle test.

---

## Quiz next meeting (they hear this now)

1. Naive time? Sweep time in n and I (BST version)? (2 pts)
2. Name the three event types. (2 pts)
3. After an INTER, what happens in T? (2 pts)
4. If I = n²/4, is sweep asymptotically better than naive? (2 pts)
5. Why can a list replace a BST in the lab? (2 pts)


## Extra exercises

See [[Computational Geometry/exercises/Week 06]].

---

## Notes you may still need (from the outline)

**1. Naive algorithm (10 min).** ```
for every pair of segments:
    if they intersect: report it
```
Time Θ(n²). Space O(1) extra besides the output.
If there are I = Θ(n²) intersections, **any** algorithm is Ω(n²) just to write them down. Sweep is interesting when I is smaller: maps, UI edges, CAD, almost-planar drawings.
Output-sensitive target: **O((n + I) log n)**.
---

**2. The sweep idea (20 min).** Imagine a vertical line L moving from x = −∞ to +∞.
At a typical x, L hits a subset of segments. That subset is the **status**. Order the status by y-coordinate of the hit.
**Key lemma (teaching).**  
Two segments can intersect to the right of L only if they are **neighbors** in the status, or will become neighbors after some event. So we only test neighbors.
### Event queue Q
A priority queue of x-coordinates (then y as tie-break):
| Event | When | What we do |
| --- | --- | --- |
| LEFT | left endpoint of a segment | insert segment into status; test against its two new neighbors |
| RIGHT | right endpoint | delete segment; test the two neighbors that just became adjacent |
| INTER | crossing of two segments | report the point; **swap** the two segments in the status; test new neighbor pa

**3. Bentley–Ottmann, teaching version (20 min).** ```
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
Number

**4. Why the status order is “along L,” not “by endpoint y” (10 min).** Two segments can have left-endpoint y in one order and, after they cross, the opposite order. The status must be the order **at the current x**. After an INTER, we swap.
If a student sorts T by the y of left endpoints and never swaps, they will miss later intersections.
Draw this counterexample and leave it up.
---

**5. Graphics (5 min).** - Map overlay (two road networks)
- CAD edge intersections
- Clipping a polyline against a window
- UI: do these two strokes meet?
- Mesh repair: self-intersecting outlines (Week 13 / project)
---

---

## Common mistakes

1. Testing every pair still, and calling it a sweep because a line is drawn.
2. Not swapping at INTER.
3. Inserting the same intersection twice and looping.
4. Using `touch` as `none`.
5. Vertical segments crashing the x-order.

## If we run long, cut

BST complexity proof. Keep events + swap + neighbor lemma.

## If we run short, add

Touch as a reported event, not none.
