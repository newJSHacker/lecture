# Lecture 9 — The DOM

**Course:** Web Technologies  
**Time:** 75 min lecture + 60 min live coding  
**This week:** nodes, createElement  
**Board first:** tree with a new li

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

1. Walk parent/children.
2. createElement + append.
3. Remove a node.
4. Don't rebuild the whole innerHTML for one item.
5. dataset attributes.

---

## 1. The tree is live

Elements tab is the DOM after JS. View-source is not.

## 2. Create vs clone

createElement for one item. templates later.

## 3. Lists

A todo list is the lab. This is the scene graph of the document.

## Live coding (60 min)

Todo: add item, remove item, no framework.

---

## Lab

1. Filter done items.
2. Do not use innerHTML to build the list from a string of tags if the text is user-provided — textContent on a created li.

---

## Homework

1. Written: source vs DOM.
2. Code: list of 20 items created in a loop.

---

## Quiz (10 min)

1. createElement (3)
2. appendChild (3)
3. Why not innerHTML for user text (4)

## Snippet

```js
const li = document.createElement('li');
li.textContent = text;
ul.append(li);
```

---

## Common mistakes

- innerHTML += in a loop (slow and XSS).

---

## Board drawings

1. DOM tree.
2. li append.

