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
- you couldn't finish / needed the solution walked through
- you failed a **+7-day cold revisit** — set a new due date; don't delete the lesson

**Do not add a row when** you solved it clean, in time, and could talk through it.
63 entries is a diary. ~15–25 entries is a study tool.

**Two moves (keep it simple):**
1. **Soon** — if you couldn't finish, practice that pattern again within a few days (notes OK). Don't wait a week to touch it.
2. **Cold due (+7 days)** — re-solve with no notes/hints. Pass → `PASSED` + Closed. Fail → `RECURRED`, new due = today + 7.

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
Revisit due  : 2026-09-23
Status       : OPEN
```

```
Date logged  : 2026-09-16
Problem      : Max Consecutive Ones III
Chapter      : Arrays and strings
Went wrong   : Couldn't state the sliding-window invariant out loud — knew the
               mechanic but not why shrinking on failure is safe.
Revisit due  : 2026-09-23
Status       : OPEN
```

Note what is **not** in there: the correct solution. Checked answers are indexed in
[`SOLUTIONS.md`](SOLUTIONS.md). On a cold revisit, re-solve first — don't open that file until the attempt is over.

---

## Open entries

| # | Date logged | Problem | Chapter | Went wrong | Revisit due | Status |
|---|---|---|---|---|---|---|
| 2 | 2026-09-17 | Maximum Average Subarray I | Sliding window | Cold revisit 2026-10-03: couldn't identify the fixed-size sliding-window approach and needed the solution. | 2026-10-10 | RECURRED |
| 4 | 2026-09-20 | K Radius Subarray Averages | Prefix sum | Couldn't finish the centered window. Cold 2026-09-28: built the prefix, then couldn't say which slice each center averages. | 2026-10-05 | RECURRED |
| 5 | 2026-09-20 | Reverse Words in a String III | Two pointers / strings | Misread: reversed entire string instead of each word. Cold 2026-09-29: word-bounds loop was the right idea, but couldn't finish — helper used full-string indexes on a word-sized list. | 2026-10-06 | RECURRED |
| 6 | 2026-09-20 | Is Subsequence | Two pointers | Cold 2026-09-29: pointer rules held, then the loop stopped one index early (`len - 1`). Another clean pass requested. | 2026-10-06 | OPEN |
| 8 | 2026-09-22 | Missing Number | Hashing | Cold revisit 2026-10-03: searched for a missing neighbor after values; returns `n+1` when `0` is missing. | 2026-10-10 | RECURRED |
| 9 | 2026-09-24 | Counting Elements | Hashing | Cold revisit 2026-10-03: indexed a set (`element_set[i]`), which raised `TypeError`; still needs a clean pass. | 2026-10-10 | RECURRED |
| 10 | 2026-09-28 | Find Players With Zero or One Losses | Hashing | Needed a walkthrough — counted the match/win instead of losses, and did not keep 0 as a real count. | 2026-10-05 | OPEN |
| 11 | 2026-09-29 | Largest Unique Number | Hashing | Counted frequencies after a descending sort, then returned -1 on the first repeated number instead of scanning for the next count of 1. | 2026-10-06 | OPEN |
| 12 | 2026-09-29 | Maximum Number of Balloons | Hashing | Took the min raw count of balloon letters that appeared, so a missing letter was ignored and `l`/`o` were not divided by 2. | 2026-10-06 | OPEN |
| 13 | 2026-09-30 | Contiguous Array | Hashing | Couldn't finish. Mapped an index to a contribution instead of a running score to the first index where that score appeared. | 2026-10-07 | OPEN |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

**Status values:** `OPEN` · `PASSED` (re-solved clean at the cold revisit) · `RECURRED` (failed the revisit — set a new `Revisit due` 7 days out)

---

## Up next

Parked before an attempt. Not a mistake. Removed when you start the stub.

| Problem | Chapter | Stub | Parked |
|---|---|---|---|

---

## Closed entries

Move a row here once it's `PASSED`. Keep them — the tally is your progress measure.

| # | Problem | Chapter | First logged | Closed | Notes |
|---|---|---|---|---|---|
| 1 | Squares of a Sorted Array | Two pointers | 2026-09-16 | 2026-09-20 | Interview re-solve; backward fill + `<=` |
| 3 | Max Consecutive Ones III | Sliding window | 2026-09-18 | 2026-10-03 | Cold revisit passed; maintain a window with at most `k` zeros |
| 7 | Check if the Sentence Is Pangram | Hashing | 2026-09-22 | 2026-10-03 | Cold revisit passed; track distinct letters with a set |

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
