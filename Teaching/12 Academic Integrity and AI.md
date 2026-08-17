# 12 — Academic integrity and AI

Students will use other people’s code and generative models. Pretending otherwise is not a policy. Your job is to define **allowed collaboration**, **required disclosure**, and **what mastery still means**.

This note is about teaching and assessment design, not about evading detection.

## Say the rule in week 1, in human language

A usable policy has four lines:

1. **You may** discuss ideas, draw pictures, and compare error messages.
2. **You may not** copy another student’s kernel, shader, or report, or share your repo with a student who has not submitted.
3. **You may use AI** as a rubber duck, for syntax, and for first drafts of comments **if** you disclose the tool and you can explain every line you submit.
4. **You may not** submit an AI-generated project you cannot modify live.

Put the same four lines in the syllabus, the repo, and the project spec. See [[Teaching/04 First Day and Syllabus]].

## Design so cheating is less attractive

People copy when the work is impossible, unclear, or irrelevant, or when they are drowning.

- Starters that run
- Rubrics that are public
- Milestones
- Help that arrives before the night before
- Assessments that require **process** (trace, oral, change request)

If the only artifact is a zip of source, you are grading the internet.

## What to assess that AI is bad at (today)

- Changing a running system under a new constraint (“handle collinear points,” “cut texture memory by half”)
- Explaining a picture you point at
- A 10-minute oral: “what does this function return on this triple?”
- A paper trace of an algorithm
- A live tweak in office hours or demo day
- Git history that matches the story (not 1 commit at 3:59 a.m. with 4,000 lines)

You are not trying to “catch AI.” You are trying to see a mind.

## Disclosure template (give them this)

```
Tools used: (none / Copilot / ChatGPT / other)
I used them for: (syntax / idea / draft paragraph / debug suggestion)
I did not use them for: (the kernel / the report argument / ...)
I can explain: (file names)
```

A disclosure is not a confession of guilt. It is part of professional practice.

## Collaboration vs collusion

| Allowed | Not allowed |
| --- | --- |
| Whiteboard of the sweep-line idea | Photos of another student’s finished code |
| Pair lab when the spec says pair | Pair homework when the spec says individual |
| Using Three.js docs and examples | Pasting a whole example and changing variable names |
| Stack Overflow for an error you still fix | Paying someone to finish the project |

When in doubt, they should ask **before** the deadline.

## Process when you suspect a problem

Stay calm. You are an investigator of the work, not a prosecutor of a soul.

1. Compare artifacts (structure, comments, identical bugs, identical wrong comments).
2. Invite the student to a meeting: “Walk me through this function.”
3. Take notes. Another faculty member present if policy says so.
4. Follow the **department process**. Do not invent a private punishment.
5. Do not post the case on Slack. Do not gossip.

If they can modify and explain, the learning goal may still be met; you may still mark a policy violation if they lied about authorship. If they cannot explain, they have not met the goal.

Never threaten. Never promise “this stays between us” if the university requires a report.

## AI-specific classroom moves

- Live-code with AI **once**, as a demo: show a plausible wrong shader and how you test it
- Require a “diff of understanding”: they annotate three AI lines they changed and why
- Ban AI on the midterm if the midterm is about unaided explanation; say so
- Allow AI on a take-home **only** with disclosure and an oral

Do not run a secret “AI detector” as sole evidence. Those tools are unreliable. Use the student’s performance on the work.

## Plagiarism in writing

Theses and reports: teach citation in week 1 of the project, not after the misconduct meeting. Show a bad paraphrase. Show a good one. Point at [[05 Sample Graduation Thesis]] as a structure, not as text to reuse.

## Exercise

Rewrite your integrity paragraph to 120 words. Then add one oral or live-tweak checkpoint to the project so authorship is visible.
