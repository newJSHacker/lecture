# Lecture 3 — Image as texture

**Week 3 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** prompt → image → Three map; human picks among retries; cite model+date  
**Success check:** they can apply a generated or mock albedo and fill one asset-table row

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/02-asset-table.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: look-dev with a dice roll, still PBR slots | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
prompt → image → map (sRGB)
human picks among 4     not first-output-wins

| file | source | license | gen? | prompt/model | edits |

budget 1024     not 8k
one diffuse ≠ full PBR
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** This is look-dev with a dice roll. They still know albedo vs roughness from RTR/Blender. Claiming PBR from one diffuse fails. Demo 02-asset-table.html.

**Ask:** If the map is 8k, what did we forget? Wait. Want: budget.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *gen → glTF/Three*.

**Do not:** 8k gens.

### Minutes 10–12 — Frame

**Say:** colorSpace sRGB for albedo. Seed, size, retries. Cite prompt + model + date. Reject three images on purpose.

**Ask:** What column is required if generated? is yes?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Pipeline. Then the table — even for a mock PNG.

**Board:** asset table header. Circle gen? and prompt.

**Say:** Second sphere handmade color for comparison.

**Ask:** Why not first-output-wins in the report?

**They do:** Fill one asset-table row for the lab map.

**Do not:** Put API keys in client JS. Skip integrity.

### Minutes 35–50 — Show

**Say:** Mock or real albedo on a sphere; handmade neighbor. Plant 8k. Plant 'I modeled this'. Fill the table.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Apply map + one table row. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: reject 3; budget 1024. Homework: cite the model. Quiz: sRGB, table, not full PBR.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Image → map | Plant client key again. |
| 15–40 | Asset table row | Plant unlabeled Midjourney. |
| 40–55 | 1024 budget | 8k plant. |
| 55–60 | They compare handmade | Circulate. |

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

None this meeting.


## Snippet

```js
map.colorSpace = THREE.SRGBColorSpace;
```

---

## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 03]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. 8k gens.
2. claiming PBR from one diffuse.

## If we run long, cut

Full material gen. Keep albedo + table.

## If we run short, add

Budget 1024 on the board.
