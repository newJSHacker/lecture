# Extra exercises — Week 04 (Transform feedback name)

Lecture: [[GPU Programming/Lecture 04 Transform feedback name]]

## Written and coding

1. Define this week's kernel in one sentence (VS output captured).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
gl.transformFeedbackVaryings(prog, ['v_pos'], gl.SEPARATE_ATTRIBS);
```
