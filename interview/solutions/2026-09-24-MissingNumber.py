"""
Problem: Missing Number
Difficulty: Easy
Session: interview companion
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        myset = set(nums)

        # How many numbers are we checking are missing? 
        # 1.

        for i in range(len(myset) + 1):
            if i not in myset:
                return i
        
        return 0
        


if __name__ == "__main__":
    s = Solution()
    # print(s.missingNumber([3, 0, 1]))  # 2
    # print(s.missingNumber([0, 1]))  # 2
    # print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
