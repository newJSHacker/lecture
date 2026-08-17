# Extra exercises — Week 08 (Midterm and ray marching intro)

Lecture: [[Shader Programming/Lecture 08 Midterm and ray marching intro]]

## Written and coding

1. Define this week's kernel in one sentence (midterm; sphere trace idea).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```glsl
for(int i=0;i<64;i++){ float d = map(p); if(d<eps) break; p += rd*d; t+=d; if(t>far) break; }
```
