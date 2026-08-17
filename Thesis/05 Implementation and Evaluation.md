Source: [ChatGPT — Curriculum Design Advice](https://chatgpt.com/share/6a7fa45a-d4c0-83eb-b5c4-121a78bda55e)

---

# Chapter 5

# Implementation and Experimental Evaluation of an Interactive 3D Web Graphics System

## 5.1 Introduction

The previous chapter established the architecture of the proposed Interactive Graphics and Web Technologies system. The architecture integrates React, React Three Fiber, Three.js, WebGL, physically based materials, external 3D assets, animation systems, and interactive user interfaces.

This chapter describes the practical implementation of the proposed system and establishes an experimental methodology for evaluating its functionality and performance.

The principal objective is to demonstrate that modern web technologies can support sophisticated interactive 3D experiences while maintaining an architecture that is modular, maintainable, and suitable for real-world deployment.

The implemented system is designed around an interactive 3D product visualization scenario. Users can inspect a three-dimensional object, rotate and zoom the camera, modify material properties, select product configurations, and observe real-time visual changes.

The overall implementation process can be summarized as:

Asset Creation→Asset Optimization→Web Integration→Scene Construction→Interaction→Rendering→Evaluation 

The chapter first describes the development environment, followed by the implementation of the rendering system, model-loading pipeline, material system, interaction system, animation, shader functionality, and optimization procedures. Finally, an experimental framework is established for evaluating the resulting application.

---

# 5.2 Implementation Environment

## 5.2.1 Hardware Environment

Real-time graphics performance depends strongly on the underlying hardware.

The experimental environment should therefore record at least the following parameters:

| Category         | Parameter                   |
| ---------------- | --------------------------- |
| CPU              | Processor model             |
| GPU              | Graphics processor model    |
| GPU Memory       | VRAM capacity               |
| RAM              | System memory               |
| Storage          | SSD/HDD                     |
| Display          | Resolution and refresh rate |
| Operating System | Version                     |
| Browser          | Browser and version         |

For an academic experiment, these parameters should be recorded explicitly because performance measurements cannot be meaningfully compared without knowing the hardware configuration.

---

## 5.2.2 Software Environment

The implementation uses a modern JavaScript development environment.

The principal software components are:

* Node.js
* React
* React Three Fiber
* Three.js
* JavaScript or TypeScript
* GSAP
* Blender
* WebGL-compatible browser

The conceptual software stack is:

---

# 5.3 Project Initialization

The project is initialized as a modern web application.

A simplified installation process is:

Bash

The principal graphics dependencies can then be installed:

Bash

The resulting project provides a foundation for combining conventional web development with real-time graphics.

---

# 5.4 Application Entry Point

The application begins with a React root component.

A simplified implementation is:

JavaScript

The application architecture separates the root React application from the graphics scene.

This separation becomes increasingly important as the application grows.

---

# 5.5 Canvas Initialization

React Three Fiber provides the `<Canvas>` component as the main rendering surface.

A simplified implementation is:

JavaScript

The canvas establishes the environment in which the Three.js scene is rendered.

Within the canvas, components can represent:

* Cameras
* Lights
* Meshes
* Models
* Environments
* Controls
* Effects

---

# 5.6 Scene Implementation

The scene is separated into reusable components.

A typical structure is:

A simplified implementation is:

JavaScript

This architecture allows each component to be modified independently.

---

# 5.7 Camera Implementation

The camera determines how the three-dimensional scene is projected onto the display.

A perspective camera is generally appropriate for product visualization because it approximates the perspective characteristics of human vision.

The camera can be configured using:

JavaScript

The parameters represent:

* Camera position
* Field of view
* Near clipping distance
* Far clipping distance

The relationship between field of view and perspective was discussed in Chapter 3.

---

# 5.8 Camera Interaction

Interactive camera control is implemented using orbit-style interaction.

A simplified implementation is:

JavaScript

This enables the user to:

* Rotate around the object
* Zoom in
* Zoom out

Pan can be disabled when the application is intended to maintain the product at the center of the viewport.

---

# 5.9 3D Asset Preparation

The 3D asset pipeline begins in Blender.

The workflow consists of:

Before export, unnecessary geometry and unused resources should be removed.

This reduces:

* File size
* GPU memory consumption
* Loading time
* Rendering overhead

---

# 5.10 Model Optimization

The model is optimized according to its intended viewing distance.

A high-detail model may be appropriate when the camera can approach the object closely.

However, unnecessary geometric detail increases processing requirements.

Therefore, the model should be evaluated according to:

Visual Importancevs.Computational Cost 

For example, small details that occupy only a few pixels may not require full geometric representation.

---

# 5.11 glTF/GLB Export

After preparation in Blender, the model is exported to glTF or GLB.

The GLB format is particularly convenient because geometry, material definitions, and associated resources can be packaged into a single file.

The resulting directory can be structured as:

The application can then load the asset from a predictable URL.

---

# 5.12 Model Loading

The model can be loaded using the GLTF loader abstraction provided by the Three.js ecosystem.

With React Three Fiber and Drei, a simplified implementation can use `useGLTF`.

JavaScript

This approach significantly reduces the amount of manual loader management required.

---

# 5.13 Model Preloading

For applications in which the model is known in advance, preloading can reduce perceived loading latency.

Conceptually:

JavaScript

The resource can begin loading before the component is displayed.

This is particularly useful when the model represents the primary visual content of the page.

---

# 5.14 Loading State

Large models require visible loading feedback.

The interface can provide a loading screen:

The loading state should disappear automatically after the required resources have been successfully initialized.

In a production system, loading and error states should be treated as normal application states rather than exceptional conditions.

---

# 5.15 Material Implementation

The proposed system uses physically based materials.

For example:

JavaScript

The parameters influence the appearance of the surface.

### Metalness

The metalness parameter controls whether the material behaves approximately as a conductive or non-conductive material.

### Roughness

Roughness determines the spread of reflected light.

Low roughness generally produces sharp reflections.

High roughness produces broader reflections.

---

# 5.16 Material Configuration

A material configuration system can be implemented using JavaScript objects.

JavaScript

This allows users to select predefined materials without modifying the geometry.

---

# 5.17 Interactive Material Selection

The interface can expose the available materials:

JavaScript

The current material becomes part of application state.

JavaScript

The graphics component then reads this state and updates the material accordingly.

---

# 5.18 Color Customization

Product visualization frequently requires color customization.

A color picker can update the material dynamically.

Conceptually:

This demonstrates an important characteristic of interactive graphics:

> A small user-interface operation can cause a complete change in the visual output of the rendering pipeline.

---

# 5.19 Environment Lighting

An environment map provides realistic lighting and reflection information.

The scene can be configured using an HDR environment.

Conceptually:

JavaScript

The environment serves two purposes:

1. Lighting the object.
2. Providing reflection information.

This is particularly important for metallic materials.

---

# 5.20 Lighting Configuration

In addition to environmental lighting, directional or area-style lights may be introduced.

For example:

JavaScript

The lighting configuration should be designed around the intended visual purpose.

For a product visualization application, the goal is usually:

* Clear form definition
* Controlled highlights
* Natural shadows
* Readable materials
* Attractive presentation

---

# 5.21 Ground and Contact Shadows

A product floating in an empty environment often appears visually disconnected from its surroundings.

A ground plane and shadow can provide spatial context.

Conceptually:

The shadow communicates:

* Object height
* Light direction
* Contact with the ground
* Spatial position

This can significantly improve visual perception without requiring additional geometry.

---

# 5.22 Animation Implementation

Animation is implemented using frame-based updates.

For example:

JavaScript

Because the increment is multiplied by elapsed time, the animation remains substantially more consistent across frame rates than a fixed per-frame increment.

The resulting relationship is:

Δθ\=ωΔt 

where ω represents the desired angular velocity.

---

# 5.23 Interactive Camera Animation

Camera movement can also be animated.

For example, a product introduction may begin with the camera positioned farther away and then move toward the product.

The sequence can be represented as:

This produces a more deliberate presentation than immediately displaying the final camera position.

---

# 5.24 GSAP-Based Motion

GSAP can be used for presentation-oriented animation.

A simplified example is:

JavaScript

The use of an easing function creates a more natural transition.

Without easing, movement can appear mechanically linear.

---

# 5.25 Scroll-Driven Interaction

The system can also connect page scrolling with the 3D scene.

For example:

If scroll progress is represented by

p∈\[0,1\] 

then a camera position can be interpolated between two states:

C(p)\=(1−p)C0​+pC1​ 

This allows the webpage itself to become an interaction mechanism for the 3D scene.

---

# 5.26 Shader Implementation

Although Three.js provides high-level materials, custom shaders can be introduced when specialized visual effects are required.

A shader-based architecture consists primarily of:

The vertex shader processes geometry.

The fragment shader determines the appearance of individual fragments.

---

# 5.27 Vertex Shader

A simplified vertex shader is:

glsl

This operation represents the transformation process discussed in Chapter 3.

The vertex position is transformed from model coordinates toward clip space.

---

# 5.28 Fragment Shader

A basic fragment shader can produce a constant color:

glsl

Although simple, this demonstrates the fundamental role of the fragment shader.

More advanced shaders can incorporate:

* Time
* UV coordinates
* Normals
* Noise
* Light direction
* Camera position
* Procedural patterns

---

# 5.29 Procedural Shader Effects

Procedural shaders can generate visual information mathematically rather than relying entirely on textures.

For example, a periodic pattern can be created from:

f(x)\=sin(x) 

More sophisticated patterns can use:

* Perlin noise
* Simplex noise
* Fractional Brownian motion
* Signed distance functions

Such techniques are especially useful in creative coding and generative graphics.

---

# 5.30 Ray Marching

Ray marching provides a technique for rendering implicit geometry.

Instead of explicitly storing triangles, a scene can be represented using signed distance functions.

For example, a sphere can be represented conceptually as:

SDF(p)\=∥p−c∥−r 

where:

* p \= sampled position
* c \= sphere center
* r \= radius

A ray is then advanced through the scene according to the estimated distance to the nearest surface.

Ray marching is computationally expensive compared with conventional rasterization, but it provides an excellent example of how mathematical algorithms can be executed directly on the GPU.

---

# 5.31 Post-Processing

After the primary scene has been rendered, additional effects can be applied.

The conceptual pipeline is:

Post-processing can significantly enhance the visual quality of an interactive graphics application.

However, every additional pass increases rendering cost.

---

# 5.32 Bloom

Bloom simulates the appearance of intense light spreading beyond its original region.

Conceptually:

Bloom can make:

* Emissive surfaces
* Light sources
* Neon objects
* Bright highlights

appear more visually prominent.

---

# 5.33 Responsive Rendering

The application must respond to changes in viewport size.

The renderer should adapt to the browser dimensions while maintaining an appropriate pixel ratio.

A conceptual implementation is:

JavaScript

For high-density screens, pixel ratio should be controlled rather than blindly using the maximum available value.

---

# 5.34 Performance Optimization

Performance optimization is evaluated at several levels.

### Geometry

Reduce unnecessary polygons.

### Materials

Avoid unnecessarily complex shaders.

### Textures

Reduce excessive resolution.

### Draw Calls

Combine or instance objects when possible.

### Shadows

Use appropriate shadow-map resolution.

### Post-Processing

Avoid unnecessary rendering passes.

### Resolution

Adapt rendering resolution according to device capabilities.

---

# 5.35 Level of Detail

Level of Detail (LOD) allows different versions of a model to be displayed depending on camera distance.

If an object occupies only a small portion of the screen, rendering extremely detailed geometry provides little visual benefit.

LOD therefore improves the ratio between visual quality and computational cost.

---

# 5.36 Instanced Rendering

When many identical objects are required, instanced rendering can reduce overhead.

For example, a particle system may contain thousands of identical geometric elements.

Instead of submitting thousands of independent objects, instances can share the same geometry and material.

Conceptually:

One Geometry+N Transforms→N Instances 

This approach is particularly effective for:

* Particles
* Vegetation
* Repeated architecture
* Crowds
* Visualization datasets

---

# 5.37 Experimental Methodology

The experimental evaluation should measure both **functional correctness** and **rendering performance**.

The evaluation consists of four principal categories:

1. Functional evaluation
2. Visual evaluation
3. Performance evaluation
4. Compatibility evaluation

The experimental methodology is designed to answer the following research questions:

### RQ1

Can modern web technologies provide an effective framework for interactive 3D graphics?

### RQ2

Can physically based materials provide visually convincing real-time product visualization?

### RQ3

How does scene complexity affect real-time rendering performance?

### RQ4

Which optimization techniques provide the greatest performance improvement?

---

# 5.38 Functional Evaluation

The following functions should be tested.

| Test                | Expected Result                      |
| ------------------- | ------------------------------------ |
| Application startup | Scene loads correctly                |
| Model loading       | GLB model appears                    |
| Camera rotation     | Object rotates around view           |
| Zoom                | Camera distance changes              |
| Material selection  | Material changes                     |
| Color selection     | Object color changes                 |
| Animation           | Object moves smoothly                |
| Resize              | Scene remains correctly proportioned |
| Loading failure     | Error state is displayed             |

Each test should be repeated sufficiently to ensure that the behavior is deterministic.

---

# 5.39 Visual Evaluation

Visual evaluation examines the quality of the rendered result.

The following properties should be assessed:

* Material realism
* Lighting consistency
* Shadow quality
* Texture correctness
* Geometric accuracy
* Camera composition
* Animation smoothness

A qualitative rating scale may be used:

| Score | Interpretation |
| ----- | -------------- |
| 1     | Very poor      |
| 2     | Poor           |
| 3     | Acceptable     |
| 4     | Good           |
| 5     | Excellent      |

For a formal university thesis, these evaluations should preferably involve multiple evaluators rather than relying solely on the developer's subjective judgment.

---

# 5.40 Performance Evaluation

Performance should be measured using frame time and frames per second.

The fundamental relationship is:

FPS\=Tframe​1000​ 

when frame time is expressed in milliseconds.

For example:

Tframe​\=16.67ms 

corresponds approximately to:

FPS\=60 

The experiment should record:

* Average FPS
* Minimum FPS
* Average frame time
* Maximum frame time
* Draw calls
* Triangle count
* GPU memory where available

---

# 5.41 Experimental Scene Complexity

To determine the influence of scene complexity, multiple configurations can be evaluated.

### Configuration A — Simple

* Low-poly model
* One material
* Basic lighting
* No post-processing

### Configuration B — Medium

* Medium-poly model
* Multiple materials
* Environment lighting
* Shadows

### Configuration C — Complex

* High-poly model
* Multiple high-resolution textures
* PBR materials
* Shadows
* Post-processing
* Animation

The expected relationship is:

Complexity↑⇒Rendering Cost↑ 

However, the actual relationship should be measured experimentally.

---

# 5.42 Performance Benchmark Table

The final thesis should include measured values such as:

| Configuration | Triangles    | Draw Calls   | Avg. FPS     | Frame Time   |
| ------------- | ------------ | ------------ | ------------ | ------------ |
| Simple        | \[measured\] | \[measured\] | \[measured\] | \[measured\] |
| Medium        | \[measured\] | \[measured\] | \[measured\] | \[measured\] |
| Complex       | \[measured\] | \[measured\] | \[measured\] | \[measured\] |
| Optimized     | \[measured\] | \[measured\] | \[measured\] | \[measured\] |

**These values should be replaced with actual measurements from the implemented application.**

This distinction is important for academic integrity: benchmark numbers should not be fabricated merely to make the thesis appear complete.

---

# 5.43 Optimization Experiment

An optimization experiment can compare the system before and after optimization.

The procedure is:

Possible optimizations include:

* Mesh simplification
* Texture reduction
* Draw-call reduction
* Shadow reduction
* LOD
* Instancing
* Reduced post-processing

The improvement can be expressed as:

Improvement(%)\=Poriginal​Poptimized​−Poriginal​​×100 

where P represents the selected performance metric.

---

# 5.44 Expected Experimental Behavior

Although exact results depend on hardware and implementation, several general behaviors can be hypothesized.

### Hypothesis H1

Increasing geometric complexity will increase rendering cost.

### Hypothesis H2

Increasing texture resolution will increase GPU memory requirements and may affect performance.

### Hypothesis H3

Additional post-processing passes will increase frame time.

### Hypothesis H4

Reducing unnecessary geometry and draw calls will improve rendering performance.

### Hypothesis H5

PBR materials combined with appropriate environment lighting will provide greater visual realism than basic unlit materials.

These hypotheses should be validated using measured experimental data.

---

# 5.45 Compatibility Testing

The application should be tested across several modern browser environments.

A test matrix may be structured as follows:

| Browser | Desktop | Mobile | WebGL | Result     |
| ------- | ------- | ------ | ----- | ---------- |
| Chrome  | ✓       | ✓      | ✓     | \[Result\] |
| Firefox | ✓       | ✓      | ✓     | \[Result\] |
| Edge    | ✓       | ✓      | ✓     | \[Result\] |
| Safari  | ✓       | ✓      | ✓     | \[Result\] |

The exact browser versions used in the experiment should be recorded.

---

# 5.46 Usability Evaluation

Because the proposed system is interactive, technical performance alone is insufficient.

Users should also be able to understand how to interact with the scene.

A small user evaluation can measure:

* Ease of navigation
* Camera control
* Material selection
* Visual clarity
* Loading experience
* Overall satisfaction

For example, participants could rate each category from 1 to 5.

The average score can be calculated as:

xˉ\=n1​i\=1∑n​xi​ 

where n is the number of participants.

---

# 5.47 Experimental Results Structure

For the final thesis, experimental results should be presented using both tables and figures.

Recommended figures include:

### Figure 5.1

Application architecture.

### Figure 5.2

Initial rendered scene.

### Figure 5.3

Interactive camera view.

### Figure 5.4

Material comparison.

### Figure 5.5

PBR environment lighting.

### Figure 5.6

Shader-generated effect.

### Figure 5.7

Performance comparison.

### Figure 5.8

Optimization results.

### Figure 5.9

Responsive rendering on different screen sizes.

These figures should be generated from the actual implementation.

---

# 5.48 Discussion

The implementation demonstrates that modern web technologies can provide a complete development environment for interactive three-dimensional graphics.

The combination of React and React Three Fiber provides a convenient architecture for integrating conventional web interfaces with 3D content.

Three.js abstracts many low-level graphics operations while retaining access to essential concepts such as:

* Geometry
* Materials
* Cameras
* Lighting
* Textures
* Shaders
* Render targets

This allows developers to construct sophisticated graphics applications without directly implementing every component of the underlying WebGL pipeline.

However, abstraction does not eliminate the need for graphics knowledge.

For example, developers must still understand:

Model→View→Projection 

to correctly reason about camera behavior.

Similarly, understanding:

Roughness+Metalness+Fresnel+Lighting 

is necessary to produce convincing physically based materials.

---

# 5.49 Advantages of the Proposed Architecture

The proposed architecture provides several advantages.

## 5.49.1 Component Reusability

Graphics components can be reused across multiple applications.

## 5.49.2 Separation of Concerns

UI, application state, graphics, and assets can be maintained independently.

## 5.49.3 Web Accessibility

The resulting application can be distributed through a standard web browser.

## 5.49.4 Interactive Capabilities

The system supports direct user interaction with three-dimensional content.

## 5.49.5 Extensibility

Additional technologies such as WebGPU, WebXR, AI services, and advanced shaders can be integrated later.

---

# 5.50 Limitations

The system also has several limitations.

### Hardware Dependence

Rendering performance depends heavily on GPU capabilities.

### Browser Dependence

Different browsers and graphics drivers may produce different performance characteristics.

### Asset Complexity

High-quality 3D models can require significant memory and bandwidth.

### Mobile Constraints

Mobile GPUs generally impose stricter performance constraints.

### WebGL Limitations

WebGL provides a powerful abstraction but does not expose every capability available through native graphics APIs.

### Experimental Scope

A single application cannot represent every category of interactive graphics workload.

These limitations should be considered when interpreting the experimental results.

---

# 5.51 Future WebGPU Extension

The proposed architecture can be extended toward WebGPU.

The conceptual transition is:

WebGPU provides a more modern GPU programming interface and enables more explicit control over GPU resources and computation.

Potential future applications include:

* Compute shaders
* Large-scale particle simulations
* GPU-based image processing
* Advanced procedural generation
* Machine-learning-assisted graphics

This makes WebGPU an important direction for future versions of the system.

---

# 5.52 AI Integration

The architecture can also be extended with AI functionality.

For example:

An AI system could interpret natural-language requests such as:

> "Change the material to brushed aluminum."

The system could translate this request into structured application state:

JavaScript

The graphics system would then update the corresponding material.

More advanced applications could integrate AI for:

* Asset generation
* Texture generation
* Scene configuration
* Natural-language interaction
* Image analysis
* Design assistance

This represents an important intersection between artificial intelligence and interactive graphics.

---

# 5.53 Overall Evaluation

The implementation establishes a practical connection between the theoretical foundations presented in Chapter 3 and the system architecture described in Chapter 4.

The complete process can be summarized as:

Mathematics→GraphicsTheory→SoftwareArchitecture→Implementation→Interaction→Evaluation​ 

The mathematical concepts of vectors, matrices, transformations, and projection are implemented through the graphics engine.

The theoretical concepts of lighting and physically based rendering are implemented through materials, environment lighting, and shaders.

The software architecture translates these graphics concepts into reusable components.

Finally, the experimental methodology provides a framework for determining whether the resulting application satisfies its functional and performance requirements.

---

# 5.54 Chapter Conclusion

This chapter presented the implementation and evaluation methodology for the proposed interactive 3D web graphics system.

The implementation combines modern web development technologies with real-time GPU-accelerated graphics. React provides the application framework, React Three Fiber provides the declarative connection to Three.js, Three.js provides the 3D graphics abstraction, and WebGL provides access to GPU-accelerated rendering.

A complete asset pipeline was established using Blender and glTF/GLB. The system supports physically based materials, environment lighting, interactive camera control, dynamic configuration, animation, shader effects, and post-processing.

Performance optimization was treated as an integral part of implementation rather than an afterthought. Geometry complexity, draw calls, texture resolution, shader complexity, shadows, and post-processing all influence rendering cost. Accordingly, the proposed evaluation methodology measures both visual quality and computational performance.

The chapter also established a reproducible experimental framework for evaluating:

* Functional correctness
* Visual quality
* Rendering performance
* Browser compatibility
* Usability
* Optimization effectiveness

The resulting system demonstrates the feasibility of building sophisticated interactive 3D experiences using standard web technologies.

However, the final experimental claims must be supported by measurements obtained from the actual implementation. In particular, FPS, frame-time, memory, draw-call, and user-evaluation values should be collected experimentally rather than estimated.

The next chapter therefore moves beyond implementation and focuses on **results, analysis, and discussion**, where the collected experimental data can be presented and interpreted.
