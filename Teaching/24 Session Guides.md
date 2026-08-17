# 24 — What to call the documents, and how to run a meeting

This note corrects two naming habits that make the IGWT files weaker than they are.

## Your two questions

**“Lecture plan” is the wrong name for the 15-week course file.** That file is a **course plan** (or syllabus). A lecture plan, in ordinary school language, is a short outline of one talk. What you actually need in the classroom is a **session guide**: what you say, what you write, what you project, what they do, and what you cut.

**“Week 01” is not wrong. It is the calendar. “Lecture 1” is the meeting.** Students live in weeks (LMS, homework due Friday of week 3). You live in lectures (you walk in and teach). Put **both** on the page. Do not throw “week” away, and do not call a midterm “a lecture” without saying it is an exam.

| Thing | Call it | Do not call it |
| --- | --- | --- |
| 15-week file (`12 Introduction to Programming.md`) | **Course plan** / syllabus | Lecture plan |
| One class day (75 min + 60 min live coding) | **Session guide** | “The week notes,” “slides” |
| The 75-minute talk | **Lecture 1, 2, …** | Week 1 (that is the calendar slot) |
| The 60-minute build | **Live coding** (same session) | Lecture 1b |
| Extra problem sheet | **Exercises, week 1** | Another lecture |
| Week 8 written exam | **Lecture 8 — Midterm** (say: this meeting is an exam) | A normal lecture |
| Week 14 | **Lecture 14 — Studio** | A content lecture |
| Week 15 | **Lecture 15 — Presentations** | A content lecture |
| Student-facing calendar | Week 1–15 | “Lecture 1” only (they will miss due dates) |

**Session** is the accurate word for the whole afternoon. **Lecture** is the accurate word for the 75 minutes with the board. IGWT files are named **Lecture N** because that is what you prepare. The header still says **Week N of 15**.

## What a session guide is

Not a transcript. Not a slide deck. Not a textbook chapter.

It is a **sequence of moves** a substitute could run:

- **Say** — the sentences (short). Not a paragraph they could read at home.
- **Ask** — one question, then wait (count to seven).
- **Board** — what is on the board at the end of the block. Students photograph this.
- **Slide** — only what the board cannot do: a photo, an animation, a 20pt code dump, a broken screenshot. Most blocks have **no slide**.
- **They do** — write, predict, type, vote. Nodding is not a move.
- **Do not** — the amateur trap for this block.

[[Teaching/03 Lesson Planning]] stays the one-page timing sheet you fill on Sunday. The session guide is the **fleshed meeting**. If you only have the one-pager, you can still teach. If you only have slides, you have a talk.

## Board vs slides vs mouth

| Channel | Use it for | Ban |
| --- | --- | --- |
| Mouth | Why we care, the question, the wait, the mistake you plant | Reading bullets |
| Board | The argument: boxes, arrows, one equation, the invariant | Tiny code, photographs |
| Slide | Screenshot of a bug, animation of a pipeline, code you must not misspell under time | Paragraphs, the whole lecture |
| Live editor | The kernel, the error, the fix | Decorating CSS |

**Rule:** the argument is born on the board. Slides illustrate. If a slide has the argument in sentences, delete the sentences and write them on the board while you talk.

Leave a **parked strip** on the left or top of the board all hour:

```
Lecture 1  |  Goal: …  |  Invariant: …
```

Do not erase that strip.

## Shape of 75 minutes (same as [[Teaching/05 Lecture Craft]])

| Min | Phase | Student action |
| ---: | --- | --- |
| 0–8 | Retrieve / hook | Predict or recall |
| 8–12 | Frame | Write today’s question |
| 12–35 | Build | Watch the board; copy the picture |
| 35–50 | Show | See a demo or 15 lines of live code |
| 50–65 | Attempt | They try a fragment (paper or starter) |
| 65–75 | Land | Recap the invariant; lab hook |

Then stand up for **live coding** (60 min). That is not “more slides.”

## File name

```
Lecture 01 What a program is.md
```

First line:

```markdown
# Lecture 1 — What a program is

**Week 1 of 15** · Introduction to Programming
```

Number with two digits in the filename so they sort. Say “Lecture 1” out loud, not “week oh-one.”

## The template (copy into a new lecture)

```markdown
# Lecture N — Title

**Week N of 15** · Course name  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** one function or one picture  
**Success check:** what you look at in the attempt or lab

## Before you enter

- Demo path (local, no CDN)
- Backup if the demo dies
- Quiz from last lecture (except Lecture 1)
- Parked board strip: goal + invariant

## Board at the end (they photograph this)

1.
2.
3.

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | | |

## Lecture

### Minutes 0–8 — Hook
**Say:**
**Ask:**
**Board:**
**Slide:** none / #
**They do:**
**Do not:**

### Minutes 8–12 — Frame
…

### Minutes 12–35 — Build
…

### Minutes 35–50 — Show
…

### Minutes 50–65 — Attempt
…

### Minutes 65–75 — Land
**Say (lab hook, not “any questions?”):**

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | | |
| 10–30 | | |
| 30–45 | | |
| 45–60 | They type; you circulate | |

## Lab / homework / quiz
(keep the lists)

## If we run long, cut
## If we run short, add
```

A worked example: [[Programming/Lecture 01 What a program is]].

## Common wrong views (corrected)

| Wrong | Right |
| --- | --- |
| The 15-week markdown is my lecture plan | That is the **course plan**. Each meeting needs a **session guide**. |
| Rename everything to Lecture and drop Week | Keep **Week** on the syllabus and due dates. Use **Lecture N** for the meeting. |
| More slides = more contentful | More **moves**. A contentful lecture has a board photograph and an attempt. |
| Script every sentence | Script the **moves**. You may change the words. You may not skip the attempt. |
| Lecture 8 is still a lecture | It is a **midterm meeting**. Say that in the title. |
| Week 01, 02 look more official | They look like a folder dump. “Lecture 1” is what you say at the door. |

## Exercise

Take next meeting. Fill the template through **Attempt**. If you cannot name a slide list of length ≤ 6, you are planning a talk, not a class.
