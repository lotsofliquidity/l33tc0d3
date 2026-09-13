# Interview Companion

A realistic LeetCode-style technical interview simulator for [Cursor](https://cursor.com/).  
There is no application code in this workspace — the experience lives in Agent chat via the **interview-companion** skill.

---

## Prerequisites

- [Cursor](https://cursor.com/)

---

## Setup — Turn Off Autocomplete

To keep practice realistic, this workspace disables IntelliSense and Cursor completions (see `.vscode/settings.json`).

**Also turn off Cursor Tab** for this session (workspace settings can't always kill Tab alone):

1. Click the **Tab** indicator in the bottom-right status bar, or
2. Command Palette → **Disable Cursor Tab**

Re-enable Tab when you're done practicing.

---

## How to Start a Session

### 1. Open Agent chat
Open a new Agent chat in this workspace.

### 2. Start the Interviewer
Either:

- Type `/interview-companion`, or
- Just ask to start — the skill should pick up interview requests automatically

### 3. Kick Off the Interview

**Let the interviewer pick a problem:**
> "Give me a medium problem."  
> "Pick something hard."

**Choose your own problem:**
> "Interview me on Two Sum."  
> "Let's do LeetCode 15 — 3Sum."

**Set a difficulty + Hardcore mode (no hints at all):**
> "Hard problem, Hardcore mode."

---

## Interview Flow

Each session follows a structured format that mirrors a real technical interview:

| Phase | What happens |
|---|---|
| **1. Problem** | The interviewer presents the problem, constraints, and examples |
| **2. Clarifications** | You ask questions; the interviewer answers like a real interviewer would |
| **3. Approach** | You explain your thinking — brute force first, then optimal. No coding yet. |
| **4. Coding** | A Python stub is created in `solutions/`. You write your solution there. |
| **5. Review** | Say *"done"*, *"check my code"*, or *"question complete"* when finished |
| **6. Analysis** | Discuss time complexity, space complexity, and edge cases |
| **7. Feedback** | Structured feedback including hiring signal, areas to improve, and study recommendations |

You cannot skip phases — the interviewer will redirect you if you try.

---

## Feedback You'll Receive

At the end of each session the interviewer gives:

- **Hiring signal** — Strong Hire / Hire / No Hire / Strong No Hire
- **What went well** — specific things you did right
- **Areas to improve** — concrete gaps with context on why they matter
- **Code notes** — observations on your Python solution (correctness, style, edge case handling)
- **To improve on this type of problem** — targeted study recommendations based on the specific problem and pattern you just practiced
- **To become more hireable overall** — session-based feedback on interview skills: communication, handling being stuck, complexity reasoning, and more

If the session went badly (hints used, wrong first approach, couldn't explain why, incorrect solution, or No Hire), the interviewer also appends a row to [`MISTAKES.md`](MISTAKES.md). Clean Hire / Strong Hire sessions leave that file alone.

---

## Hint System

Hints are phrased as leading questions, never direct answers. They're only given when you explicitly ask or after repeated wrong attempts.

| Difficulty | Hints available |
|---|---|
| Easy | 3 |
| Medium | 2 |
| Hard | 1 |
| Hardcore | 0 — full simulation, no hints |

---

## Solution Files

Your solutions are saved in `solutions/`, date-stamped and named after the problem:

```
solutions/
  2026-09-14-TwoSum.py
  2026-09-14-ContainsDuplicate.py
  2026-09-22-LowestCommonAncestorOfABinarySearchTree.py
```

---

## Tips

- **Think out loud.** The interviewer responds to partial thinking — narrating your reasoning is part of what's being evaluated.
- **Don't ask for hints directly** unless you're genuinely stuck. Work through it first.
- **Treat every session like the real thing.** The interviewer won't let you skip steps or coast through vague answers.
- **Review your feedback carefully.** The study recommendations at the end are tailored to what you just struggled with — follow them before your next session.
