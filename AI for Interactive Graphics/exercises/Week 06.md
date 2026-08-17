# Extra exercises — Week 06 (RAG idea)

Lecture: [[AI for Interactive Graphics/Lecture 06 RAG idea]]

## Written and coding

1. Define this week's kernel in one sentence (retrieve then generate).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
const hits = docs.filter(d => d.text.includes(q)).slice(0,3);
```
