# Interview mode

Realistic LeetCode-style mock interviews via `/interview-companion`.

Solutions go in `solutions/`. Do not put course notes or chapter examples here.

---

## Setup — Turn Off Autocomplete

For realistic practice, turn off helpers while interviewing.

**Cursor:** click **Tab** in the status bar → disable / snooze, or Command Palette → **Disable Cursor Tab**.

**VS Code:** click the Copilot icon in the status bar → **Disable Completions**, or Command Palette → **GitHub Copilot: Disable Completions**.

Workspace settings already tone down IntelliSense (see `.vscode/settings.json`). Turn completions back on when you switch to course study.

---

## Start a session

1. Open Agent chat (Cursor) or Copilot Chat (VS Code)
2. `/interview-companion`
3. Kick off:

> "Give me a medium problem."  
> "Interview me on Two Sum."  
> "Hard problem, Hardcore mode."

---

## Flow

| Phase | What happens |
|---|---|
| **1. Problem** | Problem, constraints, examples |
| **2. Clarifications** | You ask; interviewer answers like a real interviewer |
| **3. Approach** | Brute force → optimal. No coding yet |
| **4. Coding** | Stub created in `solutions/`; you write the solution |
| **5. Review** | Say *done* / *check my code* / *question complete* |
| **6. Analysis** | Time / space / edge cases |
| **7. Feedback** | Hiring signal + study notes; may append to `../MISTAKES.md` |

Hints are leading questions only (Easy 3 / Medium 2 / Hard 1 / Hardcore 0).

---

## Tips

- Think out loud. Don't ask for hints until you're stuck.
- Treat it like the real thing — no skipping phases.
- Course learning belongs under `../course/` with `/course-companion`.
