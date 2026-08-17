#!/usr/bin/env python3
"""Rewrite thin IGWT lecture outlines into Teaching/24 session guides.

Skips files that already have minute-by-minute Say/Ask/Board blocks
(Programming Lectures 1–2). Wraps Computer Graphics / Computational Geometry
with a session-guide header and keeps their detailed bodies.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------------
# Course metadata
# ---------------------------------------------------------------------------

COURSE_INVARIANT = {
    "Introduction to Programming": "a computer only follows instructions",
    "Web Technologies": "the browser requests, parses, then paints",
    "Mathematics for Computer Graphics": "point ≠ vector; freeze the convention",
    "Modern JavaScript Development": "one binding, one module, no hidden globals",
    "Interactive Web Development": "time is rAF; input is events; draw is a function",
    "WebGL Programming": "CPU fills buffers; GPU runs the shader; P*V*M; CCW",
    "Three.js Development": "Three.js is an engine, not the algorithm",
    "Blender for Real-Time Graphics": "units, facing, and budget travel with the asset",
    "Shader Programming": "a shader is a program over pixels or vertices",
    "Real-Time Rendering": "a frame is a budget; name the pass",
    "GPU Programming": "data lives where the kernel runs",
    "Interactive Experience Development": "3D and DOM are two clocks",
    "Virtual and Augmented Reality": "comfort and tracking beat extra polygons",
    "AI for Interactive Graphics": "no secrets in the frontend; cite the model",
    "Advanced Computer Graphics": "local lighting is bounce 0; GI is the rest",
    "Capstone Project": "the problem is users, not a tech list",
    "Computer Graphics I": "a picture is an array; putPixel lives in pixels",
    "Computational Geometry": "predicates before constructions; degeneracy is the course",
}

COURSE_DO_NOT = {
    "Introduction to Programming": "Mix Python syntax into a JS term. Skip the attempt.",
    "Web Technologies": "Lecture HTML as a visual design tool. Use a CDN.",
    "Mathematics for Computer Graphics": "Start with eigenvalues. Mix row-vector formulas.",
    "Modern JavaScript Development": "Install a new bundler mid-lecture. Use a CDN.",
    "Interactive Web Development": "Start with Three.js. Canvas 2D is the kernel.",
    "WebGL Programming": "Wrap the first triangle in Three.js. Unfreeze conventions.",
    "Three.js Development": "Treat the inspector as the renderer. Load Three from a CDN.",
    "Blender for Real-Time Graphics": "Model at unknown scale. Skip apply rotation.",
    "Shader Programming": "Paste a 200-line Shadertoy as the first kernel.",
    "Real-Time Rendering": "Invent fps numbers. Measure or omit.",
    "GPU Programming": "Require CUDA. Stay in the browser (WebGL/WebGPU).",
    "Interactive Experience Development": "Fight React state with the frame loop silently.",
    "Virtual and Augmented Reality": "Require a headset to pass week 1. Skip the desktop fallback.",
    "AI for Interactive Graphics": "Put API keys in client JS. Skip integrity.",
    "Advanced Computer Graphics": "Start with a production path tracer.",
    "Capstone Project": "Start in an engine before the problem statement.",
}

DEMOS = {
    ("Introduction to Programming", 3): "Programming/code/03-grade.html",
    ("Introduction to Programming", 4): "Programming/code/04-checker.html",
    ("Introduction to Programming", 5): "Programming/code/05-clamp.html",
    ("Introduction to Programming", 6): "Programming/code/06-arrays.html",
    ("Introduction to Programming", 7): "Programming/code/07-centroid.html",
    ("Introduction to Programming", 8): "Programming/code/05-clamp.html",
    ("Introduction to Programming", 9): "Programming/code/08-search.html",
    ("Introduction to Programming", 10): "Programming/code/09-sort.html",
    ("Introduction to Programming", 11): "Programming/code/10-fact.html",
    ("Introduction to Programming", 12): "Programming/code/05-clamp.html",
    ("Introduction to Programming", 13): "Programming/code/11-point.html",
    ("Introduction to Programming", 14): "Programming/code/12-sandbox.html",
    ("Mathematics for Computer Graphics", 1): "Mathematics for Computer Graphics/code/01-axes.html",
    ("Mathematics for Computer Graphics", 2): "Mathematics for Computer Graphics/code/02-add.html",
    ("Mathematics for Computer Graphics", 3): "Mathematics for Computer Graphics/code/03-dot.html",
    ("Mathematics for Computer Graphics", 4): "Mathematics for Computer Graphics/code/04-cross.html",
    ("Mathematics for Computer Graphics", 5): "Mathematics for Computer Graphics/code/05-line.html",
    ("Mathematics for Computer Graphics", 6): "Mathematics for Computer Graphics/code/06-matmul.html",
    ("Mathematics for Computer Graphics", 7): "Mathematics for Computer Graphics/code/06-matmul.html",
    ("Mathematics for Computer Graphics", 8): "Mathematics for Computer Graphics/code/10-pvm.html",
    ("Mathematics for Computer Graphics", 9): "Mathematics for Computer Graphics/code/07-rotate.html",
    ("Mathematics for Computer Graphics", 10): "Mathematics for Computer Graphics/code/07-rotate.html",
    ("Mathematics for Computer Graphics", 11): "Mathematics for Computer Graphics/code/08-bezier.html",
    ("Mathematics for Computer Graphics", 12): "Mathematics for Computer Graphics/code/09-lookat.html",
    ("Mathematics for Computer Graphics", 13): "Mathematics for Computer Graphics/code/10-pvm.html",
    ("Web Technologies", 1): "Web Technologies/code/01-skeleton.html",
    ("Web Technologies", 2): "Web Technologies/code/01-skeleton.html",
    ("Web Technologies", 3): "Web Technologies/code/02-form.html",
    ("Web Technologies", 4): "Web Technologies/code/03-box.html",
    ("Web Technologies", 5): "Web Technologies/code/04-flex.html",
    ("Web Technologies", 6): "Web Technologies/code/05-grid.html",
    ("Web Technologies", 7): "Web Technologies/code/06-responsive.html",
    ("Web Technologies", 9): "Web Technologies/code/07-toggle.html",
    ("Web Technologies", 10): "Web Technologies/code/07-toggle.html",
    ("Web Technologies", 11): "Web Technologies/code/09-fetch.html",
    ("Web Technologies", 12): "Web Technologies/code/10-transform.html",
    ("Modern JavaScript Development", 1): "Modern JavaScript/code/01-arrows.html",
    ("Modern JavaScript Development", 2): "Modern JavaScript/code/02-spread.html",
    ("Modern JavaScript Development", 3): "Modern JavaScript/code/08-modules.html",
    ("Modern JavaScript Development", 4): "Modern JavaScript/code/03-promise.html",
    ("Modern JavaScript Development", 5): "Modern JavaScript/code/04-async.html",
    ("Modern JavaScript Development", 9): "Modern JavaScript/code/05-mapset.html",
    ("Modern JavaScript Development", 10): "Modern JavaScript/code/06-closure.html",
    ("Modern JavaScript Development", 11): "Modern JavaScript/code/07-loop.html",
    ("Interactive Web Development", 1): "Interactive Web/code/01-canvas.html",
    ("Interactive Web Development", 2): "Interactive Web/code/02-raf.html",
    ("Interactive Web Development", 3): "Interactive Web/code/03-pointer.html",
    ("Interactive Web Development", 7): "Interactive Web/code/09-gsap.html",
    ("Blender for Real-Time Graphics", 1): "Blender/code/01-units.html",
    ("Blender for Real-Time Graphics", 11): "Blender/code/02-export.html",
    ("Blender for Real-Time Graphics", 12): "Blender/code/03-budget.html",
    ("AI for Interactive Graphics", 2): "AI for Interactive Graphics/code/01-proxy-mock.html",
    ("AI for Interactive Graphics", 3): "AI for Interactive Graphics/code/02-asset-table.html",
    ("Advanced Computer Graphics", 2): "Advanced Computer Graphics/code/01-radiosity2.html",
    ("Advanced Computer Graphics", 3): "Advanced Computer Graphics/code/02-tracer.html",
    ("GPU Programming", 2): "GPU Programming/code/01-pong.html",
    ("Capstone Project", 1): "Capstone/code/01-moscow.html",
    ("Capstone Project", 11): "Capstone/code/02-readme.html",
    ("Capstone Project", 7): "Capstone/code/03-budget.html",
    ("WebGL Programming", 1): "WebGL/demos/index.html",
    ("Three.js Development", 1): "ThreeJS/demos/01-hello-cube.html",
    ("Shader Programming", 1): "WebGL/shadertoy/index.html",
}

FOLDER_COURSE = {
    "Programming": "Introduction to Programming",
    "Web Technologies": "Web Technologies",
    "Mathematics for Computer Graphics": "Mathematics for Computer Graphics",
    "Modern JavaScript": "Modern JavaScript Development",
    "Interactive Web": "Interactive Web Development",
    "WebGL Programming": "WebGL Programming",
    "ThreeJS Development": "Three.js Development",
    "Blender": "Blender for Real-Time Graphics",
    "Shader Programming": "Shader Programming",
    "Real-Time Rendering": "Real-Time Rendering",
    "GPU Programming": "GPU Programming",
    "Interactive Experience": "Interactive Experience Development",
    "XR": "Virtual and Augmented Reality",
    "AI for Interactive Graphics": "AI for Interactive Graphics",
    "Advanced Computer Graphics": "Advanced Computer Graphics",
    "Capstone": "Capstone Project",
    "Computer Graphics": "Computer Graphics I",
    "Computational Geometry": "Computational Geometry",
}

# Extra teaching lines keyed by (course, week). Optional; parser fills the rest.
GOLD: dict[tuple[str, int], dict] = {}


def gold_load() -> None:
    """Fill GOLD for Programming 3–15 and Math 1–15, then extra catalogs."""
    P = "Introduction to Programming"
    M = "Mathematics for Computer Graphics"

    GOLD[(P, 3)] = dict(
        kernel="`if (x === 0)` and the live bug `if (x = 0)`",
        success="every student has used `===` in the attempt and can say why `=` inside `if` is a bug",
        invariant="a condition is a yes/no; assignment is not a question",
        goal="branch on a fact",
        board="""```
if (cond) { … } else if { … } else { … }

===  compare value and type
=    assign (forbidden as the condition)

&&  both     ||  either     !  not
NaN === NaN  →  false
```""",
        slides=[("Screenshot of `if (x = 0)` assigning 0 and taking the true branch", "the console lie is a photo")],
        hook_say="Last time we named values. Today the program chooses. A graphics program that cannot refuse a bad input is a black screen later — `if (!gl)` is this lecture in WebGL.",
        hook_ask="What is the difference between `=` and `===`? Wait seven seconds. Take two answers. Then write both on the board.",
        frame_say="We use `===` and `!==` in this course. I will show `==` once as a bug. Nested `if` more than two deep is a smell — extract a function (Lecture 5).",
        frame_ask="What should a program do when the WebGL context is null?",
        build=[
            "**Say:** A boolean is `true` or `false`. Comparisons produce booleans. `===` asks: same value **and** same type.",
            "**Board:** a diamond: condition → true path / false path. Then the three-way `if / else if / else`.",
            "**Say:** `&&` both, `||` either, `!` not. `NaN === NaN` is false — show it. That is why we never test NaN with `===`.",
        ],
        ask_build="Predict `0 == ''`. Hands. Then show `true`. Then `0 === ''` → `false`. That is why `==` is banned.",
        they_build="On paper: write the `if` for age ≥ 18. Collect two papers.",
        show_say="I will write a grade classifier: A/B/C/F. Then I will plant `if (score = 0)`. Watch the console. I will read the result out loud. Then I will fix it to `===`.",
        attempt_say="Fizz for multiples of 3 (not Buzz yet). Use `%` and `=== 0`. Eight minutes. I do not help for three.",
        land_say="Photograph the board. Lab: guessing game 1–10 and fizz. Homework: rock-paper-scissors and a paragraph on `==` vs `===`. Quiz next time: `0 == ''`, age `if`, why `===`.",
        live=[
            ("0–10", "Grade classifier with `===`", "Plant a missing `else`. Fix: F is the else."),
            ("10–30", "`if (score = 0)`", "Plant on purpose. Fix `===`. Write `=` vs `===` again."),
            ("30–45", "`NaN === NaN`", "Show false. “Flashlight, not a design tool.”"),
            ("45–60", "They type the guessing-game kernel", "Circulate. Do not sit."),
        ],
        cut="Nested if examples. Keep `===` and the assignment bug.",
        add="`&&` short-circuit: `gl && gl.drawArrays`. Still no `==` in student code.",
    )
    GOLD[(P, 4)] = dict(
        kernel="`for (let i = 0; i < n; i++)` and an 8×8 checkerboard in the console",
        success="they can say how many times `i < 10` from 0 runs (10) and print two nested loops",
        invariant="the loop variable counts 0 .. n−1 unless you have a reason",
        goal="repeat without copy-paste",
        board="""```
for (let i = 0; i < n; i++) { … }     // n times, i = 0..n-1

fenceposts:  4 posts, 3 rails
nested:      n * n cells

invariant of sum: after k steps, s is the sum of the first k items
```""",
        slides=[("Optional: a photo of a picket fence", "only if you will not draw four posts")],
        hook_say="If you can write a loop, you can walk pixels. Computer Graphics I is nested loops over a triangle. Today we walk numbers.",
        hook_ask="How many times does `for (let i = 0; i < 10; i++)` run? Wait. Want: 10, not 9, not 11.",
        frame_say="`for` is the default. `while` is for unknown count. Off-by-one is the professional disease. We draw fenceposts.",
        frame_ask="Is the last index of an array of length n `n` or `n-1`?",
        build=[
            "**Say:** `i` from 0 inclusive to `n` exclusive. That is vertices, pixels, and students in a list.",
            "**Board:** four posts, three rails. Inclusive vs exclusive end.",
            "**Say:** Nested loops make a grid. A checkerboard is `#.` rows. Infinite loop: `i` never changes, or `while (true)` with no `break`.",
        ],
        ask_build="If the inner loop runs n times and the outer n times, how many cells? Want: n².",
        they_build="On paper: trace `s = 0; for i in 0..3: s += i`. What is s?",
        show_say="I print a triangle of stars, then an 8×8 checkerboard. Zoom 140%. I will plant `i <= a.length` later in live coding and crash.",
        attempt_say="Sum 1..100 in a loop. Eight minutes. Then we write the invariant: after k steps, s is the sum of 1..k.",
        land_say="Lab: sum and a prime checker n ≤ 200. Homework: FizzBuzz 1..100 and the invariant paragraph. Quiz: how many times `i < 10`, infinite loop, n×n count.",
        live=[
            ("0–10", "Sum 1..10, narrate the invariant", "Plant `i <= 10` extra iteration. Fix `<`."),
            ("10–30", "Triangle of stars", "Off-by-one on the inner bound."),
            ("30–45", "8×8 checkerboard", "Plant `i <= a.length` if using an array."),
            ("45–60", "They type sum 1..100", "Circulate."),
        ],
        cut="Prime checker derivation. Keep 0..n−1 and nested loops.",
        add="`break` / `continue` names. Still no `forEach` as the required kernel.",
    )
    GOLD[(P, 5)] = dict(
        kernel="`clamp(x,a,b)` and `lerp(a,b,t)` with `console.assert`",
        success="they write a function that **returns** a value, not only `console.log`",
        invariant="parameters in, one return out; locals die at the brace",
        goal="name a recipe",
        board="""```
        in →  [ clamp ]  → out
               x, a, b

function clamp(x, a, b) {
  return Math.max(a, Math.min(b, x));
}

missing return  →  undefined
```""",
        slides=[],
        hook_say="A function is a named recipe. `putPixel`, `dot`, `orient` later are functions. If you cannot write `clamp`, you cannot write a renderer.",
        hook_ask="What does a function return if you forget `return`? Wait. Want: `undefined`.",
        frame_say="Parameters are local names. Arguments are the values you pass. `console.log` inside is a side effect — fine for debugging, not the result of a math helper.",
        frame_ask="Is `clamp` allowed to print instead of returning? Want: no.",
        build=[
            "**Say:** Draw a box. Arrows in: `x,a,b`. Arrow out: the clamped number.",
            "**Board:** two stack frames: `main` calls `clamp`. Locals of `clamp` are not visible in `main`.",
            "**Say:** `let` is block-scoped. Loop `i` dies after the `for`. No globals for math helpers. Name functions with verbs: `clamp`, `lerp`, `countVowels`.",
        ],
        ask_build="Why `const` for `t` in lerp? Want: we do not rebind t.",
        they_build="On paper: write `lerp(a,b,t)` in one line.",
        show_say="I implement `clamp`, `lerp`, `min3`. I `console.assert(lerp(0,10,0.5)===5)`. When an assert fails, I read it out loud.",
        attempt_say="Write `isEven` and `max3` that **return**. Eight minutes. I reject solutions that only log.",
        land_say="Lab: isEven, max3, countVowels. Homework: 8 tests for lerp; side effect vs return. Quiz: missing return, `let` in for, write clamp.",
        live=[
            ("0–10", "`clamp` with asserts", "Plant a swapped min/max."),
            ("10–30", "`lerp`", "Plant `a + t*b` wrong formula. Fix `a + (b-a)*t`."),
            ("30–45", "`min3`", "Show nested calls."),
            ("45–60", "They write countVowels kernel", "Circulate."),
        ],
        cut="Closures. They wait until Modern JS.",
        add="A function that returns another function — name only.",
    )
    GOLD[(P, 6)] = dict(
        kernel="`const b = a.slice()` and average / max-index of an array",
        success="they can say whether two names point at the same array (alias) or a copy",
        invariant="index 0 is the first; `length-1` is the last; `push` mutates even on `const`",
        goal="store many values",
        board="""```
[  10 |  20 |  30 ]     indices 0, 1, 2
         ↑
       a[1]

const a = [];  a.push(1);   // legal: const blocks rebind, not mutation
const b = a;     // alias
const c = a.slice();  // copy
```""",
        slides=[],
        hook_say="Vertices will be arrays of points. An off-by-one here is a missing triangle in Computer Graphics I. Today: index, push, copy.",
        hook_ask="What is the index of the last element of `a`? Wait. Want: `a.length - 1`.",
        frame_say="`map`/`filter` are names only this week. Required kernel is a `for` loop. `const a = []` can still `push`.",
        frame_ask="Does `const a = []` mean the array cannot grow?",
        build=[
            "**Say:** Boxes 0..n−1. Holes (`a[9]` when length 3) are forbidden in this course.",
            "**Board:** alias vs copy. Two arrows to one row vs two rows.",
            "**Say:** `a = a.push(x)` is a bug: `push` returns the new length. Copy with `slice` before you sort if you need the original.",
        ],
        ask_build="After `const b = a; b.push(1)`, what is `a.length`?",
        they_build="On paper: reverse a 4-element array on a copy.",
        show_say="Average of an array; then index of the max. I will plant `a = a.push(x)` and read the number that appears.",
        attempt_say="Reverse a **copy**. Do not mutate the original. Eight minutes.",
        land_say="Lab: reverse copy; remove duplicates with nested loop (n small). Homework: letter histogram; index vs value. Quiz: last index, push return, copy vs alias.",
        live=[
            ("0–10", "Build an array with push", "Plant `a = a.push`."),
            ("10–30", "Average and max index", "Off-by-one on the loop."),
            ("30–45", "`slice` vs alias", "Mutate both; show the shared row."),
            ("45–60", "They reverse a copy", "Circulate."),
        ],
        cut="`map` as required. Keep for-loop + slice.",
        add="`for...of` vs index when you need the i.",
    )
    GOLD[(P, 7)] = dict(
        kernel="`const p = { x, y }` and centroid of an array of points",
        success="they read `p.y` and can stringify a point without functions inside",
        invariant="an object is named fields; an array is ordered slots — do not use objects as lists",
        goal="name the parts of a thing",
        board="""```
p = { x: 1, y: 2 }      p.x      p['x']

centroid = average of {x,y} points

JSON:  '{"x":1,"y":2}'   no functions, no NaN
```""",
        slides=[("Optional: JSON of a point in DevTools", "the quotes are easier to photograph")],
        hook_say="A mesh vertex is `{x,y,z}`. A student is `{name, scores: []}`. Today we make records. Midterm next week on values through objects.",
        hook_ask="How do you read y of `{x:1, y:2}`? Wait. Want: `p.y`.",
        frame_say="Dot when you know the key. Brackets when the key is in a variable. `p[x]` without quotes looks up a variable named x — usually a bug.",
        frame_ask="When would you use `p[key]` instead of `p.x`?",
        build=[
            "**Say:** Nesting: `{ name, scores: [] }`. This is the address book.",
            "**Board:** point record. Arrow from `p` to a box with x and y.",
            "**Say:** `JSON.stringify` / `parse`. JSON cannot store functions or NaN. Clipboard paste is enough; file I/O waits.",
        ],
        ask_build="Is `[0,1,2]` or `{0:0,1:1,2:2}` the list? Want: the array.",
        they_build="On paper: write a point and a student with three scores.",
        show_say="Array of `{x,y}`; compute centroid. Assert it. Plant `p[x]` without quotes.",
        attempt_say="Three-person address book as objects in an array. Eight minutes.",
        land_say="Photograph the board. Lab: address book; comment on shallow vs deep copy. Homework: parse JSON of points, sum x. Quiz next meeting is the midterm topic list — objects included. Midterm is Lecture 8, on paper.",
        live=[
            ("0–10", "Literal `{x,y}`", "Plant `p[x]`."),
            ("10–30", "Centroid", "Empty array: decide a policy, do not crash."),
            ("30–45", "stringify / parse", "Show functions disappear."),
            ("45–60", "They build the address book", "Circulate."),
        ],
        cut="Deep clone algorithms. Keep literal + centroid.",
        add="Optional chaining `p?.x` name only.",
    )
    GOLD[(P, 8)] = dict(
        kernel="read a stack trace; `console.assert`; one breakpoint",
        success="after the exam, they can point at the first stack line of a planted bug",
        invariant="syntax vs runtime vs wrong answer are three different diseases",
        goal="sit the midterm, then debug",
        board="""```
syntax     red squiggle / failed to parse
runtime    throws: TypeError, ReferenceError
wrong      runs, lies

read the FIRST line of the stack
console.assert(clamp(5,0,3)===3, 'clamp high')
```""",
        slides=[("A real TypeError stack, first line circled", "do not draw Chrome’s UI")],
        hook_say="This meeting is a **midterm**, then a short lecture on debugging. No laptop for the exam.",
        hook_ask=None,
        frame_say="Exam: values, if, loops, functions, arrays, objects. Then we debug.",
        frame_ask=None,
        kind="midterm",
        midterm_topics="values and `'3'+1`; `let`/`const`; `===`; loops 0..n−1; functions that return; arrays (copy vs alias); objects `{x,y}`.",
        show_say="After collection: a broken `average` that divides by `length-1`. Breakpoint on the return. `console.assert`.",
        attempt_say="They fix one planted bug in a starter after the exam (if time). Otherwise this is the lab.",
        land_say="Lab: three planted bugs and 5 asserts for last week’s centroid. Homework: rewrite one missed midterm item. No quiz next — wait, quiz Lecture 9 on search. Next lecture is search.",
        live=[
            ("0–15", "Broken average + breakpoint", "They watch you; then they try."),
            ("15–40", "Three error kinds on the board", "Plant a silent wrong answer (no throw)."),
            ("40–60", "They write asserts for centroid", "Circulate."),
        ],
        cut="Live coding if the exam ran long. Keep the error-kinds board.",
        add="Binary-search a bug: comment out half.",
    )
    GOLD[(P, 9)] = dict(
        kernel="linear search and binary search on the same sorted array; log comparison counts",
        success="they state the sorted precondition of binary search and have a test that fails on unsorted input",
        invariant="binary search is allowed only on sorted data; mid is an integer index",
        goal="find a value without scanning everything — when you may",
        board="""```
linear:  scan 0..n-1          Θ(n)
binary:  sorted!  mid probe    Θ(log n)

while (lo <= hi) {
  const mid = (lo + hi) >> 1;   // integer, not /2 float
  …
}
```""",
        slides=[],
        hook_say="Picking, BVH, kd-trees are search. Binary search is the warmup. Today we count comparisons — we do not invent timings.",
        hook_ask="If the array is not sorted, may I binary search? Wait. Want: no.",
        frame_say="Linear is always correct and slow. Binary is fast and **wrong** if unsorted. Off-by-one in `hi` is the classic bug.",
        frame_ask="What is the mid index of length 8, lo=0, hi=7?",
        build=[
            "**Say:** Linear: walk until found or end. Return index or −1.",
            "**Board:** sorted row of numbers; circle the mid probe; shrink left or right.",
            "**Say:** Teaching-level Θ(n) vs Θ(log n). Doubling n adds one comparison in binary, not a doubling. `mid = (lo+hi)/2` can be a float — we use `>> 1` or `Math.floor`.",
        ],
        ask_build="Worst-case comparisons for linear on n=100? Want: 100.",
        they_build="On paper: binary-search trace for 7 in `[1,3,4,7,9]`. Write lo, hi, mid each step.",
        show_say="Both searches on the same array. Log comparison counts. Then I feed unsorted data to binary and it lies.",
        attempt_say="Tests: found, missing, empty, one element. Plant unsorted and show binary fail. Eight minutes for the test list even if code is incomplete.",
        land_say="Lab: those tests. Homework: one page why sorted is required; optional recursive binary. Quiz: precondition, linear worst case, mid formula.",
        live=[
            ("0–10", "Linear search", "Return −1 policy."),
            ("10–35", "Binary search", "Plant `hi = mid` infinite loop. Fix `mid-1` / `mid+1`."),
            ("35–50", "Unsorted trap", "Show a wrong index."),
            ("50–60", "They add empty-array test", "Circulate."),
        ],
        cut="Recursive binary. Keep iterative + precondition.",
        add="Count comparisons in a table for n=16.",
    )
    GOLD[(P, 10)] = dict(
        kernel="selection sort by hand and in code; count swaps; measure n=1000 vs 2000",
        success="they can run selection sort on 6 numbers on paper and not call `array.sort` in the lab",
        invariant="nested loops over n are Θ(n²) teaching-level; doubling n roughly quadruples that work",
        goal="put an array in order and say why it costs",
        board="""```
selection: for i: find min in i..n-1; swap into i

n cards → n² comparisons (teaching picture)

built-in:  array.sort((a,b)=>a-b)   // exists; not the lab
```""",
        slides=[("Optional: stopwatch photo of two n’s on **this** machine", "never invent a millisecond")],
        hook_say="Sorting is so you can binary search. We implement selection sort so you **feel** n². Built-in sort exists; it is not today’s lab.",
        hook_ask="If n doubles, what happens to nested-loop work? Wait. Want: about four times, not two.",
        frame_say="Find min, swap to front. Easy to see. No Master theorem. No invented timings — if we time, we time on this machine.",
        frame_ask="May you call `.sort` in the lab? Want: no.",
        build=[
            "**Say:** Trace 6 numbers on the board. Circle the min each pass.",
            "**Board:** n vs n² sketch. Label “teaching picture, not a proof.”",
            "**Say:** `array.sort((a,b)=>a-b)` — remember the comparator or you get lexicographic strings. Project may use built-in; lab may not.",
        ],
        ask_build="How many times does the inner loop run, roughly? Want: about n²/2.",
        they_build="On paper: one pass of selection sort on `[4,1,3,2]`.",
        show_say="Sort 12 numbers on the board then in code. Count swaps. I will not quote an fps or a millisecond I did not measure.",
        attempt_say="Implement selection sort on a 6-element array. Tests: already sorted, reversed, duplicates.",
        land_say="Lab: selection sort + tests; **measure** n=1000 vs 2000 (write the numbers you saw). Homework: why n²; insertion sort optional. Quiz: idea, doubling, built-in in project?",
        live=[
            ("0–15", "Trace 6 numbers", "They copy the board."),
            ("15–40", "Implement", "Plant `.sort` as a “shortcut” then delete it."),
            ("40–55", "Time n=1000 vs 2000 if the machine allows", "Write the real numbers. If noisy, say so."),
            ("55–60", "They add a duplicate test", "Circulate."),
        ],
        cut="Insertion sort. Keep selection + doubling.",
        add="Stable vs unstable: name only.",
    )
    GOLD[(P, 11)] = dict(
        kernel="`fact(n)` with base case first; stack of `fact(4)`",
        success="they can draw four stack frames and name the base case",
        invariant="write the base case before the recursive call; recurse on a smaller n",
        goal="a function that calls itself on purpose",
        board="""```
fact(n):  if n <= 1 return 1;   else return n * fact(n-1)

fact(4)
  fact(3)
    fact(2)
      fact(1) → 1

no base case → stack overflow
```""",
        slides=[],
        hook_say="Scene graphs, kd-trees, closest-pair divide-and-conquer: recursion is not optional in IGWT. Today: factorial so you can see the stack.",
        hook_ask="What happens if you omit the base case? Wait. Want: stack overflow / infinite recursion.",
        frame_say="Factorial as a loop is finer. Recursion is for divide-and-conquer **structure**. Fibonacci naive is slow — we will count calls, not invent timings.",
        frame_ask="What is the base case of `fact`?",
        build=[
            "**Say:** Base case first. Then the recursive case on `n-1`, not on `n`.",
            "**Board:** stack frames for `fact(4)`. Then a tree of naive `fib` — explosion of calls.",
            "**Say:** Recursive sum of an array: index `i` or `slice`. Prefer index so you do not copy.",
        ],
        ask_build="One later IGWT use of recursion? Want: scene graph / kd-tree / closest pair.",
        they_build="On paper: stack drawing for `fact(4)`.",
        show_say="`fact`, then recursive sum. I plant `return n * fact(n)` and we hang. Kill it. Fix `n-1`.",
        attempt_say="Naive fib + count calls for `fib(8)` or `fib(10)`. Write the number you counted.",
        land_say="Lab: fib + call count; flatten nested array extra. Homework: stack drawing; recursive binary search. Quiz: base case, no base, one later use.",
        live=[
            ("0–15", "fact", "Plant recurse on n."),
            ("15–35", "Recursive sum by index", "Slice copy as the wrong extra."),
            ("35–50", "fib call count", "They see the tree."),
            ("50–60", "They draw fact(4)", "Circulate."),
        ],
        cut="Flatten. Keep base case + stack.",
        add="Tail recursion name only — JS does not guarantee it.",
    )
    GOLD[(P, 12)] = dict(
        kernel="`export function lerp` in `math.js`; `import` from `main.js`; serve locally",
        success="lerp runs from a second file on a local server, not as a 400-line paste",
        invariant="a file is a set of named functions; `file://` often blocks modules",
        goal="split a program without globals",
        board="""```
main.js  ──import──►  math.js   export function lerp …

<script type="module" src="main.js"></script>

python -m http.server     (not file://)
```""",
        slides=[("Error screenshot of CORS / module on `file://`", "the red text is a photo")],
        hook_say="Later: `kernel.js` vs `raster.js`. Today: `math.js` with clamp and lerp. A 400-line file is not simplicity.",
        hook_ask="Why might `import` fail when you double-click HTML? Wait. Want: `file://` / modules / CORS.",
        frame_say="`type=\"module\"` and `export function`. Same rule as WebGL demos. Interface: named functions, no hidden globals.",
        frame_ask="Name two files you expect in Computer Graphics I’s kernel.",
        build=[
            "**Say:** Script order vs modules. Modules are deferred and strict.",
            "**Board:** arrows main → math. Export / import syntax.",
            "**Say:** README run line is part of the program. Circular imports: do not.",
        ],
        ask_build="What is the export syntax for lerp?",
        they_build="Write the import line for lerp on paper.",
        show_say="Move clamp/lerp into math.js. Break it on `file://` on purpose if the room allows, then serve.",
        attempt_say="Three-file mini: math, strings, main. README: how to serve.",
        land_say="Homework: why `file://` breaks modules; one export/import pair. Quiz: export syntax, why serve, two CG I file names.",
        live=[
            ("0–15", "Split lerp", "Forget type=module."),
            ("15–35", "Serve", "Plant file:// failure."),
            ("35–50", "README one line", "They copy the command."),
            ("50–60", "They add clamp export", "Circulate."),
        ],
        cut="Bundlers. Keep export/import + serve.",
        add="`import { lerp as mix }` name only.",
    )
    GOLD[(P, 13)] = dict(
        kernel="`class Point { dist(q){…} }` or record + `dist(p,q)` — student choice, with tests",
        success="they can say what `this` is in one sentence and they did not build an inheritance tree",
        invariant="`this` is the receiver; losing it in a callback is a later course; inheritance is skipped",
        goal="a method that uses the object",
        board="""```
p.dist(q)     this is p

class Point {
  constructor(x,y){ this.x=x; this.y=y; }
  dist(q){ return Math.hypot(this.x-q.x, this.y-q.y); }
}

has-a  (sprite has a point)    not  is-a  trees
```""",
        slides=[("Optional: `this` undefined in a detached callback", "the TypeError is a photo")],
        hook_say="A method is a function stored on an object. `this` is the receiver. Inheritance is skipped — composition: a sprite **has** a point.",
        hook_ask="In `p.dist(q)`, what is `this`? Wait. Want: `p`.",
        frame_say="`class` is optional sugar. Records plus functions are enough for IGWT math kernels. Demo `this` lost in a callback once; do not spend the hour on it.",
        frame_ask="Why skip inheritance this term?",
        build=[
            "**Say:** `counter.inc()` mutates. Prefer `add` that returns a **new** vector for the lab.",
            "**Board:** has-a vs is-a. Point method box.",
            "**Say:** BankAccount deposit/withdraw as the live-coding story; then Point.dist.",
        ],
        ask_build="Write dist of two points in one line with hypot.",
        they_build="On paper: a Vector add that returns new, does not mutate.",
        show_say="BankAccount, then Point. Plant an unbound `this`. Name it. Fix or avoid.",
        attempt_say="Vector object with add (returns new). No inheritance. Tests.",
        land_say="Homework: `this` in one paragraph; Point class **or** record+functions, tests. Quiz: what is this, why no inheritance, dist. Next week is studio — freeze scope.",
        live=[
            ("0–15", "BankAccount", "Negative withdraw policy."),
            ("15–40", "Point.dist", "Plant this unbound."),
            ("40–50", "Has-a sprite", "No extends."),
            ("50–60", "They write Vector.add", "Circulate."),
        ],
        cut="Getters. Keep this + no inheritance.",
        add="`#private` name only.",
    )
    GOLD[(P, 14)] = dict(
        kernel="tests for the project kernel + README that runs on a lab machine",
        success="a TA can run the README and see a test or a playable loop without opening a second tool",
        invariant="pretty CSS without functions is a fail; freeze scope today",
        goal="studio — not a content lecture",
        kind="studio",
        board="""```
Report headings:
1 Problem
2 Functions
3 Tests
4 How to run
5 Limitations
6 Who wrote what

If behind: drop graphics, keep functions + tests + README
```""",
        slides=[("Clock / 12+5 rubric preview", "do not paint a slide deck of features")],
        hook_say="This meeting is **studio**, not a content lecture. Guessing game, quiz, snake-in-console, or a tiny canvas clicker. Not Three.js.",
        hook_ask="If you are behind, what do you cut first?",
        frame_say="Desk review: functions, tests, README. One teammate map. Rehearse 12+5.",
        show_say="I review one volunteer repo against the headings. I do not add features for them.",
        attempt_say="You work. I circulate. Tests first.",
        land_say="Homework: report draft + repo. Next week presentations 12+5. No new features after freeze.",
        live=[
            ("0–10", "Headings on the board", "They photograph."),
            ("10–50", "Desk review", "Kernel tests first."),
            ("50–60", "Rehearse one 60-second demo", "Stop them at 60."),
        ],
        cut="New features. Keep freeze.",
        add="30s recording optional.",
    )
    GOLD[(P, 15)] = dict(
        kernel="12 minute demo + 5 minutes questions; repo + short report",
        success="they stop at 12, name a loop and a function, and do not debug on stage",
        invariant="no new features today",
        goal="presentations — not a content lecture",
        kind="presentations",
        board="""```
12 min  +  5 questions

Must be able to point at: a loop, a function, a bug you fixed
Who wrote what

Rubric: demo runs · explanation · tests · honesty about limits
```""",
        slides=[("Timer visible", "not a slide of code")],
        hook_say="This meeting is **presentations**. 12+5. Recording backup. No new features.",
        hook_ask=None,
        frame_say="Questions I will ask: where is a loop? A function? A bug you fixed?",
        show_say="None. They present. Live coding slot is more talks.",
        attempt_say="Present.",
        land_say="This habit — name the function, test it — is the rest of IGWT.",
        live=[("0–60", "Talks continue", "Cut at 12. No debugging on stage.")],
        cut="Extra features. Keep the clock.",
        add="If a slot empties: one more question on tests.",
    )

    GOLD[(M, 1)] = dict(
        kernel="plot a point with y flipped; `deg * Math.PI / 180`",
        success="they can point at math +y up and canvas +y down on the same figure",
        invariant="Math.cos takes radians; canvas y is down; say it every plot",
        goal="put a point on an axis and not lie about y",
        board="""```
math:     +x right, +y up
canvas:   +x right, +y down     (CG I flips in the viewport)

180° = π rad
rad = deg * Math.PI / 180

a cube is vertices; a camera is a matrix
```""",
        slides=[("Optional: a canvas plot with y unflipped, labels upside-down", "the bug is a photo")],
        hook_say="A cube is vertices. A camera is a matrix. This course is the algebra Computer Graphics I will spend on pictures. Today: axes, points, radians.",
        hook_ask="If you plot y = x on a canvas without flipping, which way does the line go? Wait.",
        frame_say="High-school algebra is enough. We freeze conventions: right-handed, Y-up on paper. Canvas is the exception we name.",
        frame_ask="Does `Math.cos` want degrees or radians?",
        build=[
            "**Say:** Graphics is numbers. Preview the CG I space chain as five boxes — do not derive P.",
            "**Board:** two y-axes side by side. Unit circle preview (cos, sin).",
            "**Say:** Convert on the board. Store radians in code. Degrees in `cos` is the professional disease.",
        ],
        ask_build="π radians in degrees? Want: 180.",
        they_build="Table: 30°, 45°, 90° → radians. Leave 45° as π/4, not a decimal they invent.",
        show_say="Plot 8 points on a canvas with y flipped; label axes. Demo `Mathematics for Computer Graphics/code/01-axes.html`.",
        attempt_say="Distance between two points on paper, then in code. Eight minutes.",
        land_say="Lab: degree table + distance. Homework: why radians; plot y=sin(x) with the flip. Quiz: π in degrees, canvas y, point vs pixel.",
        live=[
            ("0–15", "Axes + one point", "Plant y unflipped."),
            ("15–35", "Radian conversion", "Plant `Math.cos(90)`."),
            ("35–50", "8 points", "Labels."),
            ("50–60", "They add distance", "Circulate."),
        ],
        cut="Space-chain preview. Keep two y’s and radians.",
        add="A third axis named only.",
    )
    GOLD[(M, 2)] = dict(
        kernel="vec2 add, sub, scale, len, normalize; refuse p+q",
        success="they subtract two points to get a vector and they do not normalize zero",
        invariant="a point is a location; a vector is a displacement; p+q is meaningless",
        goal="draw an arrow that is not a point",
        board="""```
point P     vector a (arrow, free to slide)

a + b   parallelogram
s a     stretch
|a|     hypot(ax, ay)
â       a / |a|     if |a| ≠ 0
```""",
        slides=[],
        hook_say="If they cannot say whether something is a point or a vector, they cannot write M correctly. That is the course principle.",
        hook_ask="Why is P+Q not a point? Wait. Want: two locations do not add; their difference is a vector.",
        frame_say="CG I Week 4 is this in 3D with w. Today 2D arrows.",
        frame_ask="What is P − P?",
        build=[
            "**Say:** Parallelogram rule. Scale. Length `Math.hypot`.",
            "**Board:** arrow not attached to the origin. Then unit arrow.",
            "**Say:** Zero vector: do not divide. Return a policy (skip, or (0,0) with a comment) — do not NaN silently.",
        ],
        ask_build="Unit of (0,2)? Want: (0,1).",
        they_build="On paper: |(3,4)|. Want: 5.",
        show_say="Interactive two arrows add. Demo `02-add.html`.",
        attempt_say="Implement add, sub, scale, len, normalize. Tests including zero.",
        land_say="Homework: why p+q is meaningless; 8 tests. Quiz: length (3,4), unit (0,2), p minus p.",
        live=[
            ("0–15", "add / parallelogram", "Draw it."),
            ("15–35", "len / normalize", "Plant divide by zero."),
            ("35–50", "sub of two points", "Label the result a vector."),
            ("50–60", "They write tests", "Circulate."),
        ],
        cut="3D. Keep 2D + zero policy.",
        add="Column vs row name; we use columns later.",
    )
    GOLD[(M, 3)] = dict(
        kernel="dot product; projection; Lambert as n·ℓ preview",
        success="they compute a·b and a projection, and they know perpendicular means 0",
        invariant="a·b = |a||b|cosθ only if you mean that; unit-ize before treating the number as cosine",
        goal="turn two arrows into one number that means angle",
        board="""```
a·b = ax bx + ay by     =  |a||b| cosθ

proj_a b  =  ((a·b)/(a·a)) a

a·b = 0  ⊥     >0 acute     <0 obtuse
Lambert preview:  n·ℓ
```""",
        slides=[],
        hook_say="Lighting and collision are this product. Today 2D. Lambert in Computer Graphics I is n·ℓ — bounce 0, not GI.",
        hook_ask="If two unit vectors are perpendicular, what is the dot? Wait. Want: 0.",
        frame_say="Two formulas: sum of products, and cosine. Do not mix them with un-normalized vectors and call it cosθ.",
        frame_ask="cos of 0° between unit vectors?",
        build=[
            "**Say:** Algebra first. Then the shadow picture: projection.",
            "**Board:** two arrows; shadow of b on a. Sign: acute / right / obtuse. Back-face intuition.",
            "**Say:** `a·a` in the denominator — zero vector again.",
        ],
        ask_build="Write the projection formula.",
        they_build="On paper: (1,0)·(2,2) and the projection of (2,2) onto (1,0).",
        show_say="Slider θ; show dot and a numeric projection. Demo `03-dot.html`.",
        attempt_say="`project(b,a)`. Reject a perpendicular pair with an assert.",
        land_say="Homework: Lambert one sentence; tests including 90°. Quiz: perpendicular, cos 0°, projection formula.",
        live=[
            ("0–15", "dot as sum", "Forget z if someone pastes 3D."),
            ("15–35", "projection", "Plant forgetting a·a."),
            ("35–50", "sign / back-face", "Draw it."),
            ("50–60", "They write project", "Circulate."),
        ],
        cut="3D z. Keep 2D + projection.",
        add="Clamp n·ℓ to 0 as Lambert preview.",
    )
    GOLD[(M, 4)] = dict(
        kernel="`cross2(a,b) = ax by − ay bx`; triangle normal (b−a)×(c−a)",
        success="they get a signed area and they can show i×j=k on the right-hand rule",
        invariant="IGWT is right-handed; unsigned area throws away the predicate",
        goal="a number that knows left from right",
        board="""```
2D:  ax by − ay bx     signed area of parallelogram
     same kernel as orient(a,b,c) in Computational Geometry

3D:  i × j = k     n = (b−a) × (c−a)

flip two vertices → flip n
```""",
        slides=[],
        hook_say="Computational Geometry’s `orient` is this 2D cross. Lighting normals are the 3D cross of edges.",
        hook_ask="(2,0)×(0,3) in 2D? Wait. Want: 6.",
        frame_say="Right-hand thumb on the axis. Do not switch handedness ‘until it looks right.’",
        frame_ask="What is i×j?",
        build=[
            "**Say:** 2D signed area. Positive vs negative winding.",
            "**Board:** hands. Triangle normal.",
            "**Say:** Determinant mnemonic for 3D. Area of parallelogram is the magnitude.",
        ],
        ask_build="Why does winding matter for a GPU triangle?",
        they_build="On paper: signed area of triangle (0,0),(1,0),(0,1).",
        show_say="2D signed area; 3D n on a drawn triangle. Demo `04-cross.html`.",
        attempt_say="orient clone; normal of a triangle in the xy plane.",
        land_say="Homework: right-hand rule; tests i×j=k. Quiz: 2D cross, i×j, winding.",
        live=[
            ("0–20", "cross2", "Unsigned abs as the wrong extra."),
            ("20–40", "orient three points", "Collinear → 0."),
            ("40–55", "3D i×j=k", "Left-hand plant."),
            ("55–60", "They test xy triangle", "Circulate."),
        ],
        cut="Full 3D lighting. Keep 2D + i×j=k.",
        add="Scalar triple product name only.",
    )
    GOLD[(M, 5)] = dict(
        kernel="`p(t) = a + t d`; segment t∈[0,1], ray t≥0; plane n·(x−p)=0",
        success="they can write a parametric line and say the t domain of a segment",
        invariant="t unclamped is a line, not a segment",
        goal="name the set of points on a line",
        board="""```
p(t) = a + t d
  line: t ∈ ℝ     ray: t ≥ 0     segment: t ∈ [0,1]

plane:  n · (x − p) = 0
```""",
        slides=[],
        hook_say="Rays, segments, planes: the same objects Computer Graphics I will intersect. Today the equations.",
        hook_ask="What t values make a segment? Wait. Want: 0 to 1.",
        frame_say="A triangle defines a plane. Ray–triangle later uses this plus barycentric. Distance to line is optional (cross/|d|).",
        frame_ask="Ray vs line in one sentence?",
        build=[
            "**Say:** Parametric first — it codes. Implicit 2D ax+by+c=0 teaching.",
            "**Board:** p(t). Plane. Mark t=0 and t=1.",
            "**Say:** Intersect ray vs plane idea: solve for t, then test domain.",
        ],
        ask_build="Write the plane equation.",
        they_build="On paper: point at t=0.5 on a segment.",
        show_say="Drag a ray across a line; mark t. Demo `05-line.html`.",
        attempt_say="onSegment using t and a bounding box; ray–line intersection 2D.",
        land_say="Homework: ray vs segment; closest point on segment extra. Quiz: t domain, plane, ray vs line.",
        live=[
            ("0–15", "p(t) draw", "t=2 still drawn as a segment — plant."),
            ("15–40", "Intersect", "No hit vs t<0."),
            ("40–55", "Plane in 3D on paper", "n not unit for equation (ok) vs distance (need |n|)."),
            ("55–60", "They clamp t", "Circulate."),
        ],
        cut="Full ray–triangle. Keep parametric + domain.",
        add="AABB reject name.",
    )
    GOLD[(M, 6)] = dict(
        kernel="multiply 2×2 by hand and in code; show AB ≠ BA on a square",
        success="they multiply 2×2 and they can say columns are where the basis goes",
        invariant="column vectors; multiplication is composition; not commutative",
        goal="a linear map as a box of numbers",
        board="""```
columns of A = images of basis e1, e2

I A = A
AB ≠ BA     (same story as T R vs R T)

v' = A v
```""",
        slides=[],
        hook_say="A matrix is a linear function. Columns are where basis vectors go. That sentence is Computer Graphics I’s model matrix.",
        hook_ask="Is AB the same as BA? Wait. Want: no.",
        frame_say="We use **column** vectors in this program. Do not mix row-vector formulas from a random blog.",
        frame_ask="What is I times A?",
        build=[
            "**Say:** Identity. Then multiply: row-column. Composition.",
            "**Board:** basis images. Non-commute: scale then rotate vs reverse.",
            "**Say:** Rotate/scale as 2×2. Code: tiny `mul2`; nested loops later.",
        ],
        ask_build="2×2 rotate 90° of (1,0) — freeze **one** convention on the board.",
        they_build="Multiply two 2×2 matrices by hand.",
        show_say="Apply a 2×2 to a square’s four corners; before/after. Demo `06-matmul.html`.",
        attempt_say="mat2 mul tests; scale then rotate vs reverse.",
        land_say="Homework: columns as images of basis; mul2. Quiz: I A, AB vs BA, rotate 90 of (1,0).",
        live=[
            ("0–15", "By hand mul", "Row-vector plant."),
            ("15–40", "Square corners", "Non-commute."),
            ("40–55", "mul2", "Index bugs."),
            ("55–60", "They write I test", "Circulate."),
        ],
        cut="3×3. Keep 2×2 + non-commute.",
        add="3×3 identity named.",
    )
    GOLD[(M, 7)] = dict(
        kernel="det 2×2; invert when det≠0; rotation inverse is transpose",
        success="they compute det, invert a rotation by transpose, and refuse det 0",
        invariant="det is area scale; det 0 means no inverse — collapsed geometry",
        goal="undo a linear map when you may",
        board="""```
det [a b; c d] = ad − bc     area scale; negative = flip

R⁻¹ = Rᵀ     (rotation)
(sI)⁻¹ = (1/s) I   if s ≠ 0

det = 0  →  singular, no inverse
normals preview: (M⁻¹)ᵀ
```""",
        slides=[],
        hook_say="Undo. If det=0 the geometry collapsed. Inverting by transposing a **scale** is a bug.",
        hook_ask="What is det of a rotation? Wait. Want: 1 (or −1 if a flip snuck in).",
        frame_say="Solve 2×2 with inverse at teaching level. (M⁻¹)ᵀ for normals: name it; 2D non-uniform scale demo.",
        frame_ask="Singular means?",
        build=[
            "**Say:** Area scale picture. Negative det flips winding.",
            "**Board:** no inverse. Transpose of R.",
            "**Say:** Divide by det 0 → do not. Detect and throw or skip.",
        ],
        ask_build="Inverse of Ry — wait, 2D R(θ)? Want: R(−θ) = transpose.",
        they_build="Invert [[2,0],[0,2]] and try [[1,0],[2,0]].",
        show_say="Non-uniform scale a square; wrong vs right normal. Demo matmul page or board.",
        attempt_say="invert2 when det≠0; detect singular.",
        land_say="Homework: det 0 picture; tests. Quiz: det of rotate, inverse of R, singular. Midterm next week: vec, dot, cross, mul2, det — then homogeneous after the exam.",
        live=[
            ("0–15", "det by hand", "Sign."),
            ("15–40", "invert2", "Plant transpose of scale."),
            ("40–55", "normal demo", "Non-uniform."),
            ("55–60", "They detect singular", "Circulate."),
        ],
        cut="Gaussian elimination. Keep det + 2×2 inverse.",
        add="Cramer name only.",
    )
    GOLD[(M, 8)] = dict(
        kernel="homogeneous (x,y,1) vs (x,y,0); translate a triangle with 3×3",
        success="after the exam they can say why translation needs an extra 1",
        invariant="w=1 point, w=0 direction; translation ignores directions",
        goal="midterm, then w",
        kind="midterm",
        midterm_topics="vectors add/scale/len; point vs vector; dot and projection; 2D cross / i×j; p(t); 2×2 mul and det.",
        board="""```
point      (x, y, 1)
direction  (x, y, 0)    lights-as-directions; translation skipped

T(tx,ty) * (x,y,1) = (x+tx, y+ty, 1)
T * (x,y,0) = (x,y,0)
```""",
        slides=[],
        hook_say="This meeting is a **midterm**, then homogeneous coordinates. Translation does not fit 2×2 linear. Add a 1. CG I Week 5 is the 4×4 version.",
        show_say="3×3 2D affine: translate a triangle. T on a direction unchanged.",
        attempt_say="T(1,0)*point; T*direction unchanged.",
        land_say="Homework: why 3×3 for 2D affine; midterm reflection. No quiz. Next: rotations.",
        live=[
            ("0–20", "Homogeneous column", "Plant translating a normal as a point."),
            ("20–45", "Translate triangle", "w forgotten → garbage."),
            ("45–60", "They test w=0", "Circulate."),
        ],
        cut="4×4. Keep 3×3 + w.",
        add="Preview 4×4 identity.",
    )
    GOLD[(M, 9)] = dict(
        kernel="R2(θ) frozen on the board; Ry(90)*(1,0,0) test; same Ry as CG I",
        success="they write one 2D rotation matrix and they do not put degrees in it",
        invariant="write one R and freeze; order of 3D Euler angles matters; quaternions named not required",
        goal="turn an angle into a matrix",
        board="""```
R2(θ) = [[c, -s], [s, c]]     // FREEZE THIS (or the documented variant — one only)

thumb on axis, fingers rotation sense

Euler: order matters; gimbal lock named
quaternions: name only
```""",
        slides=[("Optional: gimbal lock photo or a small animation", "do not derive quaternion slerp")],
        hook_say="Same Ry as [[Computer Graphics/Lecture 05 Homogeneous Transforms]]. Mixing conventions is the bug.",
        hook_ask="R(90°) of (1,0) with **our** matrix? Compute on the board.",
        frame_say="Rx, Ry, Rz. Euler gimbal lock: name and a picture. Quaternions named, not required.",
        frame_ask="Why does order of Rx Ry Rz matter?",
        build=[
            "**Say:** 2D first. Cos/sin in **radians**.",
            "**Board:** thumb. Euler vs one matrix.",
            "**Say:** Compose two rotations. Degrees in matrices — do not.",
        ],
        ask_build="Gimbal lock in one sentence.",
        they_build="Rotate (1,0) by 90° with the frozen matrix.",
        show_say="Rotate a square; or cube wireframe with Ry. Demo `07-rotate.html`.",
        attempt_say="Ry(90)*(1,0,0) test; two Euler orders compared.",
        land_say="Homework: gimbal lock in 6 sentences; rotateZ. Quiz: R(90) of (1,0), order, gimbal name.",
        live=[
            ("0–15", "Freeze R2", "The other convention as a plant."),
            ("15–40", "Compose 2D", "Degrees plant."),
            ("40–55", "Euler warning", "Picture."),
            ("55–60", "They test Ry 90", "Circulate."),
        ],
        cut="Quaternion code. Keep R2 + freeze.",
        add="Axis-angle name.",
    )
    GOLD[(M, 10)] = dict(
        kernel="`(x,y) = (r cos t, r sin t)`; N-gon vertices",
        success="they convert polar to cartesian in radians and they know sin²+cos²=1",
        invariant="trig in this course is the unit circle and polar — not a trig identity exam",
        goal="put a point on a circle",
        board="""```
unit circle: (cos θ, sin θ)
polar:  x = r cos θ,  y = r sin θ
sin²+cos² = 1     (only identity required)

Math.cos(degrees) is wrong
```""",
        slides=[],
        hook_say="A planet, a pendulum, an N-gon, a cylinder vertex: polar. Law of cosines named for a lighting picture — not a lab.",
        hook_ask="cos(0)? Wait. Want: 1.",
        frame_say="Small-angle approximations not required. Oscillation as animation: y = cos(t).",
        frame_ask="Why sin²+cos² matters for a unit vector?",
        build=[
            "**Say:** Unit circle. Polar.",
            "**Board:** N-gon vertices from i * 2π/N.",
            "**Say:** r=0 is a point, not a crash. Degrees plant.",
        ],
        ask_build="Polar to xy formula.",
        they_build="Vertices of a square from polar (r, k·π/2).",
        show_say="Point on a circle, θ slider; pendulum. Demo rotate page or axes.",
        attempt_say="polar(r,θ); Lissajous extra.",
        land_say="Homework: polar to a cylinder vertex extra; N-gon. Quiz: cos 0, polar, why sin²+cos².",
        live=[
            ("0–15", "Unit circle", "Degrees in cos."),
            ("15–40", "N-gon", "Off-by-one closing the loop."),
            ("40–55", "Pendulum", "t in radians."),
            ("55–60", "They write polar()", "Circulate."),
        ],
        cut="Lissajous. Keep polar + N-gon.",
        add="Law of cosines on the board as a name.",
    )
    GOLD[(M, 11)] = dict(
        kernel="`lerp(a,b,t)`; quadratic Bezier as lerp of lerps; cubic sampled",
        success="they write lerp and a quadratic Bezier and they know t is not arc length",
        invariant="t is a parameter, not distance; slerp is a different word",
        goal="walk from A to B, then along a handle",
        board="""```
lerp(a,b,t) = a + t(b−a)

quadratic: lerp( lerp(A,C,t), lerp(C,B,t), t )   De Casteljau

t ∉ [0,1]  →  say whether you extrapolate
t is not arc length
```""",
        slides=[],
        hook_say="Colors, camera paths, keyframes, fonts, SVG: lerp and Bézier. Do not call Bézier slerp.",
        hook_ask="lerp t=0 is? Wait. Want: a.",
        frame_say="Policy: clamp t or allow extrapolate — say it. Cubic Bézier named for fonts/UI.",
        frame_ask="Is t=0.5 halfway in **distance** on a cubic? Want: not necessarily.",
        build=[
            "**Say:** Segment picture. Then De Casteljau.",
            "**Board:** handles. Two control points for cubic.",
            "**Say:** Sample 32 points. Parametric speed warning.",
        ],
        ask_build="Quadratic as lerps — say it.",
        they_build="lerp tests t=0,1,0.5 on paper.",
        show_say="Drag 4 Bézier handles; sample 32. Demo `08-bezier.html`.",
        attempt_say="lerp tests; quadratic Bezier function.",
        land_say="Homework: t vs distance; cubic Bézier. Quiz: lerp t=0, quadratic as lerps, arc-length warning.",
        live=[
            ("0–15", "lerp", "Wrong formula a+t*b."),
            ("15–40", "Quadratic", "De Casteljau."),
            ("40–55", "Cubic sample", "t vs speed."),
            ("55–60", "They test t=0,1", "Circulate."),
        ],
        cut="Arc-length parameterization. Keep lerp + quadratic.",
        add="Name slerp once.",
    )
    GOLD[(M, 12)] = dict(
        kernel="a frame = origin + axes; orthonormal 2D from one vector + perp; lookAt sketch",
        success="they can say M’s columns are object axes in world",
        invariant="a frame is origin + axes; orthonormal means length 1 and dot 0",
        goal="name where you are standing",
        board="""```
frame: origin + x-axis + y-axis (+ z)

columns of M = object axes (and origin) in world

orthonormal:  |axis|=1,  axis_i · axis_j = 0
lookAt builds one
```""",
        slides=[],
        hook_say="Object space is a frame. World is a frame. Camera is a frame. The model matrix **is** a frame.",
        hook_ask="What is a frame, in three words? Wait. Want: origin plus axes.",
        frame_say="CG I Week 6. Right-handed three axes. Scaling axes and still calling them orthonormal is a bug.",
        frame_ask="Are scaled axes orthonormal?",
        build=[
            "**Say:** Two frames, same point, two coordinate pairs.",
            "**Board:** columns. Change of coordinates teaching-level.",
            "**Say:** Build orthonormal 2D: n = normalize(v), perp = (−n.y, n.x) in right-handed 2D.",
        ],
        ask_build="M’s columns?",
        they_build="Sketch lookAt: eye, target, up → axes.",
        show_say="Local frame on a rotated box; world frame. Demo `09-lookat.html`.",
        attempt_say="Orthonormal 2D from one vector + perp; tests.",
        land_say="Homework: M’s columns; rotate a frame. Quiz: frame, columns, orthonormal. Next week maps this course onto Computer Graphics I.",
        live=[
            ("0–20", "Two frames", "Same point."),
            ("20–40", "Columns of M", "Origin in the last column / homogeneous reminder."),
            ("40–55", "lookAt sketch", "Do not derive the full 4×4 if time is short."),
            ("55–60", "They build perp", "Circulate."),
        ],
        cut="Full lookAt 4×4. Keep 2D orthonormal + columns.",
        add="Name the camera frame.",
    )
    GOLD[(M, 13)] = dict(
        kernel="recite object → world → view → clip → NDC → pixels; p_clip = P V M p",
        success="they can point at which weeks of this course sit in that chain and they do not claim they wrote a GPU",
        invariant="do not derive P today; this course supplied the algebra, CG I implements the picture",
        goal="hand the baton to Computer Graphics I",
        board="""```
object → world → view → clip → NDC → pixels

p_clip = P * V * M * p     (column vectors)

this course: vectors, matrices, frames, lerp, w
CG I: putPixel, raster, z-buffer
Comp Geo: orient, barycentric
```""",
        slides=[("Optional: joint figure with CG I Week 1 six boxes", "only if the board is full")],
        hook_say="Map: math week → CG I week. Homogeneous multiply chain. `orient` and barycentric are this course’s cross and areas.",
        hook_ask="Six spaces, in order? Wait. Fill slowly.",
        frame_say="What they implement next semester: a software rasterizer, not a GPU shrine. Three.js is not the weekly engine there.",
        frame_ask="Which course implements the z-buffer?",
        build=[
            "**Say:** Walk the map table. Vectors → lighting. Matrices → M. Frames → camera. Lerp → attributes.",
            "**Board:** pipeline. w of a point is 1.",
            "**Say:** Numerical PVM on one point if the CG I kernel exists; else 3×3 affine only.",
        ],
        ask_build="w of a direction?",
        they_build="One-page map: math week → CG I week (start in class, finish in lab).",
        show_say="Demo `10-pvm.html` or multiply one point on the board.",
        attempt_say="Three numerical PVM multiplies extra; the map is the lab.",
        land_say="Homework: six spaces; no new code required. Quiz: six spaces, w of a point, who implements z-buffer. Then studio.",
        live=[
            ("0–20", "Six boxes", "Fill slowly."),
            ("20–40", "One point through M then V", "Skip deriving P."),
            ("40–55", "Map table", "They copy."),
            ("55–60", "They write w=1 vs 0", "Circulate."),
        ],
        cut="Numerical P. Keep the chain + map.",
        add="NDC range named as CG I’s job.",
    )
    GOLD[(M, 14)] = dict(
        kernel="canvas explainer of one topic + tests for the math kernel + README",
        success="a TA sees tests for the kernel before a pretty graph",
        invariant="no Three.js as the math; freeze",
        goal="studio — not a content lecture",
        kind="studio",
        board="""```
Projects: vec visualizer · Bézier editor · 2×2 explorer · lookAt basis drawer

Cuts: drop 3D; keep 2D + tests
Report: definitions, screenshots, limitations
```""",
        slides=[],
        hook_say="This meeting is **studio**. Pretty graphs with no tests fail.",
        hook_ask="If behind, what do you cut?",
        frame_say="Desk review: kernel tests first.",
        show_say="Volunteer review against headings.",
        attempt_say="Studio. Tests first.",
        land_say="Report + repo. Next week 12+5. Be ready to derive one formula on the board.",
        live=[
            ("0–10", "Headings", "Photograph."),
            ("10–50", "Desk review", "Tests first."),
            ("50–60", "60s rehearsal", "Stop."),
        ],
        cut="New math. Keep freeze.",
        add="One more test for det 0 or normalize 0.",
    )
    GOLD[(M, 15)] = dict(
        kernel="12+5; demo the visualizer; derive one formula if asked",
        success="they stop at 12 and they can say vector vs matrix vs frame",
        invariant="no new math today",
        goal="presentations — not a content lecture",
        kind="presentations",
        board="""```
12 + 5
Questions: dot meaning? det 0? homogeneous w?
Next: Computer Graphics I · Computational Geometry
Habit: name the object — vector, matrix, frame
```""",
        slides=[("Timer", "not Wikipedia")],
        hook_say="Presentations. 12+5. Repo. Stop at 12.",
        show_say="None. Present.",
        attempt_say="Present.",
        land_say="Name the object. That habit is CG I.",
        live=[("0–60", "Talks", "Cut at 12. No new math.")],
        cut="Slides of Wikipedia.",
        add="One extra question on a missed formula.",
    )
    extra = Path(__file__).resolve().parent
    for p in sorted(extra.glob("gold_*.py")):
        ns: dict = {}
        exec(p.read_text(encoding="utf-8"), ns)
        if callable(ns.get("register")):
            ns["register"](GOLD)


def list_after(heading: str, text: str) -> list[str]:
    m = re.search(
        rf"^## {re.escape(heading)}\s*$([\s\S]*?)(?=^## |\Z)",
        text,
        re.M,
    )
    if not m:
        return []
    items = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if re.match(r"^\d+\.\s+", line):
            items.append(re.sub(r"^\d+\.\s+", "", line))
        elif line.startswith("- "):
            items.append(line[2:].strip())
    return items


def section_block(heading: str, text: str) -> str:
    m = re.search(
        rf"^## {re.escape(heading)}\s*$([\s\S]*?)(?=^## |\Z)",
        text,
        re.M,
    )
    return m.group(1).strip() if m else ""


def numbered_sections(text: str) -> list[tuple[str, str]]:
    found = re.findall(
        r"^## (\d+)\. (.+)$([\s\S]*?)(?=^## |\Z)",
        text,
        re.M,
    )
    return [(num, title, body.strip()) for num, title, body in found]


def first_code(text: str) -> str:
    m = re.search(r"```(?:js|html|css)?\n([\s\S]*?)```", text)
    return m.group(0).strip() if m else ""


def parse(text: str, folder: str) -> dict:
    hm = re.search(r"^# Lecture (\d+)\s*[—–-]\s*(.+)$", text, re.M)
    week = int(hm.group(1)) if hm else 0
    title = hm.group(2).strip() if hm else "Untitled"
    course = FOLDER_COURSE.get(folder, folder)
    cm = re.search(r"\*\*Course:\*\*\s*(.+)", text)
    if cm:
        course = cm.group(1).strip()
    wm = re.search(r"\*\*Week \d+ of 15\*\*\s*[·.]\s*(.+)", text)
    if wm:
        course = wm.group(1).strip()
    this_week = ""
    m = re.search(r"\*\*This week:\*\*\s*(.+)", text)
    if m:
        this_week = m.group(1).strip()
    board_first = ""
    m = re.search(r"\*\*Board first:\*\*\s*(.+)", text)
    if m:
        board_first = m.group(1).strip()
    kernel_line = ""
    m = re.search(r"\*\*Kernel this week:\*\*\s*(.+)", text)
    if m:
        kernel_line = m.group(1).strip()
    m = re.search(r"\*\*Kernel(?: \(after the exam\))?:\*\*\s*(.+)", text)
    if m and not kernel_line:
        kernel_line = m.group(1).strip()
    if kernel_line and not this_week:
        this_week = kernel_line
    success = ""
    m = re.search(r"\*\*Success check:\*\*\s*(.+)", text)
    if m:
        success = m.group(1).strip()
    goals = list_after("Learning goals", text)
    if not goals:
        g = section_block("Learning goals", text)
        goals = [ln.strip("1. ") for ln in g.splitlines() if ln.strip() and not ln.startswith("By ")]
        goals = [re.sub(r"^\d+\.\s*", "", x) for x in goals if x]
    live = section_block("Live coding (60 min)", text) or section_block("Live coding", text)
    lab = list_after("Lab", text)
    hw = list_after("Homework", text)
    quiz_block = section_block("Quiz (10 min)", text) or section_block("Quiz", text)
    quiz_items = []
    for line in quiz_block.splitlines():
        line = line.strip()
        if re.match(r"^\d+\.\s+", line):
            quiz_items.append(re.sub(r"^\d+\.\s+", "", line))
    snippet = ""
    sm = re.search(
        r"^## Snippet\s*$([\s\S]*?)(?=^## |\Z)",
        text,
        re.M,
    )
    if sm:
        snippet = sm.group(1).strip()
    mistakes = list_after("Common mistakes", text)
    boards = list_after("Board drawings", text)
    sections = numbered_sections(text)
    return dict(
        week=week,
        title=title,
        course=course,
        folder=folder,
        this_week=this_week,
        board_first=board_first,
        kernel_line=kernel_line,
        success=success,
        goals=goals,
        live=live,
        lab=lab,
        hw=hw,
        quiz_items=quiz_items,
        snippet=snippet,
        mistakes=mistakes,
        boards=boards,
        sections=sections,
        raw=text,
    )


def kind_of(p: dict, g: dict) -> str:
    if g.get("kind"):
        return g["kind"]
    t = p["title"].lower()
    if "defense" in t:
        return "presentations"
    if "presentation" in t:
        return "presentations"
    if "midterm" in t and "demo" in t:
        return "studio"
    if "midterm" in t:
        return "midterm"
    if "studio" in t or "freeze" in t:
        return "studio"
    if t.startswith("sprint") or "sprint-" in t or "sprint —" in t or "Sprint" in p["title"]:
        return "studio"
    if "survey presentation" in t:
        return "presentations"
    return "content"


def demo_path(p: dict) -> str:
    d = DEMOS.get((p["course"], p["week"]))
    if d:
        return d
    folder = p["folder"]
    code = ROOT / folder / "code"
    if code.is_dir():
        htmls = sorted(
            x.name
            for x in code.glob("*.html")
            if x.name not in ("index.html",)
        )
        if htmls:
            idx = min(max(p["week"] - 1, 0), len(htmls) - 1)
            return f"{folder}/code/{htmls[idx]}"
    return f"{folder}/code/"


def join_list(items: list[str]) -> str:
    if not items:
        return "_(none this meeting)_"
    return "\n".join(f"{i}. {x}" for i, x in enumerate(items, 1))


def board_block(p: dict, g: dict) -> str:
    if g.get("board"):
        return g["board"].strip()
    lines = [p["board_first"]] if p["board_first"] else []
    lines.extend(p["boards"])
    if not lines:
        lines = [p["this_week"] or p["title"]]
    return "```\n" + "\n".join(x for x in lines if x) + "\n```"


def slides_table(p: dict, g: dict) -> str:
    slides = g.get("slides")
    if slides is None:
        slides = []
    if not slides:
        # photograph-only default: at most one
        if p["week"] not in (8, 14, 15) and "screenshot" not in (p["live"] or "").lower():
            return (
                "| # | What is on it | Why it is not the board |\n"
                "| ---: | --- | --- |\n"
                "| 1 | — | Most blocks have **no slide**. Argument on the board. |\n"
            )
        slides = [
            ("Screenshot of the demo or a bug", "photograph / animation / 20pt code only"),
        ]
    rows = [
        "| # | What is on it | Why it is not the board |",
        "| ---: | --- | --- |",
    ]
    for i, pair in enumerate(slides[:6], 1):
        what, why = pair
        rows.append(f"| {i} | {what} | {why} |")
    return "\n".join(rows)


def live_table(p: dict, g: dict) -> str:
    beats = g.get("live")
    if beats:
        rows = ["| Min | Beat | Plant / fix |", "| ---: | --- | --- |"]
        for a, b, c in beats:
            rows.append(f"| {a} | {b} | {c} |")
        return "\n".join(rows)
    live = (p["live"] or "They type; you circulate.").strip().split("\n")[0]
    return f"""| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: {p['this_week'] or p['title']} | Plant the first common mistake. |
