# Lecture 11 — Configurator + AI

**Course:** AI for Interactive Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** constrained generation  
**Board first:** SKU allowlist + LLM copy

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

1. The 3D configurator is **structured** (enums).
2. LLM writes copy or suggests from allowlist.
3. Don't let the model invent a SKU.
4. JSON schema name.
5. Human confirm apply.

---

## 1. Pattern

Graphics product: parts, materials, camera beats. AI is a **salesperson**, not the CAD kernel.

## 2. Schema

Model must return `{part, finish}` from enums. Parse + validate.

## 3. Undo

Every apply is undoable.

## Live coding (60 min)

Three finishes; LLM (or mock) may only pick among them; apply on confirm.

---

## Lab

1. invalid JSON handling.
2. undo.

---

## Homework

1. Written: why allowlist.
2. demo.

---

## Quiz (10 min)

1. SKU invent (4)
2. schema (3)
3. undo (3)

## Snippet

```js
if (!FINISHES.includes(data.finish)) throw new Error('invalid');
```

---

## Common mistakes

- freeform 'make it gold-er' writing new shaders.
- no validate.

---

## Board drawings

1. Enums + confirm.

