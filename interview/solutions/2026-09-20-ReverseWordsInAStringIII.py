"""
Problem: Reverse Words in a String III
Difficulty: Easy
Session: interview companion

Went wrong: reversed the whole string; need reverse each word, preserve word order.
"""

from typing import List, Optional


class Solution:
    def reverseWords(self, s: str) -> str:
        # --- your attempt (incorrect for this problem) ---
        left = 0
        right = len(s) - 1
        arr = [0] * len(s)

        while left <= right:
            arr[left] = s[right]
            arr[right] = s[left]
            left += 1
            right -= 1

        return "".join(arr)


if __name__ == "__main__":
    s = Solution()
    # print(s.reverseWords("Let's take LeetCode contest"))
