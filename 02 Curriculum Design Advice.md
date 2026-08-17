
Your curriculum is already at the level of a modern specialization rather than a traditional computer science program. The biggest challenge now is **how to teach each course**, not what topics to include.

A good university course should be built around five pillars:

1. **Theory** (Why?)
    
2. **Demonstration** (How?)
    
3. **Hands-on Practice** (Do it yourself)
    
4. **Project** (Apply the knowledge)
    
5. **Assessment** (Prove mastery)
    

I would standardize every course around the same structure so students always know what to expect.

---

# Standard Structure for Every Course

Every week should include:

|Part|Duration|Purpose|
|---|---|---|
|Lecture|60–90 min|Explain concepts|
|Live Coding / Demo|60 min|Show implementation|
|Lab|2–3 hours|Students practice|
|Homework|4–8 hours|Individual work|
|Weekly Quiz|10–15 min|Reinforce theory|

Every semester should end with a substantial project rather than only a written examination.

---

# Example Course Design

## Course 1 — Introduction to Programming

### Goal

Students learn computational thinking.

---

### Professor Preparation

Before the semester:

- Lecture slides
    
- Python examples
    
- Programming exercises
    
- Auto-grading system
    
- Coding standards
    

---

### Weekly Lecture

Week 1

Variables

Professor:

- explains variables
    
- demonstrates examples
    
- shows common mistakes
    

Lab:

Students build

- calculator
    
- temperature converter
    

Homework:

Simple calculator

---

Week 2

Conditions

Live coding

```
if
else
```

Lab

Guessing game

Homework

Rock-paper-scissors

---

Week 3

Loops

Live coding

Pattern printing

Homework

Prime number finder

---

Continue similarly until

- functions
    
- files
    
- OOP
    
- algorithms
    

---

Final Project

Console game

or

Task manager

---

Assessment

30% Labs

30% Homework

10% Quiz

30% Final Project

---

# Course 2 — Web Technologies

Goal

Understand how browsers work.

---

Professor prepares

Slides

Browser DevTools demos

Code examples

Assignments

---

Lecture

Instead of

"This is HTML"

The professor writes HTML from scratch.

Students watch.

Then students repeat.

---

Example

```
HTML

↓

Browser Parser

↓

DOM

↓

CSSOM

↓

Layout

↓

Paint

↓

Composite
```

Students actually inspect DevTools.

---

Lab

Create

Portfolio website

---

Homework

Clone Apple's homepage

(Not perfectly,  
just layout)

---

Project

Responsive business website

---

# Course 4 — Computer Graphics I

Full plan and weekly notes: [[10 Computer Graphics I]] · [[Computer Graphics/00 Lectures]]

This course is where things become exciting. Students implement a **tiny software renderer** first. Three.js is a named map of that pipeline in Week 13, not the weekly lab. GPU catalogs: [[07 WebGL and Shader Snippets]], [[08 Three.js Snippets]].

---

Professor Preparation

- Pipeline posters (spaces; triangle → pixels)
- Shared `vec3` / `mat4` / barycentric kernel
- Software rasterizer starter (`ImageData`)
- Course cube (12 triangles) reused from Week 6
- Recorded 8-minute demos for Weeks 1–9
- Three.js orbit demo as a **5-minute oracle** in Week 7 only

---

Lecture Example

Coordinate Systems (Week 7 / 9)

Instead of drawing on PowerPoint only, the professor runs the **student** `lookAt` and PVM product so the cube moves. Optionally open Three.js for five minutes and say: this is the same V and P with different names. Then close it.

World Space

↓

View Space

↓

Clip Space

↓

NDC → pixels

---

Lab

Weeks 1–12: `putPixel` through textured z-buffered cube.

Week 13: same cube on WebGL2.

---

Homework

Solar system is **Week 6** (scene graph), not a substitute for the rasterizer.

---

Project

Interactive 3D scene **they can explain as a pipeline**. Rubric in [[10 Computer Graphics I]].

---

# Course 7 — WebGL Programming

Students should NOT begin with frameworks.

They should struggle a little.

Professor prepares

- shader examples — start from [[07 WebGL and Shader Snippets]]
    
- WebGL boilerplate — `WebGL/demos/_gl.js` and demo 01
    
- debugging guide — [[WebGL/01 Conventions]] black-screen checklist
    

---

Lecture

Explain

GPU

↓

Vertex Buffer

↓

Vertex Shader

↓

Rasterizer

↓

Fragment Shader

↓

Framebuffer

Every lecture should draw this pipeline.

---

Lab

Draw

Triangle

