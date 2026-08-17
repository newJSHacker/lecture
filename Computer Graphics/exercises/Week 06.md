# Extra exercises — Week 6 (scene graph)

Lecture: [[Computer Graphics/Week 06 Scene Graphs]] · Demo: [09-scene-graph](../code/09-scene-graph.html)

## Written

1. What does M do to a vertex?
2. `world = ? * local`
3. Expand `worldMoon` as a product.
4. Instancing vs cloning vertices.
5. Why a normal matrix if parent has non-uniform scale.

## Coding

6. Two-bone arm or turret. Moving parent moves child; not vice versa.
7. Draw RGB axes at each node.

```js
function draw(node, parentWorld) {
  const world = m4mul(parentWorld, node.local);
  drawMesh(node.mesh, world);
  node.children.forEach((ch) => draw(ch, world));
}
```
