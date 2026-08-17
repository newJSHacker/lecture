# Extra exercises — Week 12 (A mini 2D engine)

Lecture: [[Interactive Web/Lecture 12 A mini 2D engine]]

## Written and coding

1. Define this week's kernel in one sentence (entities, loop, input).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
entities.forEach(e => e.update(dt));
entities.forEach(e => e.render(ctx));
```
