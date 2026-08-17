# Lecture 3 — Semantic HTML and forms

**Course:** Web Technologies  
**Time:** 75 min lecture + 60 min live coding  
**This week:** nav, main, form controls  
**Board first:** label tied to input id

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

1. Use header/main/footer.
2. Build a form with label+input.
3. Choose GET vs POST for a form.
4. Know button types.
5. Don't skip name attributes.

---

## 1. Semantics

Screen readers and the outline. Inclusive teaching: [[Teaching/10 Inclusive Teaching and Accessibility]].

## 2. Forms

input, textarea, select. label[for]. required. This is how a configurator collects a material name later.

## 3. Accessibility

Focus order. Alt text. Color not the only channel.

## Live coding (60 min)

A contact form that logs FormData in the console (no backend).

---

## Lab

1. Fieldset of radio materials.
2. One error message associated with an input.

---

## Homework

1. Written: why label-for.
2. Code: form that prevents default and logs JSON.

---

## Quiz (10 min)

1. main vs div (3)
2. label for (4)
3. button type submit vs button (3)

## Snippet

```html
<label for="email">Email</label>
<input id="email" name="email" type="email" required/>
```

---

## Common mistakes

- Placeholder as label.
- Unlabeled inputs.

---

## Board drawings

1. Page outline.
2. FormData.

