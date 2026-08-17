# Extra exercises — Week 04 (HDR and tonemap)

Lecture: [[Real-Time Rendering/Lecture 04 HDR and tonemap]]

## Written and coding

1. Define this week's kernel in one sentence (Reinhard / ACES names).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```glsl
vec3 reinhard(vec3 x){ return x / (1.0 + x); }
```
