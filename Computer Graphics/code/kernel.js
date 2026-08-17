/**
 * IGWT Computer Graphics I kernel (software renderer).
 * Teaching code: readable, not a production engine.
 * Copy a function into a student starter rather than importing this forever.
 *
 * Conventions: right-handed, Y-up, camera looks −Z,
 * column-major mat4, p_clip = P * V * M * p, CCW front.
 */
(function (global) {
  "use strict";

  const EPS = 1e-8;
  const CG = { EPS };

  function clamp(x, a, b) {
    return Math.max(a, Math.min(b, x));
  }

  function vec3(x, y, z) {
    return { x: x, y: y, z: z };
  }

  function vadd(a, b) {
    return { x: a.x + b.x, y: a.y + b.y, z: a.z + b.z };
  }
  function vsub(a, b) {
    return { x: a.x - b.x, y: a.y - b.y, z: a.z - b.z };
  }
  function vscale(a, s) {
    return { x: a.x * s, y: a.y * s, z: a.z * s };
  }
  function vdot(a, b) {
    return a.x * b.x + a.y * b.y + a.z * b.z;
  }
  function vcross(a, b) {
    return {
      x: a.y * b.z - a.z * b.y,
      y: a.z * b.x - a.x * b.z,
      z: a.x * b.y - a.y * b.x,
    };
  }
  function vlen(a) {
    return Math.hypot(a.x, a.y, a.z);
  }
  function vnormalize(a) {
    const L = vlen(a);
    if (L < EPS) return { x: 0, y: 1, z: 0 };
    return vscale(a, 1 / L);
  }
  function vlerp(a, b, t) {
    return vadd(vscale(a, 1 - t), vscale(b, t));
  }
  function cross2(ax, ay, bx, by) {
    return ax * by - ay * bx;
  }

  /** Column-major 4×4. */
  function m4ident() {
    return [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1];
  }
  function m4mul(a, b) {
    const o = new Array(16);
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
  function m4mulVec(m, x, y, z, w) {
    w = w == null ? 1 : w;
    return {
      x: m[0] * x + m[4] * y + m[8] * z + m[12] * w,
      y: m[1] * x + m[5] * y + m[9] * z + m[13] * w,
      z: m[2] * x + m[6] * y + m[10] * z + m[14] * w,
      w: m[3] * x + m[7] * y + m[11] * z + m[15] * w,
    };
  }
  function m4translate(tx, ty, tz) {
    const m = m4ident();
    m[12] = tx;
    m[13] = ty;
    m[14] = tz;
    return m;
  }
  function m4scale(sx, sy, sz) {
    const m = m4ident();
    m[0] = sx;
    m[5] = sy;
    m[10] = sz;
    return m;
  }
  function m4rotateX(t) {
    const c = Math.cos(t), s = Math.sin(t);
    const m = m4ident();
    m[5] = c;
    m[6] = s;
    m[9] = -s;
    m[10] = c;
    return m;
  }
  function m4rotateY(t) {
    const c = Math.cos(t), s = Math.sin(t);
    const m = m4ident();
    m[0] = c;
    m[2] = -s;
    m[8] = s;
    m[10] = c;
    return m;
  }
  function m4rotateZ(t) {
    const c = Math.cos(t), s = Math.sin(t);
    const m = m4ident();
    m[0] = c;
    m[1] = s;
    m[4] = -s;
    m[5] = c;
    return m;
  }
  function m4lookAt(eye, target, up) {
    let w = vnormalize(vsub(eye, target));
    let u = vcross(up, w);
    if (vlen(u) < 1e-6) {
      const alt = Math.abs(up.y) < 0.9 ? vec3(0, 1, 0) : vec3(1, 0, 0);
      u = vcross(alt, w);
    }
    u = vnormalize(u);
    const v = vcross(w, u);
    return [
      u.x, v.x, w.x, 0,
      u.y, v.y, w.y, 0,
      u.z, v.z, w.z, 0,
      -vdot(u, eye), -vdot(v, eye), -vdot(w, eye), 1,
    ];
  }
  function m4perspective(fovY, aspect, near, far) {
    const f = 1 / Math.tan(fovY / 2);
    const nf = 1 / (near - far);
    const m = new Array(16).fill(0);
    m[0] = f / aspect;
    m[5] = f;
    m[10] = (far + near) * nf;
    m[11] = -1;
    m[14] = (2 * far * near) * nf;
    return m;
  }
  function m4ortho(l, r, b, t, n, f) {
    const m = m4ident();
    m[0] = 2 / (r - l);
    m[5] = 2 / (t - b);
    m[10] = -2 / (f - n);
    m[12] = -(r + l) / (r - l);
    m[13] = -(t + b) / (t - b);
    m[14] = -(f + n) / (f - n);
    return m;
  }
  function m4normal(m) {
    const a = m[0], b = m[1], c = m[2];
    const d = m[4], e = m[5], f = m[6];
    const g = m[8], h = m[9], i = m[10];
    const A = e * i - f * h;
    const B = f * g - d * i;
    const C = d * h - e * g;
    const det = a * A + b * B + c * C;
    if (Math.abs(det) < EPS) return m4ident();
    const inv = 1 / det;
    return [
      A * inv, (c * h - b * i) * inv, (b * f - c * e) * inv, 0,
      B * inv, (a * i - c * g) * inv, (c * d - a * f) * inv, 0,
      C * inv, (b * g - a * h) * inv, (a * e - b * d) * inv, 0,
      0, 0, 0, 1,
    ];
  }

  function putPixel(img, x, y, r, g, b, a) {
    x = x | 0;
    y = y | 0;
    if (x < 0 || y < 0 || x >= img.width || y >= img.height) return;
    const i = (y * img.width + x) * 4;
    img.data[i] = r;
    img.data[i + 1] = g;
    img.data[i + 2] = b;
    img.data[i + 3] = a == null ? 255 : a;
  }
  function clear(img, r, g, b, a) {
    r = r == null ? 28 : r;
    g = g == null ? 28 : g;
    b = b == null ? 32 : b;
    a = a == null ? 255 : a;
    const d = img.data;
    for (let i = 0; i < d.length; i += 4) {
      d[i] = r;
      d[i + 1] = g;
      d[i + 2] = b;
      d[i + 3] = a;
    }
  }
  function over(sr, sg, sb, sa, dr, dg, db, da) {
    const a = sa / 255, da01 = da / 255;
    const oa = a + da01 * (1 - a);
    if (oa < EPS) return [0, 0, 0, 0];
    return [
      (sr * a + dr * da01 * (1 - a)) / oa,
      (sg * a + dg * da01 * (1 - a)) / oa,
      (sb * a + db * da01 * (1 - a)) / oa,
      oa * 255,
    ];
  }
  function overPixel(img, x, y, r, g, b, a) {
    x = x | 0;
    y = y | 0;
    if (x < 0 || y < 0 || x >= img.width || y >= img.height) return;
    const i = (y * img.width + x) * 4;
    const o = over(r, g, b, a, img.data[i], img.data[i + 1], img.data[i + 2], img.data[i + 3]);
    img.data[i] = o[0];
    img.data[i + 1] = o[1];
    img.data[i + 2] = o[2];
    img.data[i + 3] = o[3];
  }

  function barycentric(p, a, b, c) {
    const area = cross2(b.x - a.x, b.y - a.y, c.x - a.x, c.y - a.y);
    if (Math.abs(area) < EPS) return null;
    const alpha = cross2(b.x - p.x, b.y - p.y, c.x - p.x, c.y - p.y) / area;
    const beta = cross2(c.x - p.x, c.y - p.y, a.x - p.x, a.y - p.y) / area;
    const gamma = 1 - alpha - beta;
    return { a: alpha, b: beta, g: gamma };
  }
  function fillTriangle(img, a, b, c, ca, cb, cc) {
    const minX = Math.max(0, Math.floor(Math.min(a.x, b.x, c.x)));
    const maxX = Math.min(img.width - 1, Math.ceil(Math.max(a.x, b.x, c.x)));
    const minY = Math.max(0, Math.floor(Math.min(a.y, b.y, c.y)));
    const maxY = Math.min(img.height - 1, Math.ceil(Math.max(a.y, b.y, c.y)));
    for (let y = minY; y <= maxY; y++) {
      for (let x = minX; x <= maxX; x++) {
        const w = barycentric({ x: x + 0.5, y: y + 0.5 }, a, b, c);
        if (!w || w.a < -1e-5 || w.b < -1e-5 || w.g < -1e-5) continue;
        const r = w.a * ca[0] + w.b * cb[0] + w.g * cc[0];
        const g = w.a * ca[1] + w.b * cb[1] + w.g * cc[1];
        const bl = w.a * ca[2] + w.b * cb[2] + w.g * cc[2];
        putPixel(img, x, y, r, g, bl, 255);
      }
    }
  }

  function viewport(ndc, width, height) {
    return {
      x: (ndc.x * 0.5 + 0.5) * width,
      y: (1 - (ndc.y * 0.5 + 0.5)) * height,
      z: ndc.z * 0.5 + 0.5,
    };
  }
  function toNdc(clip) {
    if (Math.abs(clip.w) < EPS) return null;
    return { x: clip.x / clip.w, y: clip.y / clip.w, z: clip.z / clip.w };
  }

  function makeDepth(w, h) {
    return new Float32Array(w * h).fill(1);
  }
  function fillTriangleDepth(img, depth, a, b, c, ca, cb, cc) {
    const minX = Math.max(0, Math.floor(Math.min(a.x, b.x, c.x)));
    const maxX = Math.min(img.width - 1, Math.ceil(Math.max(a.x, b.x, c.x)));
    const minY = Math.max(0, Math.floor(Math.min(a.y, b.y, c.y)));
    const maxY = Math.min(img.height - 1, Math.ceil(Math.max(a.y, b.y, c.y)));
    const area = cross2(b.x - a.x, b.y - a.y, c.x - a.x, c.y - a.y);
    if (area <= EPS) return;
    for (let y = minY; y <= maxY; y++) {
      for (let x = minX; x <= maxX; x++) {
        const w = barycentric({ x: x + 0.5, y: y + 0.5 }, a, b, c);
        if (!w || w.a < -1e-5 || w.b < -1e-5 || w.g < -1e-5) continue;
        const z = w.a * a.z + w.b * b.z + w.g * c.z;
        const di = y * img.width + x;
        if (z >= depth[di]) continue;
        depth[di] = z;
        putPixel(
          img, x, y,
          w.a * ca[0] + w.b * cb[0] + w.g * cc[0],
          w.a * ca[1] + w.b * cb[1] + w.g * cc[1],
          w.a * ca[2] + w.b * cb[2] + w.g * cc[2],
          255
        );
      }
    }
  }

  function cubeMesh() {
    const p = [
      [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
      [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1],
    ];
    const faces = [
      [0, 1, 2, 3, [0, 0, -1]],
      [5, 4, 7, 6, [0, 0, 1]],
      [4, 0, 3, 7, [-1, 0, 0]],
      [1, 5, 6, 2, [1, 0, 0]],
      [3, 2, 6, 7, [0, 1, 0]],
      [4, 5, 1, 0, [0, -1, 0]],
    ];
    const uv = [[0, 1], [1, 1], [1, 0], [0, 0]];
    const tris = [];
    faces.forEach((f) => {
      const n = { x: f[4][0], y: f[4][1], z: f[4][2] };
      const idx = [0, 1, 2, 0, 2, 3];
      for (let k = 0; k < 2; k++) {
        const i0 = f[idx[k * 3]], i1 = f[idx[k * 3 + 1]], i2 = f[idx[k * 3 + 2]];
        tris.push({
          p: [p[i0], p[i1], p[i2]],
          n,
          uv: [uv[idx[k * 3]], uv[idx[k * 3 + 1]], uv[idx[k * 3 + 2]]],
        });
      }
    });
    return tris;
  }

  function lambert(n, l, kd, ka) {
    kd = kd == null ? 0.8 : kd;
    ka = ka == null ? 0.15 : ka;
    const d = Math.max(0, vdot(n, l));
    return ka + kd * d;
  }
  function blinnPhong(n, l, v, kd, ks, shin, ka) {
    kd = kd == null ? 0.65 : kd;
    ks = ks == null ? 0.35 : ks;
    shin = shin == null ? 32 : shin;
    ka = ka == null ? 0.12 : ka;
    const ndl = vdot(n, l);
    const diff = kd * Math.max(0, ndl);
    let spec = 0;
    if (ndl > 0) {
      const h = vnormalize(vadd(l, v));
      spec = ks * Math.pow(Math.max(0, vdot(n, h)), shin);
    }
    return ka + diff + spec;
  }
  function toSrgb(c) {
    return Math.pow(clamp(c, 0, 1), 1 / 2.2) * 255;
  }
  function fromSrgb(b) {
    return Math.pow(clamp(b / 255, 0, 1), 2.2);
  }

  function sampleNearest(tex, u, v, mode) {
    if (mode === "repeat") {
      u = u - Math.floor(u);
      v = v - Math.floor(v);
    } else {
      u = clamp(u, 0, 1);
      v = clamp(v, 0, 1);
    }
    const x = Math.min(tex.width - 1, Math.floor(u * tex.width));
    const y = Math.min(tex.height - 1, Math.floor(v * tex.height));
    const i = (y * tex.width + x) * 4;
    return [tex.data[i], tex.data[i + 1], tex.data[i + 2], tex.data[i + 3]];
  }
  function checkerTex(size) {
    size = size || 64;
    const data = new Uint8ClampedArray(size * size * 4);
    for (let y = 0; y < size; y++) {
      for (let x = 0; x < size; x++) {
        const on = ((x >> 3) + (y >> 3)) & 1;
        const i = (y * size + x) * 4;
        const c = on ? 230 : 40;
        data[i] = c;
        data[i + 1] = on ? 70 : 180;
        data[i + 2] = on ? 70 : 80;
        data[i + 3] = 255;
      }
    }
    return { width: size, height: size, data };
  }

  function projectTri(tri, PVM, width, height) {
    const pts = [];
    for (let i = 0; i < 3; i++) {
      const p = tri.p[i];
      const clip = m4mulVec(PVM, p[0], p[1], p[2], 1);
      if (clip.w <= EPS) return null;
      const ndc = toNdc(clip);
      const pix = viewport(ndc, width, height);
      pts.push({ x: pix.x, y: pix.y, z: pix.z, uv: tri.uv[i] });
    }
    return pts;
  }

  function drawWorldAxes(img, PVM, len) {
    len = len || 1.4;
    const o = m4mulVec(PVM, 0, 0, 0, 1);
    if (o.w <= EPS) return;
    const orig = viewport(toNdc(o), img.width, img.height);
    [
      [[len, 0, 0], [220, 60, 60]],
      [[0, len, 0], [60, 180, 80]],
      [[0, 0, len], [60, 100, 220]],
    ].forEach((ax) => {
      const q = m4mulVec(PVM, ax[0][0], ax[0][1], ax[0][2], 1);
      if (q.w <= EPS) return;
      const p = viewport(toNdc(q), img.width, img.height);
      const steps = 40;
      for (let i = 0; i <= steps; i++) {
        const t = i / steps;
        putPixel(
          img,
          orig.x + (p.x - orig.x) * t,
          orig.y + (p.y - orig.y) * t,
          ax[1][0], ax[1][1], ax[1][2]
        );
      }
    });
  }

  CG.vec3 = vec3;
  CG.vadd = vadd;
  CG.vsub = vsub;
  CG.vscale = vscale;
  CG.vdot = vdot;
  CG.vcross = vcross;
  CG.vlen = vlen;
  CG.vnormalize = vnormalize;
  CG.vlerp = vlerp;
  CG.cross2 = cross2;
  CG.m4ident = m4ident;
  CG.m4mul = m4mul;
  CG.m4mulVec = m4mulVec;
  CG.m4translate = m4translate;
  CG.m4scale = m4scale;
  CG.m4rotateX = m4rotateX;
  CG.m4rotateY = m4rotateY;
  CG.m4rotateZ = m4rotateZ;
  CG.m4lookAt = m4lookAt;
  CG.m4perspective = m4perspective;
  CG.m4ortho = m4ortho;
  CG.m4normal = m4normal;
  CG.putPixel = putPixel;
  CG.clear = clear;
  CG.over = over;
  CG.overPixel = overPixel;
  CG.barycentric = barycentric;
  CG.fillTriangle = fillTriangle;
  CG.viewport = viewport;
  CG.toNdc = toNdc;
  CG.makeDepth = makeDepth;
  CG.fillTriangleDepth = fillTriangleDepth;
  CG.cubeMesh = cubeMesh;
  CG.lambert = lambert;
  CG.blinnPhong = blinnPhong;
  CG.toSrgb = toSrgb;
  CG.fromSrgb = fromSrgb;
  CG.sampleNearest = sampleNearest;
  CG.checkerTex = checkerTex;
  CG.projectTri = projectTri;
  CG.drawWorldAxes = drawWorldAxes;
  CG.clamp = clamp;

  global.CG = CG;
})(typeof window !== "undefined" ? window : globalThis);
