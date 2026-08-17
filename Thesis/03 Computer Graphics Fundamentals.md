Source: [ChatGPT — Curriculum Design Advice](https://chatgpt.com/share/6a7fa45a-d4c0-83eb-b5c4-121a78bda55e)

---

# Chapter 3

# Computer Graphics Fundamentals

## Part 1: Mathematical Foundations

---

# 3.1 Introduction

Computer graphics is fundamentally built upon mathematics. Every object rendered on a computer screen is represented numerically and manipulated using mathematical operations. Whether rotating a camera, animating a character, simulating physics, or rendering realistic lighting, graphics systems rely heavily on vectors, matrices, coordinate systems, and linear algebra.

Modern graphics APIs such as OpenGL, WebGL, Vulkan, Direct3D, and WebGPU all employ similar mathematical foundations. Even high-level libraries such as Three.js internally perform matrix multiplications, coordinate transformations, and vector calculations before issuing rendering commands to the GPU.

Therefore, understanding the mathematical principles behind computer graphics is essential for developing efficient and visually accurate real-time applications.

This chapter introduces the mathematical concepts that serve as the theoretical foundation for the implementation described later in this thesis.

---

# 3.2 Mathematical Representation of Graphics

A computer has no understanding of concepts such as "cube," "camera," or "light." Instead, every graphical object is represented using numerical data.

For example, a cube is represented by:

* Vertex positions
* Surface normals
* Texture coordinates
* Triangle indices
* Material properties

A single vertex may be stored as

P\=(x,y,z) 

where

* x represents horizontal position,
* y represents vertical position,
* z represents depth.

A cube therefore consists of multiple vertices connected into triangles.

During rendering, the GPU performs millions of mathematical calculations every second to transform these vertices from their local positions into pixels displayed on the monitor. Modern graphics pipelines rely on matrix transformations and coordinate-space conversions to accomplish this efficiently. VTK Book+1

---

# 3.3 Vectors

## 3.3.1 Definition

A vector represents both **magnitude** and **direction**.

Unlike a point, which specifies a location, a vector describes movement or displacement between locations. Understanding this distinction is important because graphics systems treat points and vectors differently during transformations. UW Graphics+1

A two-dimensional vector is written as

v\=(x,y) 

while a three-dimensional vector is written as

v\=(x,y,z) 

Example

v\=(3,4,2) 

This indicates movement

* 3 units along the X-axis
* 4 units along the Y-axis
* 2 units along the Z-axis

Vectors are used extensively in graphics for:

* Object movement
* Camera direction
* Surface normals
* Light direction
* Physics simulations
* Animation
* Reflection calculations

---

## 3.3.2 Vector Length

The magnitude (or length) of a vector is

∣v∣\=x2+y2+z2​ 

Example

v\=(3,4,0) 

Then

∣v∣\=32+42​\=5 

The length determines how far the vector extends through space.

---

## 3.3.3 Unit Vector

Many graphics calculations require vectors that represent only direction.

These are called **unit vectors**.

A unit vector has

∣v∣\=1 

Normalization is computed by dividing each component by the vector length.

v^\=∣v∣v​ 

Example

Original

(3,4,0) 

Length

5 

Normalized

(0.6,0.8,0) 

Lighting calculations almost always use normalized vectors because illumination depends on direction rather than distance. Chortle+1

---

## 3.3.4 Vector Addition

Vectors can be added.

a+b\=(ax​+bx​,ay​+by​,az​+bz​) 

Example

(2,1,5)+(4,2,1)\=(6,3,6) 

Applications include:

* Character movement
* Camera motion
* Physics
* Animation blending

---

## 3.3.5 Scalar Multiplication

A scalar changes vector magnitude.

kv\=(kx,ky,kz) 

Example

2(3,2,1)\=(6,4,2) 

Scaling vectors is commonly used for:

* Velocity
* Camera zoom
* Object scaling
* Physics simulations

---

## 3.3.6 Dot Product

The dot product measures the similarity between two vectors.

a⋅b\=ax​bx​+ay​by​+az​bz​ 

Alternatively,

a⋅b\=∣a∣∣b∣cosθ 

where

θ

is the angle between the vectors.

Interpretation

* Positive → same direction
* Zero → perpendicular
* Negative → opposite directions

Applications include:

* Diffuse lighting
* Back-face culling
* Surface orientation
* Visibility tests

For example, Lambertian diffuse shading computes light intensity using the dot product between the surface normal and the light direction. Oberlin College Computer Science+1

---

## 3.3.7 Cross Product

The cross product exists only in three dimensions.

a×b\=c 

Its result

* is perpendicular to both vectors,
* follows the right-hand rule,
* has magnitude
∣a∣∣b∣sinθ 

Applications include:

* Computing surface normals
* Camera orientation
* Physics
* Reflection
* Mesh generation

Nearly every 3D rendering engine uses cross products to calculate normal vectors required for lighting.

---

# 3.4 Matrices

## 3.4.1 Introduction

Matrices are rectangular arrays of numbers used to transform vectors and points.

Unlike vectors, matrices can simultaneously perform:

* Translation
* Rotation
* Scaling
* Projection
* Reflection
* Shearing

Graphics hardware is optimized for matrix multiplication, making matrices the standard representation for geometric transformations. HWS Mathematics and Computer Science+1

---

## 3.4.2 Matrix Representation

A matrix is commonly written as

A\=​a11​a21​a31​​a12​a22​a32​​a13​a23​a33​​​ 

Most graphics APIs use **4 × 4 matrices** because they support homogeneous coordinates, allowing translation, rotation, scaling, and projection to be represented within a single transformation framework. Flylib+1

---

## 3.4.3 Matrix Multiplication

Matrix multiplication combines transformations.

Suppose

Rotation

↓

Scaling

↓

Translation

Instead of executing each separately, they are combined into one transformation matrix.

This greatly improves GPU efficiency.

One important property is that matrix multiplication is **not commutative**:

AB\=BA 

Therefore, the order of transformations matters.

For example,

Scale

↓

Rotate

↓

Translate

produces a different result from

Translate

↓

Rotate

↓

Scale

Understanding transformation order is one of the most important skills in graphics programming.

---

# 3.5 Coordinate Systems

Coordinate systems define where objects exist and how they are interpreted by the rendering pipeline.

A point's numerical coordinates have meaning only with respect to a chosen coordinate frame. Computer graphics therefore uses multiple coordinate systems, each serving a specific purpose in the rendering process. ScienceDirect+1

Modern graphics systems generally employ several coordinate spaces.

---

## 3.5.1 Object (Model) Space

Every object begins in its own local coordinate system.

Example

A chair

Origin

(0,0,0) 

may be positioned at its geometric center.

This coordinate system is independent of the rest of the scene.

---

## 3.5.2 World Space

Objects are transformed into a shared coordinate system known as world space.

Example

Chair

(5,0,−2) 

Table

(−3,0,8) 

Lamp

(1,4,−5) 

All scene objects coexist in this global reference frame.

---

## 3.5.3 View (Camera) Space

The camera observes the scene.

The rendering engine transforms world coordinates into coordinates relative to the camera position and orientation.

From the camera's perspective, the camera itself is always located at the origin while the world moves relative to it. VTK Book+1

---

## 3.5.4 Clip Space

Perspective projection converts the visible scene into a normalized viewing volume.

Vertices outside this volume are clipped before rasterization.

---

## 3.5.5 Screen Space

Finally,

Clip Space

↓

Viewport Transformation

↓

Screen Space

Coordinates become pixel positions displayed on the monitor.

The complete transformation pipeline is therefore:

This sequence is fundamental to all modern graphics APIs, including WebGL and Three.js. VTK Book+1

---

# 3.6 Chapter Summary (Part 1)

This first part of Chapter 3 introduced the mathematical foundations required for computer graphics. It distinguished between points and vectors, explained vector operations such as normalization, dot products, and cross products, and demonstrated the role of matrices in geometric transformations. The chapter also introduced the hierarchy of coordinate systems—object, world, view, clip, and screen space—that underpins the modern rendering pipeline.

---

## Part 2: Transformations, Camera Systems, and Projection

---

# 3.7 Geometric Transformations

After defining an object in its local coordinate system, it must be positioned within the virtual scene. This process is achieved through **geometric transformations**, which modify the position, orientation, and size of graphical objects while preserving their geometric relationships.

Geometric transformations form one of the most fundamental operations in computer graphics. Every visible object in a three-dimensional scene undergoes a sequence of transformations before it is displayed on the screen. Modern graphics APIs such as WebGL, OpenGL, Vulkan, and Direct3D implement these operations primarily through matrix multiplication, allowing the GPU to process millions of vertices efficiently in parallel.

The three basic transformations are:

* Translation
* Rotation
* Scaling

More advanced transformations include reflection, shearing, and projection, although these are used less frequently in interactive graphics applications.

---

# 3.7.1 Translation

Translation moves an object from one location to another without changing its orientation or dimensions.

If an object is translated by the vector

T\=(tx​,ty​,tz​) 

every vertex is displaced by the same amount.

For a point

P\=(x,y,z) 

the translated position becomes

P′\=(x+tx​,y+ty​,z+tz​) 

Translation is used extensively in applications such as:

* Character movement
* Camera movement
* Object placement
* Animation
* Physics simulations

In Three.js, translation can be applied directly through an object's position properties.

JavaScript

Internally, the engine converts this operation into a transformation matrix before sending it to the GPU.

---

# 3.7.2 Scaling

Scaling changes the size of an object.

Uniform scaling enlarges or reduces an object equally along all axes.

Non-uniform scaling allows each axis to be modified independently.

Given

S\=(sx​,sy​,sz​) 

the transformed point becomes

P′\=(xsx​,ysy​,zsz​) 

Applications include:

* Object resizing
* Character growth
* Interface animation
* Level-of-detail adjustments

Improper scaling can distort object proportions and alter lighting calculations if surface normals are not updated correctly.

---

# 3.7.3 Rotation

Rotation changes an object's orientation around one or more axes.

Three-dimensional graphics generally support rotation about:

* X-axis
* Y-axis
* Z-axis

Rotation matrices preserve distances between vertices while changing their orientation.

For example,

rotation around the Y-axis is represented mathematically as

Ry​(θ)\=​cosθ0−sinθ​010​sinθ0cosθ​​ 

Rotations are fundamental for:

* Camera control
* Character animation
* Vehicle steering
* Planetary motion
* Interactive product visualization

Three.js stores rotations internally using Euler angles but also supports quaternions for smoother interpolation and to avoid gimbal lock.

---

# 3.7.4 Transformation Order

One of the most common mistakes made by beginner graphics programmers is assuming that transformations may be applied in any order.

Matrix multiplication is **not commutative**.

Therefore,

produces a different result from

For example,

scaling before translation enlarges the object around its local origin.

Translating before scaling enlarges the translation distance itself.

Most graphics engines apply transformations in the following order:

1. Scaling
2. Rotation
3. Translation

This sequence preserves intuitive object manipulation.

---

# 3.8 Homogeneous Coordinates

Translation cannot be represented using a standard 3×3 matrix alone. To overcome this limitation, modern graphics systems use **homogeneous coordinates**.

Instead of representing a point as

(x,y,z) 

it becomes

(x,y,z,1) 

Vectors use

(x,y,z,0) 

This additional component allows translation, scaling, rotation, and projection to be combined into a single 4×4 transformation matrix.

Homogeneous coordinates are used throughout OpenGL, WebGL, Direct3D, Vulkan, and WebGPU.

---

# 3.9 Model, View, and Projection Matrices

The rendering pipeline transforms every vertex through three primary matrices:

## Model Matrix

Transforms local object coordinates into world coordinates.

Responsible for:

* Translation
* Rotation
* Scaling

Each object has its own model matrix.

---

## View Matrix

Represents the position and orientation of the camera.

Rather than moving the camera itself, graphics systems transform the entire world relative to the camera.

Consequently,

the camera always remains at

(0,0,0) 

in view space.

---

## Projection Matrix

Converts three-dimensional coordinates into a two-dimensional viewing volume suitable for rasterization.

This matrix determines:

* Perspective
* Viewing angle
* Aspect ratio
* Near clipping plane
* Far clipping plane

The combined transformation is

P\=Projection×View×Model 

commonly abbreviated as the **MVP matrix**.

This is one of the most important equations in computer graphics.

---

# 3.10 Camera Systems

A camera determines how the virtual world is viewed.

Unlike physical cameras, virtual cameras are mathematical constructs consisting of:

* Position
* Viewing direction
* Up vector
* Projection parameters

Modern rendering engines generally provide two projection models.

---

## 3.10.1 Perspective Camera

Perspective projection imitates human vision.

Objects farther from the camera appear smaller.

Characteristics include:

* Depth perception
* Realistic appearance
* Vanishing points
* Suitable for games and visualization

Perspective projection is used by most interactive 3D applications because it resembles natural vision.

Three.js provides the `PerspectiveCamera` class for this purpose.

---

## 3.10.2 Orthographic Camera

Orthographic projection removes perspective distortion.

Objects remain the same size regardless of distance.

Advantages include:

* Engineering drawings
* CAD systems
* Architectural plans
* Scientific visualization
* User interfaces

Unlike perspective projection,

parallel lines remain parallel.

---

# 3.11 Viewing Frustum

A perspective camera observes only a limited region of space known as the **viewing frustum**.

The frustum resembles a truncated pyramid.

Its boundaries consist of:

* Left
* Right
* Top
* Bottom
* Near Plane
* Far Plane

Objects outside the viewing frustum are discarded before rasterization.

This optimization is called **frustum culling** and significantly reduces GPU workload.

---

# 3.12 Projection

Projection converts three-dimensional geometry into two-dimensional screen coordinates.

Two projection methods dominate computer graphics.

### Perspective Projection

Advantages

* Realistic
* Natural depth perception
* Immersive

Disadvantages

* Objects shrink with distance.

---

### Orthographic Projection

Advantages

* Accurate measurements
* Engineering visualization
* Technical illustration

Disadvantages

* Reduced realism.

The choice depends upon application requirements.

---

# 3.13 Clipping

Not every object within a scene should be rendered.

Objects:

* behind the camera,
* outside the frustum,
* beyond the far plane,

are removed before rasterization.

This process is called **clipping**.

Benefits include:

* Reduced GPU workload
* Faster rendering
* Improved frame rate

Modern GPUs perform clipping automatically during the rendering pipeline.

---

# 3.14 Viewport Transformation

After clipping,

coordinates are transformed into

**Normalized Device Coordinates (NDC)**

where

x,y,z∈\[−1,+1\] 

The viewport transformation converts NDC into pixel coordinates on the display.

For example,

an NDC point

(−1,−1) 

maps to the lower-left corner of the viewport,

while

(1,1) 

maps to the upper-right corner.

This transformation allows the rendered image to fit displays of different resolutions while preserving the chosen aspect ratio.

---

# 3.15 Practical Application in Three.js

Three.js encapsulates these mathematical concepts through a concise application programming interface.

A typical scene includes:

* Scene
* PerspectiveCamera
* Mesh
* Renderer

Example:

JavaScript

Although the developer interacts with only a few lines of code, the graphics engine internally performs the complete sequence of model, view, and projection transformations before the GPU executes the rendering pipeline.

---

# 3.16 Chapter Summary (Part 2)

This part introduced the geometric transformations that position, orient, and scale objects within a virtual scene. It explained homogeneous coordinates, the Model–View–Projection (MVP) transformation, camera models, projection techniques, viewing frustums, clipping, and viewport transformation. Together, these concepts describe how three-dimensional geometry is mathematically converted into a two-dimensional image suitable for display.

These topics provide the essential bridge between mathematical representations and practical graphics programming. In **Part 3**, the chapter will examine **lighting models, rasterization, texture mapping, material systems, and the modern GPU rendering pipeline**, completing the theoretical foundation required for the implementation chapters of this thesis.

---

### Review

---

## Part 3A: Lighting Fundamentals, Reflection Models, Rasterization, and Texture Mapping

---

# 3.17 Lighting Fundamentals

## 3.17.1 Introduction

Lighting is one of the most important components of computer graphics. Without lighting, three-dimensional objects appear flat and lack depth, making it difficult for users to perceive shape, orientation, or material properties.

In the physical world, objects become visible because light emitted from a source interacts with their surfaces and is reflected toward the human eye. Computer graphics simulates this process mathematically. The objective of lighting algorithms is not necessarily to reproduce physics perfectly, but to generate visually convincing images while maintaining interactive performance.

Modern real-time graphics applications, including those built with Three.js and WebGL, perform lighting calculations for millions of fragments every second. These calculations determine the final color of each pixel by considering the interaction between light sources, surface materials, and camera position. Grainger Courses+1

---

## 3.17.2 Components of Light

A virtual lighting system generally consists of three primary elements:

* Light source
* Surface
* Observer (camera)

The interaction among these components determines the appearance of an object.

Figure 3.17 illustrates this concept.

**Figure 3.17** Basic interaction between light, surface, and camera.

The rendering equation used in physically based rendering is considerably more complex, but most real-time applications approximate this interaction using simplified illumination models.

---

## 3.17.3 Types of Light Sources

Modern rendering engines support several categories of light sources.

### Ambient Light

Ambient light represents indirect illumination that appears to originate from every direction.

Characteristics include:

* Uniform intensity
* No direction
* No shadows
* Low computational cost

Although ambient lighting is not physically accurate, it prevents completely black surfaces and improves overall scene visibility. Grainger Courses+1

---

### Directional Light

Directional lights simulate distant light sources such as the sun.

Properties include:

* Parallel light rays
* Infinite distance
* Constant direction
* Suitable for outdoor scenes

Examples include:

* Sunlight
* Moonlight

---

### Point Light

Point lights emit light equally in every direction.

Their intensity decreases with distance according to an attenuation function.

Examples include:

* Light bulbs
* Candles
* Lamps

Point lights are widely used in indoor visualization.

---

### Spot Light

Spot lights illuminate a limited cone.

They are commonly used for:

* Flashlights
* Stage lighting
* Vehicle headlights
* Museum displays

Because the illumination is directional, spot lights provide strong visual emphasis.

---

### Environment Light

Modern physically based rendering often employs environment lighting using High Dynamic Range (HDR) images.

Instead of defining individual light sources, the surrounding environment provides illumination from all directions.

Advantages include:

* Realistic reflections
* Soft global illumination
* Improved material realism

Environment lighting has become standard in commercial product visualization systems.

---

# 3.18 Reflection Models

## 3.18.1 Introduction

When light reaches a surface, it is reflected toward the observer.

Different materials reflect light differently.

For example,

* Wood scatters light.
* Glass reflects and refracts light.
* Metal produces strong specular highlights.
* Plastic exhibits both diffuse and specular reflection.

Reflection models mathematically approximate these behaviors.

---

## 3.18.2 Ambient Reflection

The simplest reflection component is ambient reflection.

Its illumination is assumed constant across the entire object.

The ambient intensity is

Iambient​\=ka​La​ 

where

* ka​ \= ambient reflection coefficient
* La​ \= ambient light intensity

Ambient reflection ignores light direction and shadows.

Although physically unrealistic, it provides a useful approximation for indirect illumination.

---

## 3.18.3 Lambert Diffuse Reflection

Diffuse reflection models rough surfaces.

According to Lambert's cosine law,

brightness depends on the angle between the surface normal and the incoming light.

The diffuse component is

Id​\=kd​Lmax(0,N⋅L) 

where

* N \= normalized surface normal
* L \= normalized light direction

If

N⋅L\=1 

the surface directly faces the light and appears brightest.

If

N⋅L\=0 

the surface receives no direct illumination.

Lambertian reflection remains one of the most widely used lighting models because of its simplicity and physical basis. Grainger Courses+1

---

## 3.18.4 Phong Reflection Model

The Phong reflection model extends Lambertian shading by introducing specular highlights.

It consists of three components:

* Ambient
* Diffuse
* Specular

The complete equation is

I\=Ia​+Id​+Is​ 

The specular term is

Is​\=ks​(R⋅V)n 

where

* R \= reflection vector
* V \= viewing direction
* n \= shininess exponent

Higher values of

n 

produce smaller and sharper highlights.

Although Phong illumination is empirical rather than physically based, it became the standard real-time lighting model for many years because it offers a good balance between image quality and computational efficiency. Wikipedia+1

---

## 3.18.5 Blinn–Phong Reflection

Blinn proposed a more efficient alternative.

Instead of computing the reflection vector,

Blinn introduced the half-vector

H\=∣L+V∣L+V​ 

The specular intensity becomes

Is​\=(N⋅H)n 

Advantages include:

* Faster computation
* Better numerical stability
* Reduced GPU workload

For many years Blinn–Phong became the default lighting model in real-time graphics engines before the widespread adoption of physically based rendering. Grainger Courses+1

---

# 3.19 Rasterization

## 3.19.1 Introduction

After geometric transformations have positioned objects within the scene, the rendering system must determine which pixels belong to each object.

This process is known as **rasterization**.

Rasterization converts geometric primitives, typically triangles, into fragments that correspond to individual screen pixels.

Modern GPUs perform rasterization entirely in hardware, enabling billions of fragments to be processed each second.

---

## 3.19.2 Why Triangles?

Although objects may appear smooth, nearly all real-time graphics systems represent surfaces using triangles.

Triangles possess several desirable properties:

* Always planar
* Computationally efficient
* Simple interpolation
* Hardware friendly

Complex objects are therefore approximated by triangle meshes.

A detailed automobile model may contain several hundred thousand triangles.

---

## 3.19.3 Rasterization Process

The rasterization stage performs the following operations:

Each triangle is converted into a collection of fragments.

Each fragment stores information such as

* Position
* Depth
* Surface normal
* Texture coordinates
* Material properties

These fragments are then processed by the fragment shader.

The rasterization pipeline is optimized for speed and remains the dominant approach for interactive graphics despite the emergence of hardware-accelerated ray tracing. Stanford University+1

---

## 3.19.4 Depth Buffer

When multiple objects overlap,

the renderer must determine which surface is visible.

This is accomplished using the **depth buffer** (Z-buffer).

Each fragment stores its depth.

Before writing a pixel,

the GPU compares the fragment's depth against the stored value.

Only the nearest fragment remains visible.

Advantages include:

* Correct visibility
* Automatic hidden surface removal
* Efficient implementation

Depth buffering is performed automatically by modern graphics hardware.

---

# 3.20 Texture Mapping

## 3.20.1 Introduction

Geometry alone cannot realistically represent complex surface detail.

Instead,

images called **textures** are mapped onto object surfaces.

Texture mapping dramatically improves realism without increasing polygon count.

Examples include:

* Wood grain
* Fabric
* Brick walls
* Metal scratches
* Leather
* Painted surfaces

Texture mapping has become an essential technique in modern graphics applications. O'Reilly Media+1

---

## 3.20.2 UV Coordinates

Textures are applied using **UV coordinates**.

Unlike spatial coordinates

(x,y,z) 

texture coordinates are represented as

(u,v) 

where

* u represents horizontal texture position
* v represents vertical texture position

Every vertex stores its corresponding UV coordinates.

During rasterization,

these coordinates are interpolated across the triangle,

allowing the GPU to determine which texel should be sampled for each fragment. Wikipedia+1

---

## 3.20.3 Texture Sampling

The fragment shader retrieves color values from texture memory.

This operation is known as **texture sampling**.

Several sampling methods are available:

* Nearest Neighbor
* Bilinear Filtering
* Trilinear Filtering
* Anisotropic Filtering

Higher-quality filters produce smoother images but require additional computation.

Most modern graphics engines employ trilinear filtering together with anisotropic filtering to improve image quality at oblique viewing angles. O'Reilly Media

---

## 3.20.4 Mipmapping

When distant objects use high-resolution textures,

aliasing may occur.

Mipmapping solves this problem by storing multiple precomputed resolutions of the same texture.

During rendering,

the GPU automatically selects the most appropriate resolution.

Benefits include:

* Reduced aliasing
* Improved performance
* Better cache efficiency

Mipmapping is widely supported in WebGL and Three.js.

---

## 3.20.5 Types of Texture Maps

Modern physically based rendering typically uses several specialized texture maps.

| Texture Type      | Purpose                    |
| ----------------- | -------------------------- |
| Base Color        | Surface color              |
| Normal Map        | Small-scale surface detail |
| Roughness Map     | Surface roughness          |
| Metalness Map     | Metallic properties        |
| Ambient Occlusion | Indirect shadowing         |
| Emissive Map      | Self-illumination          |
| Height Map        | Surface displacement       |

Using multiple texture maps enables visually rich materials without requiring additional geometric complexity. Wikipedia+1

---

# 3.21 Chapter Summary (Part 3A)

This section examined the image formation stage of the graphics pipeline. It introduced the principles of virtual lighting, common light source types, and classical reflection models, including Lambertian, Phong, and Blinn–Phong illumination. The discussion then described rasterization, depth buffering, and texture mapping, illustrating how modern GPUs convert geometric models into shaded images.

---

## Part 3B-1: Material Systems and the Modern GPU Rendering Pipeline

---

# 3.21 Material Systems

## 3.21.1 Introduction

Geometry describes the **shape** of an object, while materials describe how that object appears when illuminated.

A three-dimensional model without an appropriate material may contain millions of accurately positioned vertices and still appear visually unrealistic. A material determines properties such as surface color, reflectivity, roughness, transparency, and emission. In modern real-time rendering, these properties are generally supplied to shaders, which use them together with lighting information to calculate the final appearance of each visible fragment.

Three.js provides several material models ranging from simple unlit materials to physically based materials. The increasing complexity of these models generally provides greater visual realism at the cost of additional computation. Three.js+1

For the product configurator developed in this thesis, material representation is particularly important because users must be able to change the appearance of products without replacing the underlying geometry.

---

## 3.21.2 Material Properties

A material can be considered a collection of parameters that describe the interaction between a surface and light.

Common parameters include:

* Base color
* Metalness
* Roughness
* Normal information
* Ambient occlusion
* Emission
* Transparency
* Transmission
* Clearcoat

A simplified material representation can therefore be expressed as

M\=(Cb​,M,R,N,A,E,T) 

where:

* Cb​ \= base color
* M \= metalness
* R \= roughness
* N \= normal information
* A \= ambient occlusion
* E \= emission
* T \= transmission

The rendering system combines these parameters with geometric and lighting information to calculate the final fragment color.

---

## 3.21.3 Unlit Materials

The simplest material model does not perform lighting calculations.

In Three.js, `MeshBasicMaterial` is an example of an unlit material. Its appearance is not affected by scene lights. Three.js

This type of material is useful for:

* UI elements
* Debugging
* Background objects
* Emissive-looking surfaces
* Performance-sensitive scenes

A simplified fragment calculation can be expressed as

Cout​\=Cbase​ 

where the output depends primarily on the supplied material color and texture.

The advantage is low computational cost. The disadvantage is that the material does not provide natural interaction with the lighting environment.

---

## 3.21.4 Lambert and Phong Materials

Lambertian and Phong-based materials provide progressively more sophisticated lighting.

A Lambert material primarily models diffuse reflection.

A Phong material adds a specular component and therefore produces visible highlights.

Three.js documentation describes `MeshLambertMaterial` as performing lighting at the vertex level, while `MeshPhongMaterial` performs lighting per pixel. Three.js

These materials remain useful for:

* Stylized graphics
* Simple visualization
* Educational demonstrations
* Applications where physically based rendering is unnecessary

However, they are less appropriate for the product configurator developed in this thesis because realistic product visualization requires material parameters that correspond more closely to physical surface behavior.

---

# 3.21.5 Physically Based Materials

Physically based rendering introduced a different material philosophy.

Instead of directly specifying parameters such as "shininess," a PBR material describes properties that correspond more closely to the physical characteristics of a surface.

Two important parameters are:

roughness 

and

metalness 

Three.js's `MeshStandardMaterial` implements a metallic-roughness PBR workflow. The documentation identifies it as a standard physically based material and notes that it uses per-fragment shading. Three.js

---

## 3.21.6 Roughness

Roughness describes the microscopic irregularity of a surface.

A low roughness value produces relatively sharp reflections.

A high roughness value produces broad, diffuse reflections.

Conceptually:

versus:

In Three.js, roughness ranges from 0 to 1, with lower values producing smoother, more reflective surfaces and higher values producing rougher surfaces. Three.js+1

Examples include:

| Material       | Approximate Character |
| -------------- | --------------------- |
| Polished metal | Low roughness         |
| Glass          | Low roughness         |
| Plastic        | Medium roughness      |
| Wood           | Medium/high roughness |
| Concrete       | High roughness        |
| Fabric         | High roughness        |

The values used in an actual application depend on the specific material and authoring workflow.

---

# 3.21.7 Metalness

Metalness determines whether a surface behaves approximately as a conductor or non-metal.

A value near

0 

represents a non-metallic material.

A value near

1 

represents a metallic material.

Three.js describes the parameter in the same manner: non-metals such as wood or stone generally use values near zero, while metallic surfaces use values near one. Three.js

Examples of non-metals include:

* Wood
* Plastic
* Rubber
* Ceramic
* Stone

Examples of metals include:

* Aluminum
* Copper
* Steel
* Gold

An important consequence is that metalness should not simply be treated as an artistic "shininess" slider. It represents a fundamentally different category of light–surface interaction.

---

# 3.21.8 Texture-Based Material Properties

Material properties can be stored as textures rather than single numerical values.

For example:

R(u,v) 

can represent roughness at each surface location.

Similarly,

M(u,v) 

can represent metalness.

This enables a single object to contain different materials.

For example, a car model might contain:

* Metallic body panels
* Rubber tires
* Glass windows
* Plastic interior components
* Leather seats

A product configurator can therefore modify these properties dynamically without replacing the complete 3D model.

Three.js's `MeshStandardMaterial` supports maps for properties including base color, roughness, metalness, normal information, ambient occlusion, emissive properties, and displacement. Three.js

---

# 3.21.9 Normal Mapping

Increasing geometric detail is expensive.

Instead of adding millions of polygons to represent small surface irregularities, normal maps can modify the surface normal used during lighting calculations.

A normal map does **not** normally change the actual geometry. Instead, it changes the normal used for shading, creating the visual impression of additional detail. Three.js explicitly distinguishes normal mapping from displacement mapping in this respect. Three.js

For example, a flat wall can use a normal map to simulate:

* Brick
* Scratches
* Fabric
* Concrete
* Fine grooves

This technique provides significant visual detail without a corresponding increase in geometric complexity.

---

# 3.21.10 Displacement Mapping

Displacement mapping differs from normal mapping because it modifies actual vertex positions.

Conceptually,

P′\=P+hN 

where

* P \= original vertex position
* h \= sampled displacement value
* N \= surface normal

Unlike normal mapping, displaced geometry can affect silhouettes and can participate in geometric interactions such as casting shadows.

Three.js documentation notes this distinction explicitly: displacement modifies vertices, whereas normal and bump maps primarily modify lighting behavior. Three.js

The disadvantage is that sufficient geometric density is required to represent the displacement accurately.

---

# 3.21.11 Material Selection for the Proposed System

The proposed product configurator primarily uses physically based materials.

The basic architecture is:

This architecture separates the physical description of a surface from the geometry itself.

As a result, changing the color or material of a product does not require rebuilding its mesh.

---

# 3.22 The Modern GPU Rendering Pipeline

## 3.22.1 Introduction

The GPU rendering pipeline transforms numerical descriptions of geometry into the pixels displayed on a screen.

Although modern APIs expose different interfaces, the fundamental stages remain conceptually similar.

WebGL 2 is based closely on OpenGL ES 3.0 and exposes programmable GPU rendering functionality within the HTML canvas environment. Khronos Registry+1

A simplified rendering pipeline can be represented as:

The precise implementation contains additional stages and hardware-specific mechanisms, but this conceptual model is sufficient for understanding the architecture used in this thesis.

---

# 3.22.2 Vertex Specification

Before rendering can occur, the application must provide the GPU with vertex data.

A vertex can contain multiple attributes:

V\=(P,N,UV,C,…) 

where:

* P \= position
* N \= normal
* UV \= texture coordinates
* C \= optional color

The vertex data is stored in GPU-accessible buffers.

OpenGL's rendering model includes vertex specification followed by vertex processing, primitive assembly, rasterization, fragment processing, and subsequent per-sample operations. Khronos Wikis

---

# 3.22.3 Vertex Shader

The vertex shader is a programmable GPU stage that processes individual vertices.

Its most important responsibility in a conventional rasterization pipeline is transforming vertex positions into clip space.

A simplified transformation is:

Pclip​\=Pprojection​Pview​Pmodel​Plocal​ 

or

Pclip​\=MVPPlocal​ 

The vertex shader may also transform or prepare:

* Normals
* Texture coordinates
* Tangent vectors
* Colors
* Custom attributes

An illustrative GLSL vertex shader is:

glsl

The actual shaders generated by a high-level engine can be substantially more complex, particularly when lighting, skinning, morph targets, shadows, and other features are enabled.

---

# 3.22.4 Primitive Assembly

After vertex processing, vertices are assembled into geometric primitives.

The most common primitive for 3D rendering is the triangle.

For example:

Three vertices form one triangle.

Complex models are therefore represented as collections of triangles.

---

# 3.22.5 Rasterization

The rasterizer determines which screen locations are covered by each primitive.

For a triangle, the GPU identifies the pixels or sample locations inside its projected area.

It then interpolates vertex attributes across the triangle.

For example, if each vertex has a different texture coordinate, the rasterizer generates intermediate texture coordinates for each fragment.

This interpolation is essential for smooth shading and texture mapping.

---

# 3.22.6 Fragment Generation

Rasterization produces **fragments**, not necessarily final pixels.

A fragment contains information needed for subsequent processing, such as:

* Screen position
* Depth
* Interpolated attributes

The fragment shader then processes this information.

The distinction is important because multiple fragments may compete to write to the same screen pixel. Depth testing, blending, and other operations determine which values ultimately contribute to the framebuffer. Khronos Wikis

---

# 3.22.7 Fragment Shader

The fragment shader determines the color and, where applicable, depth information for a generated fragment.

A simplified fragment shader might be:

glsl

This produces a red output.

A realistic PBR fragment shader is considerably more complex.

It may perform:

1. Texture sampling
2. Normal reconstruction
3. Light evaluation
4. BRDF evaluation
5. Environment sampling
6. Ambient occlusion
7. Emission
8. Tone mapping preparation

The fragment shader is therefore one of the most computationally significant parts of a modern rendering system.

---

# 3.22.8 Depth Testing

When several objects overlap, the GPU must determine which surface is closest to the camera.

The depth buffer stores a depth value for previously processed fragments.

Conceptually:

If Object A is closer than Object B, its fragment should normally remain visible.

The depth test performs this comparison automatically.

This mechanism allows scenes containing many overlapping objects to be rendered correctly without requiring the application to manually sort every triangle.

---

# 3.22.9 Stencil Testing

The stencil buffer provides an additional mechanism for controlling where rendering is permitted.

Stencil operations can be used for:

* Mirrors
* Portals
* Outlines
* Masks
* Selective rendering

Although stencil operations are not central to the product configurator developed in this thesis, they are important for advanced interactive graphics.

---

# 3.22.10 Blending

Blending combines a newly generated fragment with the existing framebuffer value.

For transparent objects, the output may be represented conceptually as

Cout​\=Csrc​α+Cdst​(1−α) 

where:

* Csrc​ \= source color
* Cdst​ \= destination color
* α \= source opacity

This operation enables effects such as:

* Glass
* Smoke
* UI overlays
* Transparent plastics
* Particle effects

Transparency is more complicated than opaque rendering because the correct visual result may depend on drawing order and depth behavior.

---

# 3.22.11 Framebuffers

The final result of a rendering pass is stored in a framebuffer.

The default framebuffer represents the visible rendering surface associated with the canvas.

WebGL 2 also supports framebuffer objects that can be configured with texture and renderbuffer attachments. Khronos Registry

This capability is fundamental to advanced rendering techniques.

For example:

Framebuffer-based rendering enables:

* Bloom
* Depth-of-field
* Screen-space effects
* Blur
* Color grading
* Deferred rendering
* Shadow maps
* GPGPU techniques

These techniques become particularly important in the later chapters of this thesis.

---

# 3.22.12 GPU Parallelism

The fundamental advantage of GPUs is massive parallelism.

A CPU is optimized for relatively small numbers of powerful, general-purpose processing cores.

A GPU is designed to execute large numbers of similar operations simultaneously.

This makes GPUs particularly effective for graphics workloads where thousands or millions of vertices and fragments require similar calculations.

For example, a scene containing:

1,000,000 

fragments may require essentially the same shader computation for each fragment.

The GPU can execute these calculations concurrently through its architecture.

This parallel nature explains why shader programming is so important in real-time graphics.

---

# 3.22.13 CPU–GPU Interaction

A web-based graphics application generally involves cooperation between the CPU and GPU.

A simplified architecture is:

The CPU manages:

* Application logic
* User interaction
* Scene updates
* Resource management
* Rendering commands

The GPU performs:

* Vertex processing
* Rasterization
* Fragment shading
* Texture sampling
* Parallel numerical computation

A major performance objective is therefore to minimize unnecessary CPU–GPU synchronization and expensive rendering work.

---

# 3.22.14 Rendering Cost

The cost of a frame can be broadly understood as a combination of CPU and GPU work:

Tframe​\=TCPU​+TGPU​+Tsync​ 

where:

* TCPU​ \= CPU-side work
* TGPU​ \= GPU rendering work
* Tsync​ \= synchronization and communication overhead

For a target frame rate of 60 frames per second, the theoretical frame budget is approximately

Tframe​\=601​≈16.67 ms 

Thus, the complete system must generally complete the required work within approximately 16.67 milliseconds per frame to sustain a nominal 60 FPS rate.

This does not mean that every application must target exactly 60 FPS; the appropriate target depends on the application, display hardware, and user experience requirements. Nevertheless, frame-time budgeting provides a useful framework for analyzing interactive rendering performance.

---

# 3.22.15 Draw Calls

A draw call is an instruction that causes the graphics API to render geometry using specified state.

Large numbers of draw calls can become a performance bottleneck, particularly when CPU-side command submission becomes expensive.

Consider a scene containing:

versus a carefully organized scene using:

The second scene may render substantially more efficiently even if the total polygon count is similar.

This is why real-time optimization cannot be reduced to polygon count alone.

Other important factors include:

* Draw-call count
* Shader complexity
* Texture bandwidth
* GPU memory
* Resolution
* Overdraw
* CPU-side scene management

---

# 3.22.16 Rendering Pipeline in the Proposed Product Configurator

The rendering architecture developed for this thesis can be summarized as follows:

This architecture separates application-level interaction from low-level GPU rendering while maintaining access to advanced graphics capabilities.

---

# 3.22.17 Importance of Pipeline Awareness

Although high-level libraries simplify graphics programming, developers should understand the underlying rendering pipeline.

For example, changing the following properties can have substantially different performance implications:

* Number of vertices
* Number of draw calls
* Texture resolution
* Shader complexity
* Number of lights
* Shadow resolution
* Post-processing passes

A developer who understands the pipeline can identify whether a problem is primarily:

**CPU-bound**

or

**GPU-bound**.

This distinction is essential for effective optimization.

---

# 3.23 Part 3B-1 Summary

This section examined the two major concepts required to understand modern real-time rendering: **material systems** and the **GPU rendering pipeline**.

Material systems define how surfaces interact with light. Traditional materials such as Lambert and Phong models provide relatively simple approximations, while physically based materials use parameters such as roughness and metalness to produce more consistent material behavior. Texture maps further extend these systems by allowing material properties to vary spatially across a surface. Three.js provides a hierarchy of material implementations, including simple unlit materials and physically based `MeshStandardMaterial` and `MeshPhysicalMaterial` implementations. Three.js+2Three.js+2

The second half of the section examined the GPU rendering pipeline, from vertex specification and vertex processing through primitive assembly, rasterization, fragment shading, depth testing, blending, and framebuffer output. WebGL exposes this programmable rendering architecture to browser applications, while Three.js provides a higher-level abstraction over many of these operations. Khronos Registry+2Khronos Wikis+2

The discussion also established an important principle for the remainder of this thesis: **visual quality and rendering performance are inseparable from the underlying GPU pipeline**. A sophisticated interactive application must therefore consider not only the appearance of its materials but also the computational cost of geometry, shaders, textures, draw calls, and framebuffer operations.

The final section of Chapter 3 will build upon these foundations by examining **physically based rendering in greater detail**, including the rendering equation, BRDFs, metallic-roughness workflows, image-based lighting, tone mapping, and the relationship between physical accuracy and real-time performance.

---

## Part 3B-2: Physically Based Rendering and Chapter Conclusion

---

# 3.23 Physically Based Rendering

## 3.23.1 Introduction

Physically Based Rendering (PBR) is a rendering methodology designed to produce visually consistent images by modeling the interaction between light and surfaces according to principles derived from physics.

Traditional real-time lighting models, such as the Phong model, often use parameters that are primarily artistic abstractions. PBR instead attempts to describe materials using properties that correspond more closely to real-world behavior.

This does not mean that PBR is a complete simulation of physical reality. Real-time graphics must operate under strict computational constraints. Instead, PBR provides a carefully designed approximation that produces plausible results while remaining practical for interactive applications.

PBR has become particularly important in:

* Game development
* Product visualization
* Architectural visualization
* Digital twins
* Virtual reality
* Web-based 3D applications
* Film and animation
* E-commerce visualization

Three.js provides PBR through materials such as `MeshStandardMaterial` and `MeshPhysicalMaterial`. (threejs.org)

---

# 3.23.2 The Rendering Equation

The theoretical foundation of physically based rendering is the **rendering equation** introduced by James Kajiya.

For a surface point x, outgoing radiance can be expressed conceptually as

Lo​(x,ωo​)\=Le​(x,ωo​)+∫Ω​fr​(x,ωi​,ωo​)Li​(x,ωi​)(n⋅ωi​)dωi​ 

where:

* Lo​ \= outgoing radiance
* Le​ \= emitted radiance
* Li​ \= incoming radiance
* fr​ \= bidirectional reflectance distribution function (BRDF)
* ωi​ \= incoming light direction
* ωo​ \= outgoing/view direction
* n \= surface normal
* Ω \= hemisphere above the surface

The equation describes a fundamental idea:

> The light leaving a surface is determined by emitted light plus reflected incoming light.

The integral represents the contribution of light arriving from every possible direction.

In a theoretical renderer, evaluating this integral exactly would be computationally expensive. Real-time graphics therefore approximate it using numerical techniques, analytical models, precomputation, and hardware acceleration.

---

# 3.23.3 BRDF

The **Bidirectional Reflectance Distribution Function (BRDF)** describes how incoming light is reflected toward a particular outgoing direction.

It can be expressed as

fr​(ωi​,ωo​) 

A physically plausible BRDF should satisfy important constraints, including conservation of energy and appropriate reciprocity behavior.

The BRDF is central to PBR because it provides the mathematical relationship between:

* Material
* Incoming light
* Surface orientation
* Viewing direction

Different BRDF models produce different visual characteristics.

---

# 3.23.4 Microfacet Theory

Modern real-time PBR commonly models surfaces as collections of microscopic facets.

Although a surface may appear smooth at a macroscopic scale, its microscopic structure determines how light is reflected.

Conceptually:

Each microscopic facet has its own orientation.

A smooth material contains facets with relatively similar orientations.

A rough material contains facets with greater variation.

This explains why roughness affects the width and intensity of specular reflections.

---

# 3.23.5 Normal Distribution Function

A microfacet BRDF typically contains a **Normal Distribution Function (NDF)**.

The NDF describes the statistical distribution of microfacet orientations.

One commonly used distribution is the Trowbridge–Reitz GGX distribution.

A simplified form can be represented as

DGGX​(N,H,α)\=π\[(N⋅H)2(α2−1)+1\]2α2​ 

where:

* N \= surface normal
* H \= half-vector
* α \= roughness-related parameter

The exact implementation may use a remapped roughness value, such as

α\=r2 

where r is the user-facing roughness parameter.

The GGX distribution is widely used because it provides plausible long specular tails and behaves well for a broad range of roughness values.

---

# 3.23.6 Fresnel Reflection

The amount of reflected light changes according to viewing angle.

This phenomenon is described by the **Fresnel effect**.

At grazing angles, surfaces generally become more reflective.

For example, when looking directly at a glass surface, its reflection may be relatively subtle. When viewing the same surface at a shallow angle, the reflection becomes much stronger.

A commonly used approximation is Schlick's Fresnel approximation:

F(θ)\=F0​+(1−F0​)(1−cosθ)5 

where F0​ represents reflectance at normal incidence.

This approximation is computationally inexpensive and therefore suitable for real-time rendering.

---

# 3.23.7 Geometry Term

Microfacet BRDFs must also account for masking and shadowing between microscopic surface facets.

This is represented by a geometry term commonly written as

G(N,V,L) 

The geometry function reduces reflected energy when microfacets obscure one another.

A common approach is based on the Smith masking-shadowing model.

The geometry term is particularly important for producing plausible rough-surface behavior.

---

# 3.23.8 Cook–Torrance BRDF

A widely used physically based specular model is the **Cook–Torrance BRDF**.

Conceptually:

fr​\=4(N⋅V)(N⋅L)DGF​ 

where:

* D \= normal distribution function
* G \= geometry term
* F \= Fresnel term
* N \= surface normal
* V \= viewing direction
* L \= light direction

This formulation provides a physically motivated model for specular reflection and forms the basis of many modern PBR implementations.

The complete rendering system, however, requires more than the specular BRDF alone. Diffuse reflection, direct illumination, indirect illumination, environment lighting, and material properties must also be considered.

---

# 3.23.9 Energy Conservation

A physically plausible material should not reflect more energy than it receives.

This principle is known as **energy conservation**.

If

Ein​ 

represents incoming energy, then a simplified condition is

Eout​≤Ein​ 

This is important when combining diffuse and specular components.

For example, increasing the specular contribution should generally reduce the amount of energy available to the diffuse component.

PBR systems incorporate these relationships to prevent materials from producing physically implausible brightness.

---

# 3.23.10 Metallic-Roughness Workflow

One of the most common PBR workflows is the **metallic-roughness workflow**.

A simplified material can be represented using:

M\=(Cbase​,m,r) 

where:

* Cbase​ \= base color
* m \= metalness
* r \= roughness

The material is then interpreted according to the following conceptual model:

This workflow is particularly convenient for artists because a small number of parameters can represent a wide variety of materials.

---

# 3.23.11 Image-Based Lighting

Direct light sources are not sufficient for convincing material appearance.

Consider a polished metallic object.

A metal surface primarily reflects its environment. If the environment contains nothing interesting, the metal may appear visually flat even if the lighting calculation is mathematically correct.

**Image-Based Lighting (IBL)** addresses this problem by using an environment map as a source of illumination and reflection information.

A typical HDR environment contains substantially more dynamic range than a conventional 8-bit image.

The environment can be represented as

Lenv​(ω) 

where each direction corresponds to incoming environmental radiance.

The renderer integrates this environment over the surface hemisphere.

---

# 3.23.12 High Dynamic Range Lighting

Real-world illumination contains a very large range of intensities.

For example:

* A dark wall
* A room lamp
* A bright window
* Direct sunlight

may all exist within the same scene.

Standard 8-bit color values cannot represent this entire range accurately.

HDR rendering therefore uses floating-point representations that allow values beyond the conventional display range.

Conceptually,

CHDR​ 

is calculated first, followed by conversion to displayable output:

Cdisplay​\=ToneMap(CHDR​) 

This process is important for realistic lighting and physically based materials.

---

# 3.23.13 Tone Mapping

A monitor cannot directly display arbitrary HDR values.

Tone mapping converts high-dynamic-range values into a displayable range.

A simplified tone-mapping function can be represented as

Cout​\=T(CHDR​) 

where T is the tone-mapping operator.

Different operators produce different visual characteristics.

Common approaches include:

* Reinhard
* ACES-inspired operators
* Filmic operators

Tone mapping influences the final artistic appearance of an application and therefore should be treated as part of the rendering pipeline rather than merely a post-processing effect.

---

# 3.23.14 Gamma and Color Management

Another important consideration is color space.

Color values used for image display are not necessarily linear representations of light intensity.

Rendering calculations generally require a linear-light representation.

A simplified workflow is:

Incorrect color-space handling can produce:

* Incorrect brightness
* Incorrect material appearance
* Washed-out images
* Incorrect blending
* Unrealistic lighting

Therefore, color management is an essential component of a modern graphics system.

---

# 3.23.15 PBR in Three.js

Three.js provides `MeshStandardMaterial` for physically based metallic-roughness rendering. It also provides `MeshPhysicalMaterial`, which extends the standard PBR material with additional properties such as transmission, thickness, clearcoat, sheen, and related physical effects. (threejs.org)

A simplified example is:

JavaScript

A more advanced physical material can include additional properties:

JavaScript

The exact visual result depends on the renderer configuration, lighting environment, geometry, textures, and color-management settings.

---

# 3.23.16 PBR and Product Visualization

PBR is particularly appropriate for product visualization.

A product configurator may need to represent:

* Brushed aluminum
* Polished steel
* Matte plastic
* Glossy plastic
* Leather
* Glass
* Ceramic
* Wood

Instead of creating a separate 3D model for every variation, the same geometry can be combined with different material parameters.

For example:

Product\=Geometry+Material 

Therefore:

This dramatically reduces asset duplication.

---

# 3.23.17 Performance Considerations

PBR improves visual consistency but increases computational complexity.

Performance is affected by:

* Number of lights
* Shadow calculations
* Texture resolution
* Environment map resolution
* Shader complexity
* Material features
* Screen resolution
* Post-processing
* Number of visible objects

Therefore, a production-quality interactive graphics application must balance:

Visual Quality 

against

Rendering Performance 

The objective is not maximum graphical complexity.

Instead, the objective is an appropriate quality-to-cost ratio.

---

# 3.23.18 Real-Time Constraints

For interactive applications, rendering must happen continuously.

At a target of 60 FPS,

Tframe​≈16.67ms 

At 120 FPS,

Tframe​≈8.33ms 

Therefore, doubling the target frame rate approximately halves the available time for each frame.

This becomes especially important for:

* VR
* AR
* Interactive 3D websites
* Games
* Real-time product configurators

Virtual reality can impose particularly demanding latency and frame-rate requirements because rendering delays can directly affect the user's perception of responsiveness.

---

# 3.23.19 Web Graphics and PBR

The development of WebGL and modern browser graphics APIs has made sophisticated rendering available directly through web browsers.

A web-based graphics application can therefore combine:

This enables applications that previously would have required specialized desktop software.

Examples include:

* Interactive portfolios
* Product configurators
* 3D e-commerce
* Architectural visualization
* Scientific visualization
* Virtual exhibitions
* Educational simulations

The web therefore represents an important deployment platform for interactive computer graphics.

---

# 3.23.20 Relationship Between Graphics Theory and the Proposed System

The theoretical concepts presented throughout Chapter 3 can now be connected to the architecture of the proposed application.

The complete process can be summarized as:

This pipeline demonstrates how the mathematical foundations introduced at the beginning of the chapter ultimately produce the visual image presented to the user.

---

# 3.24 Chapter Conclusion

This chapter established the theoretical foundation for interactive three-dimensional computer graphics.

The discussion began with the mathematical concepts required to represent and manipulate graphical objects. Vectors provide representations of direction, displacement, and orientation, while matrices provide an efficient framework for geometric transformation. These mathematical structures allow objects to be translated, rotated, scaled, and projected through multiple coordinate spaces.

The chapter then examined the transformation pipeline from object space through world space, view space, clip space, normalized device coordinates, and finally screen space. This process forms the mathematical basis for converting three-dimensional geometry into a two-dimensional image.

The second major topic was lighting and image formation. Classical illumination models such as Lambert, Phong, and Blinn–Phong were introduced to demonstrate how surface orientation, light direction, and camera position affect appearance. Rasterization and texture mapping were then examined as the mechanisms that convert geometric primitives into fragments and apply detailed surface information.

The chapter subsequently introduced modern material systems. Parameters such as base color, roughness, metalness, normal information, and emission allow a rendering engine to represent a broad range of real-world materials. These properties are particularly important for interactive product visualization because they allow a single geometric model to support numerous visual configurations.

Finally, the chapter examined the modern GPU rendering pipeline and physically based rendering. The rendering equation, BRDFs, microfacet theory, Fresnel reflection, energy conservation, image-based lighting, HDR rendering, tone mapping, and color management were discussed as the theoretical foundations of modern PBR.

The resulting conceptual model is:

Geometry→Transformation→Rasterization→Material→Lighting→PBR→Image​ 

Understanding this sequence is essential for the subsequent implementation chapters. Rather than treating Three.js, WebGL, or React Three Fiber as isolated software libraries, the developer can now understand the underlying mathematical and computational processes represented by those abstractions.

---

## 3.25 Transition to the Next Chapter

With the theoretical foundations established, the thesis can now move from **what computer graphics is** to **how an interactive graphics system is implemented**.

The next chapter should therefore introduce the implementation architecture of the proposed **Interactive Graphics and Web Technologies** system.

A logical Chapter 4 structure would be:

### Chapter 4 — System Architecture and Implementation

**4.1 System Requirements**

**4.2 Overall System Architecture**

**4.3 Front-End Architecture**

**4.4 React and React Three Fiber**

**4.5 Three.js Scene Architecture**

**4.6 Asset Pipeline**

**4.7 glTF/GLB Model Loading**

**4.8 Material and Texture Management**

**4.9 Camera and Interaction System**

**4.10 Animation Architecture**

**4.11 WebGL Rendering Architecture**

**4.12 Performance Optimization**

**4.13 Responsive and Mobile Rendering**

**4.14 Implementation Results**

**4.15 Chapter Summary**

This transition is important because **Chapter 3 establishes the theory**, while Chapter 4 should demonstrate how that theory is translated into an actual web-based interactive graphics application.

---

### Chapter 3 — Completed Structure

At this point, the chapter has the following complete structure:

| Section       | Topic                                        |
| ------------- | -------------------------------------------- |
| **3.1–3.2**   | Introduction and mathematical representation |
| **3.3**       | Vectors                                      |
| **3.4**       | Matrices                                     |
| **3.5**       | Coordinate systems                           |
| **3.7**       | Geometric transformations                    |
| **3.8**       | Homogeneous coordinates                      |
| **3.9**       | Model, View, Projection matrices             |
| **3.10–3.12** | Cameras, frustums, projection                |
| **3.13–3.16** | Clipping, viewport, Three.js application     |
| **3.17–3.18** | Lighting and reflection                      |
| **3.19**      | Rasterization                                |
| **3.20**      | Texture mapping                              |
| **3.21**      | Material systems                             |
| **3.22**      | GPU rendering pipeline                       |
| **3.23**      | Physically based rendering                   |
| **3.24**      | Chapter conclusion                           |
| **3.25**      | Transition to implementation                 |
