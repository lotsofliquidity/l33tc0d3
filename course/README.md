# Course mode

Follow-along for the LeetCode DS&A course via `/course-companion`.

**Your loop:** paste the article → get solid notes → paste the example → understand it (ask when stuck) → practice → log misses in `MISTAKES.md`.

Not a mock interview — use `/interview-companion` for that.

---

## Start a session

1. Open Agent chat
2. `/course-companion`
3. Paste the course article and/or example, and say which chapter you're on

Examples:

> "Hashing chapter — here's the article: … Make notes."  
> "Here's the example problem: … I don't get why we shrink the window."  
> "Quiz me on the invariant from notes.md"

---

## What you get

| You paste / ask | Companion does |
|---|---|
| Course article | Distills into `notes.md` (when to use, invariant, template, pitfalls, tiny trace) |
| Example problem | Saves under `examples/`, explains the fit to the pattern, walks a tiny input |
| "I don't get it" | Smaller analogy / step trace first, then a plain explanation; updates notes if useful |

---

## Layout

```
arrays-and-strings/
  two-pointers/
  sliding-window/
hashing/
```

Per chapter:

- `notes.md` — your high-signal study notes (not a full article dump)
- `examples/` — worked course examples
- `practice/` — your attempts (`YYYY-MM-DD-ProblemName.py`)

Add new chapter folders as you reach them (trees, graphs, binary-search, dp, …).

---

## Mistakes

Bad practice solves get a row in [`../MISTAKES.md`](../MISTAKES.md). Clean solves write nothing. Revisit open entries after 14 days.
