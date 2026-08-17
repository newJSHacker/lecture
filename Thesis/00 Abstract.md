Source: [ChatGPT — Curriculum Design Advice](https://chatgpt.com/share/6a7fa45a-d4c0-83eb-b5c4-121a78bda55e)

---

# Abstract

**Development of a Real-Time Interactive 3D Product Configurator Using Three.js, WebGL, GLSL, and React Three Fiber**

## Abstract

The rapid evolution of web technologies has transformed modern web applications from static information systems into highly interactive digital experiences. Advances in WebGL, GPU acceleration, and modern JavaScript frameworks have enabled complex three-dimensional (3D) graphics to be rendered directly within web browsers without requiring additional plugins or native software. As a result, industries such as e-commerce, architecture, manufacturing, education, and healthcare increasingly rely on web-based interactive visualization systems to improve user engagement and support decision-making.

This thesis presents the design and implementation of a real-time interactive 3D product configurator developed using Three.js, WebGL, GLSL, and React Three Fiber. The primary objective of the research is to demonstrate how modern web graphics technologies can be integrated into a scalable and maintainable architecture capable of delivering high-quality visual experiences while maintaining real-time performance across desktop and mobile platforms.

The proposed system combines physically based rendering (PBR), custom GLSL shaders, optimized asset loading using the glTF format, efficient texture management, and component-based application architecture provided by React Three Fiber. Performance optimization techniques, including frustum culling, level-of-detail management, texture compression, asynchronous asset loading, and GPU resource optimization, are incorporated to ensure smooth rendering under varying hardware conditions. The application further supports interactive camera controls, material customization, lighting adjustment, and real-time product configuration through an intuitive graphical user interface.

To evaluate the effectiveness of the proposed framework, the implementation is analyzed using quantitative performance metrics, including frame rate (FPS), GPU memory consumption, scene loading time, rendering latency, and user interaction responsiveness. The evaluation also considers scalability by measuring system performance across scenes with different geometric complexities and texture resolutions. The results demonstrate that the proposed architecture is capable of maintaining interactive frame rates while providing visually realistic rendering suitable for commercial web applications.

In addition to implementation and performance evaluation, this thesis discusses the theoretical foundations of computer graphics, the modern WebGL rendering pipeline, shader programming, physically based rendering, and the integration of React-based application architecture with GPU-driven rendering workflows. The study illustrates how these technologies collectively contribute to the development of maintainable, extensible, and high-performance interactive graphics applications for the web.

The contributions of this thesis include a modular software architecture for web-based 3D visualization, practical implementation guidelines for integrating Three.js with React Three Fiber, an evaluation of rendering optimization techniques, and recommendations for future adoption of emerging standards such as WebGPU. The findings demonstrate that contemporary web technologies provide a practical platform for developing sophisticated interactive graphics applications that approach the visual quality traditionally associated with native desktop software.

**Keywords:** Interactive Graphics, Computer Graphics, Three.js, WebGL, GLSL, React Three Fiber, Real-Time Rendering, Physically Based Rendering, Web Development, GPU Programming, Product Configurator.
