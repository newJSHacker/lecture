"""Full-script GOLD for Modern JavaScript Development and Interactive Web Development (15 meetings each)."""


def register(GOLD: dict) -> None:
    C = "Modern JavaScript Development"
    GOLD[(C, 1)] = dict(
        kernel="let/const (no var); arrow as expression; default param",
        success="they rewrite a var/function helper to const + arrow and can say why new Arrow() fails",
        invariant="one binding, one module, no hidden globals",
        goal="stop teaching 1999 JavaScript",
        board="""```
let     rebind OK, block scope
const   no rebind; object fields still mutable
var     hoists — forbidden in this course

const add = (a, b = 0) => a + b;
=>  lexical this;  not a constructor
```""",
        slides=[],
        hook_say="IGWT ships ES modules. Three.js samples are arrows and const. If we spend a week on var, the rest of the program fights us. Today: bindings and arrows.",
        hook_ask="What happens if you write const n = 1; n = 2? Wait seven seconds. Want: TypeError, not silent.",
        frame_say="Block scope. const is the default; let when you rebind. Arrow is shorter and lexical this — it is not function. We freeze: no var, no new on an arrow.",
        frame_ask="Can you call an arrow with new? Want: no.",
        build=[
            "**Say:** A binding is a name. var hoists and leaks out of blocks — that is why we ban it.",
            "**Board:** function add(a,b) vs const add = (a,b=0) => a+b. Circle default param.",
            "**Say:** Arrows do not get their own this and cannot be constructors. Methods that need this wait until week 10.",
        ],
        ask_build="Does const freeze the object? Want: no — only the binding.",
        they_build="On paper: five arrows (double, even?, clamp, lerp, identity) plus one default-param helper.",
        show_say="Rewrite a var/function script into const/arrows live. Plant var i in a for and log it after the loop. Demo Modern JavaScript/code/01-arrows.html. Serve the folder if you later add type=module.",
        attempt_say="Five arrows with a console.assert each. Default-param helper last. Eight minutes.",
        land_say="Photograph the board. Lab: arrows + asserts; a default-param helper. Homework: one page on this vs arrows; rewrite a var script. Quiz: const rebound, arrow as constructor, default param.",
        live=[
            ("0–10", "const vs let vs var", "Plant var hoisting after a block."),
            ("10–30", "Rewrite to arrows", "Plant new on an arrow. Read the TypeError."),
            ("30–45", "Default param + map", "They copy 01-arrows.html kernel."),
            ("45–60", "They write five arrows", "Circulate. No CDN."),
        ],
        cut="Defaults if the rewrite is still messy. Keep const + arrow.",
        add="A default-param helper with a test.",
    )
    GOLD[(C, 2)] = dict(
        kernel="{x,y}=p and [...a, x]; object spread is shallow",
        success="they merge two option objects with spread and can name one nested field that is still shared",
        invariant="spread copies one level; nested objects are aliases",
        goal="pattern-match a point without p.x soup",
        board="""```
const { x, y } = p;
const q = { ...p, y: 0 };

[...a, x]          rest: (...args)

shallow:  nested mesh.geometry  still shared
```""",
        slides=[],
        hook_say="Last time: one binding. Today: take a point apart. Graphics code is full of {x,y,z}. If they think spread deep-copies a mesh, they will mutate someone else’s geometry.",
        hook_ask="After const q = { ...p }; q.nested.k = 1 — does p.nested.k change? Wait. Want: yes, same object.",
        frame_say="Destructure in assignment and in parameters. Spread arrays and objects. Rest collects the leftover. Deep copy is structuredClone or a serializer — name only today.",
        frame_ask="Rename while destructuring: const { x: px } = p — what is px?",
        build=[
            "**Say:** A pattern on the left matches a shape on the right. Missing fields are undefined unless you default.",
            "**Board:** swap [a,b] = [b,a]. Clone array [...a]. Clone point { ...p }.",
            "**Say:** Merge options: { ...defaults, ...user }. Last wins. Nested user.mesh is not cloned.",
        ],
        ask_build="Rest vs spread — which is the left side of a signature?",
        they_build="On paper: merge {color:'#111', size:2} with {size:4}. Write the result. Star the nested alias pitfall.",
        show_say="Swap via destructure; clone an array; clone a point; then mutate a nested field. Demo Modern JavaScript/code/02-spread.html. Read the shared nested key out loud.",
        attempt_say="Merge two option objects. Eight minutes. Then write one sentence: what is still shared.",
        land_say="Lab: merge + deep-copy discussion. Homework: shallow vs deep paragraph; eight tests. Quiz: clone array, rename destructure, shallow pitfall.",
        live=[
            ("0–10", "{x,y}=p", "Plant p.x still after rename — they forgot the new name."),
            ("10–30", "Spread clone + nested mutate", "Plant ‘it copied everything’."),
            ("30–45", "Merge options", "Last-wins demo."),
            ("45–60", "They merge on paper then in the file", "Circulate."),
        ],
        cut="Rest parameters. Keep destructure + shallow spread.",
        add="Deep copy discussion: structuredClone name, JSON round-trip cost.",
    )
    GOLD[(C, 3)] = dict(
        kernel="named export / import; type=module; serve the folder",
        success="they split lerp into math.js and import it; they can say why file:// failed",
        invariant="a file is an API; no hidden globals; file:// often breaks modules",
        goal="two files, one named export",
        board="""```
// math.js
export function lerp(a, b, t) { return a + (b-a)*t; }

// main.js   <script type="module" src="main.js">
import { lerp } from './math.js';

file://  →  often fails     python -m http.server
named exports = course policy
```""",
        slides=[("Optional: console CORS / module error on file://", "photograph the error; do not draw Chrome")],
        hook_say="If it is not a module with a test, it is not a kernel. Today the file boundary is the API. Mixing a CDN script until it ‘works’ is how secrets and version skew arrive.",
        hook_ask="Why did import fail when you double-clicked the HTML? Wait. Want: file:// / modules / CORS.",
        frame_say="Named exports for kernels. Default is optional, not the policy. Browsers need type=module and a local server. Bundlers preview — Vite is next week, not today.",
        frame_ask="Relative path: './math.js' — may you omit the .js in the browser? Want: no, not without a bundler.",
        build=[
            "**Say:** export is the public list. import names what you take. Nothing else leaks.",
            "**Board:** two files, one arrow between them labeled lerp.",
            "**Say:** Serve: python -m http.server or npx serve in the folder. No CDN. No remote script URL glued to a local import.",
        ],
        ask_build="Named vs default — which does this course write for kernels?",
        they_build="On paper: three modules — math.js (lerp, clamp), io.js (name only), main.js imports both.",
        show_say="Split lerp into math.js; import in main.js. Plant file://. Read the error. Then serve. Demo Modern JavaScript/code/08-modules.html is the reminder page — you still write the two files live.",
        attempt_say="Three modules on disk. README: how to serve. Eight minutes for lerp+import even if io.js is a stub.",
        land_say="Lab: three modules + README serve. Homework: ESM vs classic script; import clamp. Quiz: export syntax, why serve, named vs default.",
        live=[
            ("0–10", "type=module + file://", "Plant double-click. Error out loud."),
            ("10–30", "math.js lerp + import", "Plant missing .js or wrong path."),
            ("30–45", "http.server", "They reload; import works."),
            ("45–60", "They add clamp export", "Circulate. No CDN."),
        ],
        cut="Bundlers preview. Keep named export + serve.",
        add="README serve: one command, one URL.",
    )
    GOLD[(C, 4)] = dict(
        kernel="Promise states; then / catch / finally; Promise.all of two loads",
        success="they construct a timeout Promise and attach catch; they can name the three states",
        invariant="a Promise is pending, fulfilled, or rejected — once; then without catch loses the failure",
        goal="one async value with an error path",
        board="""```
pending  →  fulfilled(value)
         →  rejected(error)

p.then(onOk).catch(onErr).finally(cleanup)

Promise.all([a, b])     allSettled  (name)
```""",
        slides=[],
        hook_say="Fetch returns a Promise. A texture load is a Promise. If they only then(), the rejection is an unhandled scream later. Today: the state machine.",
        hook_ask="Does then() run if the Promise already fulfilled? Wait. Want: yes — it still schedules.",
        frame_say="new Promise((resolve, reject) => …). Do not wrap already-sync math in a Promise. all waits for every success; one reject fails the all. allSettled named for later.",
        frame_ask="What is the return type of fetch('data.json') before you call json()?",
        build=[
            "**Say:** Three states. You cannot un-fulfill. finally runs either way — good for a spinner name.",
            "**Board:** then chain. Circle catch. Forgotten catch = unhandled rejection.",
            "**Say:** Fake load: setTimeout inside new Promise. Then Promise.all of two fakes.",
        ],
        ask_build="all vs allSettled in one sentence?",
        they_build="On paper: Promise.all of two fake loads; what prints if the second rejects.",
        show_say="Fake load with setTimeout wrapped in a Promise; then fetch data.json under a local server. Demo Modern JavaScript/code/03-promise.html. Plant then without catch on a reject.",
        attempt_say="Promise.all of two timeout Promises. Eight minutes. Then add one catch that writes a visible error.",
        land_say="Lab: Promise.all + error-path UI. Homework: why promises vs callbacks; timeout promise. Quiz: three states, fetch return type, unhandled rejection.",
        live=[
            ("0–10", "pending → fulfill", "Plant resolve twice — second is ignored."),
            ("10–30", "timeout Promise + then/catch", "Plant missing catch."),
            ("30–45", "fetch data.json", "Plant file://. Serve. 04-async.html is next week’s await."),
            ("45–60", "They all() two fakes", "Circulate."),
        ],
        cut="allSettled details. Keep states + catch.",
        add="Error path UI: a <pre> that shows the rejection message.",
    )
    GOLD[(C, 5)] = dict(
        kernel="async function; await; try/catch; sequential await vs Promise.all",
        success="they rewrite a then-chain as await and can say when two fetches should run in parallel",
        invariant="await pauses that async function, not the whole page; independent work uses all",
        goal="readable async without a then pyramid",
        board="""```
async function go() {
  const res = await fetch('data.json');
  if (!res.ok) throw new Error(res.status);
  return res.json();
}

sequential:  await a; await b;
parallel:    const [a,b] = await Promise.all([fa, fb]);
```""",
        slides=[],
        hook_say="await is then with a stack you can read. The bug is await in a map without all — you thought you parallelized and you did not. We measure order, we do not invent milliseconds.",
        hook_ask="What does an async function return if you never await it? Wait. Want: a Promise, already started.",
        frame_say="try/catch around await. Empty catch is a bug. for-await named only. Two independent JSON files: all, not await a then await b unless order is required.",
        frame_ask="await inside a non-async function — legal? Want: no (unless the function is async).",
        build=[
            "**Say:** Sugar. The Promise is still there. Errors become throw.",
            "**Board:** two timelines — sequential vs all. Same two fetches.",
            "**Say:** Serve the folder. fetch from file:// throws or CORS-fails — catch must say serve.",
        ],
        ask_build="Why is await Promise.all(urls.map(fetch)) different from urls.map(async u => await fetch(u))?",
        they_build="On paper: sequential vs parallel timing sketch. No fake fps — just order of start/finish.",
        show_say="Load two JSON files in parallel; render. Plant await a then await b first. Switch to all. Demo Modern JavaScript/code/04-async.html. Plant file:// and read ‘serve folder’.",
        attempt_say="Rewrite last week’s then-chain as await. Then time sequential vs all with performance.now() — report which started together, not a made-up speedup.",
        land_say="Lab: sequential vs parallel (measure); try/catch around fetch. Homework: when not to parallelize; Promise.all code. Quiz: async return, await-in-loop smell, try/catch.",
        live=[
            ("0–10", "then → await rewrite", "Plant forgotten async keyword."),
            ("10–30", "two fetches sequential", "They see the wait."),
            ("30–45", "Promise.all", "Plant map(async) without all."),
            ("45–60", "They add try/catch + serve note", "Circulate."),
        ],
        cut="for-await. Keep await + all vs sequential.",
        add="try/catch around fetch that prints res.status when !ok.",
    )
    GOLD[(C, 6)] = dict(
        kernel="fetch JSON; AbortController; no API keys in the frontend",
        success="they abort a previous search fetch and can say where a key must not live",
        invariant="fetch talks HTTP; a race without abort is a stale answer; secrets are not in git",
        goal="GET local JSON, cancel in-flight, never ship a key",
        board="""```
const c = new AbortController();
fetch(url, { signal: c.signal });
c.abort();                 // new search

if (!res.ok) throw …       // 404 is not a throw from fetch

KEY SKULL   —  not in source, not in the bundle
```""",
        slides=[],
        hook_say="AI course and capstone will fetch. Today: local data.json, abort on a new search, and a skull on the board for keys. A CDN or a pasted token is a fail.",
        hook_ask="Does fetch throw on HTTP 404? Wait. Want: no — check res.ok.",
        frame_say="GET JSON is the lab. POST to a local mock is extra. Headers named. Cache: the browser may reuse GET — we do not invent cache timings. Abort cancels the previous in-flight request.",
        frame_ask="Where do API keys live? Want: server / env / never the repo.",
        build=[
            "**Say:** Request, response, body. .json() parses. Serve — file:// breaks fetch the same way it broke modules.",
            "**Board:** AbortController. Race: slow response arrives after a new query.",
            "**Say:** Secrets. No keys in source. AI course will repeat this. Handle 500 with a visible message.",
        ],
        ask_build="What does abort() do to an await fetch?",
        they_build="On paper: search-as-you-type: abort previous, then fetch. Three boxes.",
        show_say="Search-as-you-type fake: abort previous. Serve Modern JavaScript/code/ and fetch data.json (see 04-async.html). Plant a key in a const. Erase it. Plant ignoring !ok.",
        attempt_say="Abort on a second button click. Handle 404/500 with text on the page. Eight minutes.",
        land_say="Lab: abort + handle 500; optional POST to a local mock. Homework: why keys not in git; abort code. Quiz: AbortController, where keys live, GET cache name.",
        live=[
            ("0–10", "fetch data.json + ok", "Plant file:// and missing ok."),
            ("10–30", "AbortController", "Plant race: late response overwrites."),
            ("30–45", "Key skull", "Plant a fake key. Delete. No CDN."),
            ("45–60", "They abort on second click", "Circulate."),
        ],
        cut="POST mock if abort is still shaky. Keep GET + abort + no keys.",
        add="Handle 500 with a visible status.",
    )
    GOLD[(C, 7)] = dict(
        kernel="package.json scripts; Vite for apps that need a bundler; commit the lockfile",
        success="they npm init, add a test script that runs node asserts, and can say why node_modules is not in git",
        invariant="reproducible install is the lockfile; node_modules is generated; no CDN as a bundler",
        goal="one project a TA can npm install && npm test",
        board="""```
package.json
  scripts: { "dev": "vite", "test": "node test.js" }
  dependencies vs devDependencies

package-lock.json    COMMIT
node_modules/        .gitignore

static serve still OK for tiny labs
```""",
        slides=[],
        hook_say="Modules in the browser needed a server. Apps with many files need a bundler. Course policy: Vite when you need it; python -m http.server when you do not. Installing a new bundler mid-lecture is forbidden.",
        hook_ask="Do we commit node_modules? Wait. Want: no.",
        frame_say="npm init. scripts are the API for TAs. lockfile = reproducible lab machines. Global npm installs as the only method is a smell. Import maps named — Vite is what we scaffold today.",
        frame_ask="dev vs build — which command do they run in class?",
        build=[
            "**Say:** Why a bundler: many imports, later TS. Tiny labs still static-serve.",
            "**Board:** scripts, lockfile, gitignore node_modules.",
            "**Say:** Scaffold vite vanilla; import last week’s math module; npm run dev. No CDN script tags.",
        ],
        ask_build="Why commit the lockfile?",
        they_build="On paper: a scripts block with dev and test. Write .gitignore one line: node_modules.",
        show_say="Scaffold vite vanilla; import the math module; run dev. Plant committing node_modules. Plant a CDN <script> ‘just this once’. There is no Vite HTML in code/ — 07-loop.html is a later dt demo, not today’s scaffold.",
        attempt_say="Add a script test that runs node asserts on lerp. Eight minutes. README: npm install, npm test, npm run dev.",
        land_say="Lab: test script + README. Homework: why lockfile; vite project in a repo subfolder. Quiz: node_modules in git?, dev vs build, lockfile. Midterm next week: weeks 1–7.",
        live=[
            ("0–10", "npm init + gitignore", "Plant node_modules add."),
            ("10–30", "vite scaffold + import math.js", "Plant CDN. Remove it."),
            ("30–45", "scripts.test = node test.js", "They see PASS."),
            ("45–60", "They write README serve/dev", "Circulate."),
        ],
        cut="Lockfile sermon if init is slow. Keep scripts + gitignore.",
        add="README: three commands.",
    )
    GOLD[(C, 8)] = dict(
        kernel="JSDoc (or optional TS) on lerp/clamp; Point as {x,y} with a type name",
        success="after the exam they can annotate lerp in JSDoc and say why any is a smell",
        invariant="types are comments the machine can check; any is opting out",
        goal="midterm, then a typed kernel without requiring a TS build",
        kind="midterm",
        midterm_topics="let/const vs var; arrows not constructors; shallow spread; named export + why serve; Promise states + catch; await vs Promise.all; fetch res.ok + abort + no keys; npm scripts, lockfile, no node_modules in git.",
        board="""```
/** @param {number} a @param {number} b @param {number} t */
export function lerp(a, b, t) { return a + (b - a) * t; }

// optional TS leftover
type Point = { x: number; y: number };

any  =  smell
```""",
        slides=[("Optional: JSDoc tooltip on lerp in the editor", "photograph — do not draw the IDE")],
        hook_say="This meeting is a **midterm**, then types as a preview. No laptop for the exam. After: JSDoc on the kernel. TypeScript is optional homework, not a second course.",
        hook_ask="What does any mean? Wait. Want: skip the checker.",
        frame_say="Exam: weeks 1–7. Leftover: why types — catch lerp(a,b,'x') before runtime. JSDoc works without a build. Interface for Point if the lab already has vite+ts. Skip generics.",
        frame_ask="JSDoc vs .ts — which is required this term? Want: neither required; JSDoc is the leftover kernel.",
        build=[
            "**Say:** The exam is over. Types name the kernel so a TA can read lerp without running it.",
            "**Board:** JSDoc on lerp. Point type. Circle any as a smell.",
            "**Say:** Optional: a .ts Point if vite+ts is already there. We do not install a TS toolchain in the leftover hour.",
        ],
        ask_build="Why not start a new Vite+TS project in the exam hour?",
        they_build="On paper: JSDoc for clamp(n, lo, hi). Typed clamp in the attempt if time.",
        show_say="Add JSDoc to lerp; or a .ts Point if the lab has vite+ts. Demo Modern JavaScript/code/08-modules.html as the module reminder. Plant any on lerp. Remove it.",
        attempt_say="Typed clamp — JSDoc or .ts. Midterm reflection if time is gone.",
        land_say="Lab: typed clamp + midterm reflection. Homework: optional TS Point tests. No quiz this week. Next: Map and Set.",
        live=[
            ("0–15", "JSDoc on lerp", "Plant any. Fix number."),
            ("15–40", "Point type name", "They copy. No new bundler."),
            ("40–60", "They JSDoc clamp", "Circulate."),
        ],
        cut="Live coding if the exam ran long. Keep the JSDoc board.",
        add="One more leftover: clamp JSDoc with a failing call they can see.",
    )
    GOLD[(C, 9)] = dict(
        kernel="Map for arbitrary keys; Set for uniqueness; object keys are strings",
        success="they histogram with Map and unique an array with Set; they can say why {} as a dict is a trap",
        invariant="object keys stringify; Map keeps the key you gave it",
        goal="the right collection, not everything in {}",
        board="""```
{}     keys → strings (and symbols)
Map    any key, insertion order     m.set(p, 1); m.get(p)
Set    unique                       s.has(x)

__proto__ as a key on {}  =  fail
WeakMap  name: GC cache
```""",
        slides=[],
        hook_say="A vertex dict keyed by point objects will break if you use {}. Computational Geometry unique-before-hull is a Set. Today: Map and Set as the default collections.",
        hook_ask="Is m.get(p) the same as m.get(otherPointWithSameXY) for two objects? Wait. Want: no — identity, unless you key on a string.",
        frame_say="Map: any key, .set .get .has .delete. Set: unique values. WeakMap named for caches that should not keep objects alive. We do not implement a hashmap.",
        frame_ask="When is {} still OK? Want: a record with known string fields, not a dictionary of arbitrary keys.",
        build=[
            "**Say:** Histogram: Map from word to count. Object-key bug: __proto__ or toString as a key.",
            "**Board:** Map vs object keys table. Set of numbers [1,1,2] → size 2.",
            "**Say:** Unique vertices: Set, or Map if you need a payload. WeakMap name only.",
        ],
        ask_build="Set.has vs array.includes — why Set for a large unique list (teaching-level)?",
        they_build="On paper: anagram check — two Maps of character counts, or one Map and decrement.",
        show_say="Histogram with Map; unique with Set. Demo Modern JavaScript/code/05-mapset.html. Plant {}['__proto__'] as a key. Then Map.",
        attempt_say="Anagram check via maps. Eight minutes. Then unique points with a string key `${x},${y}` if object identity is wrong.",
        land_say="Lab: anagram + object-key bug demo. Homework: when Map; unique points. Quiz: Map vs object, Set.has, WeakMap name.",
        live=[
            ("0–10", "Set unique", "Plant [1,1,2] with {} flags."),
            ("10–30", "Map histogram", "Plant object key stringify of a point."),
            ("30–45", "__proto__ on {}", "They see the trap. Switch to Map."),
            ("45–60", "They write anagram Maps", "Circulate."),
        ],
        cut="WeakMap. Keep Map vs {} + Set.",
        add="Object-key bug demo as a two-minute live.",
    )
    GOLD[(C, 10)] = dict(
        kernel="closure = function + environment; factory; this lost on a callback",
        success="they write makeCounter and fix a button handler that lost this — arrow or bind",
        invariant="a closure remembers bindings, not a photocopy of values at call time unless you wrap them",
        goal="private state without a global",
        board="""```
function makeCounter() {
  let n = 0;
  return () => ++n;     // closes over n
}

this  in a method = the receiver
lost on callback →  arrow  or  .bind(this)
not window
```""",
        slides=[],
        hook_say="Module state is a closure. A GL context held in a closure is common and easy to leak — we name that, we do not open WebGL. Today: factory and this.",
        hook_ask="After const inc = makeCounter(); inc(); inc(); what does the third inc() return? Wait. Want: 3.",
        frame_say="Function plus the environment it was created in. Closures are not magic. this is the receiver of a method; passing obj.method as a listener loses it. Arrow lexical this, or bind. No this = window hacks.",
        frame_ask="Does an arrow inside makeCounter close over n? Want: yes.",
        build=[
            "**Say:** Environment box on the board: n lives after makeCounter returns.",
            "**Board:** makeCounter. Then a class-or-object method handed to addEventListener.",
            "**Say:** Graphics: closing over a heavy context — mention leak. Week 13 will put state in one object instead of a pile of closures.",
        ],
        ask_build="bind vs arrow — name one difference (teaching-level).",
        they_build="On paper: once(fn) — extra factory that runs fn at most once.",
        show_say="makeCounter(); then a button this bug and fix. Demo Modern JavaScript/code/06-closure.html. Plant this as window. Fix with arrow or bind.",
        attempt_say="once(fn) extra. Tests for counter: 1,2,3. Eight minutes.",
        land_say="Lab: once + counter tests. Homework: closure vs global; fix this. Quiz: what a closure keeps, this in arrow, bind.",
        live=[
            ("0–10", "makeCounter", "Plant a global n. Then hide n in the factory."),
            ("10–30", "button this bug", "Plant obj.method as listener. Read undefined."),
            ("30–45", "arrow or bind", "They pick one and freeze it."),
            ("45–60", "They write once(fn)", "Circulate."),
        ],
        cut="GL leak mention. Keep factory + this fix.",
        add="Tests for counter: three asserts.",
    )
    GOLD[(C, 11)] = dict(
        kernel="performance.now() before/after; allocations in a hot loop; reuse vs new",
        success="they measure two versions of a loop and refuse to ship a micro-opt without a number they just took",
        invariant="invented timings are forbidden; measure or omit; do not invent fps",
        goal="a number from the machine, not a vibe",
        board="""```
const t0 = performance.now();
… work …
const t1 = performance.now();   // ms, this run, this machine

hot loop:  no new Vec2 per pixel
prealloc  vs  push in a growing array

Big-O name from Programming — not a substitute for a measure
```""",
        slides=[("Optional: Performance panel screenshot of two measures", "photo; no fps caption you did not record")],
        hook_say="A janky game loop is often allocations, not ‘JavaScript is slow.’ Same rule as CG reports: invented timings are a fail. Today we measure.",
        hook_ask="If you did not call performance.now(), may you write ‘twice as fast’ in the report? Wait. Want: no.",
        frame_say="Measure. GC: new objects per pixel die. Reuse vectors in a renderer. Big-O from Programming week 10 is the sketch; the lab is a table of measured runs. Profiling tab named — optional.",
        frame_ask="Why is new {x,y} inside a 1e7 loop a GC story?",
        build=[
            "**Say:** Two runs, same machine, same input size. Write both numbers. Do not invent fps.",
            "**Board:** performance.now wrap. Alloc vs reuse. Prealloc length vs push.",
            "**Say:** Unreadable micro-opt without a number is a fail. Cap the story at one rewrite.",
        ],
        ask_build="What belongs in the homework table? Want: n, version A ms, version B ms — not a slogan.",
        they_build="On paper: the measure snippet and a two-row table header.",
        show_say="Sum 1e7 numbers; compare push in loop vs prealloc. Demo Modern JavaScript/code/07-loop.html for a dt-capped rAF — we do not quote fps from it. Read the two now() deltas out loud.",
        attempt_say="Don't ship a micro-opt without a number. One GC-friendly rewrite. Eight minutes to fill the table even if the rewrite is incomplete.",
        land_say="Lab: measured pair + one GC-friendly rewrite. Homework: when not to optimize; measured table. Quiz: performance.now, alloc in pixel loop, prealloc.",
        live=[
            ("0–10", "now() wrap", "Plant a claimed speedup with no numbers."),
            ("10–30", "push vs prealloc 1e7", "Read both times. No fps."),
            ("30–45", "alloc in a fake pixel loop", "Reuse one object."),
            ("45–60", "They fill a two-row table", "Circulate."),
        ],
        cut="Big-O recap. Keep measure + one alloc rewrite.",
        add="One GC-friendly rewrite they can screenshot.",
    )
    GOLD[(C, 12)] = dict(
        kernel="assert that throws; a page or node script that prints PASS/FAIL; fixtures",
        success="they have a failing test they then fix; tests that only log 'ok' are rejected",
        invariant="a test that cannot fail is not a test; hidden fixtures do not count",
        goal="the kernel has a red/green list",
        board="""```
function assert(name, cond) {
  if (!cond) throw new Error(name);
}

PASS  lerp 0
FAIL  clamp high     ← keep this case; do not delete

AAA: arrange, act, assert   (name)
No Jest required
```""",
        slides=[],
        hook_say="CG kernels and geometry predicates live or die on fixtures. If it is not a module with a test, it is not a kernel. Today: a tiny runner, not a framework.",
        hook_ask="If every test logs 'ok' and never throws, how do you know lerp is wrong? Wait. Want: you don’t.",
        frame_say="console.assert is allowed; a throw-on-fail runner is clearer on a page. CI / GitHub Actions named, not required this term. Do not delete FAIL cases to go green.",
        frame_ask="What is a fixture here? Want: a known input/output pair.",
        build=[
            "**Say:** Culture: same habit as Computational Geometry. Name the case.",
            "**Board:** PASS/FAIL list. assert helper. Deliberate fail then fix.",
            "**Say:** Port lerp/clamp tests to test.html or node test.js from week 7. Serve if it is a module page.",
        ],
        ask_build="Why keep a test that failed this morning?",
        they_build="On paper: five fixtures for clamp (low, high, inside, equal bounds, NaN policy — pick one and freeze).",
        show_say="Port lerp/clamp tests to a test.html. Plant a test that only console.log('ok'). Then throw. 08-modules.html is the serve reminder — the test page is new today.",
        attempt_say="Five more fixtures. A deliberately failing test then fix. Eight minutes.",
        land_say="Lab: five fixtures + fail-then-fix. Homework: why hidden fixtures; test page. Quiz: AAA name, assert, deleting tests.",
        live=[
            ("0–10", "assert helper", "Plant log-'ok' tests."),
            ("10–30", "test.html lerp/clamp", "Serve if type=module."),
            ("30–45", "Deliberate FAIL then fix", "Do not delete the case."),
            ("45–60", "They add five fixtures", "Circulate."),
        ],
        cut="CI. Keep runner + one red test.",
        add="A deliberately failing test then fix, photographed.",
    )
    GOLD[(C, 13)] = dict(
        kernel="rAF loop; update(dt) then render(); one state object; cap dt",
        success="they can pause/reset a bouncing ball without putting physics inside draw",
        invariant="time is a delta; draw does not simulate; setInterval(16) is not the loop",
        goal="architecture for a graphics app, not a new renderer",
        board="""```
function frame(t) {
  const dt = Math.min(0.05, (t - last) / 1000);
  last = t;
  update(dt);
  render();
  requestAnimationFrame(frame);
}

state = { … }     serialize later
dirty flags       name for editors
```""",
        slides=[],
        hook_say="Interactive Web already has rAF. Computer Graphics I already has a tick. Today it is modules and state: one object, update vs render, tests on the kernel. This is the last content week before studio.",
        hook_ask="Why cap dt? Wait. Want: a backgrounded tab or a hitch must not teleport the ball.",
        frame_say="Loop as architecture. State is one object — JSON extra in lab. Dirty flags named for editors, not required. No Three.js. No invented fps on the HUD.",
        frame_ask="Where does bounce live — update or render?",
        build=[
            "**Say:** Interactive Web and CG I already; now files: loop.js, state, render.",
            "**Board:** update vs render boxes. Cap dt. pause flag.",
            "**Say:** setInterval(16) desyncs and does not pause in a hidden tab the way rAF does.",
        ],
        ask_build="What goes in JSON.stringify(state) — functions? Want: data only.",
        they_build="On paper: state to JSON extra — which fields survive a round-trip.",
        show_say="A bouncing ball with dt, pause, reset. Demo Modern JavaScript/code/07-loop.html (dt-capped rAF). Plant setInterval(16). Plant uncapped dt after a debugger pause.",
        attempt_say="State to JSON extra. Cap dt if missing. Eight minutes.",
        land_say="Lab: JSON state + cap dt. Homework: update vs render paragraph; loop code. Quiz: rAF, dt, pause. Next: studio.",
        live=[
            ("0–10", "rAF + cap dt", "Plant setInterval(16)."),
            ("10–30", "update vs render ball", "Plant physics in render."),
            ("30–45", "pause / reset", "State object, not a global pile."),
            ("45–60", "They JSON.stringify state", "Circulate."),
        ],
        cut="Dirty flags. Keep loop + state + cap dt.",
        add="Cap dt on a hitch they trigger with a debugger pause.",
    )
    GOLD[(C, 14)] = dict(
        kernel="small tool: modules + tests + README how to run (npm test or python -m http.server)",
        success="a TA can follow the README and see tests or the tool without a second undocumented app",
        invariant="drop TypeScript if behind; keep modules + tests; no new bundler today",
        goal="studio — not a content lecture",
        kind="studio",
        board="""```
Must:  named exports · at least 5 asserts · README
Ideas: JSON pretty · fetch dashboard (local) · math lib
Cuts:  drop TS; drop extra UI; keep kernel + tests

npm test     or     python -m http.server
No CDN
```""",
        slides=[("Clock / 12+5 rubric preview", "not a feature list")],
        hook_say="This meeting is **studio**. A small tool, not a framework. JSON pretty, a local fetch dashboard, or a module math lib with tests. Not Three.js.",
        hook_ask="If you are behind, what do you cut first? Wait. Want: TS and chrome; not tests.",
        frame_say="Desk review: import graph + tests. One teammate map. Rehearse 60 seconds. I do not add features for them.",
        frame_ask="What must a TA type to run this?",
        build=[
            "**Say:** Freeze. Tests and README beat a new library.",
            "**Board:** headings: problem, modules, tests, how to run, limits, who wrote what.",
            "**Say:** Serve or npm test first. Then look.",
        ],
        ask_build="May you add Vite today if the tool already serves static? Want: no.",
        they_build="Write a cut list in one column. Then work.",
        show_say="Volunteer review against the board. Demo only if blocked: Modern JavaScript/code/08-modules.html as a serve reminder.",
        attempt_say="Studio. Tests first. I circulate.",
        land_say="Photograph the headings. Homework: report + repo. Next week 12+5. No surprise scope. Ask them: where is await? where is the loop?",
        live=[
            ("0–10", "Headings", "They photograph."),
            ("10–50", "Desk review", "Import graph + tests. Serve first."),
            ("50–60", "60s rehearsal", "Stop."),
        ],
        cut="New features. Keep freeze.",
        add="One 60-second rehearsal in front of another team.",
    )
    GOLD[(C, 15)] = dict(
        kernel="12+5; demo runs; point at await or a test and at the loop if they have one",
        success="they stop at 12; who wrote what is stated; no new features on stage",
        invariant="no new features today",
        goal="presentations — not a content lecture",
        kind="presentations",
        board="""```
12 + 5
Show: a module boundary · a test or assert · how to serve
Ask:  Where is await?  Where is the loop?
No new code on stage
```""",
        slides=[("Timer", "not a slide of APIs")],
        hook_say="Modern JS presentations. 12+5. Point at a module and a test. I cut you at 12. No new features.",
        hook_ask="Where is await? Where is the loop?",
        frame_say="Questions every team gets two of: await, loop, a test, a limitation, who wrote what.",
        frame_ask="Where is await? Where is the loop?",
        build=[
            "**Say:** Timer visible. Rubric: demo runs, explanation, tests, honesty.",
            "**Board:** 12+5. Photograph.",
            "**Say:** Live-coding hour is more talks.",
        ],
        ask_build="What did you cut?",
        they_build="Present.",
        show_say="None. They present the tool. Live-coding hour is more talks.",
        attempt_say="Present the module graph and one assert.",
        land_say="This habit — a module with a test — is Interactive Web’s loop and every later IGWT kernel.",
        live=[("0–60", "Talks", "Cut at 12. No debugging on stage.")],
        cut="Q&A. Keep the clock.",
        add="One extra question on tests or a limitation.",
    )

    C = "Interactive Web Development"
    GOLD[(C, 1)] = dict(
        kernel="canvas.getContext('2d'); beginPath / moveTo / lineTo / arc / fill / stroke; save/restore",
        success="they draw a path (house or smiley) and can restore fillStyle after a nested color change",
        invariant="Canvas 2D is a drawing API, not a z-buffer renderer; one context kind per canvas",
        goal="a first picture from paths",
        board="""```
const ctx = canvas.getContext('2d');   // not webgl today

beginPath  moveTo  lineTo  arc  fill / stroke
save() / restore()     state stack: fillStyle, lineWidth

CSS size ≠ backing store   (DPI name)
0×0 canvas  =  nothing
```""",
        slides=[],
        hook_say="Computer Graphics I puts pixels. This course draws paths in Canvas 2D. WebGL and Three.js are later courses — not the kernel. If getContext('2d') is a mystery, every animation week collapses.",
        hook_ask="What happens if you request '2d' and 'webgl' on the same canvas? Wait. Want: you don’t — one context; mixing is a plant.",
        frame_say="Immediate-ish mode: you issue draws; the bitmap is what remains. State: fillStyle, lineWidth, transform. save/restore is a stack. DPI / backing store vs CSS named — same bug as CG I week 1.",
        frame_ask="Does fill() consume the current path? Want: yes — next shape needs beginPath.",
        build=[
            "**Say:** A drawing API. Not a scene graph. Not Three.js.",
            "**Board:** beginPath → move/line/arc → fill/stroke. save/restore box.",
            "**Say:** Width/height attributes are the backing store. CSS can stretch — we name it, we may cut DPI if long.",
        ],
        ask_build="Why call beginPath before a second shape?",
        they_build="On paper: smiley as three arcs + a path mouth. Indent the calls.",
        show_say="House from paths; then a circle arc. Demo Interactive Web/code/01-canvas.html. Plant 0×0 canvas. Plant fillStyle leak without restore.",
        attempt_say="Smiley. Then save/restore color bug fix. Eight minutes.",
        land_say="Lab: smiley + save/restore. Homework: ImageData vs path API; flag. Quiz: getContext 2d, save/restore, two contexts. No CDN.",
        live=[
            ("0–10", "getContext('2d') + fillRect", "Plant 0×0. Fix width/height."),
            ("10–30", "House paths + arc", "Plant missing beginPath."),
            ("30–45", "save/restore fillStyle", "Plant color leak."),
            ("45–60", "They draw smiley", "Circulate. No WebGL."),
        ],
        cut="DPI. Keep paths + save/restore.",
        add="save/restore color bug fix as a second pass.",
    )
    GOLD[(C, 2)] = dict(
        kernel="requestAnimationFrame; dt in seconds; clearRect; cap dt",
        success="they have a rAF loop that moves with dt and can toggle clear vs trails",
        invariant="time is rAF; input is events; draw is a function",
        goal="motion that does not depend on a magic 16",
        board="""```
function frame(now) {
  const dt = Math.min(0.05, (now - last) / 1000);  // seconds, capped
  last = now;
  clearRect(0,0,w,h);     // or trails on purpose
  // update + draw
  requestAnimationFrame(frame);
}

setInterval(16)  =  not the loop
```""",
        slides=[],
        hook_say="A path that does not move is week 1. Today the clock is rAF. setInterval(16) is a lie: it is not vsync, and a hidden tab keeps waking. We do not invent fps.",
        hook_ask="Why is dt in seconds, not ‘frames’? Wait. Want: motion = velocity × time; refresh rate is not a unit we assume.",
        frame_say="rAF syncs to refresh and slows when the tab is hidden — good. t in seconds; sin(t) for a path. Clear each frame or you paint trails. Cap dt so a hitch does not teleport.",
        frame_ask="What if you forget to request the next frame?",
        build=[
            "**Say:** vs setInterval. One ring: schedule the next frame at the end.",
            "**Board:** rAF ring. dt cap. clearRect vs trails.",
            "**Say:** Pause key sets a flag; the loop still runs or you stop requesting — pick one and freeze.",
        ],
        ask_build="Uncapped dt after a debugger pause — what happens to a ball with vx*dt?",
        they_build="On paper: dt-cap one-liner and a pause flag.",
        show_say="A ball on a sine; pause key. Demo Interactive Web/code/02-raf.html. Plant setInterval(16). Plant forgotten clearRect (trails). Plant uncapped dt.",
        attempt_say="dt-cap. Trail vs clear toggle. Eight minutes.",
        land_say="Lab: dt-cap + trail toggle. Homework: why rAF; loop as a module. Quiz: rAF vs interval, dt, hidden tab.",
        live=[
            ("0–10", "rAF ring", "Plant setInterval(16)."),
            ("10–30", "sine ball + dt", "Plant pixels-per-frame with no dt."),
            ("30–45", "clear vs trails + pause", "They see both."),
            ("45–60", "They cap dt", "Circulate. No fps claims."),
        ],
        cut="Pause key if dt is still wrong. Keep rAF + dt + clear.",
        add="Trail vs clear toggle.",
    )
    GOLD[(C, 3)] = dict(
        kernel="map clientX/Y through getBoundingClientRect onto the backing store; Pointer Events",
        success="they drag a circle that tracks the pointer when CSS size ≠ canvas.width",
        invariant="CSS pixels are not canvas pixels until you scale; listen, don’t poll",
        goal="the click lands on the path",
        board="""```
const r = canvas.getBoundingClientRect();
x = (ev.clientX - r.left) * canvas.width  / r.width;
y = (ev.clientY - r.top)  * canvas.height / r.height;

pointerdown / move / up     setPointerCapture
clientX as a pixel index    =  fail
```""",
        slides=[],
        hook_say="A geometry visualizer is a drag. WebGL picking later is the same mapping idea. If they use clientX as a backing-store index, every HiDPI or CSS-scaled canvas lies.",
        hook_ask="If the canvas is drawn 640 wide but CSS-styled to 320px, where is a click at the right edge in canvas space? Wait. Want: ~640, not 320.",
        frame_say="Pointer Events unify mouse and touch. Capture so drag is not lost. preventDefault on contextmenu if a right-drag is the lab. Hit-test: distance to circle centers.",
        frame_ask="Why setPointerCapture on down?",
        build=[
            "**Say:** Bounding rect + scale. Write the two lines every time until they are muscle.",
            "**Board:** client vs canvas. Circle the multiply by width/r.width.",
            "**Say:** Dragging is down → move (if captured) → up. CG visualizer pattern.",
        ],
        ask_build="offsetX vs the rect formula — when does offsetX lie? (CSS / border teaching-level.)",
        they_build="On paper: hit two circles — formula for ‘which disk contains (x,y)’.",
        show_say="Drag a circle. Right-click prevent menu if needed. Demo Interactive Web/code/03-pointer.html. Plant clientX as pixel index. Stretch the CSS and show the miss, then the scale fix.",
        attempt_say="Hit two circles. Multitouch extra if the first mapping works. Eight minutes.",
        land_say="Lab: hit two circles; multitouch extra. Homework: client vs canvas; drag. Quiz: bounding rect, pointer vs mouse, capture.",
        live=[
            ("0–10", "dots at clientX", "Plant. Stretch CSS. Miss."),
            ("10–30", "rect scale mapping", "They match 03-pointer.html."),
            ("30–45", "drag + capture", "Plant lost drag off canvas."),
            ("45–60", "They hit two circles", "Circulate."),
        ],
        cut="Multitouch. Keep mapping + one drag.",
        add="Hit two circles.",
    )
    GOLD[(C, 4)] = dict(
        kernel="SVG as DOM; viewBox as the coordinate system; pick SVG vs Canvas on purpose",
        success="they build a small SVG (chart or icon) with a viewBox and can say when Canvas is the better kernel",
        invariant="SVG retains nodes; Canvas retains pixels; 10k SVG particles is the wrong tool",
        goal="a graphic you can inspect in Elements",
        board="""```
<svg viewBox="0 0 100 100" width="200">
  <circle cx="50" cy="50" r="40"/>
</svg>

viewBox  =  user space     CSS width = paint size
Canvas   =  bitmap         SVG = DOM (hover, a11y)
```""",
        slides=[],
        hook_say="Last week the hit was math on a bitmap. Today the hit can be a DOM node. Icons, charts, overlays: SVG. Particles and per-pixel: Canvas. We do not use SVG as a fake WebGL.",
        hook_ask="What does viewBox='0 0 100 100' mean if the SVG is 400px wide? Wait. Want: user unit 1 is 4 CSS px — coordinates stay 0..100.",
        frame_say="Retained vs immediate. viewBox decouples coordinates from CSS size. Interop: HUD icons later. 3D stays Canvas/WebGL next semester — name only.",
        frame_ask="Why is a 10k-particle sim a bad SVG?",
        build=[
            "**Say:** Elements: circle, rect, polygon, text. You can addEventListener on a node.",
            "**Board:** viewBox 0 0 100 100. Stretch without viewBox = mess.",
            "**Say:** Bar chart from an array: createElementNS, set attributes. Namespace is not optional.",
        ],
        ask_build="createElement('circle') vs createElementNS — why NS?",
        they_build="On paper: hover fill — CSS :hover or a pointer listener on a rect.",
        show_say="An SVG bar chart from an array. Demo Interactive Web/code/04-svg.html. Plant missing viewBox stretch. Plant createElement without NS (silent fail).",
        attempt_say="Interactive hover fill. Eight minutes. Export SVG extra if short.",
        land_say="Lab: hover fill; export extra. Homework: SVG vs Canvas paragraph; chart. Quiz: viewBox, when canvas, DOM node cost.",
        live=[
            ("0–10", "svg + viewBox circle", "Plant no viewBox, CSS stretch."),
            ("10–30", "bars from array", "Plant HTML namespace."),
            ("30–45", "hover fill", "DOM, not a pixel test."),
            ("45–60", "They add one bar", "Circulate. No 10k nodes."),
        ],
        cut="Interop lecture. Keep viewBox + one chart.",
        add="Export SVG extra (serialize or copy markup).",
    )
    GOLD[(C, 5)] = dict(
        kernel="CSS transition on transform/opacity; hover/focus/class states; prefers-reduced-motion",
        success="they lift a button on hover with transform and can disable the motion when reduced-motion is on",
        invariant="transition specific properties; transform/opacity composite; transition:all is a smell",
        goal="a state change that eases, not a second animation engine",
        board="""```
.btn { transition: transform 0.2s ease; }
.btn:hover, .btn:focus { transform: translateY(-4px); }

@media (prefers-reduced-motion: reduce) {
  * { transition: none; }
}

width / top  →  layout    transform → composite
```""",
        slides=[],
        hook_say="Not every motion is rAF. A HUD button that lifts is CSS. Animating width is layout tax. We name composite vs layout; we do not invent fps. Reduced motion is not optional politeness.",
        hook_ask="Is transition: all 1s a good default? Wait. Want: no — unknown properties, long layout.",
        frame_say="States: hover, focus, class on. Properties: transform and opacity. Layout-triggering props jank. Inclusive: prefers-reduced-motion. Keyboard focus must lift too, not only hover.",
        frame_ask="Why not transition width to ‘grow’ a card?",
        build=[
            "**Say:** From / to are CSS states. The browser interpolates. No loop yet — that is keyframes next week.",
            "**Board:** transform lift. reduced-motion query. Circle :focus.",
            "**Say:** Class toggle from JS is the same transition. Do not start GSAP this week.",
        ],
        ask_build="Does :hover fire on a touch phone? Want: unreliable — class or :focus-visible matters.",
        they_build="On paper: reduced-motion media query that kills transitions.",
        show_say="A button that lifts on hover; a class toggle. Demo Interactive Web/code/05-css.html shows keyframes + reduced motion — live-code the hover lift beside it. Plant transition:all. Plant width animation.",
        attempt_say="reduced-motion query. Don't transition width — use transform. Eight minutes.",
        land_say="Lab: reduced-motion + no width transition. Homework: why transform; card. Quiz: which props, reduced motion, transition all smell.",
        live=[
            ("0–10", "hover lift transform", "Plant top: instead of transform."),
            ("10–30", "class toggle + :focus", "Plant hover-only, no keyboard."),
            ("30–45", "reduced-motion", "They toggle the OS/emulation."),
            ("45–60", "They kill transition:all", "Circulate. No fps."),
        ],
        cut="Long motion sermon. Keep transform + reduced-motion.",
        add="Don't transition width — a side-by-side plant.",
    )
    GOLD[(C, 6)] = dict(
        kernel="@keyframes; animation-iteration; steps() for a sprite; playState from JS",
        success="they write a spinner (or bounce) in CSS and can pause it on hover without a rAF loop",
        invariant="keyframes are declarative UI motion, not a physics engine",
        goal="a loop the stylesheet owns",
        board="""```
@keyframes spin { to { transform: rotate(360deg); } }
.spinner { animation: spin 0.8s linear infinite; }

steps(4)  +  background-position   sprite strip

el.style.animationPlayState = 'paused';
physics in keyframes  =  fail
```""",
        slides=[],
        hook_say="Transitions are A→B. Loaders and idle UI loop. That is keyframes. A bouncing rigid body still belongs in rAF. Heavy infinite filters are a tax we will not invent numbers for — we just do not ship them.",
        hook_ask="Can @keyframes replace dt integration for a game? Wait. Want: no.",
        frame_say="Declarative motion. steps() + background-position for a 4-frame sprite extra. JS control: animationPlayState. Reduced motion still applies — 05-css.html already shows the query.",
        frame_ask="linear vs ease-in-out on a continuous spinner — which hides the seam?",
        build=[
            "**Say:** Name the animation, attach it, decide infinite or forwards.",
            "**Board:** @keyframes spin. Then steps(4) sprite strip.",
            "**Say:** Pause on hover via CSS or playState. Sequence two animations extra if short.",
        ],
        ask_build="Who owns time here — rAF or CSS?",
        they_build="On paper: pause-on-hover rule. One selector.",
        show_say="A spinner; then a 4-frame sprite extra. Demo Interactive Web/code/05-css.html (bounce + reduced motion). 06-hud.html is the overlay demo for week 10 — not today’s kernel.",
        attempt_say="Pause on hover. Eight minutes. Two animations sequenced extra if they finish.",
        land_say="Lab: pause on hover; sequence extra. Homework: CSS vs rAF; spinner. Quiz: @keyframes, steps, physics in CSS?",
        live=[
            ("0–10", "@keyframes spin", "Plant a rAF spinner ‘because we can’."),
            ("10–30", "infinite + reduced-motion", "Respect the query."),
            ("30–45", "steps sprite extra", "Plant physics in keyframes."),
            ("45–60", "They pause on hover", "Circulate."),
        ],
        cut="JS playState. Keep @keyframes + infinite + reduced-motion.",
        add="Two animations sequenced extra.",
    )
    GOLD[(C, 7)] = dict(
        kernel="gsap.to tween; timeline sequence; local vendor file, no CDN",
        success="they play a 3-step timeline from a click and skip it when reduced-motion is on",
        invariant="GSAP is for UI stories; the renderer loop stays rAF; no CDN",
        goal="one timeline you can kill",
        board="""```
<script src="../vendor/gsap.min.js"></script>   /* local */

gsap.to(el, { x: 80, duration: 0.6 });
gsap.timeline().to(…).to(…).to(…);

reduced-motion  →  skip timeline
kill()  when leaving the scene
```""",
        slides=[],
        hook_say="Timelines beat ad-hoc rAF for a three-beat UI story. Games still need week 2’s loop. Course: two weeks of taste, not certification. Loading GSAP from a CDN is a fail — vendor/gsap.min.js is in the repo.",
        hook_ask="If the motion is one hover lift, do you need GSAP? Wait. Want: no — CSS was week 5.",
        frame_say="Why a library: sequence, stagger, kill. Bundle cost: know it, do not invent KB. Reduced motion: skip. Do not tween every particle of a sim.",
        frame_ask="tween vs timeline in one sentence?",
        build=[
            "**Say:** Local script tag. If gsap is undefined, the path is wrong — not ‘use a CDN’.",
            "**Board:** gsap.to. Then a 3-step timeline: fade, move, color.",
            "**Say:** Stagger extra. matchMedia reduced-motion like 09-gsap.html.",
        ],
        ask_build="What does kill() prevent?",
        they_build="On paper: stagger of three boxes — one timeline or three tweens?",
        show_say="A 3-step timeline: fade, move, color. Demo Interactive Web/code/09-gsap.html (loads ../vendor/gsap.min.js). Plant a CDN URL. Remove it. Plant running the timeline when reduced-motion is on.",
        attempt_say="Stagger extra. Respect reduced motion: skip timeline. Eight minutes.",
        land_say="Lab: stagger + reduced-motion skip. Homework: when not to GSAP; timeline. Quiz: tween vs timeline, kill, CSS enough? Midterm next week: weeks 1–7.",
        live=[
            ("0–10", "local vendor script", "Plant CDN. Fix relative path."),
            ("10–30", "3-step timeline", "Play on button, not autoplay."),
            ("30–45", "reduced-motion skip", "They toggle and re-click."),
            ("45–60", "They stagger", "Circulate. No particle GSAP."),
        ],
        cut="Bundle-size talk. Keep local GSAP + timeline + reduced-motion.",
        add="Respect reduced motion: skip timeline.",
    )
    GOLD[(C, 8)] = dict(
        kernel="compositor layers as a name; transform/opacity vs left/top; will-change sparingly",
        success="after the exam they can say why a left animation is the wrong leftover demo and remove a sprayed will-change",
        invariant="layers are a memory bet; will-change is not a speed cheat code; do not invent fps",
        goal="midterm, then name the compositor",
        kind="midterm",
        midterm_topics="getContext 2d, paths, save/restore; rAF, dt, clear, cap; pointer mapping via bounding rect; SVG viewBox vs Canvas; transitions on transform + reduced motion; @keyframes vs physics; local GSAP timeline, no CDN.",
        board="""```
layout  →  paint  →  composite

transform / opacity     (composite)
left / top / width      (layout)

will-change: transform;    /* hint; costs memory; remove after */
paint flashing            /* DevTools name — photograph if used */
```""",
        slides=[("Optional: paint-flashing screenshot, left vs transform", "photo; no fps overlay you invented")],
        hook_say="This meeting is a **midterm**, then the compositor leftover from Web Technologies week 12, now with motion. No laptop for the exam. After: layers as a name. We do not invent fps.",
        hook_ask="Does will-change: transform on every node help? Wait. Want: no — memory, extra layers.",
        frame_say="Exam: weeks 1–7. Leftover: compositor thread name. Paint flashing as a DevTools verb. will-change is a hint you remove. Prefer transform, same policy as Web Tech.",
        frame_ask="Which leftover demo: animate left or transform? Want: show both; keep transform.",
        build=[
            "**Say:** The exam is over. Motion lives on layers if you are lucky; left drags layout.",
            "**Board:** pipeline. will-change warning. Remove after the animation.",
            "**Say:** 08-cull.html is next month’s particle cull — optional glance, not the leftover kernel.",
        ],
        ask_build="Why spray will-change: all?",
        they_build="On paper: remove a will-change after the tween. One rule.",
        show_say="Paint flashing on a janky left animation vs transform. Do not quote fps. Plant will-change on everything. Remove it.",
        attempt_say="Remove a will-change after. Midterm reflection if time is gone.",
        land_say="Lab: remove will-change + midterm reflection. Homework: written layers. No quiz this week. Next: IntersectionObserver.",
        live=[
            ("0–15", "left vs transform", "Plant left. No invented fps."),
            ("15–40", "will-change spray", "Remove after."),
            ("40–60", "They write the three-stage names", "Circulate."),
        ],
        cut="Live coding if the exam ran long. Keep the leftover board.",
        add="One more leftover: photograph paint flashing if DevTools is already open.",
    )
    GOLD[(C, 9)] = dict(
        kernel="IntersectionObserver callback; CSS position:sticky; no raw onscroll without throttle",
        success="they reveal sections with IO and can stick a nav with CSS first",
        invariant="the browser can tell you when a box enters the viewport; scroll listeners are a last resort",
        goal="scroll as a signal, not a per-pixel handler",
        board="""```
const io = new IntersectionObserver((ents) => {
  for (const e of ents) e.target.classList.toggle('in', e.isIntersecting);
});
io.observe(el);     io.disconnect() when done

position: sticky; top: 0;     /* CSS first */
onscroll without throttle     =  fail
```""",
        slides=[],
        hook_say="Storytelling sites and later R3F scroll controls are this idea grown up. A scroll handler that writes layout every pixel is jank we will not measure as a fake fps — we just use IO.",
        hook_ask="Does IntersectionObserver fire on every scroll pixel? Wait. Want: no — it fires on threshold crossings.",
        frame_say="IO: reveal on enter, lazy class on images extra. Sticky: CSS first, not JS top=. If you must listen to scroll, rAF-throttle. Unobserve when the node goes away.",
        frame_ask="What is isIntersecting?",
        build=[
            "**Say:** Observe, toggle a class, CSS does the fade. Do not set element.style.top in the callback.",
            "**Board:** intersection ratio. sticky nav. disconnect.",
            "**Say:** Lazy images: class that sets src or a data-src swap extra — still IO, not onscroll.",
        ],
        ask_build="IO vs scroll listener — one sentence for the homework.",
        they_build="On paper: lazy class on images extra — observe, swap, unobserve.",
        show_say="Sections that fade in via IO. There is no dedicated IO file in code/; do not demo 09-gsap.html as this kernel. Plant onscroll that sets style.top. Plant IO never disconnected.",
        attempt_say="Lazy class on images extra. Sticky nav. Eight minutes.",
        land_say="Lab: lazy class + sticky nav. Homework: IO vs scroll listener; reveal. Quiz: IO callback, sticky, layout in scroll.",
        live=[
            ("0–10", "observe + .in class", "Plant onscroll."),
            ("10–30", "several sections", "Threshold 0.1 name."),
            ("30–45", "sticky CSS nav", "Plant JS stick."),
            ("45–60", "They unobserve", "Circulate."),
        ],
        cut="Scroll-jank deep dive. Keep IO + sticky CSS.",
        add="sticky nav.",
    )
    GOLD[(C, 10)] = dict(
        kernel="HTML overlay HUD on a Canvas 2D scene; pointer-events none except controls",
        success="they position a labeled button over the canvas and add a shape without painting the UI in pixels",
        invariant="HUD is DOM for keyboard and labels; the bitmap is the scene; one state object",
        goal="a sandwich: canvas below, UI above",
        board="""```
.stage { position: relative; }
canvas { display: block; }
.hud { position: absolute; inset: 0; pointer-events: none; }
.hud button { pointer-events: auto; }

all UI painted in canvas  =  no keyboard  =  fail
```""",
        slides=[],
        hook_say="Configurators later are WebGL + DOM labels. This week the scene is Canvas 2D. If the score is only pixels, Tab cannot reach it. pointer-events is the sandwich.",
        hook_ask="If the overlay is inset 0 and pointer-events is auto, can you drag the canvas? Wait. Want: no — the HUD ate the hits.",
        frame_say="HUD: position absolute over the canvas. none on the overlay, auto on controls. SVG overlay extra is the same sandwich. State: one object, same as Modern JS week 13.",
        frame_ask="Why is a <button> better than a canvas hit-rect for ‘Add shape’?",
        build=[
            "**Say:** Two clocks: DOM events and rAF. One state. The button writes state; the loop draws it.",
            "**Board:** sandwich. pointer-events none / auto.",
            "**Say:** a11y: do not ship canvas-only UI. Week 11 will add audio on a gesture — also a DOM control.",
        ],
        ask_build="Who owns the score text — ctx.fillText or a DOM node?",
        they_build="On paper: SVG overlay extra — same absolute layer, pointer-events.",
        show_say="Canvas scene + HTML button that adds a shape. Demo Interactive Web/code/06-hud.html. Plant all UI in fillText. Plant overlay blocking pointer mapping from week 3.",
        attempt_say="SVG overlay extra. a11y: button, not only canvas click. Eight minutes.",
        land_say="Lab: SVG overlay + button. Homework: why HUD in DOM; overlay. Quiz: pointer-events none, why DOM HUD, one state.",
        live=[
            ("0–10", "relative stage + overlay", "Plant overlay eating clicks."),
            ("10–30", "button adds a shape", "State++, loop draws."),
            ("30–45", "pointer-events none/auto", "They drag canvas again."),
            ("45–60", "They replace fillText score with DOM", "Circulate."),
        ],
        cut="State sermon. Keep sandwich + one button.",
        add="a11y: button not only canvas click.",
    )
    GOLD[(C, 11)] = dict(
        kernel="AudioContext after a user gesture; AnalyserNode; draw bars in Canvas 2D",
        success="they start audio on click, draw analyser bars, and can mute without creating a new context every frame",
        invariant="autoplay is blocked; one AudioContext; bars are data, not a 3D engine",
        goal="click-to-start, then a picture of the sound",
        board="""```
click  →  audioCtx.resume()   // or create on gesture
AnalyserNode  fftSize  getByteFrequencyData(buf)
rAF:  analyser → bars on canvas 2d

autoplay noise              =  fail
new AudioContext every frame =  fail
```""",
        slides=[],
        hook_say="Browsers block autoplay. A visualizer is analyser bins into week 1’s fillRect. Semester 5 audio viz is this grown up. No Three.js. No CDN synth library.",
        hook_ask="Why did new AudioContext() in the first script line stay silent? Wait. Want: policy — need a gesture, then resume.",
        frame_say="Gesture first. Oscillator or a local file input extra. Analyser frequencyBinCount. Optional sync from audio.currentTime — name, may cut. Mute is gain or suspend, not a new context.",
        frame_ask="Where does the analyser sit in the graph? Want: source → analyser → destination.",
        build=[
            "**Say:** Click-to-start. Read the autoplay error if you plant autoplay.",
            "**Board:** analyser fft bars. One context.",
            "**Say:** Draw in the rAF you already have. Do not invent fps for the bars.",
        ],
        ask_build="Mute: dest.disconnect vs gain.value = 0 vs suspend — pick one and freeze.",
        they_build="On paper: mute button — which node it touches.",
        show_say="Click-to-start oscillator or file; draw bars. There is no audio demo in code/; do not open 09-gsap.html for this. Plant autoplay. Plant new AudioContext inside rAF.",
        attempt_say="Mute button. File input extra if the oscillator works. Eight minutes.",
        land_say="Lab: mute + file input extra. Homework: autoplay policy; bars. Quiz: why click first, AnalyserNode, autoplay.",
        live=[
            ("0–10", "autoplay plant", "Silent. Then click resume."),
            ("10–30", "oscillator + analyser bars", "Canvas 2D, not WebGL."),
            ("30–45", "one context forever", "Plant construct-in-loop."),
            ("45–60", "They add mute", "Circulate."),
        ],
        cut="currentTime sync. Keep gesture + analyser + bars.",
        add="file input extra.",
    )
    GOLD[(C, 12)] = dict(
        kernel="entities with update(dt) and render(ctx); input as a keys set; a cap on n",
        success="they spawn on click into a list the loop updates, without an 800-line god object",
        invariant="the loop is shared; each entity is a small object; physics is not inside render",
        goal="a mini 2D engine, not Unity",
        board="""```
entities.forEach(e => e.update(dt));
entities.forEach(e => e.render(ctx));

keys = new Set()     keydown add / keyup delete
n ≈ 200 circles OK     n = 200000 not this course

god object 800 lines   =  fail
```""",
        slides=[],
        hook_say="Architecture enough to later map onto a Three.js scene: objects, a loop, input. Today it is Canvas 2D bouncers and a WASD player. Full engines are skipped on purpose.",
        hook_ask="If render draws and also writes vx, what breaks pause? Wait. Want: pause cannot skip sim independently.",
        frame_say="Entity {update, render}. Input: a set of keys, not one global lastKey. Bounds: freeze a cap n. Collision can be naive. Pause is a flag in the loop from week 2.",
        frame_ask="Who calls requestAnimationFrame — each entity or the engine?",
        build=[
            "**Say:** List of entities. Engine owns time and clear. Mapping to later 3D: mesh ≈ entity, not this week’s kernel.",
            "**Board:** update vs render. keys set. cap n.",
            "**Say:** Spawn on click using week 3 mapping. Do not paste an engine from the internet.",
        ],
        ask_build="Why a Set for keys instead of wasd booleans only?",
        they_build="On paper: spawn on click — push entity with vx,vy,r.",
        show_say="Bouncers with WASD player. Demo Interactive Web/code/07-engine.html. Plant physics in render. Plant one 800-line script.",
        attempt_say="Spawn on click. Pause. Eight minutes.",
        land_say="Lab: spawn + pause. Homework: entity table; mini engine. Quiz: update vs render, input map, cap n.",
        live=[
            ("0–10", "entity list + rAF", "Plant god object."),
            ("10–30", "bouncers dt", "Plant sim in render."),
            ("30–45", "WASD keys set", "keyup missing plant."),
            ("45–60", "They spawn on click", "Circulate. Cap n."),
        ],
        cut="n=200 discussion. Keep entities + loop + input.",
        add="pause flag.",
    )
    GOLD[(C, 13)] = dict(
        kernel="skip draw if AABB is off-canvas; pool instead of new per particle; measure with performance.now",
        success="they toggle culling on 1000 particles and can say they must measure before pooling",
        invariant="cull is a boolean skip; pooling is reuse; do not invent fps",
        goal="the same engine, fewer wasted draws",
        board="""```
if (x < -r || x > w + r || y < -r || y > h + r) return;  // skip draw

pool:  dead[i] = true;  reuse slot instead of new
measure:  t0 = performance.now();  …  t1

invented fps           =  fail
pooling without a number =  fail
```""",
        slides=[("Optional: DevTools screenshot of two runs, cull on vs off", "photo of numbers you just took")],
        hook_say="Week 12 spawned freely. Today we skip offscreen draw and we reuse slots. Computational Geometry AABB is the test. Same rule as Modern JS week 11: measure or omit. 08-cull.html already has the toggle.",
        hook_ask="If a particle is off-canvas, do we still update(dt)? Wait. Want: usually yes — it may come back; we skip render.",
        frame_say="Culling: AABB vs canvas. Pooling: reuse particles. Measure with performance.now on a batch — not an fps HUD you made up. Overdraw named.",
        frame_ask="Does culling replace a smaller spawn cap?",
        build=[
            "**Say:** Update can still run. Render returns early. Write the four inequalities.",
            "**Board:** offscreen skip. Pool slot. now() wrap.",
            "**Say:** Toggle cull like the demo. Read two now() deltas. No fps slogan.",
        ],
        ask_build="When is pooling wasted work?",
        they_build="On paper: pool extra — acquire/release two functions.",
        show_say="1000 particles: naive vs skip-offscreen. Demo Interactive Web/code/08-cull.html (checkbox; hint says do not invent fps). Plant an fps number on the board. Erase it. Plant pooling without a measure.",
        attempt_say="Pool extra. Optional readout of two now() numbers — not an fps widget. Eight minutes.",
        land_say="Lab: pool extra; measured readout. Homework: when to pool; cull. Quiz: offscreen skip, pool, overdraw. Next: studio.",
        live=[
            ("0–10", "AABB skip draw", "Plant skipping update too, then discuss."),
            ("10–30", "1000 particles toggle", "08-cull.html. Measure, no fps."),
            ("30–45", "pool acquire/release", "Plant new every spawn."),
            ("45–60", "They write two now() times", "Circulate."),
        ],
        cut="Pooling if cull is not in. Keep skip-draw + measure.",
        add="A measured on/off table, two rows, no fps.",
    )
    GOLD[(C, 14)] = dict(
        kernel="interactive page: rAF loop + pointer or keys + README how to serve",
        success="a TA can serve the folder and see time, input, and a clear without a new library",
        invariant="drop GSAP if behind; keep loop + input; Canvas 2D or SVG, not Three.js",
        goal="studio — not a content lecture",
        kind="studio",
        board="""```
Must:  rAF · dt cap · mapped input or DOM HUD · README
Ideas: instrument · tiny game · data sketch · 2D HUD mock
Cuts:  drop GSAP; drop audio; keep loop + input

python -m http.server     No CDN     No WebGL kernel
```""",
        slides=[("Clock / 12+5 rubric preview", "not a feature list")],
        hook_say="This meeting is **studio**. An interactive page: instrument, tiny game, data sketch, or a 2D HUD mock. Not a 3D engine. Time, input, and a clear are the kernel.",
        hook_ask="If you are behind, what do you cut first? Wait. Want: GSAP and extra scenes; not the loop.",
        frame_say="Desk review: loop and input first. Then culling if they claim many particles. Rehearse 60 seconds. I do not add features for them.",
        frame_ask="Where is dt? Can I Tab to a control?",
        build=[
            "**Say:** Freeze. README beat a new vendor file.",
            "**Board:** headings: loop, input, what you cut, how to serve, who wrote what.",
            "**Say:** Serve first. Then look.",
        ],
        ask_build="May you add Three.js today? Want: no.",
        they_build="Write a cut list. Then work.",
        show_say="Volunteer review against the board. Blocked kernel only: Interactive Web/code/02-raf.html or 07-engine.html — not a new demo.",
        attempt_say="Studio. Loop and input first. I circulate.",
        land_say="Photograph the headings. Homework: report (loop, input, perf note without invented fps). Next week 12+5.",
        live=[
            ("0–10", "Headings", "They photograph."),
            ("10–50", "Desk review", "Loop and input first. Serve."),
            ("50–60", "60s rehearsal", "Stop."),
        ],
        cut="New features. Keep freeze.",
        add="One 60-second rehearsal in front of another team.",
    )
    GOLD[(C, 15)] = dict(
        kernel="12+5; demo runs; point at dt and at SVG-or-canvas",
        success="they stop at 12; who wrote what is stated; no new features on stage",
        invariant="no new features today",
        goal="presentations — not a content lecture",
        kind="presentations",
        board="""```
12 + 5
Show: rAF · dt cap · pointer or HUD
Ask:  where is dt?  SVG or canvas why?
No new CSS/JS on stage
```""",
        slides=[("Timer", "not a slide of GSAP")],
        hook_say="Interactive Web presentations. 12+5. Point at dt and the pointer map. I cut you at 12. No new features.",
        hook_ask="Where is dt? SVG or canvas — why?",
        frame_say="Questions every team gets two of: dt, SVG vs canvas, pointer mapping, what they cut, who wrote what.",
        frame_ask="Where is dt? SVG or canvas why?",
        build=[
            "**Say:** Timer visible. Rubric: demo runs, explanation, honesty about limits.",
            "**Board:** 12+5. Photograph.",
            "**Say:** Live-coding hour is more talks.",
        ],
        ask_build="What did you cut?",
        they_build="Present.",
        show_say="None. They present the page. Live-coding hour is more talks.",
        attempt_say="Present the loop and one input path.",
        land_say="Time, input, and a clear stay the kernel when they meet WebGL next semester. Do not throw away the 2D loop.",
        live=[("0–60", "Talks", "Cut at 12. No debugging on stage.")],
        cut="Q&A. Keep the clock.",
        add="One extra question on a limitation or reduced motion.",
    )