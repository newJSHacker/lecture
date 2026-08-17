# Lecture 8 — Midterm and JS in the page

**Week 8 of 15** · Web Technologies  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** script in the page; document.querySelector; textContent  
**Success check:** after the exam they can change a heading from a script without innerHTML of untrusted strings

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `Web Technologies/code/08-todo.html` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: JS talks to the tree; innerHTML of user text is a hole`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** request cycle; skeleton; labels; box model; flex vs grid; viewport.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
<script src="main.js"></script>   <!-- end of body -->

document.querySelector('h1').textContent = 'IGWT';

textContent  not  innerHTML  for user strings
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** This meeting is a **midterm**, then JS in the page. No laptop for the exam. After: the script is how a HUD will talk to Three.js later.

**Ask:** What is the leftover picture?

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.



### Show / attempt if time

**Say:** A button that toggles a class on main. Plant script in head without defer — empty querySelector. Move to end of body.

**They do:** Toggle a class. textContent only.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Script at end of body | Plant head without defer. |
| 15–40 | querySelector + textContent | Plant innerHTML. |
| 40–60 | Toggle class | They type. Circulate. |

---

## Lab

1. Three planted CSS bugs to fix.
2. A counter button.

---

## Homework

1. Midterm reflection + toggle lab finished.

---

## Quiz next meeting

None this week — midterm. Next quiz is Lecture 9.

## Extra exercises

See [[Web Technologies/exercises/Week 08]].

## If we run long, cut

Modules today. Keep querySelector + textContent.

## If we run short, add

defer as a name.
