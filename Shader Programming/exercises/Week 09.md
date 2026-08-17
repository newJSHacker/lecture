# Extra exercises — Week 09 (Ray marched lighting)

Lecture: [[Shader Programming/Lecture 09 Ray marched lighting]]

## Written and coding

1. Define this week's kernel in one sentence (soft shadow, AO names).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```glsl
float shadow(vec3 p, vec3 l){ /* march toward l, return 0 if blocked */ }
```
