# Extra exercises — Week 06 (Volume marching)

Lecture: [[Advanced Computer Graphics/Lecture 06 Volume marching]]

## Written and coding

1. Define this week's kernel in one sentence (heterogeneous, woodcock name).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```glsl
for(float t=0.; t<far; t+=dt){ float d = density(p); acc += emit*d*dt*T; T *= exp(-d*dt); }
```
