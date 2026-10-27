# String problems (stacks)

## In one sentence
Walk a string left to right, push characters onto a stack, and at each step compare the current character with the top — the stack is the “history” of previous / unresolved characters.

## When to use it
- Matching / nesting (brackets, tags): the closer must pair with the **most recent** opener.
- Adjacent deletions that cascade (dupes, backspaces): removing something mid-string exposes a new adjacent pair that was not adjacent in the original.
- Typed history with undo (`#` backspace): last typed character is the first deleted.
- Signal: “the thing that resolves next is the one I saw most recently” → LIFO.

## Core idea / invariant
At every index, the stack holds only characters that are still open / still present. The top is always the most recent unresolved one. A closing action either matches that top (pop and continue) or proves the string invalid / triggers a delete.

## Pattern / template

### Valid Parentheses (20)
**Recognition key:** the problem is LIFO — the last (most recent) opening bracket is the first to be closed. That is why a stack fits.

If the string starts `"({["` and the next three characters are closers, they must come in reverse order of how recently the openers appeared: `"]})"`. Anything else leaves a mismatch like `"[)"`.

Push openers. On a closer, the top opener must be its match. Associate pairs with a **hash map** (opener → closer); use the popped top as the key and check that the value equals the current character. Empty stack on a closer → invalid (e.g. `"{}"` then `"]"`). End with an empty stack — leftover openers like `"(){"` are invalid.

```python
class Solution:
    def isValid(self, s: str) -> bool:
        matching = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            if c in matching:          # opener
                stack.append(c)
            else:                      # closer
                if not stack or matching[stack.pop()] != c:
                    return False
        return not stack
```

Time O(n), space O(n): each character is pushed or popped at most once; the stack can grow with the input.

### Remove All Adjacent Duplicates In String (1047)
**Recognition key:** not every deletion is available at the start. Deleting one pair can expose a new adjacent pair deeper in the history. On `"abbaca"`, `"aa"` only becomes deletable after `"bb"` is gone. On `"abccba"`, the deletion order is `c → b → a` — last character involved is the first deleted. That cascade is LIFO.

Push each char. If it equals the top, they are adjacent (at this moment in the reduced string) — pop instead of pushing. Cascades fall out for free.

A stack is only the interface (add/remove same end). In Python a `list` is fine, then `"".join(stack)`. Other languages often use a mutable string / `StringBuilder` as the stack so the answer is already a string.

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
```

Time O(n), space O(n): stack ops are O(1); the stack can grow to the input length.

### Backspace String Compare (844)
**Recognition key:** a backspace deletes the character that was typed most recently — again LIFO. Simulate typing with a stack, then compare the two results.

Letter → push. `#` → pop if the stack is non-empty (backspace on an empty editor is a no-op). Do not compare `s` and `t` by index; `#` does not line up positionally.

```python
def build(s: str) -> list[str]:
    stack = []
    for c in s:
        if c != "#":
            stack.append(c)
        elif stack:
            stack.pop()
    return stack

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return build(s) == build(t)
```

Time and space linear in the input sizes, same as the other two.

## Complexity
All three: O(n) time (each char pushed/popped at most once), O(n) space for the stack.

## Pitfalls
- Popping on an empty stack (lone closer, leading `#`, or more `#`s than letters) — always check `if stack`.
- For brackets: mapping the wrong way (closer → opener) or forgetting to require an **empty** stack at the end (`"(){"` looks fine until the leftover `{`).
- Thinking adjacent-dupe deletions must be found with nested scans — the stack makes “became adjacent later” automatic.
- Matching the pop rule without the invariant: **the stack already holds the reduced form of the prefix**, so a new char can only pair with the top, and after a pop nothing below needs re-checking — that older pair was already good. This is why one pass suffices; if you can’t say that sentence, you’ve pattern-matched, not understood (1544 Make The String Great is the same move with a case check).
- Comparing backspace strings by index without simulating — `#` does not line up positionally across `s` and `t`.

## Tiny example
`s = "abbaca"` (adjacent duplicates):

| char | stack |
|---|---|
| `a` | `[a]` |
| `b` | `[a, b]` |
| `b` | `[a]` (pop — matched top) |
| `a` | `[]` (pop) |
| `c` | `[c]` |
| `a` | `[c, a]` |

Answer: `"ca"`. Deleting `bb` exposed `aa`; LIFO handled the cascade.

### Simplify Path (71)
**Recognition key:** the path is a stack of *directory names*, not of characters. `..` pops the most recent directory (LIFO); `.` and empty segments (from `//`) are no-ops; `...` is a real name and gets pushed.

Split on `'/'`, then for each part: skip `""` / `"."`; on `".."` pop if the stack is non-empty; else push. Answer is `"/" + "/".join(stack)`.

Pitfall: walking char-by-char only collapses slashes — it never sees a whole `".."` token to pop.

## Related
- Parent chapter: [../notes.md](../notes.md) — LIFO interface, push/pop/peek, recursion as a call stack.
- Not a stack: problems where the **oldest** unmatched item must resolve first (queue), or where you need random access into the history.
