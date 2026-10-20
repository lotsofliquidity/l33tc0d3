# MISTAKES.md

The DS&A error log for the 9-week plan (14 Sep – 15 Nov 2026).
Created in **W01** — first job of the plan, alongside the blind diagnostic.

---

## How to use this file

**Add an entry only when something went wrong.** A clean solve writes nothing. The
one exception is the **Cold run log** — that's a measurement record, not an error
log, so *every* cold check writes a line there, clean pass included.

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
1. **Soon** — if you couldn't finish, practice that pattern again within a few days (notes OK, ~15 min). Don't wait a week to touch it. This is the move that retires entries; the cold check only measures.
2. **Cold due (+7 days)** — re-solve with no notes/hints. Pass → `PASSED` + Closed. Fail → `RECURRED`, new due = today + 7. Either way, one line in the **Cold run log**.

**Cold checks are capped, and weekend-friendly.** *(decided 2026-10-12)*

- **Cap: 20 minutes.** The ten-minute stop applies. Running out the clock on one problem is a fail, not a study session — stop, log `RECURRED`, and take the pattern through the *soon* move instead.
- **Due Mon–Thu** → run it that day. **Due Fri–Sun** → roll it to that weekend.
- The interval never shortens below +7. Forcing every check onto a Saturday would mean gaps of 3–11 days, and a 3-day gap isn't cold.

**Notes or the solution — when.** The rule is one sentence: **cold means nothing
open.** What changes is what you may open *after* you've genuinely tried.

| Situation | Chapter notes | `SOLUTIONS.md` / `examples/` |
|---|---|---|
| Cold check (a due revisit) | closed | closed — 20-min cap, then stop and take the *soon* move |
| *Soon* move (same pattern, within a few days, ~15 min) | open | open — but only *after* an attempt, and then re-derive it with everything closed |
| New problem, first attempt | open before you start; shut once the stub is in front of you | closed until the ten-minute stop |
| Stuck ~10 min, no progress | — | handed to you, notes and all |

**In the 🧮 block (07:00–08:00, every day):** solve → if it went wrong, one line here
→ close the file. Ten seconds. Write the *reason*, not an essay and not the wrong answer.

