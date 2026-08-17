# 14 — TAs and course operations

A course is a small organization. If you treat it as a series of talks, the organization will fail in public: late grades, conflicting advice, a broken starter, a TA who invents policy.

## What a TA is for

| Role | TA does | Instructor still does |
| --- | --- | --- |
| Lab help | Desk visits, install, the weekly bug | Design of the lab, stop-the-room teaching |
| Grading | Rubric application | Rubric design, calibration, appeals |
| Forum | First-line answers within 24 hours | Policy, edge cases |
| Demo support | Second machine, camera, clone test | The live-coding narrative |
| Never | Writing new policy, changing grades alone, dating students they grade | — |

Write this on one page. Give it to TAs before week 1.

## Hiring and briefing

Prefer TAs who have **done the labs**, not only those with a high exam score. A quiet student who can sit beside someone is better than a brilliant student who grabs the keyboard.

**Pre-semester briefing (90 minutes):**

- The learning goals and the weekly machine
- The integrity and AI script
- How to do a 4-minute desk visit ([[Teaching/07 Labs and Studio]])
- What they must escalate (harassment, crisis, cheating, grade fights)
- The comment bank
- Pay, hours, and “do not work 20 unpaid hours”

## Calibration

Before each big grade event:

1. Instructor grades two submissions out loud
2. TAs grade the same two
3. Discuss disagreements until the rubric words change or the scores match
4. Only then open the pile

If you skip this, you are running two courses.

## Communication channels

Pick few:

- LMS for official deadlines
- Repo issues or a forum for technical help
- Email for personal / confidential
- Chat only if you or a TA will moderate it

A dead Discord is worse than none. A chaotic Discord is a second unpaid job.

**Response-time promise:** “Technical questions: 24 hours on weekdays. We do not answer homework help after 20:00 the night before a deadline.” Then keep it.

## The course repository

From [[02 Curriculum Design Advice]]:

```
course/
  lecture/
  starter/
  solutions/     # private or released after the deadline
  assignments/
  resources/
  admin/         # rubric keys, TA notes — not public
```

Rules:

- `main` always has a running starter
- Secrets and solution keys are not in the student remote
- Tag releases (`week-03-starter`)
- A CONTRIBUTING or TA.md that says how to open a PR for a typo

## Weekly operations rhythm

| When | Who | What |
| --- | --- | --- |
| Friday | Instructor | Next week’s starter + lab freeze |
| Sunday | TA | Run starter on a clean machine |
| Lecture day | Both | Quiz copies, HDMI, backup demo |
| Lab day | Both | 10-minute pre-brief |
| 48h after lab | TAs | Grades + two comments |
| After grades | Instructor | 10% audit + class-wide note |

## Records

Keep: syllabus version, emailed exceptions, integrity cases, accommodation letters, gradebook exports.

Do not keep: jokes about students in a shared meme channel.

## When a TA is struggling

Coach once with a concrete behavior (“you finished their shader; next time leave them at the checklist”). If they cannot follow integrity or respect rules, remove them from grading. Document. Tell the chair.

## When you have no TA

Cut scope. Autograde more. Oral feedback in lab. Shorter projects. You cannot secretly be three people. See [[Teaching/15 Time Management for Instructors]].

## Exercise

Write a one-page TA contract: hours, roles, escalation, channels, calibration date. If you cannot, the course will train TAs by accident.
