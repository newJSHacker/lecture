# Extra exercises — Week 10 (Closures and this)

Lecture: [[Modern JavaScript/Lecture 10 Closures and this]]

## Written and coding

1. Define this week's kernel in one sentence (factory, bind).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
function makeCounter(){ let n=0; return () => ++n; }
```
