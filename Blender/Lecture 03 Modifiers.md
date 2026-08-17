# Lecture 3 — Modifiers

**Course:** Blender for Real-Time Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** mirror, array, bevel  
**Board first:** stack: mirror then bevel

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

1. Use Mirror with clipping.
2. Array a bolt.
3. Bevel a hard-surface edge.
4. Apply vs keep live.
5. Don't apply until export needs it.

---

## 1. Non-destructive

Modifiers are the 'functions' of modeling. Keep them live while iterating. Apply before some exports if the engine cannot see them — glTF export applies mesh modifiers.

## 2. Order

Mirror before bevel usually. Array after the piece is right. Students reverse the stack and get double bevels.

## 3. Boolean

Name it. Use for blocking. Retopo or cleanup before animation.

## Live coding (60 min)

Mirrored headset or binoculars; bevel; array of buttons.

---

## Lab

1. Toggle modifier visibility.
2. One boolean hole, then cleanup extra.

---

## Homework

1. Written: apply vs live.
2. Screenshot of modifier stack.

---

## Quiz (10 min)

1. mirror clipping (3)
2. why order (4)
3. export applies? (3)

## Snippet

```
Mirror → Bevel → Triangulate (export)
```

---

## Common mistakes

- Applying every modifier 'to be safe' every five minutes.
- Boolean soup.

---

## Board drawings

1. Stack arrows.

