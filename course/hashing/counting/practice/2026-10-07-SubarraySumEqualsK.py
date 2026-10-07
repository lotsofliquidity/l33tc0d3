"""
Problem: Subarray Sum Equals K (LeetCode 560)
Chapter: Hashing / counting
Source: course practice

Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals k.

Example 1:
  Input: nums = [1,1,1], k = 2
  Output: 2

Example 2:
  Input: nums = [1,2,3], k = 3
  Output: 2
"""

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1, 1, 1], 2))    # 2
    print(sol.subarraySum([1, 2, 3], 3))    # 2

