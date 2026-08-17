# Lecture 4 — HDR and tonemap

**Week 4 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Reinhard / ACES names  
**Success check:** Store HDR color.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: Reinhard / ACES names | Invariant: a frame is a budget; name the pass`

## Board at the end (they photograph this)

```
hdr → [0,1] display
HDR bar.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Need. Sun is >> 1.

**Ask:** Store HDR color? Wait seven seconds. Take two answers.

**Board:** parked strip. Then hdr → [0,1] display.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Reinhard / ACES names*.

**Do not:** Tonemap per light.

### Minutes 10–12 — Frame

**Say:** Today’s question: Reinhard / ACES names. Kernel: Reinhard / ACES names. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: tonemap per light.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Need. Sun is >> 1.

**Say:** Operators. Reinhard, filmic, ACES.

**Say:** sRGB. Tonemap then encode, or a combined output pass.

**Ask:** Store HDR color? Wait seven seconds. Take two answers.

**They do:** On paper: ACES extra name in comments.

**Do not:** invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Live demo: Overbright cube; exposure; Reinhard.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** ACES extra name in comments.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: ACES extra name in comments.; false-color HDR extra.. Homework: Written: why not clamp.; Code: reinhard.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: Reinhard / ACES names | Plant the first common mistake. |
| 10–30 | Overbright cube; exposure; Reinhard. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Real-Time Rendering/code/` as the after-class check, not as the lecture.

---

## Lab

1. ACES extra name in comments.
2. false-color HDR extra.

---

## Homework

1. Written: why not clamp.
2. Code: reinhard.

---

## Quiz next meeting (they hear this now)

1. Reinhard (3)
2. exposure (3)
3. order vs gamma (4)


## Snippet

```glsl
vec3 reinhard(vec3 x){ return x / (1.0 + x); }
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 04]].

---

## Notes you may still need (from the outline)

**1. Need.** Sun is >> 1. Bloom needs leftover energy.

**2. Operators.** Reinhard, filmic, ACES. Pick one for the lab. Document it.

**3. sRGB.** Tonemap then encode, or a combined output pass.

---

## Common mistakes

1. tonemap per light.
2. gamma then tonemap backwards.

## If we run long, cut

sRGB

## If we run short, add

false-color HDR extra.
