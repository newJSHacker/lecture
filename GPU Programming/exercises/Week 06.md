# Extra exercises — Week 06 (Fluids teaser)

Lecture: [[GPU Programming/Lecture 06 Fluids teaser]]

## Written and coding

1. Define this week's kernel in one sentence (divergence-free idea).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```glsl
vec2 p = uv - dt * vel; vec4 dye = texture(u_dye, p);
```
