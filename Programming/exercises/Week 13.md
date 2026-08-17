# Extra exercises — Week 13 (Objects as programs)

Lecture: [[Programming/Lecture 13 Objects as programs]]

## Written and coding

1. Define this week's kernel in one sentence (tiny OOP, methods).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
class Point {
  constructor(x,y){ this.x=x; this.y=y; }
  dist(q){ return Math.hypot(this.x-q.x, this.y-q.y); }
}
```
