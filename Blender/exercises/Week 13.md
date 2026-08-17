# Extra exercises — Week 13 (Import in Three.js)

Lecture: [[Blender/Lecture 13 Import in Three.js]]

## Written and coding

1. Define this week's kernel in one sentence (scale, shadows, colors).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```js
loader.load('crate.glb', (g) => scene.add(g.scene));
```
