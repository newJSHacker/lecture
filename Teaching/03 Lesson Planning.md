# 03 — Lesson planning

A lesson plan is not a script of everything you will say. It is a sequence of student actions with times, materials, and a fallback.

If you only have slides, you have a talk. If you have this sheet, you have a class.

## The one-page plan

Copy this for every meeting. A filled example is at the end.

```
Course / week:
Learning goal (one sentence, observable):
Success check (what I will look at):
Materials (starter, slides, demo repo, quiz):
0–10   Hook / retrieval
10–25  Idea 1 + picture
25–40  Live demo / live coding
40–50  Student attempt (tiny)
50–65  Idea 2 or common bugs
65–75  Recap + next lab preview
If the demo dies:
If we run long, cut:
If we run short, add:
Students who will need a check:
```

Seventy-five minutes is the default lecture in [[04 Computational Geometry]]. Adjust the blocks; do not drop the success check.

## Start from the end

Write the learning goal as a verb a stranger could grade.

| Weak | Strong |
| --- | --- |
| Understand transformations | Apply a translation then a rotation to a point on paper and in code |
| Learn shaders | Write a fragment shader that colors by UV and explain the two compile errors I will plant |
| Know convex hulls | Trace Andrew’s chain on 8 points and name the left-turn test |

Then write the **evidence**: a sketch, a 10-line function, a screenshot, a two-sentence explanation.

If you cannot name the evidence, you are planning a vibe.

## Backward design (course scale)

1. What must they do in the final project or exam?
2. What weekly performances build that?
3. What lecture/lab pair produces each performance?

Do not start from “Chapter 4 of the textbook” unless that chapter is the performance.

For IGWT, the final performances are usually: a running scene, a short report, a demo, and answers to “what happens when this input is degenerate / this GPU is slower / this asset is 80 MB.”

## Timing is a moral issue

If you plan 90 minutes of content for 75 minutes, you will skip the student attempt. That is the part that causes learning. Cut content, not practice.

**Rule:** if a block has no student action, it may not exceed 15 minutes.

Student actions include: write, draw, predict, type, vote, pair-explain, run a test. Nodding is not an action.

## Prepare materials before the week begins

From [[02 Curriculum Design Advice]], the professor prepares slides, live-coding examples, lab manual, homework, project spec, recordings, and a repo. For one week that means:

| Artifact | Done when |
| --- | --- |
| Starter compiles on a lab machine and on a student laptop | Sunday |
| Solution exists, but is not in the student branch | Sunday |
| Lab manual has expected output (screenshot) | Sunday |
| Quiz has 5 items and a 3-minute key | Sunday |
| Demo file opens in one command | Before you sleep the night before |
| Backup: recorded 4-minute version of the demo | Before you sleep |

The most common amateur move is writing the lab at 8:00 for a 9:00 class.

## Board plan

Decide what will be on the board at the end. Students photograph the board. If the board is a mess of half-erased matrices, that becomes the notes.

Leave a reserved strip for:

- Today’s goal
- Named conventions (`orient > 0` means left)
- The pipeline or invariant of the day

## Differentiation without three courses

You will have students who finished a game in high school and students who still fight Git.

Plan **one core path** and **two valves**:

- **Support valve:** a hint sheet, a failing test with a message, a 10-minute TA table.
- **Challenge valve:** “add a second light,” “handle collinear points,” “measure n=10k.”

Do not make the challenge required for a full score unless it was in the spec.

## Pair and group planning

Pairs in lab: similar-ish skill, or a rotating “driver/navigator” so the strong student cannot monopolize the keyboard. See [[Teaching/07 Labs and Studio]].

Never assume they know how to pair. Teach the roles in week 1.

## The 10-minute rehearsal

The night before, stand up and:

1. Open the starter from a clean clone.
2. Run the demo.
3. Say the first two minutes out loud.
4. Write the one question you will ask at minute 20.

If the clone fails, the lesson is not ready.

## After-class note (same day)

Three bullets: what landed, what broke, what to change in the starter. This is how a course becomes good in year 2.

## Filled example (Computational Geometry, Week 2)

```
Course / week: Comp Geom / Week 2 Geometric primitives
Learning goal: Students can implement orient(a,b,c) and interpret its sign.
Success check: 8/10 lab pairs pass the hidden collinear test.
Materials: visualizer starter, 5-question quiz, board diagram of three points.
0–10   Last week: predicate vs construction. Two pictures.
10–25  Cross product in 2D. Board. Three numerical examples.
25–40  Live-code orient. Plant a sign error. Fix it.
40–50  Students compute two triples on paper, then in the starter.
50–65  Collinear, duplicate points, “almost zero.” EPS policy.
65–75  Recap. Lab: draw the sign as color. Homework: 3 written + implement onSegment.
If the demo dies: use the recorded 4-minute clip; board the code.
If we run long, cut: the third numerical example.
If we run short, add: “where this is used in picking.”
Check: anyone who missed week 1 lab.
```

## Exercise

Write next week’s one-page plan. If it does not fit on one page, you are writing a chapter, not a lesson.
