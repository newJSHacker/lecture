# Extra exercises — Week 04 (Cross product)

Lecture: [[Mathematics for Computer Graphics/Lecture 04 Cross product]]

## Written and coding

1. Define this week's kernel in one sentence (2D signed area, 3D perpendicular).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
function cross2(a,b){ return a.x*b.y - a.y*b.x; }
```
