# Extra exercises — Week 10 (Multiple objects)

Lecture: [[WebGL Programming/Lecture 10 Multiple objects]]

## Written and coding

1. Define this week's kernel in one sentence (scene loop, many uniforms).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
for (const o of objects) { setM(o.m); gl.drawElements(...); }
```
