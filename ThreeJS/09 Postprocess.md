# 09 — Postprocess

Parent: [[08 Three.js Snippets]]

Demo: `demos/18-bloom.html`.

## Bloom (the one students want)

```js
import { EffectComposer } from "three/addons/postprocessing/EffectComposer.js";
import { RenderPass } from "three/addons/postprocessing/RenderPass.js";
import { UnrealBloomPass } from "three/addons/postprocessing/UnrealBloomPass.js";
import { OutputPass } from "three/addons/postprocessing/OutputPass.js";

const composer = new EffectComposer(renderer);
composer.addPass(new RenderPass(scene, camera));
const bloom = new UnrealBloomPass(
  new THREE.Vector2(canvas.clientWidth, canvas.clientHeight),
  0.55, // strength
  0.4,  // radius
  0.85  // threshold
);
composer.addPass(bloom);
composer.addPass(new OutputPass());

function frame() {
  resize();
  composer.render();
}
```

On resize: `composer.setSize(w, h)`.

Threshold high → only emissive / bright lights bloom. Threshold 0 → a milky mess.

## Cheap alternative

Skip the composer. Put a soft `Sprite` or additive `Points` around lights. Faster, less “Unreal.”

## Order

Tone mapping belongs at the end (`OutputPass` in recent three). If the image is grey or over-bright, you applied ACES twice.

## What this is in GL

Same idea as `WebGL/demos/13-framebuffer-post.html`: scene FBO, fullscreen triangle, mix. Three.js is a stack of those passes.
