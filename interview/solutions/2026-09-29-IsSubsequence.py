"""
Problem: Is Subsequence
Difficulty: Easy
Session: interview companion
"""

from typing import List, Optional


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        index = 0

        # s = "abc"
        #      i
        # t = "ahbgdc"
        #      j
        # MATCH
        # i += 1
        # j += 1
        # s = "abc"
        #       i
        # t = "ahbgdc"
        #       j
        # NO MATCH
        # j += 1
        # s = "abc"
        #       i
        # t = "ahbgdc"
        #        j
        # MATCH

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i == len(s)
        


# Quick manual checks (optional)
if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
    # print(s.isSubsequence("axc", "ahbgdc"))
