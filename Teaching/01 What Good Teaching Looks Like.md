# 01 — What good teaching looks like

A good teacher is someone whose students can do new things they could not do last month, and who can explain those things under mild pressure.

Charisma helps. Credentials help. Neither is the definition.

## Observable signs (walk into the room)

| Sign | You will see | Counterfeit |
| --- | --- | --- |
| Clarity | Students can restate today’s goal in one sentence | Beautiful slides, foggy goal |
| Practice | Most minutes are students working or watching work being made | Lecture until the bell |
| Diagnosis | Instructor stops when faces and code diverge | “Any questions? No? Good.” |
| Feedback | Comments name the next change | Scores with no comment |
| Safety | Students will risk a wrong answer | Only the same three people speak |
| Standards | Rubric is public before the work | Surprise deductions |
| Respect for time | Lab starts with a working starter | 20 minutes of install pain |
| Honesty | Instructor says “I do not know; we will find out” | Bluffing through a shader bug |

## What students remember a year later

They rarely remember your outline. They remember:

- The week they finally saw the hull appear
- The time you sat down and found their `orient` sign error in four minutes
- The critique that was strict and not humiliating
- The project that ran on someone else’s laptop
- Whether you learned their name

Design for those memories on purpose.

## Three models (use all three)

### 1. Direct instruction

You explain, you show, they practice a tight task, you check. Best for predicates, matrix conventions, WebGL state, Git, and other things where a wrong model is expensive.

### 2. Worked-example fading

You show a complete solution while thinking aloud. Next time you leave a hole. Then they do it. Best for shaders, scene graphs, and geometry kernels.

### 3. Studio / critique

They make something; the room examines it against criteria. Best after they have a minimum technique. See [[Teaching/07 Labs and Studio]].

A common IGWT failure is jumping to studio before students have a kernel. Another is staying in lecture after they have a kernel.

## The five-pillar week, from the teacher’s side

From [[02 Curriculum Design Advice]]:

| Pillar | Teacher’s job | Failure mode |
| --- | --- | --- |
| Theory | One idea, one picture, one invariant | Five ideas, no picture |
| Demonstration | Make the idea move | Demo of a finished file you cannot reconstruct |
| Practice | A task with a visible success condition | “Explore Three.js” |
| Project | A scoped application of several weeks | A second course hidden inside the project |
| Assessment | Evidence of the learning goal | Memorizing API names |

## Expertise is a teaching hazard

You have compiled a mental library of defaults: right-handed coordinates, clip space, winding order, `lookAt`, gamma, premultiplied alpha. Students do not have that library. Your job is to **externalize** it.

Before each lecture, write the three things that are “obvious” to you and not to them. Teach those on the board. Examples:

- A vector is not a point; a translation matrix treats them differently
- A fragment shader runs per pixel, not per triangle, unless you say otherwise
- `orient > 0` is a convention you must pick and keep
- A texture that “looks dark” is often a color-space mistake, not a lighting mistake

## Authority without theater

Students need you to be competent and fair. They do not need you to be a performer.

- Arrive early. The room should work before they sit.
- Start on time. End on time. That is respect.
- Admit errors in public. Then fix them in public.
- Do not mock tools, prior instructors, or “stupid questions.”
- Do not date, flirt with, or privately favor students. See [[Teaching/13 Classroom Difficulties]].

## A weekly self-check (10 minutes)

After the last lab, write four lines:

1. What could most students do by the end?
2. Where did more than a third get stuck?
3. What will I change in the starter or the explanation?
4. Who needs a check-in before next week?

Keep these notes. They become your teaching portfolio ([[Teaching/16 Teaching Portfolio and Growth]]).

## Exercise

Pick one course you will teach. Write five observable outcomes in the form: “By week 6 a student can ___ using ___ without ___.” If you cannot fill the blanks, the course is not designed yet.
