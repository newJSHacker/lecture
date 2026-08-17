# 07 — Labs and studio

Labs are where the course happens. If lecture is the map, lab is the terrain. A bad lab is a silent room of stuck people and one instructor who answers the same Git question twelve times.

Studio (project weeks, critiques) is a lab with public criteria and less new content. Week 14 of computational geometry is a model: [[Computational Geometry/Week 14 Project Studio]].

## Before the door opens

- Starter cloned and run on a lab image **and** on a typical student Windows/Mac laptop
- Lab manual: goal, time box, expected screenshot, hints, common mistakes
- Tests or a visual oracle so they know “done”
- A parking lot on the board for issues that are not today’s goal
- TAs briefed on the one misconception of the week

If install is the lab, you did not have a lab. You had an IT session. Put install in a pre-lab video and a help hour.

## Opening the lab (10 minutes, not 30)

1. Today’s success condition (one screenshot or one test)
2. The mistake you expect
3. Where the hint sheet is
4. Pair roles if pairing
5. “Try for 8 minutes before you call me, unless the starter does not run”

Then stop talking. Your talking is their most expensive resource.

## While they work

You circulate. You do not sit at the front answering email.

**The 4-minute desk visit:**

1. “Show me what it does now.”
2. “What did you already try?”
3. Look at the screen, not only their story.
4. Give **one** next action, not a lecture.
5. Leave. If you stay, you will finish it for them.

If three groups have the same bug, stop the room. Teach that bug once. That is diagnosis, not interruption.

## Pairing

Default in early courses: pairs. Default in later courses: optional pairs plus individual kernel tests so one person cannot hide.

**Driver / navigator (25-minute swaps):**

- Driver types
- Navigator holds the checklist and the spec
- Both must be able to explain the last commit

If one student always drives, you will graduate a typist and a spectator. Swap on a timer you can hear.

## Help-seeking that you will accept

Train this script in week 1:

```
I expected: (screenshot or test name)
I got: (screenshot or error)
I tried: (two things)
I think: (one hypothesis)
```

Refuse, kindly, to debug from “it doesn’t work.” You are teaching them to be colleagues.

## Studio rules (critique)

A critique is not a roast and not a compliment circle.

**Before:** criteria on a slide. “We are looking at silhouette, frame time, and whether the README runs.”

**During:**

- Maker speaks for 60–90 seconds: goal, what is broken, what they want advice on
- Room speaks to the **work**, using the criteria
- Instructor models one high-quality comment
- Timebox. A 12-person studio cannot give everyone 15 minutes

**After:** each team writes one change they will make this week. You collect that line. That is the feedback loop.

Forbidden comments: “I just don’t like it.” Required shape: “The shadow acne is visible on the floor; a depth bias or closer near-plane would address criterion 2.”

## When the room is too quiet

Quiet can mean thinking or drowning.

- Ask two people to project their screen (volunteers first)
- A 5-minute “gallery walk”: stand, look at two neighbors, return
- A mid-lab poll: “Who has a triangle / a hull / a compile?” Hands. Then you know.

If nobody has a triangle at minute 40, the starter or the lecture failed. Do not blame “this cohort.”

## When the room is too loud

One conversation at a time during a stop-the-room moment. During work, noise is often healthy. If two tables are socializing off-task, stand near them and ask to see the screenshot.

## End of lab

Last 7 minutes:

- Commit and push (teach this until it is a reflex)
- One sentence in the lab log: “works / broken / blocked on X”
- Preview of homework, which should continue the same object, not a new universe

Do not introduce a new topic in the last 7 minutes.

## Lab manual skeleton

```
Title and week
Time: 2–3 hours
Goal (observable)
Starter: how to run
Task 1 (must)
Task 2 (must)
Task 3 (should)
Stretch (may)
Expected output (image)
Common mistakes
How to submit
How we will grade (link to rubric)
```

## Exercise

Write this week’s lab so that a TA who was not in lecture can run it. If they cannot, students cannot.
