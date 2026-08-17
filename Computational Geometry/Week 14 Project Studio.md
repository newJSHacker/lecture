# Week 14 — Project studio

**Time:** 30 min lecture, then studio until the period ends  
**No new theory**  
**Required this week:** running algorithm, one degeneracy, README

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–15 | How to write the report |
| 15–30 | Defense-style questions; presentation clock |
| 30–end | Desk review. Professor and TAs circulate. |

Do not give a third lecture on Delaunay. If a team is stuck on a predicate, debug the predicate.

---

## Learning goals (for the studio)

1. Freeze the project scope: one core algorithm, one visual story.
2. Write a report that a second examiner can grade without watching the demo twice.
3. Answer “what happens on a T-junction / collinear / duplicate?” without guessing.

---

## 1. Report structure (15 min)

6–8 pages, including figures. Not a blog post. Not a 30-page thesis.

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

## 2. Questions I will ask next week (15 min)

Give students this list. Next week you will actually ask two of them.

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

## 3. Studio rules

### Must be true before they leave today

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

## Lab

The studio **is** the lab. Attendance is required. Checkpoint grade: complete / incomplete from Week 13, plus today’s README/degeneracy check.

---

## Homework

Finish the report draft and the 30-second screen recording (portfolio). Submit the recording before Week 15 so the session cannot die on a failed HDMI cable.

---

## Quiz

None.

---

## Common failure modes this week

- Pretty UI, no tests.
- Library did the Delaunay; student drew it.
- Report is a tutorial on Three.js.
- “It works on my laptop” and no lockfile / no README.
- Three people, one git author.

---

## Board

Write only:

1. The 8 report headings
2. The 8 defense questions
3. The 12 + 5 clock

---

## Extra exercises and snippets

Sheet: [[Computational Geometry/exercises/Week 14]] · Sandbox: [20-project-sandbox.html](code/20-project-sandbox.html)

Desk-review drills (write answers in the repo, not a new essay):

1. Freeze a degenerate input as the sandbox reset state.
2. Point to the test that fails if `orient` flips sign.
3. Complexity and the n you **measured**. Do not invent timings.
4. If behind: cut Fortune → discrete Voronoi + Delaunay dual; cut shaders → unlit canvas + correct kernel.

```js
assert(andrew([
  {x:0,y:0},{x:1,y:0},{x:2,y:0},{x:1,y:1}
]).length === 3); // drop collinear middle

assert(segmentsIntersect(
  {x:0,y:0},{x:4,y:0},{x:2,y:0},{x:2,y:3}
).type === "touch");
```
