# 22 — Supervising theses

Graduation standards: [[Graduation Requirements]]. Short model: [[05 Sample Graduation Thesis]]. Long archive: [[03 Reference Thesis]]. This note is the **supervisor’s** job, not the student’s outline.

A thesis in IGWT is project-based: a running system plus a written argument. If you supervise only the vibes of the idea, you will meet a beautiful slide deck and a repo that does not clone.

## How many students

Be explicit with yourself. A serious undergraduate thesis is about 1 hour every 1–2 weeks plus extra near the end, if they are on track; more if they are not. Four students you see is better than ten you forget.

If the department assigns you too many, ask for co-supervisors or a studio model with shared meetings.

## Choosing a topic

Good undergraduate topics are **narrow, visible, and evaluable**.

| Good | Dangerous |
| --- | --- |
| Hull + Delaunay + picking in a browser, evaluated on fixtures | “A complete metaverse platform” |
| One PBR feature compared with a baseline | “A new global illumination algorithm” |
| Configurator for 3 parts with measured load time | “AI-generated everything” |
| WebXR seated exhibit with a comfort study | “Full locomotion MMO” |

The sample thesis exists so you can say: “This length, this honesty about timing tables.”

Force a sentence:

> I will build X so that a user can Y; I will know it worked when Z.

If Z is “it looks cool,” it is not a thesis yet.

## The supervision contract (week 0–1)

Write one page:

- Meeting rhythm (every 2 weeks, 20 minutes, they send an agenda)
- What “on track” means each month
- Tools and AI disclosure
- Authorship: they write; you do not ghostwrite
- What you will read (drafts with a date, not a dump the night before)
- How they reach you in a real emergency
- Exhibition and defense dates from [[Graduation Requirements]]

They run the meeting. You do not hunt them for news.

## A 15-week supervision map (final semester)

Align with the table in [[Graduation Requirements]].

| Weeks | Supervisor looks at | Kill / cut if |
| ---: | --- | --- |
| 1–2 | Proposal: X/Y/Z sentence, related work list (10 sources), repo | No sentence, no repo |
| 3–6 | Design figure, kernel or scene running, ethics/AI note | Still only mood boards |
| 7–11 | Feature freeze approaching, first measurements or a reason there are none | New scope every meeting |
| 12 | Evaluation chapter: real numbers or labeled templates | Invented FPS |
| 13 | Thesis PDF compiles, citations exist | First complete draft |
| 14 | Exhibition rehearsal | Demo only on their machine |
| 15 | Defense questions (give them a list) | They cannot explain the kernel |

Give the Week 14 defense-style questions idea from [[Computational Geometry/Week 14 Project Studio]] even if the course is not computational geometry.

## Reading drafts

You are not a copy editor for 80 pages every weekend.

- First draft: structure and claims, not commas
- Second: figures, evaluation honesty, related work coverage
- Third: only what a second examiner will attack

Use the comment shape in [[Teaching/08 Feedback and Rubrics]]. Demand captions. Demand that every performance number say how it was measured — or that it is a template, as this repository’s samples do.

**Do not write their chapters.** Line-editing a weak argument into your voice is ghostwriting. Ask questions that force them to rewrite.

## Evaluation and honesty

This program’s sample documents warn that timing tables may be templates. Students must not submit templates as measurements. Your job is to ask:

- What machine?
- What n?
- How many runs?
- What did you change between conditions?

If they did not measure, the thesis must say so. A failed experiment is acceptable. A fake table is not. See [[Teaching/12 Academic Integrity and AI]].

## Group capstones vs individual theses

If the software is shared, the **written argument and the oral** must still show an individual mind. Split chapters by ownership. Ask each person to change a part live.

## Committee and defense

Brief the student on the format in [[Graduation Requirements]]: 15–20 minutes, live demo, questions.

Give them ten questions in advance; ask two of them. Sample:

1. What is the core technical claim?
2. What would falsify it?
3. Show a failure case.
4. Why this algorithm / architecture and not the obvious alternative?
5. What did you measure, and what did you not?
6. What would break on a mid-range phone?
7. Where did AI or other code enter, and what can you change without it?
8. What would you cut if you had four weeks left?
9. What is the next experiment, exactly?
10. What should a second-year student steal from your repo?

If the demo dies, they should have a video. That is professionalism, not cheating.

## When they disappear

Email once with a date. Email again with the chair copied if policy allows. Document. You cannot supervise a ghost, and you must not invent a passing thesis.

## When the work is not passing

Say so in week 6, not at the defense. Offer: cut to a smaller X, delay if the university allows, or fail with a path to retry. Kindness that hides a fail until week 15 is cruelty.

## Letters and authorship

If the work becomes a paper, discuss authorship early. Undergraduates who did the implementation belong on the author list if they meet the field’s standard. Do not surprise them.

## Exercise

Write the one-page contract for your next thesis student. If you already have students and no contract, write it this week and send it.
