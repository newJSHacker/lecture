# Lecture 7 — Responsive and media

**Course:** Web Technologies  
**Time:** 75 min lecture + 60 min live coding  
**This week:** viewport, breakpoints  
**Board first:** phone vs laptop frames

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

1. Set viewport meta.
2. Write one min-width media query.
3. Use rem for type.
4. Don't hide essential UI on mobile.
5. Test by resizing, not only a phone emulator.

---

## 1. Viewport

`width=device-width` or the page is 980px shrunk. Required on every IGWT page.

## 2. Breakpoints

Start from the actual layout breaking, not from Bootstrap's numbers. One or two breakpoints is enough.

## 3. Images

max-width: 100%. Later: srcset name only.

## Live coding (60 min)

A page that stacks cards under 640px.

---

## Lab

1. Fix a horizontal overflow.
2. Fluid type with clamp extra.

---

## Homework

1. Written: why viewport meta.
2. Code: two-breakpoint layout.

---

## Quiz (10 min)

1. viewport meta (4)
2. min-width vs max-width (3)
3. max-width 100% on img (3)

## Snippet

```html
<meta name="viewport" content="width=device-width, initial-scale=1"/>
```

---

## Common mistakes

- Only testing at 1920px.
- Tiny tap targets.

---

## Board drawings

1. Frames.
2. Stack vs row.

