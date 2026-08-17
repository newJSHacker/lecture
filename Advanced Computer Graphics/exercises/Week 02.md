# Extra exercises — Week 02 (Radiosity idea)

Lecture: [[Advanced Computer Graphics/Lecture 02 Radiosity idea]]

## Written and coding

1. Define this week's kernel in one sentence (patches, form factors).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
for (let k=0;k<20;k++) for (let i=0;i<n;i++) B[i] = E[i] + rho[i]*dotF(i,B);
```
