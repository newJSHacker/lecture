# Extra exercises — Week 04 (Uniforms)

Lecture: [[WebGL Programming/Lecture 04 Uniforms]]

## Written and coding

1. Define this week's kernel in one sentence (mat4, time, colors).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
gl.uniform1f(gl.getUniformLocation(prog,'u_time'), t);
```
