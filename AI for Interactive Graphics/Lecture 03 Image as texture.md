# Lecture 3 — Image as texture

**Week 3 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** gen → glTF/Three  
**Success check:** Generate or mock an albedo.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/02-asset-table.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: gen → glTF/Three | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
png → TextureLoader
Prompt → map.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Pipeline. Prompt → image → Three.js map.

**Ask:** Generate or mock an albedo? Wait seven seconds. Take two answers.

**Board:** parked strip. Then png → TextureLoader.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *gen → glTF/Three*.

**Do not:** 8k gens.

### Minutes 10–12 — Frame

**Say:** Today’s question: gen → glTF/Three. Kernel: gen → glTF/Three. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: 8k gens.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Pipeline. Prompt → image → Three.js map.

**Say:** Control. Seed, size, retries.

**Say:** Cite. Prompt + model + date in README.

**Ask:** Generate or mock an albedo? Wait seven seconds. Take two answers.

**They do:** On paper: reject 3 images.

**Do not:** put API keys in client JS. Do not skip integrity.

### Minutes 35–50 — Show

**Say:** Live demo: Apply a generated/mock albedo to a sphere; second sphere with a hand-made color for comparison.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** reject 3 images.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: reject 3 images.; budget 1024.. Homework: Written: what you still had to fix by hand.; screenshots.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: gen → glTF/Three | Plant the first common mistake. |
| 10–30 | Apply a generated/mock albedo to a sphere; second sphere with a hand-made color for comparison. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `AI for Interactive Graphics/code/02-asset-table.html` as the after-class check, not as the lecture.

---

## Lab

1. reject 3 images.
2. budget 1024.

---

## Homework

1. Written: what you still had to fix by hand.
2. screenshots.

---

## Quiz next meeting (they hear this now)

1. sRGB (3)
2. why pick among 4 (4)
3. normal map space (3)


## Snippet

```js
map.colorSpace = THREE.SRGBColorSpace;
```

---

## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 03]].

---

## Notes you may still need (from the outline)

**1. Pipeline.** Prompt → image → Three.js map. This is look-dev with a dice roll. Students still know PBR slots from RTR/Blender.

**2. Control.** Seed, size, retries. A human picks among 4, not first-output-wins for the report.

**3. Cite.** Prompt + model + date in README.

---

## Common mistakes

1. 8k gens.
2. claiming PBR from one diffuse.

## If we run long, cut

Cite

## If we run short, add

budget 1024.
