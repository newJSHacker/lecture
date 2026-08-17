# Extra exercises — Week 01 (Forward rendering review)

Lecture: [[Real-Time Rendering/Lecture 01 Forward rendering review]]

## Written and coding

1. Define this week's kernel in one sentence (one pass, lights in FS).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```glsl
vec3 c = albedo * (nDotL0 + nDotL1);
```
