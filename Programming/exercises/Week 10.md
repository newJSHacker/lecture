# Extra exercises — Week 10 (Sorting and complexity)

Lecture: [[Programming/Lecture 10 Sorting and complexity]]

## Written and coding

1. Define this week's kernel in one sentence (selection sort; Θ).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
for (let i=0;i<n;i++){ let m=i; for(let j=i+1;j<n;j++) if(a[j]<a[m]) m=j; swap(a,i,m); }
```
