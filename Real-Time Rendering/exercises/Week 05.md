# Extra exercises — Week 05 (Bloom)

Lecture: [[Real-Time Rendering/Lecture 05 Bloom]]

## Written and coding

1. Define this week's kernel in one sentence (bright pass + blur + add).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```glsl
vec3 hi = max(c - vec3(1.0), vec3(0.0));
```
