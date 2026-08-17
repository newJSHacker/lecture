"""Full-script GOLD for Web Technologies (15 meetings)."""


def register(GOLD: dict) -> None:
    C = "Web Technologies"
    GOLD[(C, 1)] = dict(
        kernel="client → HTTP → server → HTML; open the Network tab",
        success="they can name client and server and point at Network for a missing file",
        invariant="the browser requests, parses, then paints",
        goal="see a request",
        board="""```
client  →  HTTP  →  server  →  HTML/CSS/JS

URL:  scheme  host  port  path  ?query

200 ok    404 missing    500 server broke
```""",
        slides=[("DevTools Network with a 404 row circled", "do not draw Chrome’s UI")],
        hook_say="IGWT lives in the browser, not a desktop OpenGL window first. Today we watch a request. If you cannot see a request, you will later call a missing texture a shader bug.",
        hook_ask="If the page is blank, where do you look first — the desktop, me, or Network? Wait seven seconds.",
        frame_say="The browser is an engine: request, parse HTML, apply CSS, run JS. HTTPS is HTTP plus TLS — name only. GET vs POST at teaching level: GET is a read, POST submits.",
        frame_ask="Who listens on a port — the browser or the server?",
        build=[
            "**Say:** Draw client and server as two boxes. The arrow is HTTP. Status codes live on the response.",
            "**Board:** URL anatomy. Circle path. Query is optional today.",
            "**Say:** DevTools: Elements, Console, Network. Network is the lab instrument for six semesters. No CDN in this program — we serve local files.",
        ],
        ask_build="GET vs POST in one sentence?",
        they_build="On paper: the request cycle for index.html plus one CSS file. Two arrows.",
        show_say="Serve this folder with python -m http.server. Load index.html. Then visit a missing path and read 404 out loud. Demo Web Technologies/code/01-skeleton.html.",
        attempt_say="Log document.title in the console. Then draw the cycle. Eight minutes.",
        land_say="Photograph the board. Lab: request cycle + title log. Homework: 200 vs 404; serve a local folder. Quiz: who listens on a port, GET vs POST, where is Network.",
        live=[
            ("0–10", "Blank page + console", "Plant: they look at the editor, not Network."),
            ("10–30", "http.server + 200", "Plant file:// and a missing CSS."),
            ("30–45", "404 on a fake path", "Read the status out loud."),
            ("45–60", "They log title", "Circulate. No CDN."),
        ],
        cut="TLS details. Keep request cycle + Network.",
        add="Headers as a name: Content-Type.",
    )
    GOLD[(C, 2)] = dict(
        kernel="<!DOCTYPE html> skeleton; html > head + body tree",
        success="they indent a nested list and the validator in their head matches the indent",
        invariant="HTML is a tree, not Photoshop",
        goal="a first page that is a tree",
        board="""```
html
  head   title, meta charset
  body   heading, p, ul, a

<!DOCTYPE html>
<html lang="en"> … </html>
```""",
        slides=[],
        hook_say="Last time: a request. Today: the document the server sent. Tags nest. If you do not indent, you will not see a broken tree.",
        hook_ask="Where does <title> show — in the page body or the tab? Wait.",
        frame_say="Skeleton: doctype, html lang, head charset, title, body. Purpose of charset: the browser must not guess. lang matters for a11y later.",
        frame_ask="Why indent?",
        build=[
            "**Say:** Tree on the board: html splits into head and body. Head is not visible text.",
            "**Board:** skeleton. Closing tags as matching brackets.",
            "**Say:** Heading, paragraph, list, link. A personal page is enough. We do not paint in a visual editor.",
        ],
        ask_build="Purpose of charset?",
        they_build="On paper: nest ul inside a section, indent.",
        show_say="Build a one-screen personal page live: heading, paragraph, list, link. Plant an unclosed <p>. Read the tree in Elements.",
        attempt_say="About-me page. Validate nesting by indenting. Eight minutes.",
        land_say="Lab: about-me + indent. Homework: Wikipedia intro layout, structure only. Quiz: charset, where title shows, why indent.",
        live=[
            ("0–10", "Skeleton", "Plant missing charset."),
            ("10–30", "Personal page", "Plant unclosed tag."),
            ("30–45", "Elements tree", "They match indent to DOM."),
            ("45–60", "They finish about-me", "Circulate."),
        ],
        cut="Every HTML5 sectioning element. Keep skeleton + tree.",
        add="One <img> with alt, local file, no CDN.",
    )
    GOLD[(C, 3)] = dict(
        kernel="nav, main, form: label+input, submit does a GET until we say otherwise",
        success="every input has a label they can click",
        invariant="semantics is for machines and humans; a div soup is not a form",
        goal="a page with a meaning",
        board="""```
header / nav / main / footer

<label for="email">Email</label>
<input id="email" name="email" />

form without label  =  fail
```""",
        slides=[],
        hook_say="A configurator later is a form on top of WebGL. If they cannot label an input, they cannot ship a UI.",
        hook_ask="Can you click the word Email and focus the box? Wait. Want: only if label for=id.",
        frame_say="nav, main, footer. Forms: name attributes are what would be submitted. We do not post to a backend this week.",
        frame_ask="Why not only placeholder instead of a label?",
        build=[
            "**Say:** Landmark elements. One main.",
            "**Board:** label+input. for/id pair.",
            "**Say:** button type submit vs button. Required and type=email as names.",
        ],
        ask_build="What does name= do?",
        they_build="On paper: a two-field form with labels.",
        show_say="A tiny search form. Plant an input with only placeholder. Then add a real label.",
        attempt_say="Contact form: name, email, message. Every control labeled. Eight minutes.",
        land_say="Lab: labeled form. Homework: landmarks on last week’s page. Quiz: for/id, one main, placeholder vs label.",
        live=[
            ("0–10", "Landmarks", "Two mains as the plant."),
            ("10–35", "Form", "Plant unlabeled input."),
            ("35–50", "Click the label", "They feel the focus."),
            ("50–60", "They add message field", "Circulate."),
        ],
        cut="Every input type. Keep label+main.",
        add="fieldset/legend name only.",
    )
    GOLD[(C, 4)] = dict(
        kernel="content + padding + border + margin; box-sizing: border-box as course policy",
        success="they can draw the box of a 200px element with padding 20 and say the used width under border-box",
        invariant="every visible thing is a box; margin is outside",
        goal="stop guessing spacing",
        board="""```
  margin
    border
      padding
        content

box-sizing: border-box     (course policy)
width includes padding+border
```""",
        slides=[("Optional: a box-model overlay screenshot from DevTools", "the overlay is a photo")],
        hook_say="CSS is not a paint program. It is boxes. If width surprises you, you forgot padding.",
        hook_ask="Is margin inside the border? Wait. Want: no.",
        frame_say="Content, padding, border, margin. Course policy: border-box so width means the box you see. display block vs inline named.",
        frame_ask="What does width include under border-box?",
        build=[
            "**Say:** Draw four nested rectangles. Label them.",
            "**Board:** border-box vs content-box with numbers: 200 + padding.",
            "**Say:** DevTools computed box. We inspect, we do not guess.",
        ],
        ask_build="Margin collapse name — do we need it today? Want: name only.",
        they_build="On paper: a 200px border-box with 20px padding — content width?",
        show_say="A card with padding. Plant content-box. Switch to border-box. Demo 03-box.html.",
        attempt_say="A card: image placeholder, title, two paragraphs. Border-box. Eight minutes.",
        land_say="Lab: card + inspect. Homework: draw three boxes from a screenshot. Quiz: four layers, border-box, margin vs padding.",
        live=[
            ("0–15", "Four layers", "Plant margin inside."),
            ("15–40", "border-box", "Plant content-box width surprise."),
            ("40–55", "Inspect", "Computed pane."),
            ("55–60", "They build the card", "Circulate."),
        ],
        cut="Position absolute. Keep the four layers.",
        add="box-shadow as a fifth decoration, not a layer of the model.",
    )
    GOLD[(C, 5)] = dict(
        kernel="flex container: direction, wrap, justify-content, align-items",
        success="they can make a row of three cards that wrap without float",
        invariant="flex is one axis plus a cross axis; float is not how we layout in this course",
        goal="a row that wraps on purpose",
        board="""```
display: flex
main axis →     justify-content
cross axis ↓    align-items

flex-wrap: wrap
```""",
        slides=[],
        hook_say="A HUD later is a flex row. Floats are history in this program.",
        hook_ask="Which axis does flex-direction: row run along? Wait.",
        frame_say="Container properties vs item flex: 1. Gap. We freeze: no float layouts.",
        frame_ask="What does wrap do when the row is too wide?",
        build=[
            "**Say:** Container first. Then items.",
            "**Board:** main vs cross. Three boxes.",
            "**Say:** justify vs align. Mix them up once on purpose.",
        ],
        ask_build="flex: 1 means?",
        they_build="On paper: nav with logo left, links right — which justify?",
        show_say="Three cards in a row, wrap. Demo 04-flex.html. Plant forgot wrap.",
        attempt_say="Header: logo + nav links with space-between. Eight minutes.",
        land_say="Lab: wrapping cards. Homework: header. Quiz: main axis, wrap, no floats.",
        live=[
            ("0–15", "Row of boxes", "Plant float."),
            ("15–40", "Wrap + gap", "Plant margin hacks."),
            ("40–55", "space-between header", "They copy."),
            ("55–60", "They wrap cards", "Circulate."),
        ],
        cut="flex-grow math. Keep wrap + axes.",
        add="align-self on one item.",
    )
    GOLD[(C, 6)] = dict(
        kernel="grid-template-columns and grid-area; a two-column page",
        success="they can place header / nav / main / footer on a grid without nested flex hacks",
        invariant="grid is two axes at once; flex is one",
        goal="a page of areas",
        board="""```
display: grid
grid-template-columns: 1fr 3fr
grid-template-areas:
  "head head"
  "nav  main"
  "foot foot"
```""",
        slides=[],
        hook_say="A portfolio and a configurator chrome are grids. Flex for a row; grid for the page.",
        hook_ask="When would you still use flex inside a grid cell? Wait. Want: the nav links.",
        frame_say="fr units. Gap. Named areas optional but we use them once so they see the map.",
        frame_ask="1fr 3fr means?",
        build=[
            "**Say:** Two-dimensional. Rows and columns.",
            "**Board:** areas diagram.",
            "**Say:** Repeat() name. Auto-fit later — not required.",
        ],
        ask_build="Grid vs flex in one sentence?",
        they_build="On paper: label areas for a docs site.",
        show_say="Two-column layout. Demo 05-grid.html. Plant 1fr 1fr when they wanted sidebar.",
        attempt_say="Holy-grail: header, nav, main, footer. Eight minutes.",
        land_say="Lab: areas. Homework: grid vs flex paragraph. Quiz: fr, areas, when flex.",
        live=[
            ("0–15", "Columns", "Plant flex-only page."),
            ("15–40", "Areas", "Typo in area name."),
            ("40–55", "Sidebar 1fr 3fr", "They see the ratio."),
            ("55–60", "They place footer", "Circulate."),
        ],
        cut="Masonry. Keep 2-column + areas.",
        add="minmax() name.",
    )
    GOLD[(C, 7)] = dict(
        kernel="viewport meta; one breakpoint with min-width; fluid images",
        success="they can show the same page readable at ~360px and desktop without a second site",
        invariant="responsive is layout change, not a separate mobile app",
        goal="one document, two widths",
        board="""```
<meta name="viewport" content="width=device-width, initial-scale=1"/>

@media (min-width: 720px) { … }

img { max-width: 100%; height: auto; }
```""",
        slides=[("Phone screenshot of a desktop-only page overflowing", "photograph")],
        hook_say="Capstone must work on a phone. Viewport meta is not optional. We do not invent a second URL.",
        hook_ask="What happens without the viewport meta on a phone? Wait.",
        frame_say="Mobile first: default is the small layout; min-width adds columns. Breakpoint: pick one number and freeze it for the lab.",
        frame_ask="min-width vs max-width — which matches mobile-first?",
        build=[
            "**Say:** Viewport. Then fluid images.",
            "**Board:** one breakpoint. Two sketches: stacked vs two-column.",
            "**Say:** DevTools device mode is a lie-detector, not a real phone — still use it today.",
        ],
        ask_build="Why height: auto on img?",
        they_build="Sketch stacked vs 720px two-column.",
        show_say="Stack cards, then row at 720px. Demo 06-responsive.html. Plant missing viewport.",
        attempt_say="Last week’s grid stacks under 720px. Eight minutes.",
        land_say="Lab: viewport + one breakpoint. Homework: overflow screenshot. Quiz: viewport, min-width, img rule.",
        live=[
            ("0–15", "Viewport", "Plant missing meta."),
            ("15–40", "Breakpoint", "Plant max-width spaghetti."),
            ("40–55", "Fluid img", "Broken height."),
            ("55–60", "They stack the grid", "Circulate."),
        ],
        cut="Three breakpoints. Keep one.",
        add="prefers-reduced-motion name — Lecture 13.",
    )
    GOLD[(C, 8)] = dict(
        kernel="script in the page; document.querySelector; textContent",
        success="after the exam they can change a heading from a script without innerHTML of untrusted strings",
        invariant="JS talks to the tree; innerHTML of user text is a hole",
        goal="midterm, then a script that touches the DOM",
        kind="midterm",
        midterm_topics="request cycle; skeleton; labels; box model; flex vs grid; viewport.",
        board="""```
<script src="main.js"></script>   <!-- end of body -->

document.querySelector('h1').textContent = 'IGWT';

textContent  not  innerHTML  for user strings
```""",
        slides=[],
        hook_say="This meeting is a **midterm**, then JS in the page. No laptop for the exam. After: the script is how a HUD will talk to Three.js later.",
        show_say="A button that toggles a class on main. Plant script in head without defer — empty querySelector. Move to end of body.",
        attempt_say="Toggle a class. textContent only.",
        land_say="Lab: toggle. Homework: midterm rewrite of one miss. Next: the DOM. No quiz this week.",
        live=[
            ("0–15", "Script at end of body", "Plant head without defer."),
            ("15–40", "querySelector + textContent", "Plant innerHTML."),
            ("40–60", "Toggle class", "They type. Circulate."),
        ],
        cut="Modules today. Keep querySelector + textContent.",
        add="defer as a name.",
    )
    GOLD[(C, 9)] = dict(
        kernel="createElement, append, textContent; a list built from an array",
        success="they can build three <li> from an array without writing HTML strings",
        invariant="the DOM is a tree you mutate; strings of tags are a last resort",
        goal="nodes, not HTML soup",
        board="""```
document.createElement('li')
li.textContent = item
ul.append(li)

querySelector  →  one
querySelectorAll → list
```""",
        slides=[],
        hook_say="A scene graph later is the same idea: create a node, append it. Today the node is an element.",
        hook_ask="Why not ul.innerHTML += '<li>'+item? Wait. Want: escaping, slowness, XSS.",
        frame_say="createElement, append, remove. textContent. querySelectorAll forEach.",
        frame_ask="append vs innerHTML for a list from data?",
        build=[
            "**Say:** Document is the root. Body is a child.",
            "**Board:** create / append. Array of strings → ul.",
            "**Say:** innerHTML of trusted static chrome is a maybe; never for user data.",
        ],
        ask_build="What does querySelectorAll return?",
        they_build="On paper: steps to add one li.",
        show_say="Build a todo list from ['a','b','c']. Demo 07-toggle.html or 08-todo.html. Plant innerHTML.",
        attempt_say="Render three people names as li. Eight minutes.",
        land_say="Lab: list from array. Homework: remove a node. Quiz: createElement, why not innerHTML, querySelectorAll.",
        live=[
            ("0–15", "createElement", "Plant innerHTML +=."),
            ("15–40", "Array → ul", "Forgot textContent."),
            ("40–55", "Remove one", "They try."),
            ("55–60", "They render names", "Circulate."),
        ],
        cut="DocumentFragment. Keep create+append.",
        add="cloneNode name.",
    )
    GOLD[(C, 10)] = dict(
        kernel="addEventListener('click'); preventDefault on a submit; bubbling named",
        success="they can stop a form from navigating and handle the click on a parent with bubbling",
        invariant="the browser fires events; you listen; preventDefault stops the default verb",
        goal="clicks without inline onclick",
        board="""```
el.addEventListener('click', handler)

form submit  →  preventDefault()   or the page reloads

bubble:  target → … → body
```""",
        slides=[],
        hook_say="WebGL picking is an event. A HUD button is an event. onclick= in HTML is forbidden in this course.",
        hook_ask="Why did the page flash and clear when I clicked Submit? Wait. Want: default form GET.",
        frame_say="addEventListener. preventDefault. stopPropagation named, not required. Touch = pointer later in Interactive Web.",
        frame_ask="Where do you put the listener — inline attribute or script?",
        build=[
            "**Say:** Target vs currentTarget teaching-level.",
            "**Board:** bubble arrows. preventDefault on submit.",
            "**Say:** One listener on ul for many li — delegation idea.",
        ],
        ask_build="What does preventDefault do on a link?",
        they_build="On paper: handler that logs the clicked li text.",
        show_say="Form that does not navigate. Then ul delegation. Demo 07-toggle.html.",
        attempt_say="Button increments a counter in the DOM. Eight minutes.",
        land_say="Lab: preventDefault form + counter. Homework: bubbling paragraph. Quiz: addEventListener, preventDefault, no onclick=.",
        live=[
            ("0–15", "click listener", "Plant onclick=."),
            ("15–40", "submit + preventDefault", "Page reload plant."),
            ("40–55", "Delegation on ul", "They see one listener."),
            ("55–60", "They build counter", "Circulate."),
        ],
        cut="Custom events. Keep click + preventDefault.",
        add="keydown Enter on a button.",
    )
    GOLD[(C, 11)] = dict(
        kernel="fetch('data.json'); response.ok; await json(); no secrets",
        success="they load local JSON and render a list; they can explain 404 vs throw",
        invariant="fetch talks HTTP; keys never in the frontend; local JSON is enough this week",
        goal="data in, DOM out",
        board="""```
const res = await fetch('data.json');
if (!res.ok) throw new Error(res.status);
const data = await res.json();

GET local file   404 → !ok
```""",
        slides=[],
        hook_say="AI course and capstone will fetch. Today: a local JSON file served from this folder. CORS and file:// will bite — we serve.",
        hook_ask="Does fetch throw on 404? Wait. Want: no — you check res.ok.",
        frame_say="async/await preview (Modern JS owns the deep version). try/catch. No API keys. No CDN.",
        frame_ask="Why serve instead of file://?",
        build=[
            "**Say:** Request, response, body. JSON.parse is what .json() does.",
            "**Board:** ok check. Then map to DOM from Lecture 9.",
            "**Say:** GET is default. POST named, not used without a server.",
        ],
        ask_build="What is in data.json if the file is an array of {name}?",
        they_build="On paper: the three lines: fetch, ok, json.",
        show_say="Load people.json, render ul. Demo 09-fetch.html. Plant file:// fail. Plant ignoring !ok.",
        attempt_say="Render names from JSON. Handle 404 with a visible message. Eight minutes.",
        land_say="Lab: fetch + list + 404 message. Homework: why file:// breaks. Quiz: res.ok, await json, no keys.",
        live=[
            ("0–15", "fetch local", "Plant file://."),
            ("15–40", "ok + json", "Plant missing ok."),
            ("40–55", "Render list", "They connect Lecture 9."),
            ("55–60", "They add 404 text", "Circulate."),
        ],
        cut="Auth headers. Keep local JSON + ok.",
        add="AbortController name.",
    )
    GOLD[(C, 12)] = dict(
        kernel="DOM → CSSOM → layout → paint → composite; transform vs top as a policy",
        success="they can name the five words and say why animating top is more expensive than transform",
        invariant="layout is geometry; paint is pixels; composite is layers — do not invent fps",
        goal="name the pipeline, do not guess speed",
        board="""```
DOM  →  CSSOM  →  render tree  →  layout  →  paint  →  composite

transform / opacity   (composite)
top / width           (layout)

measure if you claim speed
```""",
        slides=[("Optional: a Layers panel screenshot", "photo")],
        hook_say="A janky HUD over WebGL is this lecture. We name the pipeline. We do not invent milliseconds.",
        hook_ask="Does changing transform trigger layout? Wait. Want: usually no.",
        frame_say="Five stages. Reflow vs repaint teaching-level. will-change named as a last resort.",
        frame_ask="Which is cheaper to animate: top or transform?",
        build=[
            "**Say:** Parse HTML → DOM. Parse CSS → CSSOM. Together: render tree.",
            "**Board:** pipeline. Circle layout.",
            "**Say:** DevTools performance is optional; the policy is enough: prefer transform.",
        ],
        ask_build="What is paint?",
        they_build="On paper: the five words in order.",
        show_say="Toggle a class that changes top vs transform. Do not quote fps. Demo 10-transform.html.",
        attempt_say="Write the pipeline from memory. Then one CSS animation using transform. Eight minutes.",
        land_say="Lab: transform animation. Homework: five words. Quiz: order, transform vs top, do not invent fps.",
        live=[
            ("0–15", "Five words", "They copy."),
            ("15–40", "top vs transform", "No invented timings."),
            ("40–55", "Layers name", "Screenshot optional."),
            ("55–60", "They write the list", "Circulate."),
        ],
        cut="Compositor thread details. Keep five words + policy.",
        add="contain: layout name.",
    )
    GOLD[(C, 13)] = dict(
        kernel="label, alt, keyboard path, contrast; LCP as a named metric not a number we invent",
        success="they can tab through the page and every image has alt; they name LCP without a fake score",
        invariant="if it cannot be used with a keyboard, it is not done; do not invent Lighthouse scores",
        goal="usable, then maybe pretty",
        board="""```
alt on img     label on input     one :focus visible

keyboard: Tab through the lab page

LCP  =  largest contentful paint   (name; measure later, do not invent)
```""",
        slides=[],
        hook_say="R3F and XR inherit this. A canvas with no keyboard story fails the experience course. Contrast is not a theme preference.",
        hook_ask="Can you use this page with the keyboard only? Wait. Then try.",
        frame_say="alt empty only if decorative. Focus visible. Reduced motion named. LCP/CLS names — no invented scores.",
        frame_ask="When is alt=\"\" correct?",
        build=[
            "**Say:** Perceivable, operable. Skip the four-letter sermon; show the page.",
            "**Board:** alt, label, focus. LCP name.",
            "**Say:** Images without dimensions cause layout shift — CLS name.",
        ],
        ask_build="What is LCP in one sentence?",
        they_build="Tab the lab page; list what fails.",
        show_say="A pretty button that is not a button (div). Plant. Fix with <button>. No Lighthouse number unless you run it live.",
        attempt_say="Fix alt + labels + focus on last week’s page. Eight minutes.",
        land_say="Lab: keyboard path. Homework: alt audit. Quiz: alt, focus, LCP name. Next: studio.",
        live=[
            ("0–15", "div-as-button", "Plant. Fix button."),
            ("15–40", "alt + label", "Empty alt on content image."),
            ("40–55", "Tab order", "They walk it."),
            ("55–60", "They fix focus", "Circulate."),
        ],
        cut="ARIA soup. Keep alt, label, keyboard.",
        add="prefers-reduced-motion one rule.",
    )
    GOLD[(C, 14)] = dict(
        kernel="portfolio site: semantic page, one breakpoint, one fetch or static list, README how to serve",
        success="a TA can serve the folder and tab through the page without a framework",
        invariant="no React this course; freeze; tests are ‘does it serve and read’",
        goal="studio — not a content lecture",
        kind="studio",
        board="""```
Must: skeleton · flex or grid · one breakpoint · labels
Cuts: drop animation; keep structure + serve
README: python -m http.server
```""",
        slides=[],
        hook_say="This meeting is **studio**. A personal portfolio in HTML/CSS/JS. Not Next.js.",
        hook_ask="If behind, what do you cut first?",
        frame_say="Desk review: landmarks, labels, viewport, README.",
        show_say="Volunteer review against the board.",
        attempt_say="Studio. Serve first.",
        land_say="Report + repo. Next week 12+5. Keyboard path in the demo.",
        live=[
            ("0–10", "Headings", "Photograph."),
            ("10–50", "Desk review", "Serve + tab."),
            ("50–60", "60s rehearsal", "Stop."),
        ],
        cut="New libraries. Keep freeze.",
        add="One 404 page.",
    )
    GOLD[(C, 15)] = dict(
        kernel="12+5; demo the site; point at Network and a label",
        success="they stop at 12 and can show a request and a labeled input",
        invariant="no new features today",
        goal="presentations — not a content lecture",
        kind="presentations",
        board="""```
12 + 5
Show: Network · a label · one breakpoint
No new CSS on stage
```""",
        slides=[("Timer", "not a slide of CSS")],
        hook_say="Presentations. 12+5. Repo. Stop at 12.",
        show_say="None. Present.",
        attempt_say="Present.",
        land_say="This habit — inspect the tree — is Interactive Web and the HUD on WebGL.",
        live=[("0–60", "Talks", "Cut at 12.")],
        cut="Debugging on stage.",
        add="One question on alt.",
    )
