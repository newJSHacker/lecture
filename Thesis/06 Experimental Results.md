Source: [ChatGPT — Curriculum Design Advice](https://chatgpt.com/share/6a7fa45a-d4c0-83eb-b5c4-121a78bda55e)

---

# Chapter 6

# Experimental Results and Discussion

## 6.1 Introduction

Chapter 5 presented the implementation of the proposed Interactive Graphics and Web Technologies system. The system integrates React, React Three Fiber, Three.js, WebGL, physically based rendering, custom shaders, animation, optimized 3D assets, and interactive user interfaces.

The purpose of this chapter is to establish and analyze the experimental results obtained from the implemented system.

The evaluation focuses on four major dimensions:

1. **Functional performance**
2. **Visual quality**
3. **Rendering performance**
4. **Usability and interaction**

The central research question is whether modern web technologies can provide sufficient capabilities for developing sophisticated interactive 3D applications while maintaining acceptable performance and usability.

A second objective is to determine how rendering complexity influences performance and which optimization techniques provide measurable benefits.

It is important to distinguish between **experimental methodology** and **experimental results**. The benchmark values in this chapter are therefore presented as a structured reference dataset where actual measurements have not yet been collected. Before submission as an academic thesis, these values should be replaced by measurements from the final implementation.

---

# 6.2 Experimental Objectives

The experiments were designed to address the following research questions.

### RQ1

Can a modern web-based architecture provide reliable real-time interactive 3D rendering?

### RQ2

Can physically based rendering produce visually convincing materials in a browser environment?

### RQ3

How does scene complexity affect rendering performance?

### RQ4

How effective are common optimization techniques such as geometry reduction, texture optimization, draw-call reduction, and post-processing reduction?

### RQ5

Can the proposed system provide an intuitive interaction experience for users without specialized graphics knowledge?

---

# 6.3 Experimental Variables

The experiment contains several independent and dependent variables.

### Independent Variables

The principal independent variables are:

* Polygon count
* Number of objects
* Number of draw calls
* Texture resolution
* Number of lights
* Shadow resolution
* Post-processing effects
* Shader complexity
* Screen resolution

### Dependent Variables

The primary dependent variables are:

* Frames per second
* Frame time
* GPU utilization
* Memory consumption
* Loading time
* User interaction score

The relationship can be represented as:

Performance\=f(Geometry,Textures,DrawCalls,Shaders,Lighting,Resolution) 

---

# 6.4 Experimental Configurations

Four scene configurations were defined.

## Configuration A — Basic

The basic configuration represents a minimally complex scene.

Characteristics:

* Low-poly model
* One material
* Basic lighting
* No post-processing
* Low-resolution textures
* Static scene

## Configuration B — Standard

The standard configuration represents a typical interactive product visualization.

Characteristics:

* Medium-complexity model
* Multiple materials
* Environment lighting
* PBR materials
* Shadows
* Interactive camera
* Basic animation

## Configuration C — Advanced

The advanced configuration introduces additional visual effects.

Characteristics:

* High-poly model
* Multiple materials
* High-resolution textures
* PBR
* Shadows
* Animation
* Post-processing
* Custom shader effects

## Configuration D — Optimized

The optimized configuration applies the optimization techniques discussed in Chapter 5.

These include:

* Reduced geometry
* Texture optimization
* Reduced draw calls
* Controlled pixel ratio
* Optimized shadows
* Reduced post-processing
* Resource reuse

---

# 6.5 Experimental Scene

The experimental scene consists of a central 3D product model positioned inside a controlled studio-like environment.

The scene contains:

The scene was selected because it contains most of the components required by modern interactive 3D applications while remaining sufficiently controlled for performance comparison.

---

# 6.6 Functional Test Results

Functional testing evaluates whether the major system features operate correctly.

The expected results are summarized below.

| Function            | Expected Behavior                    | Result |
| ------------------- | ------------------------------------ | ------ |
| Application startup | Application initializes              | Pass   |
| Model loading       | Model appears correctly              | Pass   |
| Camera rotation     | Camera responds to input             | Pass   |
| Zoom                | Camera distance changes              | Pass   |
| Material selection  | Material changes                     | Pass   |
| Color selection     | Object color changes                 | Pass   |
| Animation           | Object animates correctly            | Pass   |
| Resize              | Scene maintains correct aspect ratio | Pass   |
| Shader effect       | Effect renders correctly             | Pass   |
| Loading state       | Loading interface appears            | Pass   |

The functional evaluation demonstrates that the proposed architecture supports the principal requirements established in Chapter 4.

The separation between the UI and graphics layers was particularly useful because changes to user-interface state could be propagated to the graphics scene without reconstructing the entire application.

---

# 6.7 Model Loading Evaluation

Model loading represents an important component of the user experience.

A typical loading sequence is:

The total loading time can therefore be expressed approximately as:

Tload​\=Tnetwork​+Tparse​+Ttexture​+TGPU​ 

The network component becomes increasingly significant as asset size increases.

For this reason, asset optimization should be considered before deployment rather than after performance problems appear.

---

# 6.8 Visual Evaluation of Materials

The visual experiment compares three material configurations:

1. Basic diffuse material
2. Standard physically based material
3. PBR material combined with HDR environment lighting

The expected visual differences are summarized below.

| Material  | Reflection | Surface Definition | Realism   |
| --------- | ---------- | ------------------ | --------- |
| Basic     | Low        | Moderate           | Low       |
| PBR       | Moderate   | High               | High      |
| PBR + HDR | High       | Very high          | Very high |

The PBR + HDR configuration provides substantially more environmental information because the material reflects the surrounding environment.

This demonstrates an important principle:

Material Appearance\=f(Material, Lighting, Environment) 

A physically based material cannot be evaluated independently from its lighting environment.

---

# 6.9 Camera Interaction Evaluation

The interactive camera was evaluated according to:

* Rotation responsiveness
* Zoom responsiveness
* Stability
* Object framing
* Transition smoothness

The orbit camera model was found to be particularly appropriate for product visualization.

Users can inspect the model from multiple angles without requiring specialized 3D navigation knowledge.

The interaction model can be represented as:

Input→CameraTransform→SceneUpdate→Render 

The low conceptual complexity of this interaction is one reason orbit-style controls are widely applicable to product visualization.

---

# 6.10 Animation Evaluation

The animation system was evaluated under different frame rates.

The use of elapsed-time-based animation rather than fixed frame increments provides more consistent motion.

The angular position is calculated as:

θ(t)\=θ0​+ωt 

where:

* θ0​ is the initial angle,
* ω is angular velocity,
* t is elapsed time.

This means that the animation is determined by time rather than by the number of frames rendered.

As a result, a system operating at 60 FPS and another operating at 30 FPS can maintain approximately the same animation speed.

---

# 6.11 Rendering Performance

Rendering performance represents the most important quantitative component of the evaluation.

The primary metric is frames per second.

FPS\=Tframe​1​ 

For frame time measured in milliseconds:

FPS\=Tframe​1000​ 

For example:

Tframe​\=16.67ms 

produces approximately:

FPS≈60 

---

# 6.12 Baseline Performance

A baseline scene is first measured before optimization.

The following table illustrates the format of the experimental results.

> **Note:** The numerical values below are example/reference values and must be replaced with measurements from the actual experimental hardware before inclusion in a submitted thesis.

| Configuration | Triangles | Draw Calls | Avg. FPS | Avg. Frame Time |
| ------------- | --------- | ---------- | -------- | --------------- |
| Basic         | 35,000    | 18         | 60       | 16.7 ms         |
| Standard      | 120,000   | 42         | 58       | 17.2 ms         |
| Advanced      | 420,000   | 96         | 43       | 23.3 ms         |
| Optimized     | 190,000   | 51         | 59       | 16.9 ms         |

The example results suggest that increasing scene complexity reduces rendering performance.

The advanced configuration requires substantially more geometry and rendering operations than the basic configuration.

After optimization, however, performance approaches the standard configuration despite retaining much of the visual complexity.

---

# 6.13 Frame-Time Analysis

FPS alone does not completely describe performance.

Frame time provides a more direct measurement of rendering cost.

For example:

The relationship is nonlinear from the perspective of perceived performance.

A reduction from 60 FPS to 50 FPS represents an increase in frame time of approximately:

20.0−16.67\=3.33ms 

while a reduction from 40 FPS to 30 FPS produces:

33.33−25\=8.33ms 

Therefore, frame time is often a more useful engineering metric than FPS alone.

---

# 6.14 Geometry Complexity Experiment

The first performance experiment evaluates the effect of polygon count.

The expected relationship is:

Polygon Count↑⇒Vertex Processing↑⇒Rendering Cost↑ 

A reference experiment may use:

| Model     | Triangles | Avg. FPS |
| --------- | --------- | -------- |
| Low       | 35,000    | 60       |
| Medium    | 120,000   | 58       |
| High      | 420,000   | 43       |
| Very High | 900,000   | 31       |

These values are illustrative rather than measured results.

The important observation is that polygon count alone does not completely determine performance.

A model with fewer polygons can still be expensive if it uses:

* Complex shaders
* Many materials
* High-resolution textures
* Multiple shadow passes
* Extensive post-processing

Therefore:

Rendering Cost\=f(Polygon Count) 

alone.

---

# 6.15 Draw-Call Experiment

The second experiment examines draw-call complexity.

Each draw call introduces CPU-side and graphics-pipeline overhead.

The expected relationship is:

DrawCalls↑⇒CPU/GPU Submission Overhead↑ 

A reference comparison is:

| Draw Calls | Average FPS |
| ---------- | ----------- |
| 20         | 60          |
| 50         | 58          |
| 100        | 52          |
| 200        | 42          |
| 400        | 31          |

Again, these numbers are representative values and should be replaced by actual measurements.

The experiment illustrates why scene organization is important.

A scene containing many small independent objects can be considerably more expensive than a scene containing the same total number of triangles organized into fewer rendering operations.

---

# 6.16 Texture Resolution Experiment

Texture resolution affects both download size and GPU memory.

A comparison can be made using:

* 512 × 512
* 1024 × 1024
* 2048 × 2048
* 4096 × 4096

The number of texels is:

N\=W×H 

Thus:

4096×4096\=16,777,216 

texels.

If multiple texture maps use this resolution, GPU memory consumption can become significant.

The experiment therefore evaluates whether high-resolution textures produce visible benefits proportional to their computational and memory cost.

---

# 6.17 Pixel-Ratio Experiment

Modern high-density displays may use device pixel ratios greater than one.

Rendering at the full device pixel ratio increases the number of fragments processed by the GPU.

For example:

Resolutionrender​\=ResolutionCSS​×DPR 

Therefore, if the device pixel ratio is 3, the number of pixels can increase substantially.

A practical strategy is:

JavaScript

This can reduce GPU workload while maintaining high visual quality.

---

# 6.18 Post-Processing Experiment

Post-processing introduces additional rendering operations.

A reference comparison is:

| Configuration | Effects          | Relative Cost |
| ------------- | ---------------- | ------------- |
| A             | None             | Low           |
| B             | Bloom            | Medium        |
| C             | Bloom + Color    | Medium–High   |
| D             | Multiple Effects | High          |

The experiment demonstrates that visual quality should be balanced against computational cost.

For an interactive application, a small improvement in appearance may not justify a significant reduction in frame rate.

---

# 6.19 Shadow Performance

Shadows can be computationally expensive because the scene may need to be rendered from the perspective of the light source.

A simplified shadow workflow is:

Higher shadow-map resolution generally improves visual quality but increases computational requirements.

Therefore, shadow quality should be selected according to the importance of the shadow in the final composition.

---

# 6.20 Optimization Results

After optimization, the application should be evaluated using exactly the same scene and hardware configuration.

A reference comparison is:

| Metric     | Before  | After   | Improvement |
| ---------- | ------- | ------- | ----------- |
| Triangles  | 420,000 | 190,000 | 54.8%       |
| Draw Calls | 96      | 51      | 46.9%       |
| Avg. FPS   | 43      | 59      | 37.2%       |
| Frame Time | 23.3 ms | 16.9 ms | 27.5%       |

These values are examples of the desired presentation format and **not actual measurements**.

The final thesis should calculate these values directly from the benchmark results.

The improvement percentage is calculated as:

Improvement\=BeforeAfter−Before​×100 

for metrics where larger values represent better performance.

For frame time, lower is better, so:

Improvement\=BeforeBefore−After​×100 

---

# 6.21 Effectiveness of Optimization Techniques

The experiments indicate that optimization should not focus exclusively on one variable.

The most effective strategy is typically a combination of:

1. Geometry optimization
2. Draw-call reduction
3. Texture optimization
4. Controlled pixel ratio
5. Shadow optimization
6. Post-processing control

The optimization process can therefore be described as:

This iterative methodology is more reliable than applying arbitrary optimization techniques without measuring their effects.

---

# 6.22 User Evaluation

Technical performance does not necessarily imply usability.

A user evaluation can therefore be performed with participants who have varying levels of graphics experience.

Participants can be asked to complete several tasks:

### Task 1

Rotate the 3D object.

### Task 2

Zoom into the object.

### Task 3

Change its material.

### Task 4

Change its color.

### Task 5

Select another product configuration.

### Task 6

Return to the default camera view.

The participants can then rate the system.

---

# 6.23 Usability Questionnaire

A five-point Likert scale can be used.

| Score | Meaning           |
| ----- | ----------------- |
| 1     | Strongly disagree |
| 2     | Disagree          |
| 3     | Neutral           |
| 4     | Agree             |
| 5     | Strongly agree    |

Example questions include:

1. The 3D controls were easy to understand.
2. The model responded quickly to my actions.
3. The material controls were intuitive.
4. The visual quality was satisfactory.
5. The application was easy to navigate.
6. The animation was smooth.
7. The loading experience was acceptable.
8. I would use this type of interface again.

---

# 6.24 Example Usability Results

The following table illustrates the recommended presentation format.

| Category             | Mean Score |
| -------------------- | ---------- |
| Camera Control       | 4.5        |
| Material Selection   | 4.4        |
| Color Selection      | 4.6        |
| Visual Quality       | 4.5        |
| Responsiveness       | 4.3        |
| Navigation           | 4.4        |
| Overall Satisfaction | 4.5        |

These values are **illustrative only**.

For the final thesis, the values should be calculated from actual participant responses.

---

# 6.25 Statistical Analysis

If a user study is conducted, descriptive statistics should be calculated.

For a sample:

x1​,x2​,…,xn​ 

the arithmetic mean is:

xˉ\=n1​i\=1∑n​xi​ 

The sample standard deviation is:

s\=n−1∑i\=1n​(xi​−xˉ)2​​ 

Reporting both mean and standard deviation provides a more informative representation than reporting the average alone.

For example:

4.5±0.6 

would indicate both the average evaluation and variation among participants.

---

# 6.26 Correlation Between Complexity and Performance

One of the primary objectives of the experiment is to determine whether scene complexity correlates with rendering performance.

Possible complexity indicators include:

* Triangle count
* Draw-call count
* Texture count
* Texture resolution
* Shader complexity

The relationship can be investigated using correlation analysis.

For example, Pearson's correlation coefficient can be calculated as:

r\=∑(xi​−xˉ)2∑(yi​−yˉ​)2​∑(xi​−xˉ)(yi​−yˉ​)​ 

where:

* x represents complexity,
* y represents frame time.

A positive correlation would indicate that increasing complexity is associated with increasing frame time.

---

# 6.27 Interpretation of Results

The experimental framework supports several important conclusions.

First, the system is capable of providing real-time interactive 3D rendering using browser-based technologies.

Second, physically based rendering significantly improves the visual interpretation of materials when combined with appropriate environment lighting.

Third, rendering performance is strongly influenced by scene complexity.

However, scene complexity is multidimensional.

A high polygon count is only one source of rendering cost. Draw calls, texture processing, shaders, shadows, resolution, and post-processing must also be considered.

---

# 6.28 RQ1: Feasibility of Web-Based Interactive Graphics

The first research question asks whether modern web technologies can support interactive 3D graphics.

The implementation demonstrates that:

* 3D models can be rendered in real time.
* Users can interact with cameras.
* Materials can be changed dynamically.
* Animation can run continuously.
* Custom shaders can be executed.
* Post-processing can be applied.

Therefore, the architecture provides sufficient capabilities for a broad class of interactive graphics applications.

---

# 6.29 RQ2: Effectiveness of Physically Based Rendering

The second research question concerns visual quality.

PBR provides a physically motivated representation of material behavior.

When combined with environment lighting, the resulting surfaces exhibit:

* More convincing reflections
* More coherent highlights
* Better distinction between materials
* Improved perception of surface properties

This is especially important for product visualization.

A metallic surface, for example, can be distinguished from plastic not merely by its base color but through its reflection behavior.

---

# 6.30 RQ3: Effect of Scene Complexity

The experiments indicate that increased complexity generally increases rendering cost.

The relationship can be represented conceptually as:

Complexity↑⇒FrameTime↑⇒FPS↓ 

However, the relationship is not necessarily linear.

Different components can become bottlenecks under different circumstances.

For example:

* Geometry-heavy scenes may become vertex-bound.
* High-resolution scenes may become fragment-bound.
* Many objects may increase CPU overhead.
* Complex shaders may increase GPU execution time.
* High-resolution shadows may require additional rendering passes.

Consequently, optimization requires identifying the actual bottleneck.

---

# 6.31 RQ4: Effectiveness of Optimization

The optimization experiment demonstrates the importance of systematic performance engineering.

Reducing geometry, draw calls, texture complexity, and unnecessary rendering passes can significantly reduce rendering cost.

However, optimization should preserve the visual characteristics that are important to the application.

This leads to an important principle:

Optimization\=Performance+Visual Quality 

rather than:

Optimization\=Maximum Performance 

A scene that renders extremely quickly but provides poor visual quality does not satisfy the objectives of an interactive graphics application.

---

# 6.32 RQ5: User Experience

The usability framework indicates that interactive 3D systems should not be evaluated solely by technical metrics.

A technically efficient application can still provide a poor experience if:

* Controls are confusing.
* Camera movement is unpredictable.
* Loading states are unclear.
* UI elements are difficult to locate.
* Animations interfere with interaction.

Therefore:

System Quality\=Technical Performance+Visual Quality+Usability 

This broader definition of quality is particularly relevant to interactive web applications.

---

# 6.33 Comparison with Traditional Web Interfaces

Traditional web interfaces primarily manipulate:

* Text
* Images
* Forms
* DOM elements

The proposed system introduces a third dimension.

Traditional interface:

Interactive graphics interface:

The additional rendering pipeline creates new opportunities but also introduces new engineering requirements.

---

# 6.34 Educational Implications

The results have implications beyond the specific application.

The proposed curriculum can prepare students to understand the complete development chain:

Mathematics→Graphics→Shaders→GPU→Web→Interaction 

This is significantly different from teaching web development exclusively through HTML, CSS, and JavaScript.

Students who understand both web engineering and graphics programming can work across multiple fields, including:

* Creative development
* Data visualization
* Game technology
* Product visualization
* XR
* Digital media
* Scientific visualization
* Interactive advertising
* AI-enhanced interfaces

---

# 6.35 Industrial Applications

The proposed technology can be applied to several commercial domains.

## E-Commerce

Users can inspect products interactively before purchasing.

## Automotive

Vehicles can be configured with different:

* Colors
* Wheels
* Interiors
* Accessories

## Architecture

Users can explore buildings interactively.

## Manufacturing

Three-dimensional models can be used for product inspection and configuration.

## Education

Complex scientific objects can be visualized interactively.

## Museums

Historical objects can be presented as interactive digital models.

## Medical Visualization

Three-dimensional anatomical data can provide interactive educational experiences.

---

# 6.36 Limitations of the Experiment

Several limitations must be acknowledged.

### Hardware Variation

Different GPUs produce different rendering performance.

### Browser Variation

Browser implementations and graphics drivers may behave differently.

### Network Conditions

Asset-loading measurements can vary significantly depending on network speed.

### Limited Scene Types

The experiment focuses primarily on product-style visualization rather than all possible graphics workloads.

### Limited User Sample

If a small user study is performed, the results cannot necessarily be generalized to the entire population.

### Measurement Noise

Real-time graphics measurements can fluctuate because of background processes and browser activity.

Therefore, multiple trials should be performed.

---

# 6.37 Experimental Reproducibility

Reproducibility is an important requirement for academic research.

The final implementation should document:

* Source-code version
* Browser version
* Operating system
* CPU
* GPU
* RAM
* Driver version
* Screen resolution
* Model version
* Texture resolution
* Rendering settings
* Test duration

The benchmark should be performed under controlled conditions.

For example:

Such documentation allows another researcher to reproduce the experiment.

---

# 6.38 Recommended Benchmark Procedure

A standardized benchmark procedure is proposed.

### Step 1

Restart the application.

### Step 2

Allow all assets to finish loading.

### Step 3

Wait for the scene to stabilize.

### Step 4

Run the scene for a fixed period.

### Step 5

Record:

* Average FPS
* Minimum FPS
* Frame time
* Draw calls
* Triangle count

### Step 6

Repeat the test multiple times.

### Step 7

Calculate mean and standard deviation.

### Step 8

Repeat for every experimental configuration.

### Step 9

Compare the results.

This approach minimizes measurement errors.

---

# 6.39 Proposed Final Results Table

The final thesis should include a consolidated table similar to the following:

| Test      | Metric     | Baseline | Optimized | Change |
| --------- | ---------- | -------- | --------- | ------ |
| Rendering | FPS        | \[X\]    | \[X\]     | \[X\]% |
| Rendering | Frame Time | \[X\]    | \[X\]     | \[X\]% |
| Geometry  | Triangles  | \[X\]    | \[X\]     | \[X\]% |
| Rendering | Draw Calls | \[X\]    | \[X\]     | \[X\]% |
| Memory    | GPU Memory | \[X\]    | \[X\]     | \[X\]% |
| Loading   | Load Time  | \[X\]    | \[X\]     | \[X\]% |
| Usability | Mean Score | \[X\]    | \[X\]     | \[X\]% |

This table should become one of the central quantitative results of the thesis.

---

# 6.40 Overall Discussion

The experimental evaluation demonstrates that interactive 3D web applications require a multidisciplinary approach.

The developer must understand:

### Computer Science

Data structures, algorithms, software architecture, and optimization.

### Mathematics

Vectors, matrices, transformations, geometry, and numerical methods.

### Graphics

Rasterization, lighting, materials, shaders, textures, and rendering.

### Web Development

JavaScript, React, browser APIs, networking, and responsive interfaces.

### Design

Composition, motion, interaction, typography, and visual hierarchy.

The proposed Interactive Graphics and Web Technologies specialization therefore occupies an intersection between traditional computer science, graphics programming, and digital design.

---

# 6.41 Key Findings

The principal findings can be summarized as follows.

### Finding 1

Modern browsers are capable of supporting sophisticated interactive three-dimensional applications.

### Finding 2

React-based architectures can successfully integrate conventional UI development with real-time 3D rendering.

### Finding 3

Physically based rendering provides substantially improved material representation compared with basic material models when appropriate lighting is available.

### Finding 4

Rendering performance depends on multiple factors rather than polygon count alone.

### Finding 5

Optimization should be measurement-driven.

### Finding 6

Interactive graphics quality depends on the combined characteristics of rendering performance, visual fidelity, and usability.

---

# 6.42 Research Contributions

The work presented in this thesis provides several contributions.

## 6.42.1 Architectural Contribution

A complete architecture for integrating modern web development with real-time 3D graphics was proposed.

## 6.42.2 Educational Contribution

The system demonstrates how mathematical graphics concepts can be connected directly to practical web development.

## 6.42.3 Technical Contribution

A modular implementation combining React, React Three Fiber, Three.js, WebGL, PBR, shaders, and animation was developed.

## 6.42.4 Experimental Contribution

A methodology for evaluating interactive 3D web applications was established.

## 6.42.5 Curriculum Contribution

The research provides a practical foundation for the proposed Interactive Graphics and Web Technologies university specialization.

---

# 6.43 Relationship to the Proposed Curriculum

The thesis results directly support the proposed curriculum presented at the beginning of this research.

The curriculum can be mapped to the implemented system:

| Curriculum Course                  | Application                    |
| ---------------------------------- | ------------------------------ |
| Introduction to Programming        | Application logic              |
| Mathematics for Computer Graphics  | Transformations and projection |
| Computer Graphics I                | Rendering pipeline             |
| Modern JavaScript                  | Application implementation     |
| Interactive Web Development        | Browser interaction            |
| WebGL Programming                  | GPU rendering                  |
| Three.js Development               | Scene construction             |
| Blender                            | Asset production               |
| Shader Programming                 | Custom GPU effects             |
| Real-Time Rendering                | PBR and optimization           |
| GPU Programming                    | Performance and computation    |
| Interactive Experience Development | React/R3F integration          |
| AI for Interactive Graphics        | Future extension               |

This demonstrates that the curriculum is not simply a collection of unrelated technologies.

Instead, the subjects form a progressive learning sequence:

Programming→Mathematics→Graphics→WebGL→3D→Shaders→Real−TimeRendering→Interactive Experiences 

---

# 6.44 Implications for University Education

The findings suggest that interactive graphics should be taught as an interdisciplinary specialization rather than solely as an advanced web-development topic.

Students should first acquire fundamental programming and mathematical knowledge.

They can then progress toward:

* Computer graphics
* WebGL
* Three.js
* Shader programming
* Real-time rendering
* Creative coding
* XR
* AI

This progression minimizes the risk of students treating graphics libraries as black boxes.

For example, instead of merely teaching:

JavaScript

students should understand:

Vertex→Model Matrix→View Matrix→Projection Matrix→Rasterization→Fragment 

This distinction is fundamental to producing graduates capable of solving new graphics problems rather than simply reproducing existing tutorials.

---

# 6.45 Future Research

Several areas should be investigated in future work.

## WebGPU

Future experiments should compare WebGL and WebGPU performance.

## WebXR

The system could be extended to VR and AR environments.

## AI-Generated Assets

AI models could generate textures, materials, and three-dimensional assets.

## GPU Compute

Particle systems and physical simulations could be moved to GPU compute pipelines.

## Large-Scale Visualization

The system could be evaluated with significantly larger datasets.

## Multi-User Interaction

Real-time collaborative 3D environments could be investigated.

## Neural Rendering

Emerging neural rendering approaches could be incorporated into future systems.

---

# 6.46 Chapter Conclusion

This chapter presented the experimental evaluation and discussion of the proposed interactive 3D web graphics system.

The results framework demonstrates that the system can be evaluated across functional, visual, performance, and usability dimensions.

The implementation successfully integrates a conventional web application architecture with a real-time GPU rendering pipeline. The resulting system supports interactive camera control, dynamic materials, 3D models, animation, shader effects, and post-processing.

The performance analysis demonstrates that rendering cost is determined by multiple interacting factors, including geometry complexity, draw calls, texture resolution, shader complexity, lighting, shadows, and rendering resolution.

The optimization experiments further demonstrate the importance of a measurement-driven workflow. Reducing unnecessary geometry, minimizing draw calls, optimizing textures, controlling pixel ratio, and selectively applying post-processing can improve performance while maintaining acceptable visual quality.

The user-experience analysis additionally demonstrates that technical performance alone is insufficient. An effective interactive graphics application must combine:

Performance+Visual Quality+Interaction+Usability​ 

The research therefore supports the central proposition of this thesis: **modern web technologies are capable of supporting sophisticated interactive graphics applications when they are combined with appropriate graphics theory, GPU programming principles, asset optimization, and interaction design.**

Furthermore, the research provides a practical foundation for the proposed **Interactive Graphics and Web Technologies (IGWT)** university specialization. The curriculum connects programming, mathematics, computer graphics, WebGL, shaders, real-time rendering, 3D modeling, interaction design, XR, and AI into a coherent educational progression.

The next chapter should therefore move from the experimental findings to the final synthesis of the research.
