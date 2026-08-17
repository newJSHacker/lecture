# Lecture 7 — Tooling

**Course:** Modern JavaScript Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** npm, vite, scripts  
**Board first:** package.json scripts

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

1. npm init.
2. dev script.
3. Vite as the course bundler.
4. gitignore node_modules.
5. Lockfile policy.

---

## 1. Why a bundler

Import maps vs Vite. Course: Vite for Semester 2+ projects that need it. Static serve still OK for tiny labs.

## 2. package.json

scripts, dependencies vs devDependencies.

## 3. Lockfile

Commit it. Reproducible lab machines.

## Live coding (60 min)

Scaffold vite vanilla; import the math module; run dev.

---

## Lab

1. Add a script test that runs node asserts.
2. README.

---

## Homework

1. Written: why lockfile.
2. Code: vite project in repo subfolder.

---

## Quiz (10 min)

1. node_modules in git? (3)
2. dev vs build (4)
3. lockfile (3)

## Snippet

```json
{ "scripts": { "dev": "vite" } }
```

---

## Common mistakes

- Committing node_modules.
- Global npm installs as the only method.

---

## Board drawings

1. Scripts.

