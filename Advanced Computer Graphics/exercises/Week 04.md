# Extra exercises — Week 04 (Materials in a tracer)

Lecture: [[Advanced Computer Graphics/Lecture 04 Materials in a tracer]]

## Written and coding

1. Define this week's kernel in one sentence (metal, glass names).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
const k = schlick(cos, 0.04); // mix reflect/refract
```
