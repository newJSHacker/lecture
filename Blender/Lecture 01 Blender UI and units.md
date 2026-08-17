# Lecture 1 — Blender UI and units

**Course:** Blender for Real-Time Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** viewport, meters, save  
**Board first:** grid = meters; origin at 0

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

1. Navigate the 3D viewport.
2. Set unit scale to meters.
3. Apply object mode vs edit mode.
4. Save .blend with a version name.
5. Do not model at 100 m for a mug.

---

## 1. Why Blender in IGWT

Semester 3 already has WebGL and Three.js. This course supplies **assets** that survive in a real-time engine: clean topology, UVs, PBR maps, and glTF. It is not a film-lighting course.

## 2. Units

Scene unit = 1 meter. A character is ~1.7 m. A product is centimeters. Wrong scale is the #1 Three.js import bug.

## 3. UI

Outliner, Properties, Timeline. N-panel. Numpad views. Edit vs Object. Students who only watch YouTube never learn the outliner.

## Live coding (60 min)

Create a 2 m cube, a 0.2 m cube, and a camera. Screenshot the dimensions panel. Save `week01.blend`.

---

## Lab

1. Rename objects in the outliner.
2. Delete the default cube only after duplicating a backup.

---

## Homework

1. Written: why meters.
2. A numbered screenshot of your outliner.

---

## Quiz (10 min)

1. Default unit (2)
2. Object vs Edit (4)
3. Why a 100 m mug fails in Three.js (4)

## Snippet

```
Scene Properties → Units → Metric, Unit Scale 1.0
```

## Extra exercises

1. Measure a real object; model a box the same size.
2. List 8 shortcuts you will actually use.
3. Draw the Object/Edit mode split.
4. Find clip start/end on the viewport camera.
5. Write the file-naming scheme for the semester.

---

## Common mistakes

- Modeling in whatever scale 'looks good'.
- Never applying scale.

---

## Board drawings

1. Meter grid.
2. Outliner.

