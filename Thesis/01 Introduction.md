Source: [ChatGPT — Curriculum Design Advice](https://chatgpt.com/share/6a7fa45a-d4c0-83eb-b5c4-121a78bda55e)

---

# Chapter 1

# Introduction

## 1.1 Background

The rapid advancement of web technologies over the past decade has fundamentally changed the capabilities of modern web applications. What were once static, document-oriented websites have evolved into sophisticated software platforms capable of delivering immersive, interactive, and visually compelling user experiences. The widespread adoption of HTML5, CSS3, JavaScript, and GPU-accelerated graphics technologies has enabled browsers to perform tasks that previously required native desktop applications.

Among these technological advancements, WebGL has emerged as a major milestone in browser-based graphics. Developed as a JavaScript interface to the OpenGL ES graphics library, WebGL allows direct access to GPU hardware from within standard web browsers. By eliminating the need for browser plug-ins, WebGL provides a cross-platform solution for developing real-time three-dimensional (3D) applications that can execute efficiently on desktop computers, laptops, tablets, and mobile devices.

Building upon WebGL, high-level graphics libraries such as Three.js have significantly reduced the complexity associated with low-level graphics programming. Three.js abstracts many aspects of the rendering pipeline while preserving access to advanced graphics features including programmable shaders, physically based rendering (PBR), shadow mapping, post-processing effects, and animation systems. As a result, web developers can focus on designing interactive experiences instead of managing low-level GPU operations.

The emergence of React Three Fiber has further transformed web graphics development by integrating Three.js into the React component ecosystem. This integration enables developers to combine declarative user interface development with real-time graphics rendering, resulting in software architectures that are modular, reusable, and easier to maintain. Such an approach is particularly suitable for large-scale commercial applications where user interface components and 3D visualization must operate seamlessly together.

These technologies have accelerated the adoption of interactive 3D visualization across numerous industries. Online retailers now allow customers to inspect and customize products in real time before purchase. Architects present virtual walkthroughs of buildings directly within web browsers. Educational institutions use interactive simulations to explain scientific concepts, while healthcare organizations increasingly employ three-dimensional visualization for anatomy education and medical planning. These examples demonstrate that real-time graphics are no longer limited to the entertainment industry but have become an essential component of modern digital services.

Despite these advances, developing high-performance browser-based graphics applications remains a challenging engineering task. Developers must balance rendering quality, responsiveness, maintainability, and compatibility across a wide range of hardware capabilities. Achieving smooth performance requires careful optimization of geometry, textures, shaders, asset loading, and GPU memory usage. Consequently, understanding both theoretical computer graphics concepts and practical software engineering techniques has become increasingly important.

This thesis investigates how contemporary web graphics technologies can be integrated to build a professional-quality interactive product configurator that demonstrates realistic rendering, responsive interaction, and scalable software architecture.

---

# 1.2 Motivation

Modern consumers increasingly expect digital experiences that closely resemble physical interaction with products. Static images and videos often fail to communicate important product characteristics such as shape, material, scale, texture, and customization options. Consequently, businesses seek technologies that allow customers to interact with products directly before making purchasing decisions.

Traditional native applications can deliver highly realistic graphics but require installation, platform-specific development, and ongoing maintenance. Browser-based applications, in contrast, provide instant accessibility, simplified deployment, and broad compatibility. Advances in WebGL and modern JavaScript frameworks have narrowed the performance gap between browser applications and native software, making web-based interactive visualization an attractive solution.

However, creating these applications requires expertise in computer graphics, GPU programming, user interface engineering, software architecture, and performance optimization. Educational resources often teach these topics independently, making it difficult for students to understand how they combine in real-world projects.

This thesis is motivated by the need for a comprehensive implementation that integrates modern graphics technologies into a cohesive software system while maintaining readability, scalability, and performance.

---

# 1.3 Problem Statement

Although WebGL and Three.js provide powerful capabilities for browser-based rendering, many existing implementations focus on isolated demonstrations rather than complete software systems. Common limitations include:

* Inefficient rendering pipelines resulting in reduced frame rates.
* Poor software architecture that complicates maintenance.
* Excessive GPU memory consumption.
* Long loading times caused by unoptimized assets.
* Limited extensibility for future functionality.
* Inadequate integration between 3D graphics and modern user interface frameworks.

These challenges become increasingly significant as application complexity grows. Therefore, there is a need for a structured development approach that integrates modern graphics technologies with established software engineering principles.

---

# 1.4 Research Objectives

The primary objective of this research is to design, implement, and evaluate a real-time browser-based 3D product configurator using contemporary web graphics technologies.

The specific objectives are:

1. Design a modular software architecture for interactive graphics applications.
2. Implement physically based rendering using Three.js.
3. Integrate React Three Fiber with a modern React application.
4. Develop custom GLSL shaders for enhanced visual quality.
5. Optimize rendering performance using GPU-aware techniques.
6. Evaluate rendering quality and application performance across representative scenes.

---

# 1.5 Research Questions

This thesis seeks to answer the following research questions:

**RQ1.**  
How can Three.js and React Three Fiber be integrated to produce scalable interactive graphics applications?

**RQ2.**  
Which rendering optimization techniques provide the greatest performance improvements in browser-based applications?

**RQ3.**  
How do custom GLSL shaders improve visual realism compared with standard materials?

**RQ4.**  
Can browser-based graphics applications achieve interactive performance suitable for commercial product visualization?

---

# 1.6 Scope of the Study

This study focuses on browser-based real-time graphics applications developed using:

* JavaScript
* React
* React Three Fiber
* Three.js
* WebGL
* GLSL

The research does not address:

* Native desktop graphics APIs
* Mobile application development
* Unity or Unreal Engine
* Distributed rendering
* Ray tracing using dedicated hardware
* Large-scale multiplayer networking

Performance evaluation is limited to a representative range of consumer hardware and browsers.

---

# 1.7 Contributions

The primary contributions of this thesis are:

* A modular architecture for browser-based interactive graphics.
* A complete implementation of a real-time 3D product configurator.
* Practical guidelines for integrating React Three Fiber with Three.js.
* An evaluation of rendering optimization techniques.
* Recommendations for future migration toward WebGPU.
* A reusable educational example suitable for computer graphics and web technology courses.

---

# 1.8 Thesis Organization

The remainder of this thesis is organized as follows.

**Chapter 2** reviews the literature related to computer graphics, browser rendering, WebGL, Three.js, physically based rendering, shader programming, and interactive visualization.

**Chapter 3** introduces the theoretical foundations of computer graphics, including coordinate systems, transformations, cameras, lighting models, rasterization, texture mapping, and the modern GPU rendering pipeline.

**Chapter 4** presents the overall system architecture and design of the proposed application, describing software components, rendering workflows, asset management, and user interaction.

**Chapter 5** describes the implementation in detail, including React Three Fiber integration, custom GLSL shaders, material systems, animation, lighting, optimization strategies, and user interface development.

**Chapter 6** evaluates the application through performance measurements, rendering benchmarks, and qualitative assessment of visual quality.

**Chapter 7** discusses the implications of the results, limitations of the implementation, and opportunities for future work.

**Chapter 8** concludes the thesis by summarizing its contributions and outlining future directions, including the adoption of WebGPU and emerging real-time rendering techniques.

---
