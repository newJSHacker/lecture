Source: [ChatGPT — Curriculum Design Advice](https://chatgpt.com/share/6a7fa45a-d4c0-83eb-b5c4-121a78bda55e)

---

# Chapter 2

# Literature Review

## 2.1 Introduction

Computer graphics has evolved from a specialized research discipline into a foundational technology for scientific visualization, engineering, entertainment, e-commerce, education, and healthcare. Simultaneously, advances in web standards and browser technologies have enabled sophisticated real-time graphics applications to execute directly within web browsers without proprietary plugins. Modern web graphics combine computer graphics theory, GPU programming, software engineering, and user interface design into a unified development ecosystem.

This chapter reviews the evolution of computer graphics, WebGL, Three.js, React Three Fiber, shader programming, physically based rendering, asset management, performance optimization, WebGPU, and existing browser-based product configurators. The chapter concludes by identifying the research gap addressed by this thesis.

---

# 2.2 Evolution of Computer Graphics

Computer graphics originated in the 1960s with vector displays used for engineering and military applications. Early systems focused on geometric precision rather than realism because hardware resources were extremely limited. During the 1970s and 1980s, raster graphics became dominant due to improvements in display technology and graphics hardware.

The introduction of dedicated Graphics Processing Units (GPUs) transformed graphics computing. Instead of relying solely on the central processing unit (CPU), GPUs were designed to perform thousands of mathematical operations simultaneously, making real-time rendering feasible. Modern GPUs execute programmable shader programs that control geometry processing, lighting calculations, texture sampling, and pixel generation.

The transition from fixed-function graphics pipelines to programmable pipelines fundamentally changed graphics programming. Earlier graphics APIs provided predefined lighting and transformation functions. Modern APIs require developers to implement these stages through shader programs, providing greater flexibility and enabling advanced rendering techniques such as physically based rendering (PBR), procedural texturing, deferred rendering, and post-processing effects. HWS Mathematics and Computer Science+1

Today, computer graphics extends beyond entertainment into fields such as digital twins, autonomous driving simulation, scientific visualization, medical imaging, architecture, manufacturing, and virtual reality.

---

# 2.3 Evolution of Web Technologies for 3D Graphics

The early World Wide Web was designed primarily for delivering hypertext documents. Interactive multimedia applications required proprietary technologies such as Adobe Flash, Java Applets, or browser plug-ins. These approaches suffered from portability, security, and maintenance issues.

The introduction of HTML5, JavaScript improvements, and the `<canvas>` element provided a standardized platform for browser graphics. Subsequently, WebGL enabled browsers to communicate directly with GPU hardware through an API derived from OpenGL ES, eliminating the need for external plugins while maintaining cross-platform compatibility. HWS Mathematics and Computer Science+1

Modern browsers now support:

* Hardware-accelerated rendering
* High-performance JavaScript engines
* WebAssembly
* WebXR
* GPU-accelerated animations
* Progressive Web Applications

These capabilities have transformed the browser into a powerful software platform capable of supporting professional visualization applications.

---

# 2.4 WebGL

WebGL is a JavaScript API that exposes GPU functionality within web browsers. Based on OpenGL ES 2.0, WebGL provides low-level access to graphics hardware while maintaining browser security.

Unlike traditional OpenGL, WebGL does not provide built-in transformation or lighting functions. Instead, developers must implement these operations through programmable shaders. Consequently, WebGL offers greater flexibility but requires a deeper understanding of graphics programming concepts such as buffers, matrices, vertex attributes, uniforms, and rendering pipelines. HWS Mathematics and Computer Science+1

A typical WebGL application consists of:

* Vertex buffers
* Index buffers
* Vertex shaders
* Fragment shaders
* Texture resources
* Framebuffers
* Rendering loop

While this architecture provides complete control over rendering, it also increases development complexity. For this reason, higher-level libraries have become the preferred approach for most commercial web applications.

---

# 2.5 Three.js

Three.js is the most widely adopted high-level JavaScript library for browser-based 3D graphics. Built on top of WebGL, it abstracts many low-level graphics operations while exposing advanced rendering capabilities when needed. Three.js+1

Three.js provides:

* Scene graph management
* Camera systems
* Geometry generation
* Material systems
* Lighting models
* Animation framework
* Shadow mapping
* Environment mapping
* Post-processing
* glTF support
* WebXR integration

Its object-oriented design enables developers to construct complex 3D scenes using reusable components rather than manipulating GPU buffers directly.

Despite these advantages, developers still require knowledge of graphics principles because rendering quality ultimately depends on scene organization, lighting, material selection, and performance optimization.

---

# 2.6 React Three Fiber

React Three Fiber (R3F) integrates Three.js into the React ecosystem using a declarative programming model.

Instead of imperatively creating objects, developers describe the scene as React components. React manages the lifecycle of these components while R3F synchronizes them with the Three.js scene graph.

Benefits include:

* Component reusability
* Improved maintainability
* Integration with React state management
* Easier UI synchronization
* Simplified animation workflows

This architecture is particularly suitable for commercial applications where graphical interfaces and business logic must coexist.

However, React introduces an abstraction layer that requires careful optimization to avoid unnecessary re-rendering and state synchronization overhead.

---

# 2.7 Shader Programming

Shaders are small programs executed directly on the GPU.

Modern rendering generally employs two programmable stages:

**Vertex Shader**

Responsible for:

* Vertex transformation
* Skinning
* Morph targets
* Normal calculation
* Coordinate conversion

**Fragment Shader**

Responsible for:

* Color computation
* Lighting
* Texture sampling
* Transparency
* Procedural effects
* Post-processing

Shader programming enables developers to implement visual effects that cannot be achieved using predefined materials.

Applications include:

* Water
* Fire
* Clouds
* Terrain
* Dissolve effects
* Glass
* Procedural animation

Because shaders execute massively in parallel, efficient shader design is critical for achieving high frame rates.

---

# 2.8 Physically Based Rendering

Physically Based Rendering (PBR) has become the industry standard for realistic rendering.

Unlike traditional Phong shading, PBR models the interaction between light and surfaces using physically motivated parameters such as:

* Base Color
* Metalness
* Roughness
* Ambient Occlusion
* Normal Maps
* Emissive Maps

Advantages include:

* Consistent lighting
* Material realism
* Predictable appearance
* Compatibility across rendering engines

Three.js implements PBR through materials such as `MeshStandardMaterial` and `MeshPhysicalMaterial`, enabling developers to achieve realistic visuals without implementing complete lighting models from scratch. Wikipedia+1

---

# 2.9 glTF Asset Format

Efficient asset management is essential for browser-based graphics.

The Graphics Language Transmission Format (glTF) has become the preferred standard for transmitting 3D assets because it is optimized for runtime performance.

Compared with OBJ or FBX, glTF supports:

* PBR materials
* Animations
* Cameras
* Lights
* Skeletons
* Compression
* Binary storage

Three.js includes native loaders for glTF, reducing loading times and simplifying integration into web applications.

---

# 2.10 Performance Optimization

Maintaining interactive frame rates requires careful optimization.

Common techniques include:

### Frustum Culling

Objects outside the camera view are not rendered.

### Level of Detail (LOD)

Different geometric models are selected according to viewing distance.

### Instanced Rendering

Multiple identical objects are rendered using a single draw call.

### Texture Compression

GPU-friendly texture formats reduce memory consumption.

### Lazy Loading

Assets are loaded only when required.

### Shader Optimization

Reducing expensive calculations improves rendering performance.

These techniques collectively improve scalability without significantly reducing visual quality.

---

# 2.11 WebGPU

Although WebGL remains the dominant browser graphics API, WebGPU represents the next generation of browser graphics programming.

Compared with WebGL, WebGPU provides:

* Lower CPU overhead
* Compute shaders
* Modern GPU pipeline management
* Better multithreading support
* Improved resource control

WebGPU is inspired by modern graphics APIs such as Vulkan, Metal, and Direct3D 12\. As browser support matures, it is expected to become an important platform for real-time graphics and general-purpose GPU computing. HWS Mathematics and Computer Science+1

---

# 2.12 Existing Web-Based Product Configurators

Interactive product configurators have become common in industries including automotive manufacturing, furniture, consumer electronics, fashion, and architecture.

Typical functionality includes:

* 360° object rotation
* Material selection
* Color customization
* Accessory configuration
* Lighting adjustment
* Animation
* Real-time pricing
* AR preview

Despite their popularity, many existing systems remain proprietary, making it difficult for researchers and educators to study their architecture or performance characteristics. Public demonstrations often emphasize visual appearance but provide little information regarding rendering pipelines, optimization strategies, or software engineering practices.

Consequently, there remains educational value in documenting a complete implementation that integrates graphics theory with modern web development.

---

# 2.13 Research Gap

The literature demonstrates significant progress in browser-based graphics technologies. However, several gaps remain.

First, many publications focus on individual technologies such as WebGL, shader programming, or React without explaining how they integrate into a cohesive application architecture.

Second, tutorials frequently emphasize visual demonstrations while providing limited discussion of scalability, maintainability, or software engineering practices.

Third, comparative evaluations of optimization strategies in browser-based graphics applications remain limited, particularly from an educational perspective.

Finally, there is a shortage of comprehensive reference implementations that combine computer graphics theory, modern JavaScript frameworks, GPU programming, and interactive product visualization within a single documented project.

This thesis addresses these gaps by presenting a modular implementation of a browser-based real-time 3D product configurator, accompanied by architectural analysis and performance evaluation.

---

# 2.14 Chapter Summary

This chapter reviewed the historical development of computer graphics and the technologies that underpin modern browser-based rendering. The discussion covered WebGL, Three.js, React Three Fiber, shader programming, physically based rendering, the glTF asset format, performance optimization techniques, WebGPU, and current approaches to interactive product visualization.

The review demonstrates that modern web technologies are sufficiently mature to support sophisticated real-time graphics applications. However, effectively integrating these technologies requires careful architectural design, performance optimization, and a solid understanding of computer graphics principles. The following chapter therefore introduces the theoretical foundations that support the implementation presented later in this thesis.
