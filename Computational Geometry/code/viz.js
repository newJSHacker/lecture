/**
 * Tiny 2D canvas helper for IGWT geometry demos.
 * Click empty space to add a point; drag a point to move it.
 */
(function (global) {
  "use strict";

  const Viz = {};

  function $(id) {
    return document.getElementById(id);
  }

  function boot(opts) {
    const canvas = $(opts.canvas || "c");
    const out = $(opts.out || "out");
    const ctx = canvas.getContext("2d");
    const state = {
      points: opts.points ? opts.points.slice() : [],
      drag: -1,
      hover: -1,
      extras: {},
      ...((opts.state || {})),
    };

    function pos(ev) {
      const r = canvas.getBoundingClientRect();
      return {
        x: ((ev.clientX - r.left) / r.width) * canvas.width,
        y: ((ev.clientY - r.top) / r.height) * canvas.height,
      };
    }

    function nearest(p, max) {
      max = max == null ? 14 : max;
      let best = -1, bestD = max * max;
      state.points.forEach((q, i) => {
        const d = (q.x - p.x) * (q.x - p.x) + (q.y - p.y) * (q.y - p.y);
        if (d < bestD) {
          bestD = d;
          best = i;
        }
      });
      return best;
    }

    function draw() {
      ctx.fillStyle = "#f7f5ef";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      if (opts.draw) opts.draw(ctx, state);
      state.points.forEach((p, i) => {
        ctx.beginPath();
        ctx.arc(p.x, p.y, i === state.drag ? 7 : 5, 0, Math.PI * 2);
        ctx.fillStyle = i === state.hover ? "#1a4f8b" : "#222";
        ctx.fill();
        ctx.fillStyle = "#444";
        ctx.font = "12px Segoe UI, sans-serif";
        ctx.fillText(opts.labels ? opts.labels(i, p) : String(i), p.x + 8, p.y - 8);
      });
      if (opts.status) out.textContent = opts.status(state);
    }

    canvas.addEventListener("pointerdown", (ev) => {
      canvas.setPointerCapture(ev.pointerId);
      const p = pos(ev);
      const i = nearest(p);
      if (i >= 0) state.drag = i;
      else if (opts.addOnClick !== false) {
        if (!opts.maxPoints || state.points.length < opts.maxPoints) {
          state.points.push(p);
          if (opts.onAdd) opts.onAdd(state, p);
        }
      }
      if (opts.onPointer) opts.onPointer(state, p, ev);
      draw();
    });

    canvas.addEventListener("pointermove", (ev) => {
      const p = pos(ev);
      state.hover = nearest(p);
      if (state.drag >= 0) {
        state.points[state.drag].x = p.x;
        state.points[state.drag].y = p.y;
      }
      if (opts.onMove) opts.onMove(state, p, ev);
      draw();
    });

    canvas.addEventListener("pointerup", () => {
      state.drag = -1;
      draw();
    });

    canvas.addEventListener("contextmenu", (ev) => {
      ev.preventDefault();
      const p = pos(ev);
      const i = nearest(p);
      if (i >= 0 && opts.removeOnRight !== false) {
        state.points.splice(i, 1);
        draw();
      }
    });

    function reset(pts) {
      state.points = (pts || opts.points || []).map((p) => ({ x: p.x, y: p.y }));
      state.drag = -1;
      if (opts.onReset) opts.onReset(state);
      draw();
    }

    if ($(opts.reset || "reset")) {
      $(opts.reset || "reset").addEventListener("click", () => reset(opts.points));
    }

    Viz._last = { canvas, ctx, state, draw, reset };
    draw();
    return Viz._last;
  }

  function segment(ctx, a, b, color, width) {
    ctx.beginPath();
    ctx.moveTo(a.x, a.y);
    ctx.lineTo(b.x, b.y);
    ctx.strokeStyle = color || "#222";
    ctx.lineWidth = width || 2;
    ctx.stroke();
  }

  function poly(ctx, P, fill, stroke) {
    if (!P.length) return;
    ctx.beginPath();
    ctx.moveTo(P[0].x, P[0].y);
    for (let i = 1; i < P.length; i++) ctx.lineTo(P[i].x, P[i].y);
    ctx.closePath();
    if (fill) {
      ctx.fillStyle = fill;
      ctx.fill();
    }
    ctx.strokeStyle = stroke || "#222";
    ctx.lineWidth = 2;
    ctx.stroke();
  }

  function box(ctx, aabb, color) {
    ctx.strokeStyle = color || "#888";
    ctx.setLineDash([5, 4]);
    ctx.strokeRect(aabb.minX, aabb.minY, aabb.maxX - aabb.minX, aabb.maxY - aabb.minY);
    ctx.setLineDash([]);
  }

  function dot(ctx, p, color, r) {
    ctx.beginPath();
    ctx.arc(p.x, p.y, r || 4, 0, Math.PI * 2);
    ctx.fillStyle = color || "#c0392b";
    ctx.fill();
  }

  function text(ctx, p, s, color) {
    ctx.fillStyle = color || "#333";
    ctx.font = "13px Segoe UI, sans-serif";
    ctx.fillText(s, p.x, p.y);
  }

  Viz.boot = boot;
  Viz.segment = segment;
  Viz.poly = poly;
  Viz.box = box;
  Viz.dot = dot;
  Viz.text = text;
  global.Viz = Viz;
})(typeof window !== "undefined" ? window : globalThis);
