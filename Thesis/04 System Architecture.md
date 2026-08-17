Source: [ChatGPT — Curriculum Design Advice](https://chatgpt.com/share/6a7fa45a-d4c0-83eb-b5c4-121a78bda55e)

---

# Chapter 4

# System Architecture and Implementation

## 4.1 Introduction

Chapter 3 established the mathematical and theoretical foundations of computer graphics, including coordinate transformations, rasterization, texture mapping, material systems, GPU processing, and physically based rendering. This chapter builds upon those foundations by describing the architecture and implementation of the proposed interactive graphics system.

The objective of the system is to demonstrate how modern web technologies can be combined with real-time 3D graphics to create an interactive application capable of presenting and manipulating three-dimensional content directly within a web browser.

The proposed architecture uses a layered approach:

This architecture separates application logic from graphics rendering while allowing both systems to communicate efficiently.

---

# 4.2 System Requirements

Before implementation, functional and non-functional requirements were identified.

## 4.2.1 Functional Requirements

The proposed system should provide:

1. Real-time 3D rendering.
2. Interactive camera control.
3. Loading of external 3D models.
4. Material modification.
5. Texture support.
6. Object animation.
7. Responsive user interaction.
8. Web-based deployment.
9. Support for modern browsers.
10. Extensibility for future graphics features.

The system should also allow developers to add advanced functionality without redesigning the entire architecture.

---

## 4.2.2 Non-Functional Requirements

The system should satisfy several performance and usability requirements.

### Performance

The renderer should maintain a stable frame rate under normal operating conditions.

### Scalability

The architecture should support increasingly complex models and scenes.

### Maintainability

Individual components should have clearly defined responsibilities.

### Accessibility

The application should remain usable across different screen sizes and input devices.

### Portability

The application should operate on modern desktop and mobile browsers supporting the required graphics APIs.

---

# 4.3 Overall System Architecture

The proposed system consists of five principal layers.

Each layer performs a distinct responsibility.

---

# 4.4 Front-End Architecture

The application interface is implemented using a component-based architecture.

A simplified structure is:

Component-based development provides several advantages.

Each component can:

* Encapsulate functionality
* Maintain local state
* Receive properties
* Be reused
* Be independently tested

This approach is particularly useful when combining traditional web interfaces with interactive graphics.

---

# 4.5 React Architecture

React provides the user-interface layer of the system.

Traditional DOM components are responsible for:

* Buttons
* Menus
* Sliders
* Forms
* Navigation
* Text

The 3D rendering area is provided by React Three Fiber.

The separation can therefore be represented as:

This architecture allows developers to use familiar React concepts while working with a real-time 3D scene.

---

# 4.6 React Three Fiber

React Three Fiber (R3F) provides a React renderer for Three.js.

Instead of manually constructing and updating a Three.js scene, developers can describe the scene declaratively using React components.

For example:

JavaScript

The developer describes the desired scene rather than manually managing every rendering operation.

This reduces boilerplate and allows graphics components to participate naturally in React's component architecture.

However, R3F does not replace knowledge of Three.js.

Understanding:

* Scene graphs
* Cameras
* Materials
* Geometry
* Render loops
* GPU resources

remains essential for developing sophisticated applications.

---

# 4.7 Scene Architecture

A Three.js scene is structured as a scene graph.

A simplified graph is:

The scene graph represents hierarchical relationships.

For example, if a wheel belongs to a vehicle object, moving the vehicle automatically moves the wheel.

This hierarchical representation is essential for:

* Animation
* Object transformation
* Scene organization
* Interaction

---

# 4.8 Asset Pipeline

Three-dimensional assets must be prepared before they can be rendered.

The proposed asset pipeline is:

Blender is used as the primary asset creation environment because it provides comprehensive modeling, UV, animation, material, and export functionality.

---

# 4.9 glTF and GLB

The proposed application uses the glTF ecosystem for 3D asset delivery.

glTF is designed as an efficient format for transmission and loading of 3D scenes and models.

The binary `.glb` variant packages the relevant data into a single binary file.

A typical model can contain:

* Meshes
* Materials
* Textures
* Cameras
* Animations
* Scene hierarchy

This makes glTF particularly appropriate for web-based real-time graphics.

---

# 4.10 Model Loading

Three.js provides `GLTFLoader` for loading glTF assets.

A simplified implementation is:

JavaScript

The asynchronous loading process prevents the browser from blocking while the asset is downloaded.

A production application should additionally provide:

* Loading indicators
* Error handling
* Asset caching
* Progressive loading where appropriate
* Resource cleanup

---

# 4.11 Asset Optimization

3D assets must be optimized before deployment.

Optimization may include:

* Polygon reduction
* Texture compression
* Mesh compression
* Removing unused materials
* Removing unused animations
* Reducing texture resolution
* Combining compatible geometry

The objective is to minimize:

Download Size+GPU Memory+Rendering Cost 

without producing unacceptable visual degradation.

---

# 4.12 Material Management

Material definitions should be separated from application logic.

For example:

JavaScript

The application can then switch materials dynamically.

JavaScript

In a larger application, material definitions can be stored in configuration files or external data structures rather than being hard-coded into components.

---

# 4.13 Dynamic Product Configuration

One of the primary use cases of the proposed architecture is interactive product customization.

For example:

The geometry remains unchanged whenever possible.

Only the relevant material or object properties are modified.

This minimizes unnecessary resource usage.

---

# 4.14 Application State

Interactive applications must maintain state describing the current configuration.

A simplified state model is:

JavaScript

When the state changes, the corresponding graphics components update.

The conceptual relationship is:

UI→State→Scene→Render 

This unidirectional data-flow model makes complex interactions easier to reason about.

---

# 4.15 Camera and Interaction System

Camera interaction is essential for an interactive 3D application.

The system may provide:

* Orbit
* Zoom
* Pan
* Rotation
* Reset
* Preset viewpoints

A typical user interaction is:

Orbit-style interaction is especially appropriate for product visualization because users can inspect an object from arbitrary directions.

---

# 4.16 Animation Architecture

Animation can be divided into two categories:

### Object Animation

Examples:

* Rotating products
* Opening doors
* Moving components
* Mechanical demonstrations

### Interface Animation

Examples:

* Menu transitions
* Page transitions
* Control-panel animations
* Camera transitions

The separation is important because interface animation and GPU-based 3D animation have different requirements.

---

# 4.17 Render Loop

Real-time applications continuously update the scene.

Conceptually:

JavaScript

At every frame:

1. User input is processed.
2. Application state is updated.
3. Object transformations are calculated.
4. Animation state is updated.
5. The scene is rendered.
6. The framebuffer is displayed.

React Three Fiber manages the underlying render loop while providing hooks for custom per-frame behavior.

---

# 4.18 Frame-Based Animation

A major principle of real-time animation is that animation should be based on elapsed time rather than frame count.

Incorrect approach:

JavaScript

The apparent animation speed can vary depending on frame rate.

A better conceptual approach is:

θnew​\=θold​+ωΔt 

where:

* ω \= angular velocity
* Δt \= elapsed time

This produces more consistent motion across different hardware.

---

# 4.19 GSAP Integration

For complex interface animation, an animation framework such as GSAP can be used.

For example:

JavaScript

This is useful for:

* Camera transitions
* Scene introductions
* UI transitions
* Product presentations
* Scroll-driven animation

The architecture can therefore use different animation systems for different responsibilities:

---

# 4.20 Lighting Architecture

The lighting system should be designed independently from individual models.

A typical product visualization scene may contain:

The environment provides broad illumination while additional lights provide controlled highlights and visual separation.

This approach is preferable to adding large numbers of independent point lights.

---

# 4.21 Environment Maps

An HDR environment map can provide both:

* Illumination
* Reflection information

This is particularly important for metallic materials.

A metal object without an environment may appear nearly black or visually uninteresting because there is little environmental information to reflect.

Therefore:

Material Quality\=Geometry Quality 

A high-quality material also requires an appropriate lighting environment.

---

# 4.22 Texture Management

Textures can represent:

* Color
* Roughness
* Metalness
* Normal information
* Ambient occlusion
* Emission

Texture resolution should be selected according to the object's visual importance.

For example:

This principle is known as allocating resources according to visual importance.

---

# 4.23 Responsive Rendering

A web-based graphics system must adapt to different viewport sizes.

When the browser dimensions change, the camera aspect ratio and renderer dimensions must be updated.

Conceptually:

Aspect\=HeightWidth​ 

The projection matrix must then be recalculated.

A simplified implementation is:

JavaScript

Failure to update the aspect ratio causes geometric distortion.

---

# 4.24 Mobile Considerations

Mobile devices introduce additional constraints.

Compared with desktop systems, they may have:

* Lower GPU performance
* Smaller memory capacity
* Higher thermal constraints
* Touch input
* Variable display resolution

Therefore, the application should consider adaptive rendering.

Potential strategies include:

* Lower pixel ratio
* Reduced shadow resolution
* Reduced texture resolution
* Fewer post-processing effects
* Lower polygon complexity

For example:

JavaScript

Limiting pixel ratio can substantially reduce GPU workload on high-density displays.

---

# 4.25 Performance Optimization

Performance optimization is a major component of real-time graphics development.

The primary performance variables are:

Performance\=f(Geometry,DrawCalls,Shaders,Textures,Resolution,Lighting,PostProcessing) 

No single optimization technique solves every performance problem.

---

## 4.25.1 Geometry Optimization

Excessive polygon counts increase:

* Vertex processing
* Memory consumption
* File size

Techniques include:

* Mesh simplification
* Level of detail
* Instance rendering
* Removing invisible geometry

---

## 4.25.2 Draw-Call Optimization

A large number of independent objects can increase CPU-side rendering overhead.

Possible techniques include:

* Instancing
* Material consolidation
* Geometry merging
* Scene restructuring

---

## 4.25.3 Texture Optimization

Textures can consume significant GPU memory.

A texture with resolution

4096×4096 

contains over 16 million texels.

Multiple such textures can rapidly consume hundreds of megabytes of memory.

Therefore, texture resolution should be selected according to actual visual requirements.

---

## 4.25.4 Shader Optimization

Fragment shaders execute potentially millions of times per frame.

Consequently, expensive operations inside a fragment shader can have significant performance implications.

For example:

Shader complexity should therefore be minimized whenever visual quality allows.

---

# 4.26 Performance Measurement

Optimization should be based on measurement rather than assumptions.

Important metrics include:

* FPS
* Frame time
* CPU time
* GPU time
* Draw calls
* Triangle count
* Texture memory
* Shader complexity

A particularly useful metric is frame time.

FPS\=Tframe​1​ 

where Tframe​ is measured in seconds.

For example,

Tframe​\=0.0167s 

corresponds approximately to

FPS\=60 

---

# 4.27 Error Handling

A production-quality graphics application must handle failures gracefully.

Potential errors include:

* Model loading failure
* Missing texture
* Unsupported format
* WebGL initialization failure
* Network timeout
* Insufficient GPU memory

A robust system should provide meaningful feedback rather than leaving the user with an empty canvas.

Example:

---

# 4.28 Loading Experience

Large 3D assets may require several seconds to download.

Therefore, the application should provide a loading state.

For example:

This improves perceived performance because users receive immediate feedback.

---

# 4.29 Security Considerations

Although graphics applications are primarily client-side, security remains important.

External assets should be loaded from trusted sources.

Applications should also consider:

* Content Security Policy
* Cross-origin restrictions
* Untrusted model files
* Third-party dependencies
* API credentials

Sensitive credentials should never be embedded in client-side JavaScript.

---

# 4.30 Deployment Architecture

The final application can be deployed as a modern web application.

A simplified deployment architecture is:

Static assets can be served through a content delivery network to reduce latency for geographically distributed users.

---

# 4.31 Proposed Project Directory

A practical project structure is:

The exact structure can vary depending on project size, but the key principle is separation of concerns.

---

# 4.32 Example System Implementation

The following simplified example demonstrates how the architecture can be combined.

JavaScript

Although this example is small, it demonstrates the principal architecture:

A complete implementation extends this structure with asynchronous model loading, application state, PBR materials, environment lighting, animations, responsive layout, and performance optimization.

---

# 4.33 Implementation Workflow

The recommended development process is iterative.

### Stage 1 — Scene Initialization

Create:

* Canvas
* Renderer
* Camera
* Basic lighting

### Stage 2 — Geometry

Add:

* Primitive geometry
* External models
* Scene hierarchy

### Stage 3 — Materials

Add:

* Base colors
* Textures
* Roughness
* Metalness

### Stage 4 — Interaction

Add:

* Orbit controls
* Object selection
* Product configuration

### Stage 5 — Animation

Add:

* Camera transitions
* Object animation
* UI motion

### Stage 6 — Optimization

Measure:

* Frame rate
* Draw calls
* GPU memory
* Asset size

### Stage 7 — Deployment

Test:

* Desktop
* Tablet
* Mobile
* Different browsers
* Different GPU capabilities

This incremental process reduces complexity and makes debugging significantly easier.

---

# 4.34 Testing Methodology

The proposed system should be evaluated at multiple levels.

## Functional Testing

Verify:

* Models load correctly.
* Materials change correctly.
* Camera controls operate correctly.
* UI controls update scene state.
* Animations execute correctly.

## Visual Testing

Verify:

* Lighting is consistent.
* Materials appear correctly.
* Textures align with geometry.
* Shadows are visually appropriate.

## Performance Testing

Measure:

* Average FPS
* Minimum FPS
* Frame time
* Draw calls
* Memory usage

## Compatibility Testing

Test on:

* Chrome
* Firefox
* Safari
* Edge

and across different GPU classes.

---

# 4.35 Chapter Summary

This chapter translated the theoretical concepts introduced in Chapter 3 into a practical web-based system architecture.

The proposed architecture combines:

React+React Three Fiber+Three.js+WebGL+GPU 

React provides the application and interface layer, while React Three Fiber connects the declarative React architecture with the Three.js scene graph. Three.js provides high-level access to 3D geometry, cameras, materials, lighting, animation, and rendering functionality. WebGL provides access to the browser's GPU-accelerated graphics pipeline.

The chapter also established an asset pipeline based on Blender and glTF/GLB, providing a practical workflow from 3D modeling through optimization and browser deployment.

Particular attention was given to material management and physically based rendering because realistic material behavior is essential to the proposed interactive visualization system. Dynamic application state allows users to modify product properties without unnecessarily rebuilding the underlying geometry.

Performance optimization was also identified as a fundamental architectural concern. Geometry complexity, draw-call count, texture resolution, shader complexity, lighting, and screen resolution all influence frame time. Consequently, performance must be measured systematically rather than estimated solely from visual complexity.

The complete architecture can therefore be summarized as:

User→React→R3F→Three.js→WebGL→GPU→Display​ 

This architecture provides a foundation for the practical implementation of interactive 3D web applications.
