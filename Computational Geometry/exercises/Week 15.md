# Extra exercises — Week 15 (presentations)

Lecture: [[Computational Geometry/Lecture 15 Presentations]]  
Tests demo: [19-kernel-tests.html](../code/19-kernel-tests.html)

There is no new algorithm. Use this sheet as a rehearsal script.

---

## Rehearsal (12 + 5)

Time yourselves once. Hard stop at 12.

| Min | Say / show |
| ---: | --- |
| 0–2 | Problem in one picture |
| 2–6 | Algorithm, one invariant, one complexity sentence |
| 6–10 | Live demo, including one ugly input |
| 10–12 | Limitations, who did what |

Then two questions from the Week 14 list.

## Oral drills (each teammate answers one)

1. Point to the predicate in the kernel. What are its three return values?
2. Point to a test that fails if that predicate flips.
3. Complexity for the n you actually ran.
4. Library vs student code: one file each.
5. Degeneracy: duplicate / collinear / T-junction / cocircular — which one, and what happens.
6. Construction vs predicate in your pipeline.
7. What you would not claim (e.g. “Delaunay is MST”, “EPS is exact”).
8. What breaks in 3D.

## Report last-pass

9. Captions on every figure. “Figure 3. Illegal edge before flip.”
10. No 200-line code dump. 15-line kernel max.
11. No invented timings.
12. Related course ideas: which weeks, which algorithms you did **not** use and why.

## Snippet — presentation timer (optional, TA laptop)

```html
<button id="go">Start 12:00</button>
<pre id="t">12:00</pre>
<script>
let end = 0, id = 0;
document.getElementById("go").onclick = () => {
  end = Date.now() + 12 * 60 * 1000;
  clearInterval(id);
  id = setInterval(() => {
    const s = Math.max(0, Math.ceil((end - Date.now()) / 1000));
    const m = Math.floor(s / 60), r = s % 60;
    document.getElementById("t").textContent =
      String(m).padStart(2, "0") + ":" + String(r).padStart(2, "0") +
      (s === 120 ? "  (10 min warning)" : s === 0 ? "  STOP" : "");
  }, 200);
};
</script>
```
