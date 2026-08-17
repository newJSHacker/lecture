/**
 * IGWT teaching helper for WebGL2 demos.
 * Not a production engine. Prefer copying a function into a student starter
 * over importing this whole file forever.
 *
 * Conventions: right-handed, Y-up, look down -Z, column-major mat4,
 * draw order u_proj * u_view * u_model * position.
 */
(function (global) {
  "use strict";

  function createGL(canvas, opts) {
    const gl = canvas.getContext("webgl2", {
      antialias: true,
      alpha: false,
      ...(opts || {}),
    });
    if (!gl) throw new Error("WebGL2 not available");
    return gl;
  }

  function resize(gl) {
    const c = gl.canvas;
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const w = Math.max(1, Math.floor(c.clientWidth * dpr));
    const h = Math.max(1, Math.floor(c.clientHeight * dpr));
    if (c.width !== w || c.height !== h) {
      c.width = w;
      c.height = h;
    }
    gl.viewport(0, 0, c.width, c.height);
    return c.width / c.height;
  }

  function compile(gl, type, src) {
    const sh = gl.createShader(type);
    gl.shaderSource(sh, src);
    gl.compileShader(sh);
    if (!gl.getShaderParameter(sh, gl.COMPILE_STATUS)) {
      const log = gl.getShaderInfoLog(sh);
      gl.deleteShader(sh);
      throw new Error((type === gl.VERTEX_SHADER ? "vertex" : "fragment") + " compile:\n" + log + "\n---\n" + src);
    }
    return sh;
  }

  function program(gl, vs, fs, attribs) {
    const p = gl.createProgram();
    const v = compile(gl, gl.VERTEX_SHADER, vs);
    const f = compile(gl, gl.FRAGMENT_SHADER, fs);
    gl.attachShader(p, v);
    gl.attachShader(p, f);
    if (attribs) {
      attribs.forEach(function (name, i) {
        gl.bindAttribLocation(p, i, name);
      });
    }
    gl.linkProgram(p);
    gl.deleteShader(v);
    gl.deleteShader(f);
    if (!gl.getProgramParameter(p, gl.LINK_STATUS)) {
      const log = gl.getProgramInfoLog(p);
      gl.deleteProgram(p);
      throw new Error("link:\n" + log);
    }
    return p;
  }

  function uniforms(gl, p) {
    const out = {};
    const n = gl.getProgramParameter(p, gl.ACTIVE_UNIFORMS);
    for (let i = 0; i < n; i++) {
      const info = gl.getActiveUniform(p, i);
      out[info.name.replace("[0]", "")] = gl.getUniformLocation(p, info.name);
    }
    return out;
  }

  function buffer(gl, data, target, usage) {
    const b = gl.createBuffer();
    gl.bindBuffer(target || gl.ARRAY_BUFFER, b);
    gl.bufferData(target || gl.ARRAY_BUFFER, data, usage || gl.STATIC_DRAW);
    return b;
  }

  function vao(gl, setup) {
    const v = gl.createVertexArray();
    gl.bindVertexArray(v);
    setup();
    gl.bindVertexArray(null);
    return v;
  }

  function enableAttrib(gl, loc, size, stride, offset, type, normalized) {
    gl.enableVertexAttribArray(loc);
    gl.vertexAttribPointer(loc, size, type || gl.FLOAT, !!normalized, stride || 0, offset || 0);
  }

  // --- vec3 / mat4 (column-major) ---

  const V3 = {
    add: (a, b) => [a[0] + b[0], a[1] + b[1], a[2] + b[2]],
    sub: (a, b) => [a[0] - b[0], a[1] - b[1], a[2] - b[2]],
    scale: (a, s) => [a[0] * s, a[1] * s, a[2] * s],
    dot: (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2],
    cross: (a, b) => [
      a[1] * b[2] - a[2] * b[1],
      a[2] * b[0] - a[0] * b[2],
      a[0] * b[1] - a[1] * b[0],
    ],
    len: (a) => Math.hypot(a[0], a[1], a[2]),
    norm: (a) => {
      const l = Math.hypot(a[0], a[1], a[2]) || 1;
      return [a[0] / l, a[1] / l, a[2] / l];
    },
  };

  function mat4Ident() {
    return new Float32Array([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]);
  }

  function mat4Mul(a, b) {
    const o = new Float32Array(16);
    for (let c = 0; c < 4; c++) {
      for (let r = 0; r < 4; r++) {
        o[c * 4 + r] =
          a[0 * 4 + r] * b[c * 4 + 0] +
          a[1 * 4 + r] * b[c * 4 + 1] +
          a[2 * 4 + r] * b[c * 4 + 2] +
          a[3 * 4 + r] * b[c * 4 + 3];
      }
    }
    return o;
  }

  function mat4T(x, y, z) {
    const m = mat4Ident();
    m[12] = x;
    m[13] = y;
    m[14] = z;
    return m;
  }

  function mat4S(x, y, z) {
    const m = mat4Ident();
    m[0] = x;
    m[5] = y == null ? x : y;
    m[10] = z == null ? x : z;
    return m;
  }

  function mat4Rx(a) {
    const c = Math.cos(a), s = Math.sin(a), m = mat4Ident();
    m[5] = c; m[6] = s; m[9] = -s; m[10] = c;
    return m;
  }

  function mat4Ry(a) {
    const c = Math.cos(a), s = Math.sin(a), m = mat4Ident();
    m[0] = c; m[2] = -s; m[8] = s; m[10] = c;
    return m;
  }

  function mat4Perspective(fovy, aspect, near, far) {
    const f = 1 / Math.tan(fovy / 2);
    const m = new Float32Array(16);
    m[0] = f / aspect;
    m[5] = f;
    m[10] = (far + near) / (near - far);
    m[11] = -1;
    m[14] = (2 * far * near) / (near - far);
    return m;
  }

  function mat4LookAt(eye, center, up) {
    const z = V3.norm(V3.sub(eye, center));
    const x = V3.norm(V3.cross(up, z));
    const y = V3.cross(z, x);
    const m = mat4Ident();
    m[0] = x[0]; m[1] = y[0]; m[2] = z[0];
    m[4] = x[1]; m[5] = y[1]; m[6] = z[1];
    m[8] = x[2]; m[9] = y[2]; m[10] = z[2];
    m[12] = -V3.dot(x, eye);
    m[13] = -V3.dot(y, eye);
    m[14] = -V3.dot(z, eye);
    return m;
  }

  function mat4Invert(m) {
    const n = m;
    const inv = new Float32Array(16);
    inv[0] = n[5]*n[10]*n[15] - n[5]*n[11]*n[14] - n[9]*n[6]*n[15] + n[9]*n[7]*n[14] + n[13]*n[6]*n[11] - n[13]*n[7]*n[10];
    inv[4] = -n[4]*n[10]*n[15] + n[4]*n[11]*n[14] + n[8]*n[6]*n[15] - n[8]*n[7]*n[14] - n[12]*n[6]*n[11] + n[12]*n[7]*n[10];
    inv[8] = n[4]*n[9]*n[15] - n[4]*n[11]*n[13] - n[8]*n[5]*n[15] + n[8]*n[7]*n[13] + n[12]*n[5]*n[11] - n[12]*n[7]*n[9];
    inv[12] = -n[4]*n[9]*n[14] + n[4]*n[10]*n[13] + n[8]*n[5]*n[14] - n[8]*n[6]*n[13] - n[12]*n[5]*n[10] + n[12]*n[6]*n[9];
    inv[1] = -n[1]*n[10]*n[15] + n[1]*n[11]*n[14] + n[9]*n[2]*n[15] - n[9]*n[3]*n[14] - n[13]*n[2]*n[11] + n[13]*n[3]*n[10];
    inv[5] = n[0]*n[10]*n[15] - n[0]*n[11]*n[14] - n[8]*n[2]*n[15] + n[8]*n[3]*n[14] + n[12]*n[2]*n[11] - n[12]*n[3]*n[10];
    inv[9] = -n[0]*n[9]*n[15] + n[0]*n[11]*n[13] + n[8]*n[1]*n[15] - n[8]*n[3]*n[13] - n[12]*n[1]*n[11] + n[12]*n[3]*n[9];
    inv[13] = n[0]*n[9]*n[14] - n[0]*n[10]*n[13] - n[8]*n[1]*n[14] + n[8]*n[2]*n[13] + n[12]*n[1]*n[10] - n[12]*n[2]*n[9];
    inv[2] = n[1]*n[6]*n[15] - n[1]*n[7]*n[14] - n[5]*n[2]*n[15] + n[5]*n[3]*n[14] + n[13]*n[2]*n[7] - n[13]*n[3]*n[6];
    inv[6] = -n[0]*n[6]*n[15] + n[0]*n[7]*n[14] + n[4]*n[2]*n[15] - n[4]*n[3]*n[14] - n[12]*n[2]*n[7] + n[12]*n[3]*n[6];
    inv[10] = n[0]*n[5]*n[15] - n[0]*n[7]*n[13] - n[4]*n[1]*n[15] + n[4]*n[3]*n[13] + n[12]*n[1]*n[7] - n[12]*n[3]*n[5];
    inv[14] = -n[0]*n[5]*n[14] + n[0]*n[6]*n[13] + n[4]*n[1]*n[14] - n[4]*n[2]*n[13] - n[12]*n[1]*n[6] + n[12]*n[2]*n[5];
    inv[3] = -n[1]*n[6]*n[11] + n[1]*n[7]*n[10] + n[5]*n[2]*n[11] - n[5]*n[3]*n[10] - n[9]*n[2]*n[7] + n[9]*n[3]*n[6];
    inv[7] = n[0]*n[6]*n[11] - n[0]*n[7]*n[10] - n[4]*n[2]*n[11] + n[4]*n[3]*n[10] + n[8]*n[2]*n[7] - n[8]*n[3]*n[6];
    inv[11] = -n[0]*n[5]*n[11] + n[0]*n[7]*n[9] + n[4]*n[1]*n[11] - n[4]*n[3]*n[9] - n[8]*n[1]*n[7] + n[8]*n[3]*n[5];
    inv[15] = n[0]*n[5]*n[10] - n[0]*n[6]*n[9] - n[4]*n[1]*n[10] + n[4]*n[2]*n[9] + n[8]*n[1]*n[6] - n[8]*n[2]*n[5];
    let det = n[0]*inv[0] + n[1]*inv[4] + n[2]*inv[8] + n[3]*inv[12];
    if (!det) return mat4Ident();
    det = 1 / det;
    for (let i = 0; i < 16; i++) inv[i] *= det;
    return inv;
  }

  function mat3Normal(model) {
    const i = mat4Invert(model);
    return new Float32Array([i[0], i[4], i[8], i[1], i[5], i[9], i[2], i[6], i[10]]);
  }

  // --- geometry ---

  function cube() {
    const p = [
      [-1,-1, 1],[ 1,-1, 1],[ 1, 1, 1],[-1, 1, 1],
      [-1,-1,-1],[-1, 1,-1],[ 1, 1,-1],[ 1,-1,-1],
      [-1, 1,-1],[-1, 1, 1],[ 1, 1, 1],[ 1, 1,-1],
      [-1,-1,-1],[ 1,-1,-1],[ 1,-1, 1],[-1,-1, 1],
      [ 1,-1,-1],[ 1, 1,-1],[ 1, 1, 1],[ 1,-1, 1],
      [-1,-1,-1],[-1,-1, 1],[-1, 1, 1],[-1, 1,-1],
    ];
    const n = [
      [0,0,1],[0,0,1],[0,0,1],[0,0,1],
      [0,0,-1],[0,0,-1],[0,0,-1],[0,0,-1],
      [0,1,0],[0,1,0],[0,1,0],[0,1,0],
      [0,-1,0],[0,-1,0],[0,-1,0],[0,-1,0],
      [1,0,0],[1,0,0],[1,0,0],[1,0,0],
      [-1,0,0],[-1,0,0],[-1,0,0],[-1,0,0],
    ];
    const u = [
      [0,0],[1,0],[1,1],[0,1],[0,0],[1,0],[1,1],[0,1],
      [0,0],[1,0],[1,1],[0,1],[0,0],[1,0],[1,1],[0,1],
      [0,0],[1,0],[1,1],[0,1],[0,0],[1,0],[1,1],[0,1],
    ];
    const idx = [];
    for (let f = 0; f < 6; f++) {
      const i = f * 4;
      idx.push(i, i + 1, i + 2, i, i + 2, i + 3);
    }
    const pos = new Float32Array(p.flat());
    const nor = new Float32Array(n.flat());
    const uv = new Float32Array(u.flat());
    const bary = new Float32Array(idx.length * 3);
    for (let t = 0; t < idx.length; t += 3) {
      bary[t * 3 + 0] = 1; bary[t * 3 + 1] = 0; bary[t * 3 + 2] = 0;
      bary[t * 3 + 3] = 0; bary[t * 3 + 4] = 1; bary[t * 3 + 5] = 0;
      bary[t * 3 + 6] = 0; bary[t * 3 + 7] = 0; bary[t * 3 + 8] = 1;
    }
    return { pos, nor, uv, idx: new Uint16Array(idx), bary, count: idx.length };
  }

  function sphere(lat, lon) {
    lat = lat || 24;
    lon = lon || 32;
    const pos = [], nor = [], uv = [], idx = [];
    for (let y = 0; y <= lat; y++) {
      const v = y / lat;
      const phi = v * Math.PI;
      for (let x = 0; x <= lon; x++) {
        const u = x / lon;
        const th = u * Math.PI * 2;
        const px = Math.sin(phi) * Math.cos(th);
        const py = Math.cos(phi);
        const pz = Math.sin(phi) * Math.sin(th);
        pos.push(px, py, pz);
        nor.push(px, py, pz);
        uv.push(u, 1 - v);
      }
    }
    for (let y = 0; y < lat; y++) {
      for (let x = 0; x < lon; x++) {
        const a = y * (lon + 1) + x;
        const b = a + lon + 1;
        idx.push(a, b, a + 1, a + 1, b, b + 1);
      }
    }
    return {
      pos: new Float32Array(pos),
      nor: new Float32Array(nor),
      uv: new Float32Array(uv),
      idx: new Uint16Array(idx),
      count: idx.length,
    };
  }

  function fullscreenVerts() {
    return new Float32Array([-1, -1, 3, -1, -1, 3]);
  }

  function checkerTexture(gl, size, a, b) {
    size = size || 8;
    a = a || [240, 240, 240, 255];
    b = b || [40, 80, 180, 255];
    const cnv = document.createElement("canvas");
    cnv.width = cnv.height = size;
    const ctx = cnv.getContext("2d");
    for (let y = 0; y < size; y++) {
      for (let x = 0; x < size; x++) {
        const on = (x + y) % 2 === 0;
        ctx.fillStyle = on
          ? "rgba(" + a.join(",") + ")"
          : "rgba(" + b.join(",") + ")";
        ctx.fillRect(x, y, 1, 1);
      }
    }
    const tex = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, tex);
    gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, 1);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, cnv);
    gl.generateMipmap(gl.TEXTURE_2D);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST_MIPMAP_LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.REPEAT);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.REPEAT);
    return tex;
  }

  function colorTexture(gl, rgb) {
    const tex = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, tex);
    gl.texImage2D(
      gl.TEXTURE_2D, 0, gl.RGBA, 1, 1, 0, gl.RGBA, gl.UNSIGNED_BYTE,
      new Uint8Array([rgb[0], rgb[1], rgb[2], 255])
    );
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST);
    return tex;
  }

  function fbo(gl, w, h, withDepth) {
    const color = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, color);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, w, h, 0, gl.RGBA, gl.UNSIGNED_BYTE, null);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
    const fb = gl.createFramebuffer();
    gl.bindFramebuffer(gl.FRAMEBUFFER, fb);
    gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, color, 0);
    let depth = null;
    if (withDepth) {
      depth = gl.createRenderbuffer();
      gl.bindRenderbuffer(gl.RENDERBUFFER, depth);
      gl.renderbufferStorage(gl.RENDERBUFFER, gl.DEPTH_COMPONENT16, w, h);
      gl.framebufferRenderbuffer(gl.FRAMEBUFFER, gl.DEPTH_ATTACHMENT, gl.RENDERBUFFER, depth);
    }
    const ok = gl.checkFramebufferStatus(gl.FRAMEBUFFER) === gl.FRAMEBUFFER_COMPLETE;
    gl.bindFramebuffer(gl.FRAMEBUFFER, null);
    if (!ok) throw new Error("framebuffer incomplete");
    return { fb, color, depth, w, h };
  }

  function depthFbo(gl, w, h) {
    const depth = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, depth);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.DEPTH_COMPONENT32F, w, h, 0, gl.DEPTH_COMPONENT, gl.FLOAT, null);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_COMPARE_MODE, gl.NONE);
    const fb = gl.createFramebuffer();
    gl.bindFramebuffer(gl.FRAMEBUFFER, fb);
    gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.DEPTH_ATTACHMENT, gl.TEXTURE_2D, depth, 0);
    gl.drawBuffers([gl.NONE]);
    gl.readBuffer(gl.NONE);
    const ok = gl.checkFramebufferStatus(gl.FRAMEBUFFER) === gl.FRAMEBUFFER_COMPLETE;
    gl.bindFramebuffer(gl.FRAMEBUFFER, null);
    if (!ok) throw new Error("depth framebuffer incomplete");
    return { fb, depth, w, h };
  }

  function orbit(canvas, opts) {
    const o = Object.assign({ yaw: 0.6, pitch: 0.4, dist: 4, target: [0, 0, 0] }, opts || {});
    let dragging = false, lx = 0, ly = 0;
    canvas.addEventListener("pointerdown", (e) => {
      dragging = true;
      lx = e.clientX;
      ly = e.clientY;
      canvas.setPointerCapture(e.pointerId);
    });
    canvas.addEventListener("pointerup", () => { dragging = false; });
    canvas.addEventListener("pointermove", (e) => {
      if (!dragging) return;
      o.yaw -= (e.clientX - lx) * 0.008;
      o.pitch += (e.clientY - ly) * 0.008;
      o.pitch = Math.max(-1.4, Math.min(1.4, o.pitch));
      lx = e.clientX;
      ly = e.clientY;
    });
    canvas.addEventListener("wheel", (e) => {
      e.preventDefault();
      o.dist *= e.deltaY > 0 ? 1.08 : 0.92;
      o.dist = Math.max(1.2, Math.min(20, o.dist));
    }, { passive: false });
    o.eye = function () {
      const cp = Math.cos(o.pitch), sp = Math.sin(o.pitch);
      const cy = Math.cos(o.yaw), sy = Math.sin(o.yaw);
      return [
        o.target[0] + o.dist * cp * sy,
        o.target[1] + o.dist * sp,
        o.target[2] + o.dist * cp * cy,
      ];
    };
    return o;
  }

  function loop(fn) {
    let t0 = performance.now();
    function frame(t) {
      fn((t - t0) / 1000, t / 1000);
      requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  global.GL = {
    createGL, resize, compile, program, uniforms, buffer, vao, enableAttrib,
    V3, mat4Ident, mat4Mul, mat4T, mat4S, mat4Rx, mat4Ry, mat4Perspective, mat4LookAt,
    mat4Invert, mat3Normal, cube, sphere, fullscreenVerts, checkerTexture, colorTexture,
    fbo, depthFbo, orbit, loop,
  };
})(window);
