# Extra exercises — Week 02 (APIs and keys)

Lecture: [[AI for Interactive Graphics/Lecture 02 APIs and keys]]

## Written and coding

1. Define this week's kernel in one sentence (server proxy).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
const r = await fetch('/api/complete', { method: 'POST', body: JSON.stringify({ prompt }) });
```
