# Lecture 8 — Midterm and rigging start

**Course:** Blender for Real-Time Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** midterm; armature idea  
**Board first:** bone parent of mesh

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

1. Sit midterm: units, topo, UV, Principled, lights, keys.
2. Add an armature.
3. Parent with automatic weights on a simple mesh.
4. Pose mode.
5. Don't rig a production character this week.

---

## 1. Midterm

Scale, normals, UV stretch, metal/rough, sun vs point, keyframes.

## 2. Bones

A bone is a transform. Skinning is weights. Real-time: keep bone count modest.

## 3. Weights

Automatic weights on a bar or a simple arm. Weight paint names only.

## Live coding (60 min)

Two-bone arm; pose it; screenshot.

---

## Lab

1. Fix a weight leaking into the other bone extra.
2. Rest pose.

---

## Homework

1. Midterm reflection + armature file.

---

## Quiz (10 min)

1. None.

## Snippet

```
Add Armature → Parent → Armature Deform / Automatic Weights
```

---

## Common mistakes

- Rigify on a stick and calling it done.
- Applying armature before weights are right.

---

## Board drawings

1. Bone chain.
2. Weight colors.

