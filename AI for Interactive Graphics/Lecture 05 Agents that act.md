# Lecture 5 — Agents that act

**Course:** AI for Interactive Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** tools, loops  
**Board first:** observe → think → tool → observe

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

1. An agent is a loop with **tools** (set color, load glTF, set camera).
2. Bounded steps.
3. Don't unconstrained 'do anything'.
4. Show the tool log in the UI.
5. Human confirm for spendy tools.

---

## 1. Graphics agents

A chatbot that calls `setMetalness(0.8)` is more IGWT than a generic assistant.

## 2. ReAct name

Thought + action. Teaching level.

## 3. Safety

Allowlist tools. No `eval`.

## Live coding (60 min)

A mock LLM (or real) that can call `setColor` / `resetCamera` on a Three.js scene; log actions.

---

## Lab

1. confirm dialog extra.
2. max 4 steps.

---

## Homework

1. Written: allowlist.
2. demo.

---

## Quiz (10 min)

1. tool (3)
2. why bound steps (4)
3. eval (3)

## Snippet

```js
const tools = { setColor(hex){ mesh.material.color.set(hex); } };
```

---

## Common mistakes

- unbounded agent with shell access.
- hidden tool log.

---

## Board drawings

1. Loop + log.

