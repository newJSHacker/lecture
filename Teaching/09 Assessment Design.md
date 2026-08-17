# 09 — Assessment design

Assessment is how you find out whether the course worked. It is also how students decide what to study. If you test API trivia, they will memorize API trivia. If you test invariants, degeneracy, and a running system, they will practice those.

## Align to goals

For each learning goal, name one piece of evidence.

| Goal | Poor evidence | Better evidence |
| --- | --- | --- |
| Understand clip space | Define clip space | Transform a point on paper; explain a clipped triangle |
| Implement hull | “Write a hull” with no tests | Hidden fixtures + visual |
| Optimize a scene | “Discuss optimization” | Before/after frame time and what they changed |
| Communicate | Long report nobody reads | 6–8 pages + a 5-minute demo |

If a goal has no evidence, it is decoration. Delete it from the syllabus or add a task.

## The program’s default mix

From [[02 Curriculum Design Advice]] and [[04 Computational Geometry]]:

| Component | Role | Notes |
| --- | --- | --- |
| Labs | Can they do this week’s skill? | Frequent, lower stakes |
| Homework | Can they do it alone, with time? | Mix of code and short writing |
| Weekly quiz | Retrieval | 10–15 minutes, start of lecture |
| Midterm | Can they explain without a laptop? | Pictures, signs, complexity, one trace |
| Project | Can they combine skills? | Demo + report, not only code |
| Participation | Did they show up as a colleague? | If you grade it, define it or do not grade it |

Do not add a huge written final on top of a huge project unless the department forces you. Students have finite hours. See [[Teaching/15 Time Management for Instructors]].

## Quizzes that are worth it

Five items. Ten minutes. Same week as the idea.

Good items:

- A picture: mark the left turns
- One complexity: “Andrew’s chain after sort is ___”
- One “what is wrong with this shader error”
- One convention: handedness, winding, color space
- One short “what would you try first if the scene is black?”

Bad items:

- Name four Three.js classes
- A 20-minute proof
- A trick question about an API flag you mentioned once

Grade them the same day if you can. The point is retrieval, not a second midterm.

## Written exams in a building course

You still need some paper. Keyboards hide whether they understand.

Exam design:

- A figure on every other question
- One trace of an algorithm they have seen
- One “here is a wrong explanation; fix it”
- One transfer: “where would you use this in picking?”
- No surprise topic that never appeared in lab

Provide a formula sheet if the goal is not memorizing the matrix. Say so in week 1.

## Projects

A project spec needs:

- A **must** list (the grade of “meets”)
- A **should** list
- A **may** list (exceeds)
- Forbidden scope (“do not also write a physics engine”)
- Deliverables: repo, README, 60-second video or in-class demo, short report
- Rubric
- Milestone dates, not only a final date
- Academic integrity and AI rules

Milestones save lives:

| Week | Must show |
| --- | --- |
| 2 | Repo + running starter + chosen topic |
| 4 | Core algorithm or scene with one interaction |
| 6 | Degeneracy or performance note + draft README |
| 8 | Feature freeze + report draft |
| 9 | Demo |

If you only have a final deadline, you will meet the project for the first time when it is too late to teach.

## Group work

Group projects need individual accountability:

- A kernel or scene file each person owns
- A short individual quiz or oral on the shared system
- A contribution statement you actually read
- A way to fire a non-contributor with a documented process, used rarely and in writing

Otherwise you are grading the strongest student’s weekend.

## Validity, reliability, fairness (in plain language)

- **Valid:** it measures the goal (a pretty demo is not a hull)
- **Reliable:** two TAs would agree
- **Fair:** time, language, and hardware do not secretly dominate the grade

Fairness examples:

- Provide a lab machine option for heavy GPU work
- Do not require a $3,000 laptop
- Extra time as formal accommodation, not as a secret deal
- Language: grade graphics English for clarity, not for literature

## Grade distributions

Do not curve to punish a strong year. Do not inflate to hide a weak exam.

If the median is a D, the assessment or the teaching failed. Investigate before you “adjust.” If the median is an A and the projects do not run, the rubric failed.

## Exercise

Write a 10-minute quiz for your next lecture **before** you write the slides. Then write only the slides that make that quiz fair.
