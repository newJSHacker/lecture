# Lecture 9 — Armatures and export pose

**Course:** Blender for Real-Time Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** rest pose, apply  
**Board first:** Ctrl+A apply rotation/scale

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

1. Apply rotation and scale on meshes.
2. Rest pose is T or A as you choose — document it.
3. Don't leave scale 0.01 on the armature.
4. Name bones.
5. Forward kinematics only unless a student already knows IK.

---

## 1. Apply transforms

Unapplied scale is the classic 'tiny model / huge model' in Three.js. Ctrl+A → All Transforms on the mesh before parenting, with a backup.

## 2. Orientation

Blender Z-up vs glTF / Three.js Y-up. Exporter converts. Students must still check in the engine.

## 3. IK

Name it. Optional extra. FK is enough for a spinning sign or a simple arm.

## Live coding (60 min)

Apply scale on last week's arm; re-parent if needed; pose two frames.

---

## Lab

1. Bone axes overlay.
2. Document rest pose in README.

---

## Homework

1. Written: Z-up vs Y-up.
2. Checklist screenshot.

---

## Quiz (10 min)

1. apply scale why (4)
2. Z vs Y (3)
3. rest pose (3)

## Snippet

```
Ctrl+A → Rotation & Scale  (object mode, backup first)
```

---

## Common mistakes

- Applying location and losing the scene.
- Negative scale to 'mirror'.

---

## Board drawings

1. Axes.
2. Apply menu.

