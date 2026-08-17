Source: [ChatGPT — Curriculum Design Advice](https://chatgpt.com/share/6a7fa45a-d4c0-83eb-b5c4-121a78bda55e)

---

# Chapter 9

# Program Evaluation, Quality Assurance, and Continuous Improvement

## 9.1 Introduction

The development of a new university program requires more than defining a collection of courses. A sustainable academic program must also establish mechanisms for evaluating educational outcomes, monitoring student achievement, maintaining academic standards, incorporating technological developments, and continuously improving the curriculum.

The proposed **Interactive Graphics and Web Technologies (IGWT)** program is situated within a rapidly changing technological environment. Web APIs, graphics hardware, rendering frameworks, artificial intelligence systems, and extended-reality platforms evolve considerably faster than traditional university curricula.

Consequently, a static curriculum is insufficient.

The program should instead be understood as a continuously evolving educational system:

Curriculum→Teaching→Assessment→Evaluation→Improvement→Curriculum​ 

This chapter proposes a quality-assurance framework for the IGWT program.

The framework evaluates five major dimensions:

1. Student learning
2. Teaching effectiveness
3. Technical competency
4. Research capability
5. Industry relevance

---

# 9.2 Need for Continuous Evaluation

Traditional academic programs can often remain relatively stable for several years.

Interactive graphics and web technologies are different.

A technology that is widely used when students enter the program may be significantly changed or replaced before they graduate.

For example, the technological progression may be represented as:

WebGL→WebGPU Traditional 3D Assets→AI Generated Assets Static Interfaces→AI Driven Interfaces Desktop Interaction→Spatial Computing 

Therefore, the curriculum should maintain stable theoretical foundations while allowing implementation technologies to evolve.

---

# 9.3 Quality Assurance Model

The proposed quality-assurance framework consists of four levels.

Each level provides feedback to the next.

---

# 9.4 Course-Level Evaluation

Every course should define measurable learning outcomes.

For example, the course **Shader Programming** could define:

### CLO1

Explain the purpose of vertex and fragment shaders.

### CLO2

Implement GLSL shaders.

### CLO3

Apply mathematical transformations within shaders.

### CLO4

Create procedural visual effects.

### CLO5

Optimize shader performance.

These outcomes should be directly connected to assessments.

---

# 9.5 Course Learning Outcomes

The relationship can be represented as:

CLO→Assessment→Evidence 

For example:

| Learning Outcome          | Assessment             |
| ------------------------- | ---------------------- |
| Understand GLSL           | Written examination    |
| Write shaders             | Laboratory             |
| Create procedural effects | Project                |
| Optimize shaders          | Performance experiment |
| Explain results           | Technical report       |

This ensures that assessment measures actual learning rather than simply attendance or completion.

---

# 9.6 Program Learning Outcomes

Course-level outcomes should contribute to program-level outcomes.

For example:

CLOShader​→PLOGPU​ CLOGraphics​→PLOComputer Graphics​ CLOResearch​→PLOResearch​ 

This produces a curriculum map.

---

# 9.7 Curriculum Mapping

A simplified mapping can be represented as follows:

| Course                      | Programming | Graphics | GPU | Web | Interaction | Research |
| --------------------------- | ----------- | -------- | --- | --- | ----------- | -------- |
| Introduction to Programming | ●●●         | —        | —   | ●   | —           | ●        |
| Mathematics for Graphics    | ●           | ●●●      | ●   | —   | —           | ●        |
| Computer Graphics I         | ●           | ●●●      | ●●  | —   | ●           | ●        |
| WebGL Programming           | ●●          | ●●●      | ●●● | ●●  | ●           | ●        |
| Three.js                    | ●●          | ●●●      | ●●  | ●●● | ●●          | ●        |
| Shader Programming          | ●●          | ●●●      | ●●● | ●●  | ●●          | ●●       |
| Real-Time Rendering         | ●           | ●●●      | ●●● | ●●  | ●●          | ●●       |
| XR                          | ●●          | ●●●      | ●●  | ●●● | ●●●         | ●●       |
| AI Graphics                 | ●●●         | ●●       | ●●  | ●●● | ●●●         | ●●●      |
| Graduation Thesis           | ●●          | ●●●      | ●●● | ●●  | ●●          | ●●●      |

Here:

* ● = introductory
* ●● = intermediate
* ●●● = advanced

This mapping allows the university to verify that every graduate competency is developed progressively.

---

# 9.8 Assessment Strategy

Assessment should occur at multiple levels.

## Formative Assessment

Used during learning.

Examples:

* Weekly exercises
* Coding tasks
* Laboratory work
* Quizzes
* Peer reviews

## Summative Assessment

Used to determine final achievement.

Examples:

* Final examinations
* Projects
* Technical reports
* Presentations
* Thesis

The combination is:

Learning\=Formative+Summative 

---

# 9.9 Practical Assessment

Because IGWT is highly technical and project-oriented, practical assessment should have substantial importance.

A student may understand the theoretical definition of a shader but still be unable to implement one.

Therefore:

Knowledge\=Skill 

A complete assessment system must evaluate both.

---

# 9.10 Project-Based Assessment

Projects should evaluate multiple competencies simultaneously.

For example, a 3D product configurator may require:

* JavaScript
* React
* Three.js
* WebGL
* Materials
* Lighting
* Animation
* UI design
* Performance optimization

Therefore, a single project can provide evidence of multiple learning outcomes.

---

# 9.11 Technical Evaluation

Student projects should be evaluated using objective technical criteria.

Possible metrics include:

### Performance

FPS FrameTime 

### Rendering Complexity

TriangleCount DrawCalls 

### Memory

TextureMemory GPU\\Memory 

### Loading

InitialLoadTime 

These measurements provide quantitative evidence of engineering quality.

---

# 9.12 Visual Evaluation

Graphics projects should also be evaluated visually.

Possible criteria include:

* Composition
* Lighting
* Material quality
* Animation
* Color
* Visual hierarchy
* Consistency
* Readability

A rubric could assign scores from 1 to 5.

| Criterion   | 1           | 3          | 5              |
| ----------- | ----------- | ---------- | -------------- |
| Lighting    | Poor        | Acceptable | Excellent      |
| Materials   | Unrealistic | Reasonable | Convincing     |
| Animation   | Limited     | Functional | Highly refined |
| Composition | Weak        | Good       | Excellent      |

This provides a structured alternative to subjective grading.

---

# 9.13 Interaction Evaluation

Interactive applications should be evaluated according to usability.

Possible criteria include:

* Learnability
* Responsiveness
* Navigation
* Feedback
* Error prevention
* Accessibility
* Interaction consistency

Students should be encouraged to test their applications with real users.

---

# 9.14 User Testing

A small user study can provide valuable evidence.

A typical study might involve:

1. Recruit participants.
2. Explain the task.
3. Observe interaction.
4. Record completion time.
5. Record errors.
6. Collect questionnaire responses.
7. Analyze results.

For example:

TaskCompletionRate\=TotalTasksSuccessfulTasks​×100 

---

# 9.15 Research Assessment

The graduation thesis should be evaluated according to academic research criteria.

Recommended criteria include:

| Criterion               | Weight |
| ----------------------- | ------ |
| Research Question       | 10%    |
| Literature Review       | 15%    |
| Methodology             | 15%    |
| Implementation          | 20%    |
| Experimental Evaluation | 20%    |
| Analysis                | 10%    |
| Academic Writing        | 10%    |

The exact weighting may be adjusted by the institution.

---

# 9.16 Thesis Defense

Every student should defend the graduation thesis before a committee.

A typical defense could consist of:

### Presentation

15–20 minutes.

### Demonstration

5–10 minutes.

### Questions

15–30 minutes.

The committee should evaluate whether the student can explain:

* Why the problem matters
* What previous research exists
* What was implemented
* Why the methodology was selected
* What the results mean
* What limitations exist
* What should happen next

---

# 9.17 Research Reproducibility

A particularly important requirement for technical theses is reproducibility.

Students should provide:

* Source code
* Dataset
* Configuration
* Hardware specifications
* Software versions
* Experimental procedures
* Raw results

The research process should ideally be:

Code+Data+Method→Reproducible Result 

This improves the academic credibility of the program.

---

# 9.18 Version Control

Git-based version control should be introduced early in the program.

Students should learn:

* Repository creation
* Branches
* Commits
* Pull requests
* Merge conflicts
* Tags
* Releases
* Documentation

By graduation, students should have experience managing a complete software project.

---

# 9.19 Documentation Standards

Every major project should include a README containing:

Documentation should be considered part of engineering quality rather than an optional addition.

---

# 9.20 Industry Advisory Board

The program should establish an advisory group consisting of professionals from relevant industries.

Potential members could come from:

* Web technology
* Game development
* 3D visualization
* XR
* AI
* Design
* Architecture
* Digital media

The advisory board could meet annually.

Its role would be to evaluate:

* Graduate skills
* Curriculum relevance
* Emerging technologies
* Employment trends
* Industry expectations

---

# 9.21 Graduate Feedback

Program evaluation should continue after graduation.

Alumni surveys can investigate:

* Employment
* Job roles
* Skills used professionally
* Missing competencies
* Technologies encountered
* Further education

This creates an important feedback loop:

University→Graduate→Industry→Feedback→University 

---

# 9.22 Employer Feedback

Employer feedback provides another source of evidence.

Employers can evaluate graduates according to:

* Programming ability
* Graphics knowledge
* Problem solving
* Communication
* Collaboration
* Research ability
* Technical adaptability

This information can identify weaknesses that internal academic evaluation may not reveal.

---

# 9.23 Annual Program Review

The program should conduct an annual review.

The review should examine:

### Student Performance

Are students achieving the learning outcomes?

### Course Performance

Which courses have unusually high failure rates?

### Graduate Performance

Are graduates finding relevant employment?

### Technology

Which technologies have become important?

### Industry

What skills are employers requesting?

### Research

What new research directions have emerged?

---

# 9.24 Curriculum Update Cycle

A practical cycle is:

This produces continuous improvement.

---

# 9.25 Technology Review

Because the program is technology-intensive, an annual technology review should identify:

* New browser APIs
* New GPU APIs
* New frameworks
* New AI systems
* New XR platforms
* New rendering techniques

However, a new technology should not automatically become a new course topic.

It should first be evaluated according to:

EducationalValue+IndustryRelevance+TechnicalMaturity 

---

# 9.26 Example: WebGPU Curriculum Decision

Suppose WebGPU becomes significantly more important in professional development.

The university could evaluate:

### Question 1

Does WebGPU represent a major technological shift?

### Question 2

Does it provide educational value beyond WebGL?

### Question 3

Are appropriate teaching resources available?

### Question 4

Can faculty support the course?

If the answers are positive, WebGPU could gradually move from:

Introduction→AdvancedTopic→CoreTopic 

rather than immediately replacing WebGL.

---

# 9.27 Example: Generative AI

The same principle applies to generative AI.

Rather than teaching a particular AI platform as a permanent course requirement, the curriculum should teach concepts such as:

* AI APIs
* Prompt engineering
* Multimodal systems
* AI-assisted programming
* Generative content
* AI evaluation
* Ethical considerations

Specific platforms can then be changed without redesigning the entire course.

---

# 9.28 Ethical Considerations

Interactive graphics and AI also introduce ethical issues.

Students should understand:

* Copyright
* Data privacy
* AI-generated content
* Model bias
* Accessibility
* Digital ownership
* Deepfakes
* User tracking

Technical capability must therefore be accompanied by responsible development.

---

# 9.29 Accessibility

Interactive 3D applications can create accessibility challenges.

Students should consider:

* Keyboard navigation
* Screen-reader compatibility
* Reduced-motion preferences
* Color contrast
* Alternative descriptions
* Performance on low-end devices

A useful principle is:

Interactive\=Inaccessible 

The objective should be to make advanced visual experiences accessible to the widest possible audience.

---

# 9.30 Performance as an Educational Outcome

Performance optimization should be treated as a fundamental competency.

Students should understand that a visually impressive application that performs poorly is not a successful real-time system.

The objective can be expressed as:

Maximize(VisualQuality×InteractionQuality) 

subject to:

FrameTime≤TargetFrameTime 

For a target of 60 FPS:

TargetFrameTime≈16.67ms 

This provides students with a concrete engineering objective.

---

# 9.31 Recommended Performance Targets

The university does not need to impose identical requirements on every project, but suggested targets could be:

| Application Type               | Suggested Target                   |
| ------------------------------ | ---------------------------------- |
| Desktop 3D                     | 60 FPS                             |
| Mobile 3D                      | 30–60 FPS                          |
| VR                             | Device-dependent high refresh rate |
| Interactive visualization      | 30+ FPS                            |
| Heavy scientific visualization | Graceful degradation               |

Students should document the hardware used to achieve the reported results.

---

# 9.32 Portfolio Assessment

The program should evaluate not only individual assignments but also the student's complete portfolio.

A graduating student should demonstrate progression:

Beginner→Intermediate→Advanced 

The portfolio should show increasing complexity.

For example:

---

# 9.33 Graduate Competency Matrix

At graduation, students should ideally demonstrate the following:

| Competency         | Target                    |
| ------------------ | ------------------------- |
| Programming        | Advanced                  |
| Mathematics        | Intermediate–Advanced     |
| Web Development    | Advanced                  |
| Computer Graphics  | Advanced                  |
| WebGL              | Advanced                  |
| Three.js           | Advanced                  |
| Shader Programming | Intermediate–Advanced     |
| Blender            | Intermediate              |
| GPU Programming    | Intermediate              |
| UX                 | Intermediate              |
| XR                 | Introductory–Intermediate |
| AI Integration     | Intermediate              |
| Research           | Advanced                  |

This matrix can be used as a graduation-readiness assessment.

---

# 9.34 Program Success Indicators

The success of the program should be measured using multiple indicators.

### Academic

* Course completion rate
* Student grades
* Thesis quality
* Research publications

### Technical

* Project quality
* Performance benchmarks
* Software engineering quality

### Career

* Employment rate
* Relevant employment
* Internship participation

### Industry

* Employer satisfaction
* Industry partnerships
* External project participation

### Student

* Student satisfaction
* Portfolio quality
* Competition participation

No single metric should determine program success.

---

# 9.35 Key Performance Indicators

A university could define a small set of KPIs.

For example:

KPI1​\=GraduationRate KPI2​\=EmploymentRate KPI3​\=EmployerSatisfaction KPI4​\=ThesisQuality KPI5​\=StudentProjectQuality KPI6​\=IndustryParticipation 

These should be reviewed annually.

---

# 9.36 Continuous Improvement Framework

The overall quality-assurance model can be represented as:

This creates a continuous quality loop.

---

# 9.37 Relationship to the Research

The quality-assurance framework is directly connected to the technical research conducted in earlier chapters.

The research demonstrated that interactive graphics systems must be evaluated according to:

* Visual quality
* Performance
* Interaction
* Technical architecture
* User experience

The same principles can be applied to the educational program.

Therefore:

TechnicalEvaluation→EducationalEvaluation 

The curriculum itself becomes a system that can be measured and improved.

---

# 9.38 Long-Term Program Development

The IGWT program should eventually evolve beyond a six-semester undergraduate curriculum.

Potential future academic pathways include:

### Undergraduate

Bachelor's degree in Interactive Graphics and Web Technologies.

### Graduate

Master's degree in:

* Real-Time Graphics
* Interactive Computing
* Creative Technology
* XR
* GPU Computing

### Doctoral Research

Research areas could include:

* Neural rendering
* Real-time global illumination
* GPU computing
* Web-based scientific visualization
* Generative 3D
* AI-driven interactive environments
* Human-computer interaction
* Spatial computing

Thus:

Bachelor→Master→Doctorate 

can form a complete academic ecosystem.

---

# 9.39 International Collaboration

Because web technologies are globally distributed, international collaboration is particularly appropriate.

Potential activities include:

* Joint research projects
* Student exchange
* International hackathons
* Shared online courses
* Collaborative XR projects
* Open-source development

Students can therefore gain experience working with geographically distributed teams.

---

# 9.40 Open-Source Development

Open-source participation should be encouraged.

Students could contribute to:

* Graphics libraries
* Web frameworks
* Developer tools
* Shader repositories
* Visualization systems

This teaches professional collaboration while also exposing students to real-world software engineering practices.

---

# 9.41 Research Publication

Exceptional graduation projects may be developed into academic publications.

The progression could be:

StudentProject→Thesis→ConferencePaper→JournalPublication 

This provides students with an opportunity to enter research careers.

---

# 9.42 Academic and Industrial Balance

The program must maintain a balance between academic depth and industry relevance.

If the curriculum focuses only on theory:

Theory→Practice 

If it focuses only on current tools:

Tools→LongTermKnowledge 

The desired balance is:

Theory+Engineering+Design+Research​ 

This balance is one of the central principles of the proposed educational model.

---

# 9.43 Chapter Conclusion

This chapter established a quality-assurance and continuous-improvement framework for the proposed Interactive Graphics and Web Technologies program.

The analysis demonstrates that a modern technology-oriented academic program cannot be designed as a static collection of courses.

Instead, it should operate as a continuously evaluated system.

The proposed framework connects:

Learning Outcomes→Assessment→Evidence→Analysis→Improvement 

This process ensures that the program remains academically rigorous while adapting to changes in technology and industry.

The chapter also established the importance of:

* Course-level learning outcomes
* Program-level competencies
* Practical assessment
* Research evaluation
* Performance measurement
* User testing
* Industry feedback
* Alumni feedback
* Curriculum review
* Technology monitoring
* Accessibility
* Ethical development
* Reproducibility

The resulting model can be summarized as:

Teach→Measure→Evaluate→Improve​ 

For the proposed IGWT program, this continuous process is particularly important because the underlying technological environment is evolving rapidly.

The long-term success of the program should therefore not be defined by whether it teaches a particular framework or API.

Instead, success should be measured by whether graduates can:

1. Understand fundamental principles.
2. Learn new technologies independently.
3. Build complex interactive systems.
4. Evaluate their own work scientifically.
5. Solve unfamiliar technical problems.
6. Conduct independent research.
7. Communicate technical results.
8. Adapt to emerging technologies.

The ultimate objective is consequently not merely to produce graduates who can build today's interactive web applications.

It is to produce graduates capable of **inventing and developing the interactive computing systems of tomorrow**.

---

## Revised Thesis Structure

With Chapter 9 added, the thesis can now follow this structure:

| Chapter | Title                                                             |
| ------- | ----------------------------------------------------------------- |
| **1**   | Introduction                                                      |
| **2**   | Literature Review and Related Technologies                        |
| **3**   | Mathematical and Computer Graphics Foundations                    |
| **4**   | System Architecture and Design                                    |
| **5**   | Implementation                                                    |
| **6**   | Experimental Results and Discussion                               |
| **7**   | Conclusion and Future Work                                        |
| **8**   | Curriculum Design and Educational Framework                       |
| **9**   | Program Evaluation, Quality Assurance, and Continuous Improvement |
| **10**  | References and Supporting Materials\*                             |

\*Strictly speaking, **References should normally not be called a numbered "Chapter 10."** For a formal university thesis, I recommend treating _References_ and _Appendices_ as unnumbered back matter.

### Recommended final structure

**Main thesis**

1. Introduction
2. Literature Review
3. Mathematical and Graphics Foundations
4. System Architecture
5. Implementation
6. Experimental Evaluation
7. Conclusion and Future Work
8. Curriculum Design
9. Program Evaluation and Quality Assurance

**Back matter**