| 10–30 | {live} | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |"""


def first_sentence(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return ""
    parts = re.split(r"(?<=[.!?])\s+", text)
    return parts[0]


def do_not_line(p: dict, g: dict) -> str:
    if p["mistakes"]:
        msg = p["mistakes"][0].rstrip(".")
        msg = re.sub(r"^(Do not:?\s*)+", "", msg, flags=re.I)
        return msg[0].upper() + msg[1:] + "."
    return COURSE_DO_NOT.get(p["course"], "Skip the attempt. Lecture from slides only.")


def quiz_next(p: dict) -> str:
    items = p["quiz_items"]
    if not items or items[0].lower().startswith("none"):
        return "None this meeting."
    return "\n".join(f"{i}. {x}" for i, x in enumerate(items, 1))


def render_content(p: dict, g: dict) -> str:
    week = p["week"]
    course = p["course"]
    inv = g.get("invariant") or COURSE_INVARIANT.get(course, "name the object; freeze the convention")
    kernel = g.get("kernel") or p["kernel_line"] or p["this_week"] or p["title"]
    success = g.get("success") or (
        p["success"]
        or (p["goals"][0] if p["goals"] else "they can do the attempt without copying the live editor")
    )
    goal = g.get("goal") or (p["this_week"] or p["title"])
    demo = demo_path(p)
    hook_say = g.get("hook_say")
    if not hook_say and p["sections"]:
        title0, body0 = p["sections"][0][1], p["sections"][0][2]
        hook_say = f"{title0}. {first_sentence(body0)}".strip()
    if not hook_say:
        hook_say = f"Today: {p['this_week'] or p['title']}. The kernel is {kernel}."
    hook_ask = g.get("hook_ask")
    if not hook_ask:
        q = p["goals"][0] if p["goals"] else p["title"]
        q = re.sub(
            r"^(Name |Write |Define |Sit |Explain |Use |Avoid |Trace |See |Get |Compute |Plot |Distinguish )",
            "",
            q,
            flags=re.I,
        )
        hook_ask = f"{q.rstrip('.')}? Wait seven seconds. Take two answers."
    frame_say = g.get("frame_say")
    if not frame_say:
        frame_say = (
            f"Today’s question: {p['this_week'] or p['title']}. "
            f"Kernel: {kernel}. We freeze conventions and we do not invent timings."
        )
    frame_ask = g.get("frame_ask") or (
        f"What would a wrong version of this look like? Want: {p['mistakes'][0]}"
        if p["mistakes"]
        else "What is the one picture we will photograph?"
    )
    build = g.get("build")
    if not build:
        build = []
        for _num, title, body in p["sections"][:3]:
            sent = first_sentence(body)
            extra = " " + sent if sent and sent.lower() not in title.lower() else ""
            build.append(f"**Say:** {title}.{extra}")
        while len(build) < 3:
            build.append("**Say:** Work one example slowly on the board.")
    ask_build = g.get("ask_build") or hook_ask
    they_build = g.get("they_build") or (
        f"On paper: {p['lab'][0]}" if p["lab"] else "On paper: one example from the board."
    )
    show_say = g.get("show_say") or (
        f"Live demo: {p['live'].splitlines()[0] if p['live'] else kernel}. Zoom 140%. Read errors out loud."
    )
    attempt_say = g.get("attempt_say") or (
        p["lab"][0] if p["lab"] else "They try a fragment of the kernel. Eight minutes. You do not help for three."
    )
    land_say = g.get("land_say")
    if not land_say:
        land_say = (
            f"Photograph the board. Lab: {'; '.join(p['lab'][:2]) or 'see below'}. "
            f"Homework: {'; '.join(p['hw'][:2]) or 'see below'}. "
            "Do not end on “any questions?” — end on the lab hook."
        )
    retrieve = week > 1
    quiz_note = (
        f"- Quiz from Lecture {week - 1} (10 min, paper or LMS).\n"
        if retrieve
        else "- No quiz (Lecture 1). Course contract lives in the land.\n"
    )
    if retrieve:
        hook_header = "### Minutes 0–10 — Retrieve (quiz)"
        hook_extra = (
            f"Hand out the Lecture {week - 1} quiz. Mark one item together. Then:\n\n"
        )
        frame_header = "### Minutes 10–12 — Frame"
        build_header = "### Minutes 12–35 — Build"
    else:
        hook_header = "### Minutes 0–8 — Hook"
        hook_extra = ""
        frame_header = "### Minutes 8–12 — Frame"
        build_header = "### Minutes 12–35 — Build"

    sec_bits = []
    for num, title, body in p["sections"]:
        compact = "\n".join(ln for ln in body.splitlines() if ln.strip())[:800]
        sec_bits.append(f"**{num}. {title}.** {compact}")
    extra_body = "\n\n".join(sec_bits)

    dn = do_not_line(p, g)
    cut = g.get("cut") or (p["sections"][-1][1] if p["sections"] else "The last example.")
    add = g.get("add") or (p["lab"][-1] if len(p["lab"]) > 1 else "One more worked example on the board.")

    snippet = g.get("snippet") or p["snippet"] or ""
    snippet_md = f"\n## Snippet\n\n{snippet}\n" if snippet else ""

    return f"""# Lecture {week} — {p['title']}

