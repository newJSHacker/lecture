# Extra exercises — Week 03 (Particle state in textures)

Lecture: [[GPU Programming/Lecture 03 Particle state in textures]]

## Written and coding

1. Define this week's kernel in one sentence (pos in RG, vel in BA).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```glsl
vec4 st = texelFetch(u_state, ivec2(gl_VertexID % W, gl_VertexID / W), 0);
```
