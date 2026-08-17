# Extra exercises — Week 08 (Midterm and WebGPU intro)

Lecture: [[GPU Programming/Lecture 08 Midterm and WebGPU intro]]

## Written and coding

1. Define this week's kernel in one sentence (midterm; device/queue).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
const adapter = await navigator.gpu.requestAdapter();
const device = await adapter.requestDevice();
```
