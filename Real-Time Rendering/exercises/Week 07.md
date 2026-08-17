# Extra exercises — Week 07 (PCF and filter)

Lecture: [[Real-Time Rendering/Lecture 07 PCF and filter]]

## Written and coding

1. Define this week's kernel in one sentence (tap neighbors).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```glsl
float s=0.0; for(int i=0;i<9;i++) s += compare(uv+off[i]); s/=9.0;
```
