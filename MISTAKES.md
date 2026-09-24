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

Note what is **not** in there: the correct solution. If you need the solution you
re-solve the problem — you don't read it back to yourself.

---

## Open entries

| # | Date logged | Problem | Chapter | Went wrong | Revisit due | Status |
|---|---|---|---|---|---|---|
| 2 | 2026-09-17 | Maximum Average Subarray I | Sliding window | Fixed-window attempt: `nums[k]` instead of `nums[i]` in build; slide used stale `i` not `right`; compared sum to average. Cold revisit 2026-09-24: looked up solution — pattern forgotten. | 2026-10-01 | RECURRED |
| 3 | 2026-09-18 | Max Consecutive Ones III | Sliding window | Window logic OK, but compared to `'0'` (string) on an int array — `curr` never counted zeros, so answer was full length. | 2026-09-25 | OPEN |
| 4 | 2026-09-20 | K Radius Subarray Averages | Prefix sum | Couldn't finish — need window i-k..i+k (size 2k+1), -1 near edges; range sum via prefix (or slide fixed window), not re-sum each center. | 2026-09-27 | OPEN |
| 5 | 2026-09-20 | Reverse Words in a String III | Two pointers / strings | Misread: reversed entire string instead of each word while keeping word order. | 2026-09-27 | OPEN |
| 6 | 2026-09-20 | Is Subsequence | Two pointers | Right idea; `j[t]` typo and only advancing `j` on mismatch — must use `t[j]` and always scan `t`. | 2026-09-27 | OPEN |
| 7 | 2026-09-22 | Check if the Sentence Is Pangram | Hashing | Knew set was the right tool; had to look up how to create/add (`set()`, `.add`). | 2026-09-29 | OPEN |
| 8 | 2026-09-22 | Missing Number | Hashing | Sought neighbor gaps (`num±1`) instead of the missing value in `[0, n]`; breaks when `0` is present (returns `-1`). | 2026-09-29 | OPEN |
| 9 | 2026-09-24 | Counting Elements | Hashing | Reused Missing Number loop; indexed a set; returned early instead of counting each `x` where `x+1` exists. | 2026-10-01 | OPEN |
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

## Closed entries

Move a row here once it's `PASSED`. Keep them — the tally is your progress measure.

| # | Problem | Chapter | First logged | Closed | Notes |
|---|---|---|---|---|---|
| 1 | Squares of a Sorted Array | Two pointers | 2026-09-16 | 2026-09-20 | Interview re-solve; backward fill + `<=` |

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
