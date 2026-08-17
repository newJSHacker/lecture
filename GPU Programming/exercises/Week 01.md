# Extra exercises — Week 01 (GPGPU idea)

Lecture: [[GPU Programming/Lecture 01 GPGPU idea]]

## Written and coding

1. Define this week's kernel in one sentence (GPU as throughput).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```glsl
outColor = vec4(uv, 0.5+0.5*sin(u_time), 1.0);
```
