# Extra exercises — Week 14 (studio)

Lecture: [[Computer Graphics/Lecture 14 Project Studio]] · Demo: [18-project-sandbox](../code/18-project-sandbox.html)

## Desk-review drills (write in the repo)

1. Point to M, V, P. Product order?
2. Where do you divide by w?
3. Show normals / UV / depth debug. Black normals would mean …?
4. Disable depth: what happens?
5. Library vs student files.
6. Affine UV: implemented? If not, where would it show?
7. Linear vs sRGB: where do you encode?
8. Freeze the sandbox reset as the ugly/debug scene.

## Snippet — viewport y-flip fixture

```js
const vp = viewport({ x: -1, y: 1, z: 0 }, 100, 50);
assert(Math.abs(vp.x) < 1e-6 && Math.abs(vp.y) < 1e-6); // top-left
```
