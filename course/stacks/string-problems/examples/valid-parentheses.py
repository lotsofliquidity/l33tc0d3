"""
Problem: Valid Parentheses (LeetCode 20)
Chapter: Stacks / string problems
Source: course article (string problems — push openers, pop on closers).

Companion file: ../practice/2026-10-21-ValidParentheses.py is the attempt.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        matching = {"(": ")", "[": "]", "{": "}"}
        stack = []

        
        for c in s: # "({})"
            if c in matching: # "})" are not in matching
                stack.append(c) # open appends the opening brackets
                print('Opening', c)
            else:
                if not stack:
                    return False
                
                previous_opening = stack.pop()
                if matching[previous_opening] != c:
                    print("Closing", matching[previous_opening])
                    return False
 
        return not stack


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("({})"))    # True
    print(sol.isValid("(){}[]"))  # True
    print(sol.isValid("(]"))      # False
    print(sol.isValid("({)}"))    # False
