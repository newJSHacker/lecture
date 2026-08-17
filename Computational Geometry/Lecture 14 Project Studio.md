# Lecture 14 — Project studio

**Week 14 of 15** · Computational Geometry  
**Meeting:** studio (not a content lecture)  
**Kernel:** core algorithm on a non-toy input + one degeneracy handled or shown + README that runs on a lab machine  
**Success check:** a TA can serve the folder, see the invariant (stack/strip/illegal/sweep), and hear where orient lives

This meeting is **studio**. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Rubric / report headings on the parked strip.
- Clock visible.
- Demo only if a volunteer asks for a blocked kernel: `Computational Geometry/code/14-voronoi-discrete.html`.
- Parked strip: `Lecture 14 | Goal: freeze and review | Invariant: predicates before constructions; degeneracy is the course`

## Board at the end (they photograph this)

```
Report: problem · weeks · algorithm+complexity · degeneracy · kernel · results · limits · refs
Defense: predicate?  complexity and n measured?  degenerate input?
         naive vs yours?  3D break?  construction vs predicate?
         test if orient flips?  library vs you?

Cuts: Fortune → discrete Voronoi + DT dual
      map editor → intersect + DCEL walk
      3D physics → 2D hull + SAT
      shaders → unlit canvas + correct kernel
Do not invent timings.
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## Lecture / studio (75 min)

### Minutes 0–10 — Frame

**Say:** This meeting is **studio**. No third Delaunay lecture. If they are stuck on a predicate, debug the predicate. A correct O(n log n) on a plain canvas beats a broken Three.js scene. Pretty UI with no tests fails.

**Ask:** If behind, what do you cut first?

**They do:** write their cut list in one column.

**Do not:** introduce a new library today.

### Minutes 10–65 — Desk review

**Say:** Desk order: kernel (orient/intersect/incircle), visualizer, tests, report outline. Comment on the algorithm, not the CSS. Rehearse 12+5: 0–2 problem, 2–6 invariant+complexity, 6–10 live ugly input, 10–12 limits and who did what.

**They do:** Studio. Serve first. Freeze a degenerate input as reset state.

**Do not:** sit at the podium. Do not add features for them.

### Minutes 65–75 — Land

**Say:** Report draft + 30s recording before Week 15. Next week 12+5. Always ask where orient is. No quiz.

**Do not:** “Any questions?” End on the clock.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Eight headings + eight questions + clock | Photograph. |
| 10–50 | Desk review | Kernel, then viz, then tests, then outline. |
| 50–60 | 60s rehearsal with ugly input | Hard stop. |

This slot is **more studio**, not a hidden lecture.

---

## Lab

_(none this meeting)_

---

## Homework

_(none this meeting)_

---

## Quiz next meeting

None this week.

## Extra exercises

See [[Computational Geometry/exercises/Week 14]].

## Notes from the outline

**1. Report structure (15 min).** 6–8 pages, including figures. Not a blog post. Not a 30-page thesis.

| Section | What we want | Typical length |
| --- | --- | --- |
| Problem | The geometric question in one paragraph | ½ page |
| Related course ideas | Which weeks, which algorithms you did **not** use and why | ½ page |
| Algorithm | Invariants, complexity, pseudocode or clear steps | 2 pages |
| Degeneracy | At least one case: handle or document | ½–1 page |
| Implementation | Kernel, visualizer, tests | 1 page |
| Results | Screenshots, a timing table if relevant | 1 page |
| Limitations and future work | Honest | ½ page |
| References | de Berg, Ericson, Shewchuk, docs | ½ page |

**Figures must have captions.** “Figure 3. Illegal edge before flip.”

**Do not** paste 200 lines of code. A 15-line kernel is enough. The repo is the code.

**Do not** invent timings. If you did not measure, say so.

---
**2. Questions I will ask next week (15 min).** Give students this list. Next week you will actually ask two of them.

1. What is the **predicate** at the center of your project?
2. What is the complexity, and for which n did you try it?
3. Show me a degenerate input. What does your program do?
4. If I replace your main algorithm with the naive one, what do I lose?
5. What would break if we moved this to 3D?
6. Which result is a **construction**, and how do you know the predicate that supports it is right?
7. Point to the test that would fail if `orient` flipped sign.
8. What did a library do, and what did you write?

### Presentation clock (Week 15)

- 12 minutes demo + story
- 5 minutes questions
- Hard stop. Rehearse once this week with a TA timer.

Suggested 12-minute shape:

| Min | Content |
| ---: | --- |
| 0–2 | Problem and one picture |
| 2–6 | Algorithm, one invariant, one complexity sentence |
| 6–10 | Live demo, including one ugly input |
| 10–12 | Limitations, who did what |

---
**3. Studio rules.** ### Must be true before they leave today

- `npm start` / `python -m http.server` / whatever is in the README works on a lab machine.
- The core algorithm runs on more than 5 toy points.
- At least one degenerate case is either handled or shown and explained.
- README: install, run, who implemented which file.

### Professor / TA desk review (10 minutes per team)

Look at, in this order:

1. The kernel file (`orient`, intersection, incircle, …)
2. The visualizer
3. Tests
4. The report outline

Comment on the **algorithm**, not the CSS.

### Scope cuts (offer these; do not let teams “add AI”)

| If they are behind | Cut |
| --- | --- |
| Fortune half-done | Discrete Voronoi + Delaunay dual |
| Full map editor | Intersection + DCEL walk, no undo stack |
| 3D physics | 2D hull + SAT |
| Pathfinding + rendering | Visibility graph on a 2D floor plan |
| Beautiful shaders | One unlit canvas and a correct kernel |

A correct O(n log n) algorithm on a plain canvas beats a broken Three.js scene.

---

## If we run long, cut

New algorithms. Keep freeze.

## If we run short, add

Point to the test that fails if orient flips sign.