Square

Cube

Textured Cube

Lighting

---

Project

Mini WebGL Engine

---

# Course 10 — Shader Programming

Probably the signature course.

Professor Preparation

Many visual demonstrations — [[WebGL/13 Noise]], [[WebGL/14 SDF and Ray Marching]], demos 09–12 and 19–21.

Never only equations.

---

Lecture Example

Noise

Professor changes one line.

Students instantly see

Clouds

Fire

Water

Terrain

---

Lab

Create

Animated Lava

---

Homework

Procedural Galaxy

---

Project

Shader Gallery

Each student creates

5 original shaders.

---

# Course 13 — Interactive Experience Development

Now students combine everything.

Lecture

Architecture

React

↓

React Three Fiber

↓

Three.js

↓

WebGL

---

Professor demonstrates

Interactive landing page

Scroll animations

Audio

Physics

Model loading

---

Project

Award-style website

Like

Codrops

Awwwards

FWA

---

# Course 17 — Capstone

This should resemble a professional software project.

Students work in teams of 3–5.

---

Every week

Sprint planning

↓

Code review

↓

Presentation

↓

Feedback

---

Deliverables

Proposal

Research

Prototype

Alpha

Beta

Final Release

Presentation

Documentation

GitHub repository

Deployment

---

# Professor Responsibilities

Every instructor should prepare the following before the semester begins:

### 1. Lecture Slides

Not text-heavy.

Lots of diagrams.

Animations.

---

### 2. Live Coding Examples

Every lecture includes coding.

Students learn by watching experts think.

---

### 3. Lab Manual

Step-by-step exercises.

Expected output.

Hints.

Common mistakes.

---

### 4. Homework

Increasing difficulty.

Should require independent thinking.

---

### 5. Project Specification

Requirements

Rubric

Examples

Deadline

Evaluation criteria

---

### 6. Video Recordings

Record every lecture.

Students can review difficult concepts.

---

### 7. GitHub Repository

Each course has

```
course/

lecture1/

lecture2/

starter-code/

solutions/

assignments/

resources/
```

---

# Teaching Philosophy

A good ratio for this specialization is:

|Activity|Percentage|
|---|--:|
|Theory|25%|
|Live Demonstration|25%|
|Hands-on Labs|35%|
|Project Work|15%|

Graphics, WebGL, shaders, and interactive systems are learned primarily by building rather than memorizing.

## Additional recommendations for an IGWT program

To make **Interactive Graphics and Web Technologies (IGWT)** distinctive and industry-aligned, consider adding these program-wide elements:

- **Version Control & Collaboration:** Introduce Git and GitHub in Semester 1 and require them in every project.
    
- **Software Engineering Practices:** Cover debugging, testing, code reviews, documentation, and project organization beginning in Semester 2.
    
- **Portfolio Development:** Require students to publish a portfolio website and document each major project. By graduation, each student should have 8–10 polished portfolio pieces.
    
- **Industry Integration:** Invite guest lecturers from graphics, visualization, game, XR, and creative technology companies each semester.
    
- **Open-Source Contribution:** Encourage students in the later semesters to contribute to libraries such as Three.js, React Three Fiber, or creative coding projects.
    
- **Research and Ethics:** In AI-related courses, discuss copyright, responsible AI use, accessibility, performance, and sustainability alongside technical implementation.
    

With these additions, graduates would be prepared not only as web developers, but as specialists in interactive graphics, real-time rendering, visualization, XR, and AI-enhanced creative technologies. This combination remains uncommon in many computer science departments and would give the program a clear identity.

---

# Becoming a good teacher (not only a course designer)

This note is the **course machine**: lecture, live coding, lab, homework, quiz, project. It does not by itself make someone a good instructor.

For classroom craft, feedback, inclusion, integrity, TAs, time, and supervision, use [[06 Becoming a Good Teacher]] and the handbook starting at [[Teaching/00 How to Use These Notes]].

A short map:

| If you need | Read |
| --- | --- |
| How students actually learn | [[Teaching/02 How Students Learn]] |
| Next week’s plan | [[Teaching/03 Lesson Planning]] |
| Live coding without hiding the work | [[Teaching/06 Live Coding Pedagogy]] |
| Labs and critiques | [[Teaching/07 Labs and Studio]] |
| Rubrics and comments | [[Teaching/08 Feedback and Rubrics]] |
| AI and copying | [[Teaching/12 Academic Integrity and AI]] |
| Printable checklists | [[Teaching/19 Checklists and Templates]] |
| First year on the job | [[Teaching/23 First Year as an Instructor]] |