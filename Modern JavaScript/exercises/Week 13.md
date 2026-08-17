# Extra exercises — Week 13 (Patterns for graphics apps)

Lecture: [[Modern JavaScript/Lecture 13 Patterns for graphics apps]]

## Written and coding

1. Define this week's kernel in one sentence (game loop, modules, state).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
function frame(t){ const dt=t-last; last=t; update(dt); render(); requestAnimationFrame(frame); }
```