**Week {week} of 15** · {course}  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** {kernel}  
**Success check:** {success}

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

{quiz_note}- Demo: `{demo}` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture {week} | Goal: {goal} | Invariant: {inv}`

## Board at the end (they photograph this)

{board_block(p, g)}

## Slides today (cap: 6)

{slides_table(p, g)}

---

## Lecture (75 min)

{hook_header}

{hook_extra}**Say:** {hook_say}

**Ask:** {hook_ask}

**Board:** parked strip. Then {p['board_first'] or 'today’s picture'}.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *{p['this_week'] or p['title']}*.

**Do not:** {dn}

{frame_header}

**Say:** {frame_say}

**Ask:** {frame_ask}

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

{build_header}

{build[0]}

{build[1]}

{build[2]}

**Ask:** {ask_build}

**They do:** {they_build}

**Do not:** {COURSE_DO_NOT.get(course, 'Skip the attempt.')}

### Minutes 35–50 — Show

**Say:** {show_say}

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** {attempt_say}

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** {land_say}

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

{live_table(p, g)}

Point them at `{demo}` as the after-class check, not as the lecture.

---

## Lab

{join_list(p['lab'])}

---

## Homework

{join_list(p['hw'])}

---

## Quiz next meeting (they hear this now)

{quiz_next(p)}

{snippet_md}
## Extra exercises

See [[{p['folder']}/exercises/Week {week:02d}]].

---

## Notes you may still need (from the outline)

{extra_body or '_none_'}

---

## Common mistakes

{join_list(p['mistakes'])}

## If we run long, cut

{cut}

## If we run short, add

{add}
"""


def render_midterm(p: dict, g: dict) -> str:
    week = p["week"]
    course = p["course"]
    inv = g.get("invariant") or COURSE_INVARIANT.get(course, "")
    kernel = g.get("kernel") or p["this_week"]
    topics = g.get("midterm_topics") or ", ".join(p["goals"][:4]) or "weeks 1–7"
    demo = demo_path(p)
    leftover = "\n\n".join(
        f"**{num}. {title}.** {body.strip()}" for num, title, body in p["sections"] if "midterm" not in title.lower()
    )
    return f"""# Lecture {week} — {p['title']}

**Week {week} of 15** · {course}  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** {kernel}  
**Success check:** {g.get('success') or 'they sit the exam; after, they can state the leftover kernel in one sentence'}

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `{demo}` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture {week} | Goal: leftover kernel | Invariant: {inv}`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** {topics}

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

