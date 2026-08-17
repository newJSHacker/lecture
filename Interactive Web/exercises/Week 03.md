# Extra exercises — Week 03 (Pointer input)

Lecture: [[Interactive Web/Lecture 03 Pointer input]]

## Written and coding

1. Define this week's kernel in one sentence (offset, buttons, touch).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
const r = c.getBoundingClientRect();
const x = (ev.clientX - r.left) * c.width / r.width;
```
