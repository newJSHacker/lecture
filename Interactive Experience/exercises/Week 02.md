# Extra exercises — Week 02 (React state vs 3D)

Lecture: [[Interactive Experience/Lecture 02 React state vs 3D]]

## Written and coding

1. Define this week's kernel in one sentence (useState, useFrame).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```jsx
useFrame((_, dt) => { ref.current.rotation.y += dt; });
```