{board_block(p, g)}

## Slides today (cap: 2)

{slides_table(p, g)}

---

## After the exam (~15–25 min lecture)

**Say:** {g.get('hook_say') or 'The exam is over. The leftover kernel is on the parked strip.'}

**Ask:** {g.get('hook_ask') or (p['goals'][1] if len(p['goals'])>1 else 'What is the leftover picture?')}

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.

{leftover}

### Show / attempt if time

**Say:** {g.get('show_say') or p['live'] or 'One demo of the leftover kernel.'}

**They do:** {g.get('attempt_say') or (p['lab'][0] if p['lab'] else 'A short fragment.')}

---

## Live coding (remaining time)

{live_table(p, g)}

---

## Lab

{join_list(p['lab'])}

---

## Homework

{join_list(p['hw'])}

---

## Quiz next meeting

None this week — midterm. Next quiz is Lecture {week + 1}.

## Extra exercises

See [[{p['folder']}/exercises/Week {week:02d}]].

## If we run long, cut

{g.get('cut') or 'Live coding. Keep the leftover board.'}

## If we run short, add

{g.get('add') or 'One more worked leftover example.'}
"""


def render_studio(p: dict, g: dict) -> str:
    week = p["week"]
    course = p["course"]
    inv = g.get("invariant") or COURSE_INVARIANT.get(course, "freeze scope; tests before paint")
    kernel = g.get("kernel") or p["this_week"] or "desk review"
    return f"""# Lecture {week} — {p['title']}

