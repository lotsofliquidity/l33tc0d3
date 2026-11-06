# Interview feedback

_Signals so far: Strong Hire 0 · Hire 2 · No Hire 2 · Strong No Hire 0 — 4 sessions_

## 2026-11-05 · Valid Parentheses · Easy · Hire

**What went well**
- You landed on the right structure: a stack that pushes openers and matches them on closers, with an early false when a closer arrives on an empty stack.
- The empty-stack guard and the final "return not stack" check are both correct and show you understood the two failure modes.
- You traced the bad case "([)]" correctly and nailed the O(n) time and space reasoning.
**Areas to improve**
- You lost confidence partway through and said you didn't think you could do it, when you were actually very close. Ride out that moment a bit longer before declaring defeat.
- Small language details cost you time: the lowercase false, and the mismatched variable names (s vs string, c vs parenthese). These are easy to catch with a careful read before saying you're done.
**Code notes**
- The logic is correct. The only real bug was lowercase false, which you fixed.
- Variable naming drifted a couple of times; keep the loop variable and the parameter names consistent.
- Your comments and the leftover "check for opening or closing" note could be cleaned up, but they don't affect correctness.
**To improve on this type of problem**
- Practice recognizing the "most recent unmatched thing" signal that points to a stack — it shows up in matching, nesting, and undo-style problems.
- Get comfortable with the push-the-complement trick so the pop comparison is a plain equality check.
**To become more hireable overall**
- Build confidence narrating your plan before coding so you don't stall mid-implementation.
- Do a quick self-review pass for syntax and naming before declaring done — it reads as polish to an interviewer.
Used hints and lost confidence mid-solve, needing prompting to complete the matching logic.

## 2026-11-05 · Valid Palindrome · Easy · No Hire

**What went well**
- You identified the right overall shape early: two pointers converging from the ends, skipping non-alphanumeric characters.
- You correctly used isalnum and lower to normalize characters.
- You responded well to the bounds issue once it was pointed out, and you kept iterating.
**Areas to improve**
- You never traced the code on a concrete input. Almost every bug here — the out-of-range index, the bound being off by one, the crossing case — would have shown up immediately if you'd walked through a tiny example like a comma followed by a space.
- You regressed twice, reverting to earlier broken versions instead of building forward. That suggests you weren't tracking what state the code was in.
- The crossing case is the core edge case of this problem, and when you got stuck there you said "I don't know" rather than reasoning about what it means for the pointers to meet.
**Code notes**
- The final version is missing the post-skip check: after both skip loops, if left is greater than or equal to right, return true.
- The bounds left <= len(s) - 1 and right >= 0 are correct but awkward; left < len(s) and right >= 0 read more naturally.
- The syntax ! for not is not valid Python; it's not.
**To improve on this type of problem**
- Always trace a small example by hand before declaring done, especially one with punctuation only or punctuation at the edges.
- When two pointers skip, the crossing condition is almost always the edge case you must handle. Ask yourself "what if one pointer runs past the other?"
- Keep a mental model of your current code state so you don't revert to old versions.
**To become more hireable overall**
- Practice narrating your trace out loud on tiny inputs — it's the single highest-leverage habit for catching edge cases under pressure.
- When stuck, don't say "I don't know" and stop; say what you do know and reason from there. Interviewers want to see your process, not silence.

## 2026-11-05 · Is Subsequence · Easy · Hire

**What went well**
- You found the two-pointer approach quickly and correctly identified the O(n squared) brute force before moving past it.
- You stated the invariant cleanly once you had it: everything in s before i is matched in t before j, and i carries it.
- You caught and fixed the double increment of j on a matching step, which was the one real bug in the loop.
**Areas to improve**
- Your first pass at the invariant was "j increments," which describes the code, not why it's correct. An invariant is a claim about the state that justifies the answer, so practice phrasing it that way from the start.
- You introduced a regression in the while condition, flipping less-than to greater-than, while talking through the example. Small edits during narration are where bugs slip in, so re-read the line you just touched.
- The session got derailed by frustration with the tooling. That's real, but in an interview you'd want to park it and keep the technical thread moving.
**Code notes**
- The final code is correct: i advances only on a match, j always advances, and the return checks whether i reached the end of s.
- Complexity is O(len(s) + len(t)) time and O(1) space, which is optimal.
- On the invariant: you stated it correctly and it held after your fix. You didn't need to revise it, since the code moved back to match the original wording rather than the other way around.
**To improve on this type of problem**
- Say the invariant as a property of the data, not of the variables: "the first i characters of s are matched in order within the first j of t."
- When you trace an example out loud, keep the code frozen and trace against it, rather than editing as you narrate.
**To become more hireable overall**
- Practice narrating while your hands stay off the keyboard, then make edits deliberately and re-read the changed line.
- Have a one-line recovery phrase for tooling problems so frustration doesn't eat interview time.

## 2026-11-06 · Make The String Great · Easy · No Hire

**What went well**
- You correctly identified that a stack was the right structure and stated the core idea early: the stack holds the reduced prefix and you only compare against the top.
- You got to a clean, working O(n) time, O(n) space solution, and you traced the second example honestly to check it.
- You self-corrected several broken conditions without giving up, which is real persistence.

**Areas to improve**
- The cancellation condition took many iterations. You kept comparing a character to a boolean, and you overcomplicated the upper/lower test instead of reducing it to one clean check.
- You could not articulate the invariant or justify why the final stack is the answer. That is the thing interviewers probe hardest on stack problems, and "I don't know how to describe it" is a real gap.
- You nearly submitted a version with a flow bug where the current character was never appended in some paths. Reading the code against a small example caught it, but you needed prompting.

**Code notes**
- The final condition is correct: same letter ignoring case, and different case. The `continue` correctly skips the append after a pop.
- Invariant: you stated a rough version early ("the stack represents the current valid string") but could not defend it in review. The precise statement is that after each step the stack equals the reduced form of the prefix processed so far, with no cancelling pair left in it, so at the end it is the fully reduced string.

**To improve on this type of problem**
- When a condition feels messy, reduce it to the simplest possible predicate before writing it. Here, "same letter, different case" is one line.
- Practice stating the loop invariant out loud for every stack problem: what does the stack hold after processing a prefix, and why does that make the final state the answer.

**To become more hireable overall**
- Build the habit of justifying correctness with the invariant, not by re-describing the loop. That single skill separates Hire from No Hire in these interviews.
- Slow down on the condition logic and test it mentally against one concrete pair before moving on.
Could not state or defend the loop invariant, and the cancellation condition needed many failed iterations before it worked.
