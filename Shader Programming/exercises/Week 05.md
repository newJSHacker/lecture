# Extra exercises — Week 05 (fBm and octaves)

Lecture: [[Shader Programming/Lecture 05 fBm and octaves]]

## Written and coding

1. Define this week's kernel in one sentence (sum scaled noise).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```glsl
float fbm(vec2 p){ float a=0.5,s=0.0; for(int i=0;i<5;i++){ s+=a*noise(p); p*=2.0; a*=0.5;} return s; }
```
