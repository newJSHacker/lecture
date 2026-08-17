# Lecture 11 — Blinn-Phong and gamma

**Week 11 of 15** · Computer Graphics I  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Blinn: h=normalize(l+v); spec=(max(0,n·h))^shininess; linear light; pow(c,1/2.2) at the end  
**Success check:** the highlight moves with the camera; gamma toggle is visible; two lights sum; they say this is not PBR

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Computer Graphics/code/11-perspective.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: specular and a gamma-aware output | Invariant: a picture is an array; putPixel lives in pixels`

## Board at the end (they photograph this)

```
v = normalize(eye − p)          same space as n
Phong: r = reflect(−l, n)       spec = (max(0,r·v))^s
Blinn: h = normalize(l + v)     spec = (max(0,n·h))^s

if n·l ≤ 0: skip spec

light in linear
out: pow(linear, 1/2.2) then *255

not energy-conserving; PBR is Semester 4
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Lambert is the moon. Specular is the highlight that depends on v. If the highlight does not move when the camera moves, they used a constant v. Do not invent fps; do not raise shininess until it looks Instagram.

**Ask:** Half-vector formula? Wait. Want: normalize(l+v).

**Board:** parked strip. Then reflection r vs half-vector h.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Blinn-Phong; linear lighting; gamma encode*.

**Do not:** `v` as (0,0,1) forever.

### Minutes 10–12 — Frame

**Say:** Shininess 16–64 for a cube; 256 is a pin spark; 0.5 is not roughness. Sum lights then min(1,color) or float then encode once. HDR/bloom is Real-Time Rendering. Toggle wrong (light in sRGB) vs right — the wrong one often ‘looks contrasty’; the projector lies; the policy stands.

**Ask:** Where does gamma encode happen?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Is Blinn-Phong PBR? No.

**Board:** n,l,v,r,h. Linear add vs sRGB add. Two lights, two highlights.

**Say:** Per-pixel: interpolate n, normalize, shade — if Gouraud from last week works.

**Ask:** Why skip spec when n·l<0?

**They do:** On paper: h vs r, one picture. Why lighting in sRGB is wrong, one paragraph.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Blinn-Phong cube, shininess slider, two lights, gamma toggle, specular-only (kd=0). Demo 14-blinn-phong.html. Plant v=(0,0,1) forever. Plant adding spec in sRGB then encoding again.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** blinnPhong tests: n=l=v → spec>0; n opposite l → spec 0. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: two lights; gamma encode; debug keys N/L/S. Homework: shininess slider in README. Quiz: h, skip spec, where encode, not PBR.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | h vs r on the board | They copy. |
| 15–40 | Highlight vs camera | Must move. Constant v is the plant. |
| 40–50 | Gamma toggle | Do not invent a Lighthouse score. |
| 50–60 | Two lights | Clip uint8; mention it. |

Point them at `Computer Graphics/code/11-perspective.html` as the after-class check, not as the lecture.

---

## Lab

1. `blinnPhong(...)` with tests: n=l=v → spec > 0; n opposite l → spec 0.
2. Two directional lights.
3. Gamma encode function.
4. Debug keys: N (normals), L (diffuse only), S (spec only).

---

## Homework

1. Written: h vs r, one picture.
2. Written: why lighting in sRGB is wrong (one paragraph).
3. Code: shininess slider documented in README.

---

## Quiz next meeting (they hear this now)

1. Half-vector formula. (2 pts)
2. Why skip spec when n·l < 0? (2 pts)
3. Where does gamma encode happen? (3 pts)
4. Is Blinn-Phong PBR? Yes/no. (3 pts)


## Extra exercises

See [[Computer Graphics/exercises/Week 11]].

---

## Notes you may still need (from the outline)

**1. Specular (20 min).** Viewer `v = normalize(eye - p)` (world or view — same space as n).
Phong: `r = reflect(-l, n)`, spec = `(max(0, r·v))^shininess`.
Blinn: `h = normalize(l + v)`, spec = `(max(0, n·h))^shininess`.
Cheaper and the default in most real-time teaching. Shininess 16–64 for a cube; 256 is a pin spark.
```
color = ka * ambient
      + kd * max(0, n·l) * lightColor
      + ks * pow(max(0, n·h), shininess) * lightColor
```
If `n·l ≤ 0`, skip specular (light is behind the surface).
**PBR** (Semester 4): microfacets, energy conservation, IBL. Name it. Do not implement Cook-Torrance this week.
---

**2. Many lights (15 min).** Sum contributions. uint8 will clip: `min(1, color)` or store float and encode once. HDR / bloom is Real-Time Rendering. Here: clip and mention the limitation in the report.
---

**3. Gamma (20 min).** Policy from Week 2, now enforced:
1. Textures / vertex colors: treat 8-bit as sRGB → `pow(c/255, 2.2)` (approx).
2. Lights and Lambert in linear.
3. Output: `pow(linear, 1/2.2)` then * 255.
Toggle in the demo: wrong (light in sRGB) vs right. The wrong one often “looks contrasty” and students prefer it — tell them the projector lies, the policy stands.
Full sRGB curve (2.4 piecewise) is optional extra credit, not required.
---

---

## Common mistakes

1. `v` as (0,0,1) forever.
2. Adding spec in sRGB then gamma-encoding again.
3. Shininess 0.5 because they thought it was a 0–1 roughness (it is an exponent).

## If we run long, cut

Cook-Torrance. Keep Blinn + encode at the end.

## If we run short, add

Normals-as-color debug already from Week 10.
