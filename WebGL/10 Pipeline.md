# 10 — Pipeline snippets

Parent: [[07 WebGL and Shader Snippets]]

Copy these into a blank HTML file during Course 7. After week 4, students should not need this page open.

## Canvas + context

```html
<canvas id="c" style="width:100%;height:100%;display:block"></canvas>
<script>
const canvas = document.getElementById("c");
const gl = canvas.getContext("webgl2", { antialias: true, alpha: false });
if (!gl) throw new Error("Need WebGL2");
gl.clearColor(0.10, 0.10, 0.12, 1);
gl.enable(gl.DEPTH_TEST);
gl.enable(gl.CULL_FACE);
</script>
```

## Shader compile / link with logs

```js
function makeProgram(gl, vsSrc, fsSrc) {
  function sh(type, src) {
    const s = gl.createShader(type);
    gl.shaderSource(s, src);
    gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) {
      console.error(gl.getShaderInfoLog(s));
      throw new Error("compile");
    }
    return s;
  }
  const p = gl.createProgram();
  gl.attachShader(p, sh(gl.VERTEX_SHADER, vsSrc));
  gl.attachShader(p, sh(gl.FRAGMENT_SHADER, fsSrc));
  gl.linkProgram(p);
  if (!gl.getProgramParameter(p, gl.LINK_STATUS)) {
    console.error(gl.getProgramInfoLog(p));
    throw new Error("link");
  }
  return p;
}
```

A **link** error is not a compile error. Students often only check compile.

## Interleaved vs separate buffers

Separate (clearer for teaching):

```js
gl.bindBuffer(gl.ARRAY_BUFFER, posBuf);
gl.enableVertexAttribArray(0);
gl.vertexAttribPointer(0, 3, gl.FLOAT, false, 0, 0);
gl.bindBuffer(gl.ARRAY_BUFFER, nrmBuf);
gl.enableVertexAttribArray(1);
gl.vertexAttribPointer(1, 3, gl.FLOAT, false, 0, 0);
```

Interleaved `px,py,pz,nx,ny,nz,u,v` (32 bytes):

```js
const stride = 32;
gl.vertexAttribPointer(0, 3, gl.FLOAT, false, stride, 0);
gl.vertexAttribPointer(1, 3, gl.FLOAT, false, stride, 12);
gl.vertexAttribPointer(2, 2, gl.FLOAT, false, stride, 24);
```

## Indexed drawing

```js
gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, idxBuf);
gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, indices, gl.STATIC_DRAW);
gl.drawElements(gl.TRIANGLES, indices.length, gl.UNSIGNED_SHORT, 0);
```

Use `UNSIGNED_INT` + `OES_element_index_uint` (WebGL1) or WebGL2 native for meshes > 65535 verts.

## Uniforms

```js
gl.uniform1f(loc, t);
gl.uniform2f(loc, w, h);
gl.uniform3fv(loc, new Float32Array([0, 1, 0]));
gl.uniform4f(loc, r, g, b, a);
gl.uniformMatrix4fv(loc, false, mat4);
gl.uniform1i(samplerLoc, 0); // texture unit, not a boolean
```

`uniform1i` for samplers. Forgetting this leaves the sampler on unit 0 by luck — until you bind two textures.

## Texture upload

```js
const tex = gl.createTexture();
gl.bindTexture(gl.TEXTURE_2D, tex);
gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, 1);
gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, image);
gl.generateMipmap(gl.TEXTURE_2D);
gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_LINEAR);
gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
```

NPOT wrap with `REPEAT` is fine in WebGL2. In WebGL1 NPOT cannot mipmap or REPEAT.

Async image:

```js
const img = new Image();
img.onload = () => { /* texImage2D */ };
img.src = "albedo.png";
```

Until `onload`, bind a 1×1 color or you sample garbage.

## Texture units

```js
gl.activeTexture(gl.TEXTURE0);
gl.bindTexture(gl.TEXTURE_2D, albedo);
gl.uniform1i(u.u_albedo, 0);
gl.activeTexture(gl.TEXTURE1);
gl.bindTexture(gl.TEXTURE_2D, normalMap);
gl.uniform1i(u.u_normal, 1);
```

## Render to texture

```js
gl.bindFramebuffer(gl.FRAMEBUFFER, rt.fb);
gl.viewport(0, 0, rt.w, rt.h);
gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
// draw scene
gl.bindFramebuffer(gl.FRAMEBUFFER, null);
gl.viewport(0, 0, gl.canvas.width, gl.canvas.height);
```

## Readback (slow, debug only)

```js
const px = new Uint8Array(4);
gl.readPixels(x, y, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, px);
```

Origin is **lower-left** in `readPixels`, upper-left in CSS. Flip `y`.

## State you will forget to reset

| State | Default trap |
| --- | --- |
| `blend` | Left on after a transparent pass |
| `depthMask` | False after particles, then the next opaque fails |
| `viewport` | Still the FBO size |
| `activeTexture` | Not 0 |
| VAO | Still bound; next buffer upload hits the wrong VAO |

Reset at the start of a frame if you are lost:

```js
gl.bindVertexArray(null);
gl.bindFramebuffer(gl.FRAMEBUFFER, null);
gl.disable(gl.BLEND);
gl.depthMask(true);
gl.enable(gl.DEPTH_TEST);
gl.enable(gl.CULL_FACE);
```

## WebGL1 vs WebGL2 cheatsheet

| Task | WebGL1 | WebGL2 |
| --- | --- | --- |
| VAO | `OES_vertex_array_object` | native |
| Instancing | `ANGLE_instanced_arrays` | native |
| GLSL | 100 es | 300 es |
| Integer elements | extension | native |
| Depth texture | `WEBGL_depth_texture` | native |
| MRT | `WEBGL_draw_buffers` | `drawBuffers` |
