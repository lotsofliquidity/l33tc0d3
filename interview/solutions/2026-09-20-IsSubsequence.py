"""
Problem: Is Subsequence
Difficulty: Easy
Session: interview companion
"""

from typing import List, Optional


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)


# Quick manual checks (optional)
if __name__ == "__main__":
    sol = Solution()
    print(sol.isSubsequence("abc", "ahbgdc"))
    print(sol.isSubsequence("axc", "ahbgdc"))
