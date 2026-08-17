# Extra exercises — Week 07 (Camera matrices)

Lecture: [[WebGL Programming/Lecture 07 Camera matrices]]

## Written and coding

1. Define this week's kernel in one sentence (P V M in the shader).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```glsl
gl_Position = u_p * u_v * u_m * vec4(a_pos, 1.0);
```