**Week {week} of 15** · {course}  
**Meeting:** studio (not a content lecture)  
**Kernel:** {kernel}  
**Success check:** {g.get('success') or 'a TA can run the README or see the week’s deliverable without a second tool'}

This meeting is **studio**. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Rubric / report headings on the parked strip.
- Clock visible.
- Demo only if a volunteer asks for a blocked kernel: `{demo_path(p)}`.
- Parked strip: `Lecture {week} | Goal: freeze and review | Invariant: {inv}`

## Board at the end (they photograph this)

{board_block(p, g)}

## Slides today (cap: 2)

{slides_table(p, g)}

---

## Lecture / studio (75 min)

### Minutes 0–10 — Frame

**Say:** {g.get('hook_say') or 'This is studio, not a new-topic lecture. Cuts are allowed. Tests and the README beat new features.'}

**Ask:** {g.get('hook_ask') or 'If you are behind, what do you cut first? Wait seven seconds.'}

**They do:** write their cut list in one column.

**Do not:** introduce a new library today.

### Minutes 10–65 — Desk review

**Say:** {g.get('frame_say') or (p['live'] or 'I circulate. Kernel tests first. Then README. Then look.')}

**They do:** {g.get('attempt_say') or 'Work. One teammate map. Rehearse 60 seconds if presenting next week.'}

