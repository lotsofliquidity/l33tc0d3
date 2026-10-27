"""
Problem: Make The String Great (LeetCode 1544)
Chapter: Stacks / string problems
Source: no article copy — reference written for the 2026-10-28 session attempt.

Companion file: ../practice/2026-10-28-MakeTheStringGreat.py is the attempt.
"""


class Solution:
    def makeGood(self, s: str) -> str:
        # Invariant: the stack already holds the cleaned prefix, so a new
        # character can only clash with the top — one pass is enough.
        stack = []

        for c in s:
            if stack and stack[-1] != c and stack[-1].lower() == c.lower():
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)


if __name__ == "__main__":
    sol = Solution()
    print(sol.makeGood("leEeetcode"))  # leetcode
    print(sol.makeGood("abBAcC"))      # (empty)
    print(sol.makeGood("s"))           # s
    print(sol.makeGood("Aa"))          # (empty)
    print(sol.makeGood("abBcC"))       # a
