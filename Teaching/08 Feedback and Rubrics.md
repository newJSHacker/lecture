# 08 — Feedback and rubrics

Feedback is information a student can use to change the next version of the work. A number is not feedback. A paragraph that restates the spec is barely feedback.

If they cannot act before the next grade, you wrote a post-mortem, not a teaching move.

## Speed vs quality

In a 40-person course you will not write an essay on every lab. You must choose a system.

| Method | Use when | Cost |
| --- | --- | --- |
| Rubric + 2 specific comments | Weekly labs | Medium |
| Autograder + one human comment on the visual | Kernels, predicates, unit-testable code | Low after setup |
| Audio note (2 minutes) | Projects, critiques | Low time, high warmth |
| In-lab oral feedback, recorded on a checklist | Studio weeks | Lowest writing |
| Full written review | Thesis chapters, final reports | High; schedule it |

Never grade only by “I know quality when I see it.” That is how bias and exhaustion leak.

## Rubrics students see in advance

Publish the rubric with the assignment. If a criterion is not on it, you may praise it, but do not punish its absence.

**Analytic rubric (preferred for code + report):**

| Criterion | Below | Meets | Exceeds |
| --- | --- | --- | --- |
| Runs | Does not run from README | Runs on a clean clone | Runs + records a known limitation |
| Kernel / technique | Missing or wrong idea | Correct on typical input | Degenerate case handled or documented |
| Visual / UX | No way to see the idea | Idea is visible | Controls or overlay teach the idea |
| Code hygiene | Unreadable, secrets, dump | Named, structured, no secrets | Tests or comments at decisions |
| Write-up | Story without decisions | Decisions and one figure | Limitations and a next experiment |

**Holistic rubric** (letter-level descriptions) is fine for a small studio with experienced graders. It is a fight in a large course.

## Comments that change work

Use a consistent shape:

1. **Name the evidence.** “Your hull skips the middle point on the upper chain in test 04.”
2. **Name the principle.** “The left-turn test must use the last two hull points, not the first.”
3. **Name the next action.** “Draw the chain for that fixture before you change code.”

Avoid:

- “Messy”
- “Good job!” as the only line
- Rewriting their program in the comment box
- Sarcasm

If you are angry, wait 12 hours. Grades written at 1 a.m. are meaner than you think.

## How much to fix

You are not their pair programmer in the gradebook.

- Mark the first instance of a pattern (“winding is inconsistent in three files; fix the convention in the kernel”)
- Do not line-edit every file
- For writing: mark one page densely as a model, then require them to apply it

## Consistency across TAs

- Grade one sample together before the pile
- Use a shared comment bank for the five common bugs
- Blind the names if the LMS allows it, especially on reports
- Instructor re-grades a 10% sample

If two TAs differ by a full letter on the same project, the rubric is not operational yet.

## Returning work

Return labs before the next related lab. A Week 3 grade arriving in Week 7 trains them to ignore comments.

Spend 5 minutes in the next lecture on the **class-wide** pattern: “Half of you inverted the near-plane. Here is the picture.” That is efficient feedback.

## Regrade policy

Write it once:

- Regrade requests in 5 days, in writing, pointing to a rubric cell
- The whole submission may be re-read (score can go down)
- “I need a higher GPA” is not a request

This protects you and them.

## Praise

Praise **process and decision**, not identity.

- “You isolated the shader compile log before changing the mesh. That is the right order.”
- Not: “You are a natural at graphics.”

Identity praise makes the next failure feel like a verdict.

## Feedback on live performance

For presentations and defenses, use a card they can photograph:

| Item | Notes |
| --- | --- |
| Problem in one sentence | |
| Demo reliability | |
| Technical depth of answers | |
| Visuals / timing | |
| One improvement for next time | |

See [[Graduation Requirements]] and [[Teaching/22 Supervising Theses]].

## Exercise

Take last year’s assignment. Write a 4-row rubric that a new TA could apply. Then grade three old submissions. If you disagree with yourself, the rubric is still vague.