**Do not:** sit at the podium. Do not add features for them.

### Minutes 65–75 — Land

**Say:** {g.get('land_say') or 'Photograph the headings. Homework is the report/repo. Next meeting is presentations or the next sprint — no surprise scope.'}

**Do not:** “Any questions?” End on the clock.

---

## Live coding (60 min)

{live_table(p, g)}

This slot is **more studio**, not a hidden lecture.

---

## Lab

{join_list(p['lab'])}

---

## Homework

{join_list(p['hw'])}

---

## Quiz next meeting

None this week.

## Extra exercises

See [[{p['folder']}/exercises/Week {week:02d}]].

## Notes from the outline

{chr(10).join(f'**{n}. {t}.** {b}' for n,t,b in p['sections']) or '_none_'}

## If we run long, cut

{g.get('cut') or 'New features. Keep freeze.'}

## If we run short, add

{g.get('add') or 'One 60-second rehearsal in front of another team.'}
"""


def render_presentations(p: dict, g: dict) -> str:
    week = p["week"]
    course = p["course"]
    defense = "defense" in p["title"].lower()
    fmt = "defense" if defense else "12 min + 5 questions"
    return f"""# Lecture {week} — {p['title']}

**Week {week} of 15** · {course}  
**Meeting:** {fmt} — not a content lecture  
**Kernel:** {g.get('kernel') or 'the demo runs; they can answer two questions'}  
**Success check:** {g.get('success') or 'they stop on time; no new features; who wrote what is stated'}

Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Timer visible to the speaker.
- Rubric on the parked strip.
- Recording backup if the department requires it.
- Parked strip: `Lecture {week} | {fmt} | Invariant: no new features`

