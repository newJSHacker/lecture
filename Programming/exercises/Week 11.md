# Extra exercises — Week 11 (Recursion)

Lecture: [[Programming/Lecture 11 Recursion]]

## Written and coding

1. Define this week's kernel in one sentence (base case, stack).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
function fact(n){ if(n<=1) return 1; return n*fact(n-1); }
```
