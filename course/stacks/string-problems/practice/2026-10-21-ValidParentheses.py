"""
Problem: Valid Parentheses (LeetCode 20)
Chapter: Stacks / string problems

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid. The string is valid if all open brackets
are closed by the same type of closing bracket in the correct order, and each
closing bracket closes exactly one open bracket.

Example 1:
  Input: s = "({})"
  Output: True

Example 2:
  Input: s = "(){}[]"
  Output: True

Example 3:
  Input: s = "(]"
  Output: False

Example 4:
  Input: s = "({)}"
  Output: False
"""


class Solution:
    pass


if __name__ == "__main__":
    print(Solution().isValid("({})"))
    # expected: True
    print(Solution().isValid("(){}[]"))
    # expected: True
    print(Solution().isValid("(]"))
    # expected: False
    print(Solution().isValid("({)}"))
    # expected: False
