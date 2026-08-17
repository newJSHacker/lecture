# Extra exercises — Week 01 (Global illumination idea)

Lecture: [[Advanced Computer Graphics/Lecture 01 Global illumination idea]]

## Written and coding

1. Define this week's kernel in one sentence (direct vs indirect).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```
L_out = emit + ∫ BRDF * L_in * n·ω dω
```
