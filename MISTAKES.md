# MISTAKES.md

The DS&A error log for the 9-week plan (14 Sep – 15 Nov 2026).
Created in **W01** — first job of the plan, alongside the blind diagnostic.

---

## How to use this file

**Add an entry only when something went wrong.** A clean solve writes nothing.

Log a row when any of these is true:

- you used a hint, the editorial, or looked up the pattern
- you passed, but only after a wrong first approach
- it took far longer than it should have (>2× your estimate)
- you couldn't explain **why** it works after it passed
- you failed a **+14-day revisit** — re-log it with a new date; don't edit the old row

**Do not add a row when** you solved it clean, in time, and could talk through it.
63 entries is a diary. ~15–25 entries is a study tool.

**The date is the mechanism, not admin.** An entry is not closed until you have
**re-solved it successfully 14 days later**. That is what keeps this file live across
all nine weeks, and it is what feeds the W09 action *"Re-solve your 6 worst
`MISTAKES.md` entries"* (2 h).

**In the 🧮 block (07:00–08:00, every day):** solve → if it went wrong, one line here
→ close the file. Ten seconds. Write the *reason*, not an essay and not the wrong answer.

**Cursor will remind you.** At the start of `/course-companion` or `/interview-companion`
sessions, due revisits (Revisit due ≤ today) are listed so you can cold re-solve them
before new work. You can also ask: "What's due to revisit?"

**This file outlives the 9 weeks.** It carries into the optional tail (Part 5 of
`APP-ENTRY.md`) and is what you re-read before an interview.

---

## What a good entry looks like

```
Date logged  : 2026-09-16
Problem      : K Radius Subarray Averages
Chapter      : Arrays and strings
Went wrong   : Built a fresh window sum each step instead of reusing it — O(n·k).
Revisit due  : 2026-09-30
Status       : OPEN
```

```
Date logged  : 2026-09-16
Problem      : Max Consecutive Ones III
Chapter      : Arrays and strings
Went wrong   : Couldn't state the sliding-window invariant out loud — knew the
               mechanic but not why shrinking on failure is safe.
Revisit due  : 2026-09-30
Status       : OPEN
```

Note what is **not** in there: the correct solution. If you need the solution you
re-solve the problem — you don't read it back to yourself.

---

## Open entries

| # | Date logged | Problem | Chapter | Went wrong | Revisit due | Status |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

**Status values:** `OPEN` · `PASSED` (re-solved clean at the revisit) · `RECURRED` (failed the revisit — set a new `Revisit due` 14 days out)

---

## Closed entries

Move a row here once it's `PASSED`. Keep them — the tally is your progress measure.

| # | Problem | Chapter | First logged | Closed | Notes |
|---|---|---|---|---|---|
| | | | | | |

---

## W09 — the re-solve pass (2 h, week of 9 Nov)

Pick your **6 worst** entries: anything still `OPEN` or `RECURRED`, preferring
problems from the high-frequency chapters (arrays/strings → hashing → two pointers
& sliding window → trees → graphs → binary search → DP 1-D). Re-solve them cold.

| # | Problem | Chapter | Outcome |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |

---

## Blind diagnostic — W01, day 1

Three problems, cold: no notes, no hints, no lookups, no timer pressure.
Log every miss above. This is a baseline, not a test — a bad result is a *useful*
result, and this is where the file gets its first real entries.

| # | Problem | Outcome | Logged above? |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

Re-run the same three in **W09** and compare. That comparison is the honest
progress measure for the whole software track.

| # | Problem | W01 outcome | W09 outcome |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
