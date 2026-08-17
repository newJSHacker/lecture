# 02 — JS helpers (`demos/_gl.js`)

Parent: [[07 WebGL and Shader Snippets]]

The file `WebGL/demos/_gl.js` is a small teaching runtime. Students should **read it**, not treat it as magic. After Course 7 week 3 they should be able to rewrite `program()` from memory.

## Create context and resize

```js
const gl = GL.createGL(canvas);
function frame() {
  const aspect = GL.resize(gl); // sets canvas backing store + viewport
}
```

`resize` uses `clientWidth/Height` and a capped DPR. If the canvas CSS size is 0, you get a black screen — checklist item 1.

## Compile and link (always print the log)

```js
const prog = GL.program(gl, vsSource, fsSource, ["a_position", "a_normal", "a_uv"]);
const u = GL.uniforms(gl, prog);
```

`bindAttribLocation` before link keeps locations stable (0, 1, 2, …). After link, `GL.uniforms` maps names to locations (array uniforms drop `[0]`).

Raw form, for lectures without the helper:

```js
function compile(gl, type, src) {
  const sh = gl.createShader(type);
  gl.shaderSource(sh, src);
  gl.compileShader(sh);
  if (!gl.getShaderParameter(sh, gl.COMPILE_STATUS)) {
    throw new Error(gl.getShaderInfoLog(sh));
  }
  return sh;
}
```

## Buffers and VAO

```js
const vao = GL.vao(gl, () => {
  GL.buffer(gl, mesh.pos);
  GL.enableAttrib(gl, 0, 3);
  GL.buffer(gl, mesh.nor);
  GL.enableAttrib(gl, 1, 3);
  GL.buffer(gl, mesh.uv);
  GL.enableAttrib(gl, 2, 2);
  GL.buffer(gl, mesh.idx, gl.ELEMENT_ARRAY_BUFFER);
});
gl.bindVertexArray(vao);
gl.drawElements(gl.TRIANGLES, mesh.count, gl.UNSIGNED_SHORT, 0);
```

WebGL2 VAOs store the element buffer binding. Re-bind the VAO before drawing.

## Matrices

```js
const proj = GL.mat4Perspective(Math.PI / 3, aspect, 0.1, 100);
const view = GL.mat4LookAt(eye, [0, 0, 0], [0, 1, 0]);
const model = GL.mat4Mul(GL.mat4Ry(t), GL.mat4Rx(0.4));
const nmat = GL.mat3Normal(model);
gl.uniformMatrix4fv(u.u_proj, false, proj);
gl.uniformMatrix4fv(u.u_view, false, view);
gl.uniformMatrix4fv(u.u_model, false, model);
gl.uniformMatrix3fv(u.u_normal, false, nmat);
```

`false` means “already column-major.” Do not transpose twice.

## Geometry

- `GL.cube()` — 24 unique verts (normals per face), indexed
- `GL.sphere(lat, lon)` — unit sphere
- `GL.fullscreenVerts()` — one oversized triangle covering the screen

## Textures without files

```js
const tex = GL.checkerTexture(gl, 8);
gl.activeTexture(gl.TEXTURE0);
gl.bindTexture(gl.TEXTURE_2D, tex);
gl.uniform1i(u.u_tex, 0);
```

A 1×1 `GL.colorTexture(gl, [255, 80, 40])` is a valid albedo while you debug lighting.

## Framebuffers

```js
const rt = GL.fbo(gl, 512, 512, true);      // color + depth renderbuffer
const sh = GL.depthFbo(gl, 1024, 1024);     // depth texture for shadows
```

After drawing to `rt.fb`, bind `null` and sample `rt.color`.

## Orbit camera and loop

```js
const cam = GL.orbit(canvas, { dist: 4 });
GL.loop((dt, t) => {
  const eye = cam.eye();
  const view = GL.mat4LookAt(eye, cam.target, [0, 1, 0]);
});
```

Drag to orbit, wheel to dolly. `dt` is seconds since last frame; `t` is seconds since start.

## What not to add to this file

Instancing setup, skinning, glTF, and WebGPU. Those belong in a later demo or a real engine. Keep `_gl.js` small enough to read in one lab.
