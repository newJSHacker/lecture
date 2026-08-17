# Extra exercises — Week 04 (Value noise)

Lecture: [[Shader Programming/Lecture 04 Value noise]]

## Written and coding

1. Define this week's kernel in one sentence (hash, lerp).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```glsl
float hash(vec2 p){ return fract(sin(dot(p, vec2(127.1,311.7))) * 43758.5453); }
```
