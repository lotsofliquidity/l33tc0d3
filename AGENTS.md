# l33tc0d3

Two modes. Do not mix them.

| Mode | Folder | Skill |
|---|---|---|
| Course study | `course/` | `course-companion` |
| Mock interview | `interview/` | `interview-companion` |

Shared logs: `MISTAKES.md`, `SOLUTIONS.md`.

## Ten-minute stop

When the user says they have been about **10 minutes** with little or no progress — or anything along those lines ("stuck for 10 minutes", "haven't progressed", "still no progress after 10 min") — **stop the problem**. Do not keep hinting or asking Socratic questions.

1. **End the session** on that problem. One short line that the clock ran out.
2. **Give the solution.** Plain-language idea, a short trace on one example, then working code, in the same style as the course article examples for that chapter. **If the course already includes the problem, reuse its copy** in `course/<chapter>/examples/` — do not add a second file for the same problem. Otherwise write `course/<chapter>/examples/<kebab-name>.py` (or `interview/solutions/` in a mock interview). Their `practice/` attempt stays untouched — never overwrite it, and never rewrite an existing article copy. Run the problem's examples. Add or update the row in `SOLUTIONS.md`.
3. **Log `MISTAKES.md`.** Open entries, next `#`, today, problem, chapter, `Went wrong` = couldn't finish in ~10 minutes — needed the solution (the mistake, not the algorithm). `Revisit due` = today + 7 days. Status `OPEN`. If this attempt was already a due revisit, set that row to `RECURRED` and due = today + 7. Confirm in one line, including the revisit date.

Then stop. A new problem starts only if they start one.

## Due revisits

At the **start** of any course or interview session in this repo (or when the user asks what to work on / what's due):

1. Read `MISTAKES.md` → **Open entries**.
2. Today's date is the session date (from user_info if present).
3. Flag every `OPEN` or `RECURRED` row whose **Revisit due** is today or earlier.
4. If any are due, lead with a short list before other work:

```
Due revisits (cold re-solve — no notes/hints first):
- <Problem> (due <date>) — <went wrong, one line>
```

5. Ask: revisit one now, or continue with what they came for?
6. If none due: say nothing about revisits (don't spam "all clear").
7. After a successful cold revisit: set that row to `PASSED` and move it to **Closed entries**. If they fail again: `RECURRED`, new revisit due = today + 7 days; keep/re-log per `MISTAKES.md` rules.
8. Also read **Up next**. On a course session, after the due list (or first, if none are due), name each parked problem and its stub in one line. Ask whether to start one. Do not mention Up next during a mock interview. Delete that row once they start the problem.
