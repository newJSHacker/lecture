/**
 * Wrap a Shadertoy Image shader (mainImage) in WebGL2.
 * Source must NOT include #version.
 */
(function (global) {
  "use strict";

  const VS = `#version 300 es
void main(){
  vec2 p = vec2[3](vec2(-1.0,-1.0), vec2(3.0,-1.0), vec2(-1.0,3.0))[gl_VertexID];
  gl_Position = vec4(p, 0.0, 1.0);
}`;

  function wrap(src) {
    return `#version 300 es
precision highp float;
uniform vec3 iResolution;
uniform float iTime;
uniform vec4 iMouse;
uniform int iFrame;
out vec4 outColor;
${src}
void main(){ mainImage(outColor, gl_FragCoord.xy); }`;
  }

  function run(canvas, source) {
    const gl = canvas.getContext("webgl2", { antialias: false, alpha: false });
    if (!gl) throw new Error("WebGL2 required");
    const prog = GL.program(gl, VS, wrap(source));
    const u = GL.uniforms(gl, prog);
    const mouse = [0, 0, 0, 0];
    let down = false;
    function setMouse(e, click) {
      const r = canvas.getBoundingClientRect();
      const x = (e.clientX - r.left) * (canvas.width / r.width);
      const y = (r.bottom - e.clientY) * (canvas.height / r.height);
      mouse[0] = x;
      mouse[1] = y;
      if (click) { mouse[2] = x; mouse[3] = y; }
    }
    canvas.addEventListener("pointerdown", (e) => { down = true; setMouse(e, true); });
    canvas.addEventListener("pointerup", () => { down = false; });
    canvas.addEventListener("pointermove", (e) => { if (down) setMouse(e, false); });
    let frame = 0, stopped = false, t0 = performance.now();
    function tick(now) {
      if (stopped) return;
      const t = (now - t0) / 1000;
      GL.resize(gl);
      gl.useProgram(prog);
      gl.uniform3f(u.iResolution, gl.canvas.width, gl.canvas.height, 1);
      gl.uniform1f(u.iTime, t);
      gl.uniform4f(u.iMouse, mouse[0], mouse[1], mouse[2], mouse[3]);
      gl.uniform1i(u.iFrame, frame++);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
      requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
    return { gl, stop: function () { stopped = true; } };
  }

  global.Shadertoy = { run, wrap };
})(window);
