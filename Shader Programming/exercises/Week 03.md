# Extra exercises — Week 03 (UV patterns)

Lecture: [[Shader Programming/Lecture 03 UV patterns]]

## Written and coding

1. Define this week's kernel in one sentence (grid, polar, repeat).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```glsl
float checker = step(0.5, fract(uv.x*8.0)) == step(0.5, fract(uv.y*8.0)) ? 0.2 : 0.8;
```
