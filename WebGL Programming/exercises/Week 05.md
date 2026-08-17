# Extra exercises — Week 05 (A cube and depth)

Lecture: [[WebGL Programming/Lecture 05 A cube and depth]]

## Written and coding

1. Define this week's kernel in one sentence (indices, DEPTH_TEST, cull).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
gl.enable(gl.DEPTH_TEST);
gl.enable(gl.CULL_FACE);
```
