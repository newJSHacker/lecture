# Lecture 10 — Compute pass

**Course:** GPU Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** workgroups  
**Board first:** dispatch(x,y,z)

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 10 | Quiz from last week (Week 1: course contract) |
| 25 | Core definition and one picture |
| 45 | Worked examples / derivation |
| 65 | Live pitfalls and policy |
| 75 | Preview lab, then stand up for live coding |

---

## Learning goals

1. A compute shader fills a storage texture or buffer.
2. workgroup size.
3. Barriers name.
4. Don't dispatch (1,1,1) for 1M threads without thinking.
5. Read the result as a blit to screen.

---

## 1. Compute

No raster. Threads in a grid. Perfect for particles and blur.

## 2. Memory

storage buffers vs textures. Race if you write without sync.

## 3. Map

This replaces some ping-pong FS hacks.

## Live coding (60 min)

Compute a gradient or noise into a texture; blit.

---

## Lab

1. particle integrate extra if time.
2. workgroup 8×8.

---

## Homework

1. Written: workgroup.
2. WGSL compute.

---

## Quiz (10 min)

1. dispatch (3)
2. storage (4)
3. why not FS (3)

## Snippet

```wgsl
@compute @workgroup_size(8,8) fn cs(@builtin(global_invocation_id) id: vec3u) { /* ... */ }
```

---

## Common mistakes

- compute that still rasterizes a triangle per particle.
- unbounded loops in WGSL.

---

## Board drawings

1. Grid of threads.

