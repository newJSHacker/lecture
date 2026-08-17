/**
 * Tiny helper: ImageData software framebuffer + rAF loop.
 */
(function (global) {
  "use strict";

  const Raster = {};

  function boot(opts) {
    const canvas = document.getElementById(opts.canvas || "c");
    const out = document.getElementById(opts.out || "out");
    const ctx = canvas.getContext("2d", { alpha: false });
    const state = Object.assign({ t: 0, running: true }, opts.state || {});
    let img = ctx.createImageData(canvas.width, canvas.height);

    function frame(now) {
      if (!state._t0) state._t0 = now;
      state.t = (now - state._t0) / 1000;
      if (opts.draw) opts.draw(img, state);
      ctx.putImageData(img, 0, 0);
      if (opts.status && out) out.textContent = opts.status(state);
      if (state.running) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);

    document.querySelectorAll("[data-toggle]").forEach((el) => {
      el.addEventListener("click", () => {
        const k = el.getAttribute("data-toggle");
        state[k] = !state[k];
      });
    });

    Raster._last = { canvas, ctx, img, state };
    return Raster._last;
  }

  Raster.boot = boot;
  global.Raster = Raster;
})(typeof window !== "undefined" ? window : globalThis);
