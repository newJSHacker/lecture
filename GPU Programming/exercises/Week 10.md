# Extra exercises — Week 10 (Compute pass)

Lecture: [[GPU Programming/Lecture 10 Compute pass]]

## Written and coding

1. Define this week's kernel in one sentence (workgroups).
2. Give one failing input or screenshot that would fool a TA.
3. Write the live-coding snippet from memory, then diff against the notes.
4. Two quiz-style questions you would put on next week's paper.
5. Connect this week to a later IGWT course in one paragraph.


## Snippet

```wgsl
@compute @workgroup_size(8,8) fn cs(@builtin(global_invocation_id) id: vec3u) { /* ... */ }
```
