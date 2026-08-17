# 06 — Live coding pedagogy

Live coding is the signature move of this program. Students learn by watching an expert think, stall, read an error, and recover. A polished video of a finished file teaches the result. Live coding teaches the work.

If you only ever paste finished solutions, you are hiding the job.

## Why it works

- It makes process visible: where to look first, what to ignore.
- It sets a humane pace. You cannot type as fast as a recording.
- It licenses mistakes. If you can be wrong in public, they can be wrong in lab.
- It creates a shared object. After class, “the cube from minute 40” is a real cube.

## Rules

1. **Start from the same starter they have.** No secret sauce in a private folder.
2. **Zoom the editor.** 140–160%. Theme with contrast. Ligatures optional; wrapping not optional.
3. **One file on screen** unless you are teaching imports.
4. **Narrate decisions, not keystrokes.** “I need a vec3 in world space” is better than “now I type u_model.”
5. **Make a mistake on purpose** if the session is going too clean. Then show the checklist.
6. **Stop and let them type** after 8–12 minutes. Live coding is not a movie.
7. **Never live-install.** The environment is ready or you abort to the backup.

## A 60-minute live-coding arc

This matches the “Live Coding / Demo” block in [[02 Curriculum Design Advice]].

| Minutes | Move |
| ---: | --- |
| 0–5 | Recap the goal. Open the starter. Run it so they see the “before.” |
| 5–20 | Implement the first slice. Talk. Type slower than you want. |
| 20–25 | They reproduce that slice, or predict the next picture. |
| 25–40 | Second slice. Include one error (compile or visual). |
| 40–50 | They try the error-fix checklist on a planted bug in the starter. |
| 50–60 | Clean up, extract a function, write the one comment that matters, commit. |

Ending on a commit teaches that work is not done when the picture appears.

## What to narrate

Always:

- What space a vector is in
- What you are about to compile or refresh
- How you know it worked (screenshot, test, pixel color)
- The first place you will look if it is black / NaN / inverted

Sometimes:

- Why you rejected an API
- Why you are not optimizing yet
- Why this is a predicate, not a construction

Never:

- A two-minute rant about a framework
- Silent scrolling through files
- “I’ll just copy this from my other repo”

## The black-screen checklist (teach it, post it)

When the scene is black or blank:

1. Is the canvas in the DOM and sized?
2. Are we clearing to a color you would notice (not black-on-black)?
3. Did the shader compile? Read the info log.
4. Is the camera looking at the object?
5. Is the object in front of the near plane?
6. Winding / culling?
7. Depth test / write?
8. Are attributes bound to the right locations?
9. Is the texture loaded yet (async)?
10. Is the color space or alpha making it “invisible”?

For computational geometry, the sibling list is: sign convention, EPS, input order, duplicate points, and “did you sort a copy?”

Print this. Students should run it before they raise a hand.

## Failure is part of the lesson

When the unexpected happens:

1. Do not apologize for 90 seconds. Breathe.
2. Say “this is the real job.”
3. Use the checklist out loud.
4. If 5 minutes pass, switch to the backup recording or a known-good commit.
5. After class, write the incident into next year’s notes.

Students remember how you treat a broken demo more than they remember a perfect one.

## Pair live coding

Two instructors (or instructor + TA) can work as driver/navigator. The navigator faces the room and translates. This is excellent and must be rehearsed once.

Do not let the navigator become a second monologue.

## Speed

You are too fast. Almost every expert is.

- Type the identifier, then pause.
- After an error, wait so they can read it.
- Do not use 15 IDE shortcuts they do not have.

If advanced students are bored, give them the challenge valve on paper. Do not speed up past the middle of the room.

## Accessibility

- Speak what you type if anyone is using a screen reader or is far away.
- Do not rely on red squiggles alone.
- Provide the final file after class, plus a short “decisions” note, not only a dump of keystrokes.

See [[Teaching/10 Inclusive Teaching and Accessibility]].

## Anti-patterns

- Live-coding a 400-line engine on day one
- Switching windows every 10 seconds
- Dark gray text on black, 12px
- “I’ll clean this up later” and never extracting the function
- Finishing the feature after they have packed up, so only the recording sees the point

## Exercise

Record yourself live-coding for 12 minutes. Watch at 1.5×. Note every unexplained jump. Those jumps are where the class gets lost.
