# Lecture 2 — Color and gamma

**Week 2 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** pow(c, 2.2) decode; light in linear; encode for the monitor  
**Success check:** they can decode sRGB, Lambert in linear, and say why lighting in sRGB looks wrong

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: stop lighting in display space | Invariant: lighting is linear; the monitor is sRGB; pow is a teaching approx, not a CMS`

## Board at the end (they photograph this)

```
sRGB texel  --pow 2.2-->  linear  --Lambert-->  linear
linear      --pow 1/2.2->  sRGB display

do not pow(normal)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Two gradients: encoded vs forgotten encode | photograph; do not draw a color-managed UI |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Computer Graphics I named gamma. Today it is three lines in GLSL. If they light in sRGB they will later call PBR 'grey' in Real-Time Rendering.

**Ask:** Do you pow the normal? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *linear vs sRGB*.

**Do not:** Pow on normals.

### Minutes 10–12 — Frame

**Say:** Decode albedo. Light. Encode. SRGB8_ALPHA8 and Three.js colorSpace are names. pow(c, 2.2) is the teaching curve.

**Ask:** If you skip encode, who looks wrong — the shader or the monitor?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Two gradients on the board: linear ramp displayed raw vs encoded.

**Board:** toLinear / toSRGB. Circle albedo, not n.

**Say:** WebGL sRGB textures do the decode if you set the internal format — still write the helper once so they see it.

**Ask:** Write toLinear in one line.

**They do:** On paper: Lambert in linear for a white albedo 0.8 — do not pow n.

**Do not:** Paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Gradient with and without encode; screenshot both. Plant pow on a normal. Toggle encode. Local files only.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Light a Lambert quad in linear; toggle encode. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: Lambert linear + toggle. Homework: why lighting in sRGB is wrong; encode helper. Quiz: decode formula, double gamma, albedo space.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Two gradients | Plant skipped encode; blame the monitor. |
| 10–30 | Lambert in linear | Plant pow(normal). |
| 30–45 | Toggle encode | They see the mid-greys move. |
| 45–60 | They write the helpers | Circulate. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. Light a Lambert quad in linear.
2. Toggle encode.

---

## Homework

1. Written: why lighting in sRGB looks wrong.
2. Code: encode helper.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
vec3 toLinear(vec3 c){ return pow(c, vec3(2.2)); }
vec3 toSRGB(vec3 c){ return pow(c, vec3(1.0/2.2)); }
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 02]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. pow on normals.
2. Skipping encode and blaming the monitor.

## If we run long, cut

ICC profiles. Keep decode + Lambert + encode.

## If we run short, add

SRGB8_ALPHA8 as a name.
