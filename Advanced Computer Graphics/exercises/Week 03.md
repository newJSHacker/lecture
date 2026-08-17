# Extra exercises — Week 03 (Path tracing teaching)

Lecture: [[Advanced Computer Graphics/Lecture 03 Path tracing teaching]]

## Written and coding

1. Define this week's kernel in one sentence (Monte Carlo, cosine sample).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
color.add(trace(ray)); n++; display(color.clone().multiplyScalar(1/n));
```
