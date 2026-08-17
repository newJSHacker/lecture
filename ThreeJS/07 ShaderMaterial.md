# 07 — ShaderMaterial

Parent: [[08 Three.js Snippets]]

Demo: `demos/09-shader-material.html`. Raw GLSL lives in [[07 WebGL and Shader Snippets]].

## ShaderMaterial (Three includes chunks)

```js
const mat = new THREE.ShaderMaterial({
  uniforms: {
    u_time: { value: 0 },
    u_color: { value: new THREE.Color(0xe85d3a) },
  },
  vertexShader: /* glsl */ `
    varying vec3 v_n;
    varying vec2 v_uv;
    void main() {
      v_n = normalize(normalMatrix * normal);
      v_uv = uv;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `,
  fragmentShader: /* glsl */ `
    uniform float u_time;
    uniform vec3 u_color;
    varying vec3 v_n;
    varying vec2 v_uv;
    void main() {
      float l = max(dot(normalize(v_n), normalize(vec3(0.4, 1.0, 0.3))), 0.12);
      float bands = floor((v_uv.y + u_time * 0.1) * 8.0) / 8.0;
      gl_FragColor = vec4(u_color * l * (0.6 + 0.4 * bands), 1.0);
    }
  `,
});
```

Built-in: `position`, `normal`, `uv`, `projectionMatrix`, `modelViewMatrix`, `normalMatrix`.

Update:

```js
mat.uniforms.u_time.value = clock.getElapsedTime();
```

## RawShaderMaterial

No Three chunks, no automatic `#version`. You write WebGL2 GLSL yourself. Use this when bridging to Course 7.

```js
const raw = new THREE.RawShaderMaterial({
  glslVersion: THREE.GLSL3,
  vertexShader: `#version 300 es
    in vec3 position;
    uniform mat4 modelViewMatrix, projectionMatrix;
    void main() {
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }`,
  fragmentShader: `#version 300 es
    precision highp float;
    out vec4 outColor;
    void main() { outColor = vec4(0.91, 0.31, 0.22, 1.0); }`,
});
```

## OnBeforeCompile (patch Standard)

```js
material.onBeforeCompile = (shader) => {
  shader.fragmentShader = shader.fragmentShader.replace(
    "#include <output_fragment>",
    `gl_FragColor.rgb = mix(gl_FragColor.rgb, vec3(1.0,0.4,0.1), 0.15);
     #include <output_fragment>`
  );
};
```

Fragile across three versions. Prefer ShaderMaterial for class.

## Fire / water as a Three mesh

Put a Shadertoy-style `mainImage` on a **fullscreen triangle** or a plane in front of the camera. Snippets: [[WebGL/18 Shadertoy Effects]]. Do not wrap a 400-line Image shader on a box UV unless you meant that.
