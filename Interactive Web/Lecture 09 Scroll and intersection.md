# Lecture 9 — Scroll and intersection

**Course:** Interactive Web Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** IO, sticky  
**Board first:** intersection ratio

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

1. IntersectionObserver.
2. sticky header.
3. scroll-driven CSS name.
4. Don't scroll-bind layout reads.
5. Lazy images name.

---

## 1. IO

Reveal on enter. Storytelling sites. R3F scroll later.

## 2. Sticky

CSS first.

## 3. Scroll jank

rAF-throttled listeners if you must.

## Live coding (60 min)

Sections that fade in via IO.

---

## Lab

1. Lazy class on images extra.
2. sticky nav.

---

## Homework

1. Written: IO vs scroll listener.
2. Code: reveal.

---

## Quiz (10 min)

1. IO callback (4)
2. sticky (3)
3. layout in scroll (3)

## Snippet

```js
new IntersectionObserver((ents)=>{ /* toggle .in */ }).observe(el);
```

---

## Common mistakes

- onscroll without throttle.
- IO never unobserved.

---

## Board drawings

1. Reveal.

