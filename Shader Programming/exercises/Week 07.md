# Extra exercises — Week 07 (Shading an SDF)

Lecture: [[Shader Programming/Lecture 07 Shading an SDF]]

## Written and coding

1. Define this week's kernel in one sentence (normals from gradient).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```glsl
vec2 n = normalize(vec2(d(p+vec2(e,0))-d(p-vec2(e,0)), d(p+vec2(0,e))-d(p-vec2(0,e))));
```
