"""
Problem: Contiguous Array (LeetCode 525)
Chapter: Hashing / counting

Given a binary array nums, return the maximum length of a contiguous subarray
with an equal number of 0 and 1.

Example 1:
  Input: nums = [0, 1]
  Output: 2
  Explanation: [0, 1] is the longest contiguous subarray with equal 0s and 1s.

Example 2:
  Input: nums = [0, 1, 0]
  Output: 2
  Explanation: [0, 1] (or [1, 0]) is the longest.

Cold revisit: 2026-10-23 (logged #13, due 2026-10-14). No notes, no lookups.
"""

from typing import List

from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = defaultdict(int)
        balance = 0
        best = 0

        for i in range(len(nums)):
          if nums[i] == 1:
            balance += 1
          else:
            balance -= 1
          


          
        return best


if __name__ == "__main__":
    print(Solution().findMaxLength([0, 1]))
    # expected: 2
    print(Solution().findMaxLength([0, 1, 0]))
    # expected: 2