**Cursor will remind you.** At the start of `/course-companion` or `/interview-companion`
sessions you get one line on the **Cold run log** — last cold run, the tally, the next
due date — and then any due revisits (Revisit due ≤ today) are listed so you can cold
re-solve them before new work. You can also ask: "What's due to revisit?", "What did I
run last?", or "Am I allowed notes for this one?"

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
| 4 | 2026-09-20 | K Radius Subarray Averages | Prefix sum | Couldn't finish the centered window. Cold 2026-09-28: built the prefix, then couldn't say which slice each center averages. Cold 2026-10-08: had the valid centers (`range(k, n-k)`) right, but appended to an already-full `[-1] * n` list, divided each element by `k` instead of the window sum by `2k+1`, and added a `k < nums` guard that crashed. | 2026-10-15 | RECURRED |
| 9 | 2026-09-24 | Counting Elements | Hashing | Cold revisit 2026-10-03: indexed a set (`element_set[i]`), which raised `TypeError`; still needs a clean pass. Cold 2026-10-17: built the set *inside* the loop and tested `num in seen`, which the element had just been added to — always true, so the answer is just `len(arr)`; also tested the element itself rather than `num + 1`. Stopped the clock and took the solution. | 2026-10-24 | RECURRED |
| 10 | 2026-09-28 | Find Players With Zero or One Losses | Hashing | Needed a walkthrough — counted the match/win instead of losses, and did not keep 0 as a real count. Cold 2026-10-09: loss counts were right, but the second loop indexed `matches` by position and read `losers[winner]`/`losers[i]` as if a player were a match — kept hitting `TypeError`; needed the solution. Cold 2026-10-17: the second loop and both sorts finally came out right, but the first loop still counted *every* appearance (`count[team1] += 1`), so the zero-loss list was structurally unreachable and exactly-one-loss swallowed winners too — needed the one-line "the map answers losses only" hint. Passed both examples + a 3000-case fuzz after the hint, but ~20 min and hint-assisted, so not a cold solve. Same day, soon move: closed-book re-derive came out clean on the first write (both examples + a 3000-case fuzz, structurally identical to the course copy) — the pattern is close; 2026-10-24 is the measurement. | 2026-10-24 | RECURRED |
| 13 | 2026-09-30 | Contiguous Array | Hashing | Couldn't finish. Mapped an index to a contribution instead of a running score to the first index where that score appeared. Cold revisit 2026-10-07: still couldn't derive the `0 → -1` balance idea — read the solution instead of rebuilding it. | 2026-10-14 | RECURRED |
| 14 | 2026-10-07 | Subarray Sum Equals K | Hashing | Needed the solution after several hints. Never accumulated into the running sum (`curr` stayed 0), and stored the hunted value (`curr - k`) in the map instead of the real running sum — conflating "what I search for" with "what I record". | 2026-10-14 | OPEN |
| 15 | 2026-10-07 | Remove Duplicates from Sorted List | Linked lists | Needed multiple hints. First attempt used a set and never advanced the walker (infinite loop); then overwrote `head` and returned the walked-to-end pointer instead of the front. Also missed the empty-list guard. Cold 2026-10-14: wiring came out right and passed all four cases (1,1,2 / 1,1,2,3,3 / [] / 7,7,7), but peeked at the solution for the saved-front reference and the advance-only-on-mismatch step — not a cold solve. | 2026-10-21 | RECURRED |
| 16 | 2026-10-08 | Reverse Linked List | Linked lists | Couldn't finish in ~10 minutes — needed the solution. Had `prev`, `curr` and `next_node = curr.next` in place, then stalled on the flip and the pointer advance. Cold revisit 2026-10-15: same wall. Declared `prev`/`curr`, then left the body empty and wrote the *pair-swap* guard (`while head and head.next`) for a plain reversal — reached for the neighbouring pattern's skeleton instead of this one's. After the solution, three explanation passes still hadn't produced a verbal model of why the four lines are ordered that way. 2026-10-16: re-wrote the four lines correctly, but still couldn't say why the order is load-bearing — re-explained with the old-chain/new-chain model. | 2026-10-22 | RECURRED |
| 17 | 2026-10-13 | Swap Nodes in Pairs | Linked lists | Couldn't derive the pair-swap wiring across two sessions (10-09, today) even with hints — needed the solution. Set `B.next = A` but left `A.next -> B`, a two-node cycle, so `C` was unreachable; no `return` statement; never reached the guard, the loop, or the dummy boundary. Rebuild 2026-10-15: the wiring is right now and all four examples plus `[1,2,3]` pass (fuzzed 2020 cases) — but not a cold solve: needed the `dummy = head` → `head.next` correction and a reminder to actually `return`. | 2026-10-22 | RECURRED |
| 18 | 2026-10-20 | Reverse Linked List II | Linked lists | Couldn't finish — needed the solution. Compared `left`/`right` to node values, then only advanced the walker inside the range, so the loop never ended. | 2026-10-27 | OPEN |
| 19 | 2026-10-21 | Simplify Path | Stacks | Couldn't finish — needed the solution. Walked character-by-character and only collapsed `//`; never treated path segments as stack entries, so `.` / `..` / `...` were unreachable. | 2026-10-28 | OPEN |
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

## Cold run log

Every cold check gets a line, clean pass included. The Open/Closed tables hold
**status**; this holds the **dated history**, so you can see what you actually ran
on a given day without reading prose.

`PASS` = clean cold solve, no notes/hints · `HINT` = got there only after nudges or
a peek (so not a clean solve) · `FAIL` = couldn't finish, or needed the solution.
Cold checks only — non-cold rebuilds stay in the row text above.

Tally: **7 clean · 4 hint-assisted · 7 failed** (18 runs).

