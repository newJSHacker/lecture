# 05 — Lecture craft

A lecture in this program is a guided encounter with one idea, not a transfer of slides. Students can read. They cannot, by themselves, watch an expert decide what to ignore.

## One idea

If a colleague asks “what was lecture 6 about?” you should answer with a noun phrase: *clip space*, *sweep line status*, *Cook–Torrance at a glance*, *the scene graph vs the scene*.

Name the meeting **Lecture 6**, not “Week 06.” The week is when it happens. The lecture is what you do. Full naming rules: [[Teaching/24 Session Guides]].

If your answer is a list of six topics, it was not a lecture. It was a table of contents.

## The shape of 75 minutes

| Phase | Time | Purpose |
| --- | --- | --- |
| Retrieve | 5–8 min | Last week’s idea, under a little pressure |
| Frame | 3 min | Today’s question and why a graphics person cares |
| Build | 20–25 min | Board + pictures + one wrong turn |
| Show | 15–20 min | Live demo or live coding |
| Attempt | 8–12 min | They try a fragment |
| Land | 5 min | Recap, the invariant, the lab hook |

Times flex. The attempt does not disappear.

## Openings that work

- A broken picture: “Why is this mesh black?”
- A lie students believe: “More triangles will fix this silhouette.”
- A 30-second silent demo, then “write what you think happened.”
- A single numerical surprise: three collinear points and a naive `if (area == 0)`.
- One common-sense story, then the invariant: [[Teaching/25 Common Sense Anecdotes]]. Ninety seconds, then the board. Not a stand-up set.

Openings that fail: “Last time we talked about… and today we will continue…”

## Board over slides

Slides are for photographs, code you should not hand-write, and animations. The argument belongs on the board.

**Write large.** The back row is part of the class.

**Do not talk to the board.** Say the sentence, then write the short form.

**Do not erase the invariant.** Park it.

For matrices, write the **spaces** (`object → world → view → clip`) more carefully than the numbers. Students lose the spaces first.

## Voice and body

- Stand where they can see the demo machine and the board.
- Face the room when you ask a question. Wait. Waiting is the skill. Count to seven in your head.
- Walk the aisles during the attempt. You are collecting data.
- Do not pace like a talk show. It is visually noisy.

If you are soft-spoken, use a microphone. Pride is not a pedagogy.

## Language

Prefer short sentences. Define a term the first time, then use it consistently.

| Say | Avoid |
| --- | --- |
| “The camera looks down −Z in this convention” | “Obviously the camera…” |
| “This function returns a sign” | “We just do the cross product thing” |
| “I am going to make a mistake on purpose” | Silent magic edits |

Avoid filling pauses with “right?” and “make sense?” Those are not checks. Real checks are in [[Teaching/20 Questioning and Discussion]].

## Slides, if you use them

- One idea per slide
- Diagrams, not paragraphs (see [[02 Curriculum Design Advice]])
- Code no smaller than about 20pt in the room
- Dark-on-light or light-on-dark, not gray-on-teal
- Alt-text or a spoken description for every important figure ([[Teaching/10 Inclusive Teaching and Accessibility]])
- Put the slide deck in the repo **after** class if you want them listening; before class if you want them annotating. Pick one and keep it.

Never read a bullet list that they can read faster than you can speak.

## Handling the middle slump (minute 35)

Attention drops. Change the channel:

- Switch from slides to board
- Switch from talk to typed code
- A 90-second pair talk: “explain the last diagram”
- A prediction: “what color is the pixel at the center?”

## Endings

The last three minutes are not “any questions.” They are:

1. The invariant or pipeline, said again
2. The mistake they are about to make in lab
3. The exact homework prompt

Then stop. Lingering while they pack trains them to ignore endings.

## Recording

Record if you can. A recording is not a substitute for attendance if the course is studio-heavy; say that.

When you record:

- Mic on you, not the air conditioner
- Zoom the IDE to 140%
- Narrate clicks (“I am opening the fragment shader, not the vertex shader”)
- After a live fix, leave a 20-second summary for later viewers

## Guest lectures

A guest is a gift and a risk. Brief them: audience level, 15 minutes of demo, 10 minutes of Q&A, no confidential employer code. You stay in the room. You connect the guest to next week’s lab.

## Exercise

Take a slide deck you already have. Delete half the slides. Add one student attempt. If the lecture dies, the deleted slides were the lecture, and that is the problem.