## Board at the end (they photograph this)

{board_block(p, g)}

## Slides today

{slides_table(p, g)}

Student decks are their problem. Yours is a timer.

---

## The meeting

**Say:** {g.get('hook_say') or f'This meeting is presentations ({fmt}). No new features. I will cut you at the clock.'}

**Ask (every team, two of):** {g.get('frame_ask') or (p['sections'][0][2].split(chr(10))[0] if p['sections'] else 'Where is the kernel? What did you cut? Who wrote what?')}

**They do:** present. Live-coding hour is more talks.

**Do not:** debug on stage. Do not let a deck become the product.

---

## Live coding (60 min)

{live_table(p, g)}

---

## Lab

{join_list(p['lab'])}

---

## Homework

{join_list(p['hw'])}

---

## Quiz

None.

## Extra exercises

See [[{p['folder']}/exercises/Week {week:02d}]].

## If we run long, cut

{g.get('cut') or 'Q&A. Keep the clock.'}

## If we run short, add

{g.get('add') or 'One extra question on tests or a limitation.'}
"""


def wrap_rich(text: str, p: dict) -> str:
    """Keep detailed CG / CompGeo notes; insert a session-guide block after the title."""
    if "## Before you enter" in text:
        return text
    week = p["week"]
    course = p["course"]
    inv = COURSE_INVARIANT.get(course, "")
    demo = demo_path(p)
    kind = kind_of(p, {})
    kind_line = {
        "midterm": "This meeting includes a **midterm**. Say that at the door.",
        "studio": "This meeting is **studio**, not a content lecture.",
        "presentations": "This meeting is **presentations** (12+5), not a content lecture.",
        "content": "Run the 75 minutes as **moves** (Say / Ask / Board / Slide / They do). Detailed notes follow.",
    }[kind]
    block = f"""
