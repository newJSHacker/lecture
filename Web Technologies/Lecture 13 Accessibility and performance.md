# Lecture 13 — Accessibility and performance

**Course:** Web Technologies  
**Time:** 75 min lecture + 60 min live coding  
**This week:** a11y, LCP name  
**Board first:** focus ring on a button

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

1. Keyboard the lab page.
2. Contrast as a requirement.
3. alt on images.
4. Name LCP/CLS teaching-level.
5. Don't ship 10MB hero GIFs.

---

## 1. Keyboard

Tab order. Skip links name. Canvas games need a non-pointer path or a documented limit.

## 2. Performance

Images sized. JS deferred. Later: glTF budgets in Blender week.

## 3. Inclusive

[[Teaching/10 Inclusive Teaching and Accessibility]]

## Live coding (60 min)

Audit the Week 7 page with keyboard + one axe DevTools pass (or checklist).

---

## Lab

1. Fix 3 a11y issues.
2. Compress one image.

---

## Homework

1. Written: three a11y checks.
2. Code: focus styles visible.

---

## Quiz (10 min)

1. alt purpose (3)
2. Why focus ring (4)
3. One perf budget (3)

## Snippet

```css
:focus-visible { outline: 2px solid #1a4f8b; }
```

---

## Common mistakes

- outline: none without a replacement.
- Autoplaying loud video.

---

## Board drawings

1. Tab path.
2. Budget list.

