# Extra exercises — Week 06 (Shadow maps)

Lecture: [[Real-Time Rendering/Lecture 06 Shadow maps]]

## Written and coding

1. Define this week's kernel in one sentence (depth from light).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```glsl
float shadow = (zLight > mapZ + bias) ? 0.3 : 1.0;
```
