"""
Problem: Counting Elements
Difficulty: Easy
Session: interview companion
Status: incomplete / incorrect — reused Missing Number pattern
"""

from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        myset = set(arr)

        for i in range(len(myset) + 1):
            if myset[i + 1] in myset:
                return myset[i + 1]

        return 0


if __name__ == "__main__":
    s = Solution()
    # Expected: 2, 0
    # print(s.countElements([1, 2, 3]))
    # print(s.countElements([1, 1, 3, 3, 5, 5, 7, 7]))
