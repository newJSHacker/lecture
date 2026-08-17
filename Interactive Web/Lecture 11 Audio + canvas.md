# Lecture 11 — Audio + canvas

**Course:** Interactive Web Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** Web Audio, analyser  
**Board first:** analyser fft bars

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 10 | Quiz from last week (Week 1: course contract) |
| 25 | Core definition and one picture |
| 45 | Worked examples / derivation |
| 65 | Live pitfalls and policy |
| 75 | Preview lab, then stand up for live coding |

---

## Learning goals

1. AudioContext.
2. AnalyserNode.
3. User gesture to start.
4. fft to bars.
5. Don't autoplay with sound.

---

## 1. Gesture

Browsers block autoplay. Click to start.

## 2. Analyser

frequencyBinCount. Visualizer. Semester 5 audio viz is this grown up.

## 3. Sync

t from audio.currentTime optional.

## Live coding (60 min)

Click-to-start oscillator or file; draw bars.

---

## Lab

1. Mute button.
2. file input extra.

---

## Homework

1. Written: autoplay policy.
2. Code: bars.

---

## Quiz (10 min)

1. why click first (4)
2. AnalyserNode (3)
3. autoplay (3)

## Snippet

```js
const ctxA = new AudioContext();
const an = ctxA.createAnalyser();
```

---

## Common mistakes

- autoplay noise.
- creating AudioContext every frame.

---

## Board drawings

1. Bars.

