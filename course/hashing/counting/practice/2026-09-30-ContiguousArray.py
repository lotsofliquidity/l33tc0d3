"""
Problem: Contiguous Array (LeetCode 525)
Chapter: Hashing / counting
Source: course practice

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

from collections import defaultdict
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = defaultdict(int)
        first[0] = -1
        balance = 0
        best = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                balance += 1
            else:
                balance -= 1

            if balance in first:
                best = max(best, i - first[balance])
            else:
                first[balance] = i

        return best


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxLength([0, 1]))
    print(sol.findMaxLength([0, 1, 0]))
    print(sol.findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0]))
