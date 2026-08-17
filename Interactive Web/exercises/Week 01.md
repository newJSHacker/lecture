# Extra exercises — Week 01 (Canvas 2D API)

Lecture: [[Interactive Web/Lecture 01 Canvas 2D API]]

## Written and coding

1. Define this week's kernel in one sentence (getContext, paths).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
const ctx = c.getContext('2d');
ctx.beginPath(); ctx.arc(80,80,40,0,Math.PI*2); ctx.fill();
```
