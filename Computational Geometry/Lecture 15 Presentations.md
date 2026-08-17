# Lecture 15 — Project presentations

**Time:** full session of 12 + 5 minute slots  
**No new lecture**  
**Deliverables:** live demo, repo, 6–8 page report, 30-second recording

---

## Before the session

- Room: projector + one spare HDMI/USB-C dongle.
- Load each team’s recording as backup.
- Print the rubric (below) one sheet per team.
- Order: random or by project type (all Voronoi, then all picking) so comparison is fair.
- A TA keeps time: 10-minute warning, 12-minute stop.

---

## Slot format

| Time | Who | What |
| --- | --- | --- |
| 12 min | team | problem, algorithm, live demo, limitations |
| 5 min | examiner | two questions from the Week 14 list, plus one specific to their code |
| 1 min | — | switch |

If the demo dies, play the recording and continue. Do not debug for five minutes in front of the class.

---

## Required deliverables

1. **Live demo** of the student algorithm.
2. **Repository** with README, kernel, tests, and a note on libraries.
3. **Report** 6–8 pages, captions on figures.
4. **30-second recording** for the IGWT portfolio / exhibition.

Late report: follow the department rule you announced in Week 1. Suggested: −10% per 24 hours, zero after 72 hours.

---

## Rubric (30% of the course)

Copy onto the grade sheet.

| Criterion | Weight | 5 | 3 | 1 |
| --- | --- | --- | --- | --- |
| Correct algorithm (tests + degeneracy) | 30% | Kernel matches the lecture invariant; tests include a degenerate case | Algorithm works on happy input; weak tests | Library does the work, or wrong algorithm |
| Visual explanation | 20% | Viewer shows the invariant (stack, strip, illegal edge, sweep, …) | Result is visible, process is not | Screenshots of a finished mesh only |
| Code and repository | 15% | Runs from README; one kernel; clear authors | Runs with tribal knowledge | Does not run on the lab machine |
| Report | 20% | Problem, complexity, degeneracy, honest limits, citations | Write-up exists but skips complexity or degeneracy | Tutorial padding, no figures |
| Presentation and demo | 15% | 12 minutes, ugly input shown, questions answered | Demo works, story is fuzzy | Over time, or cannot answer the predicate question |

Half-points are allowed. Three teammates may receive different participation adjustments if the repo history and the Q&A make that obvious. Announce this in Week 1.

---

## Suggested questions by project type

**Map editor.** How do you report a T-junction? Do you split the DCEL edge?

**Polygon modeler.** Ear or CDT? Show a reflex vertex that is not an ear.

**Terrain / city.** Dual: which Voronoi vertex is which Delaunay triangle? Empty circle?

**Physics.** Hull policy for collinear? SAT vs segment tests?

**Picking / configurator.** What do you prune? Barycentric meaning for “which part”?

**Path demo.** Visibility edge vs Voronoi roadmap. Shortest vs safest?

**Stipple.** Discrete vs exact Voronoi. What is a vertex in the pixel picture?

**Mesh repair.** Which intersections do you insert? Is the result a valid DCEL?

Always ask: **“Where is `orient` (or incircle) in your repo?”**

---

## After the session

- Collect repos as tags / zips.
- Pick 3–4 demos for the annual IGWT exhibition.
- Note one curriculum fix for next year (where did everyone break?).
- Typical fixes: more time on `onSegment`, a provided visualizer, a smaller n cap on Delaunay.

---

## What you say in the last two minutes of the course

Computational geometry in this program is not a museum of algorithms.

It is the habit of:

1. naming the predicate,
2. drawing the invariant,
3. testing the degenerate case,
4. only then putting the result on a GPU.

That habit is what they should take into Computer Graphics I, WebGL, and the capstone.

---

## Quiz / homework

None. Grades close when the report and repo are in.

---

## Board

The rubric table. The clock. Nothing else.

---

## Extra exercises and snippets

Sheet: [[Computational Geometry/exercises/Week 15]] · Tests: [19-kernel-tests.html](code/19-kernel-tests.html)

Rehearse the 12 + 5 once with a TA timer. Each teammate answers one:

1. Predicate, three return values.
2. Test that fails if it flips.
3. Library file vs student file.
4. Degeneracy you actually shipped.

Do not add algorithms this week.
