# Extra exercises — Week 05 (async/await)

Lecture: [[Modern JavaScript/Lecture 05 async-await]]

## Written and coding

1. Define this week's kernel in one sentence (try/catch, sequential vs parallel).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
const [a,b] = await Promise.all([fetch(u1), fetch(u2)]);
```