This file is a **session guide** ([[Teaching/24 Session Guides]]) plus the detailed notes. {kind_line}

## Before you enter

- Demo: `{demo}` (local, no CDN). Serve the folder if ES modules fail.
- Backup: board first — {p['board_first'] or "today's picture"}.
- Parked strip: `Lecture {week} | {p['title']} | Invariant: {inv}`
- Quiz from last lecture (except Lecture 1 / midterm / presentations).

## Board at the end (they photograph this)

{board_block(p, {})}

## Slides today (cap: 6)

Photograph, animation, or 20pt code only. If a slide has the argument in sentences, delete the sentences and write them on the board.

## How to run this meeting

Use the **Timing** or **Classroom moves** table below as the 75-minute spine. For each block: **Say** the question, **Board** the picture, **They do** a fragment, **Do not** skip the attempt. Then stand up for live coding (60 min).
"""
    m = re.search(r"\n## ", text)
    if m:
        text = text[: m.start()] + "\n" + block + text[m.start() :]
    else:
        text = text.rstrip() + "\n" + block + "\n"
    if "## Extra exercises" not in text:
        text += f"\n\n## Extra exercises\n\nSee [[{p['folder']}/exercises/Week {week:02d}]].\n"
    return text


def is_gold_session(text: str) -> bool:
    return "### Minutes 0–8" in text or "### Minutes 0–10 — Retrieve" in text


def is_thin(text: str) -> bool:
    return "Core definition and one picture" in text


def process_file(path: Path) -> str:
    folder = path.parent.name
    text = path.read_text(encoding="utf-8")
    if folder not in FOLDER_COURSE:
        return "skip-folder"
    if folder == "Programming" and path.name in {
        "Lecture 01 What a program is.md",
        "Lecture 02 Variables and strings.md",
    }:
        return "skip-gold"
    p = parse(text, folder)
    if p["week"] == 0:
        return "skip-parse"
    g = GOLD.get((p["course"], p["week"]), {})
    kind = kind_of(p, g)
    if kind == "midterm":
        out = render_midterm(p, g)
    elif kind == "studio":
        out = render_studio(p, g)
    elif kind == "presentations":
        out = render_presentations(p, g)
    else:
        out = render_content(p, g)
    path.write_text(out.replace("\r\n", "\n"), encoding="utf-8")
    return "rewrite"


def main() -> None:
    gold_load()
    counts: dict[str, int] = {}
    for path in sorted(ROOT.rglob("Lecture *.md")):
        if "tools" in path.parts:
            continue
        status = process_file(path)
        counts[status] = counts.get(status, 0) + 1
        rel = path.relative_to(ROOT)
        if status in ("rewrite", "wrap"):
            print(f"{status:8} {rel}")
    print("---")
    for k, v in sorted(counts.items()):
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
