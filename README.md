# l33tc0d3

Two separate processes live in this repo. Use the matching skill so the agent doesn't mix modes.

Works in Cursor and in VS Code with GitHub Copilot. Skills live in `.agents/skills/` (both editors). Session rules live in [`AGENTS.md`](AGENTS.md).

| Mode | Folder | Skill | What it's for |
|---|---|---|---|
| **Interview** | [`interview/`](interview/) | `/interview-companion` | Timed mock interviews, no teaching, hiring-signal feedback |
| **Course** | [`course/`](course/) | `/course-companion` | Follow-along study for the LeetCode DS&A course — notes, examples, practice |

Shared across both: [`MISTAKES.md`](MISTAKES.md) (log only when something went wrong) and [`SOLUTIONS.md`](SOLUTIONS.md) (checked reference for each problem).  
Due revisits are flagged automatically at the start of a course or interview session.

---

## Quick start

**Mock interview**
```
/interview-companion
Give me a medium problem.
```

**Course study**
```
/course-companion
I'm on hashing — paste the article below and make notes.
Here's the example problem — I don't understand the approach yet.
```

---

## Layout

```
course/                  # course follow-along
  arrays-and-strings/
    two-pointers/
    sliding-window/
  hashing/
interview/               # interview simulations
  solutions/             # date-stamped interview attempts
MISTAKES.md              # shared error log (+7 day cold revisits)
SOLUTIONS.md             # index of checked correct solutions
AGENTS.md                # always-on session rules (Cursor + VS Code)
.agents/skills/
  interview-companion/
  course-companion/
```

See each folder's README for mode-specific setup and tips.
