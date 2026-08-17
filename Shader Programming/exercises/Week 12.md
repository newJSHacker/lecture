# Extra exercises — Week 12 (Fullscreen post)

Lecture: [[Shader Programming/Lecture 12 Fullscreen post]]

## Written and coding

1. Define this week's kernel in one sentence (scene tex → FS).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```glsl
color *= smoothstep(1.2, 0.4, length(uv-0.5));
```
