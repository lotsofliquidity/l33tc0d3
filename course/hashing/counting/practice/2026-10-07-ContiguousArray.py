"""
Problem: Contiguous Array (LeetCode 525)
Chapter: Hashing / counting
Source: cold revisit (first logged 2026-09-30)

Given a binary array nums, return the maximum length of a contiguous subarray
with an equal number of 0 and 1.

Example 1:
  Input: nums = [0,1]
  Output: 2

Example 2:
  Input: nums = [0,1,0]
  Output: 2

Example 3:
  Input: nums = [0,1,1,1,1,1,0,0,0]
  Output: 6
"""

from typing import List
from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxLength([0, 1]))                          # 2
    print(sol.findMaxLength([0, 1, 0]))                       # 2
    print(sol.findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0]))     # 6