| Date | # | Problem | Run | Note |
|---|---|---|---|---|
| 2026-09-20 | 1 | Squares of a Sorted Array | PASS | interview re-solve; backward fill + `<=` |
| 2026-09-28 | 4 | K Radius Subarray Averages | FAIL | built the prefix, then couldn't say which slice each center averages |
| 2026-10-03 | 3 | Max Consecutive Ones III | PASS | held a window with at most `k` zeros |
| 2026-10-03 | 7 | Check if the Sentence Is Pangram | PASS | distinct letters in a set |
| 2026-10-03 | 9 | Counting Elements | FAIL | indexed a set (`element_set[i]`) → `TypeError` |
| 2026-10-06 | 6 | Is Subsequence | PASS | advanced the match pointer only on equality |
| 2026-10-07 | 13 | Contiguous Array | FAIL | never derived the `0 → -1` balance; read the solution instead of rebuilding it |
| 2026-10-08 | 4 | K Radius Subarray Averages | FAIL | centers right, but divided each element by `k` instead of the window sum by `2k+1` |
| 2026-10-08 | 5 | Reverse Words in a String III | HINT | one nudge: the final-word reversal sat inside the `for` body (row closed `PASSED` — nudge only) |
| 2026-10-09 | 10 | Find Players With Zero or One Losses | FAIL | indexed `matches` by position → `TypeError`; needed the solution |
| 2026-10-09 | 11 | Largest Unique Number | HINT | two nudges: `best = (best, num)` built a tuple, and the loop shadowed `count` (row closed `PASSED` — nudges only) |
| 2026-10-12 | 12 | Maximum Number of Balloons | PASS | ~15 min; halved `l`/`o`, absent letters read 0 |
| 2026-10-14 | 2 | Maximum Average Subarray I | PASS | reused the window sum; both examples, all-negative, `k == n`, `k == 1` |
| 2026-10-14 | 8 | Missing Number | PASS | `0..n` scan against a set; 4 cases + a 2000-case fuzz |
| 2026-10-14 | 15 | Remove Duplicates from Sorted List | HINT | passed all four cases, but peeked at the solution for the saved-front reference and the advance-only-on-mismatch step |
| 2026-10-15 | 16 | Reverse Linked List | FAIL | same wall — declared `prev`/`curr`, left the body empty, wrote the *pair-swap* guard |
| 2026-10-17 | 10 | Find Players With Zero or One Losses | HINT | ~20 min; needed the "the map answers losses only" hint. Both examples + a 3000-case fuzz pass after it |
| 2026-10-17 | 9 | Counting Elements | FAIL | built the set inside the loop and tested `num in seen` (always true) instead of `num + 1 in seen`; stopped the clock |

---

## Up next

Parked before an attempt. Not a mistake. Removed when you start the stub.

| Problem | Chapter | Stub | Parked |
|---|---|---|---|
| Two Sum | Hashing | [course/hashing/practice/2026-10-09-TwoSum.py](course/hashing/practice/2026-10-09-TwoSum.py) | 2026-10-09 |

---

## Closed entries

Move a row here once it's `PASSED`. Keep them — the tally is your progress measure.

| # | Problem | Chapter | First logged | Closed | Notes |
|---|---|---|---|---|---|
| 1 | Squares of a Sorted Array | Two pointers | 2026-09-16 | 2026-09-20 | Interview re-solve; backward fill + `<=` |
| 2 | Maximum Average Subarray I | Sliding window | 2026-09-17 | 2026-10-14 | Cold revisit passed (both examples + all-negative, `k == n`, `k == 1`). Reuse the window sum: subtract the outgoing, add the incoming, track the max sum, divide by `k` once at the end. Seeded `best` from the first window instead of `0`, so all-negative input is safe. |
| 3 | Max Consecutive Ones III | Sliding window | 2026-09-18 | 2026-10-03 | Cold revisit passed; maintain a window with at most `k` zeros |
| 5 | Reverse Words in a String III | Two pointers / strings | 2026-09-20 | 2026-10-08 | Cold revisit passed; word-bounds loop + in-place helper on `list(s)`. Needed one nudge: the final-word reversal sat inside the `for` body, so it ran per character |
| 6 | Is Subsequence | Two pointers | 2026-09-20 | 2026-10-06 | Cold revisit passed; advance the match pointer only when `s[i] == t[j]` |
| 7 | Check if the Sentence Is Pangram | Hashing | 2026-09-22 | 2026-10-03 | Cold revisit passed; track distinct letters with a set |
| 8 | Missing Number | Hashing | 2026-09-22 | 2026-10-14 | Cold revisit passed (4 cases + a 2000-case fuzz). Scan `0..n` against a set of `nums` — the `range(len(nums) + 1)` upper bound is what covers both a missing `0` and a missing `n`. Took some deliberation picking between a set and a dict; the set is the right call because only existence is needed. |
| 11 | Largest Unique Number | Hashing | 2026-09-29 | 2026-10-09 | Cold revisit passed; count frequencies, then scan all values keeping the largest with count 1. Needed two nudges: `best = (best, num)` built a tuple instead of a running max, and the loop variable shadowed the dict name `count`. |
| 12 | Maximum Number of Balloons | Hashing | 2026-09-29 | 2026-10-12 | Cold revisit passed (~15 min): halved `l`/`o` this time and let the absent letters read 0 off the `defaultdict`. Needed one correction first — a `freq["s"]` term dragged every case to 0; `balloon` has no `s`. Left over: a no-op `text.lower()`. |

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
