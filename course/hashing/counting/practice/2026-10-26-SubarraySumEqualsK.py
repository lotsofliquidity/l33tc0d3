"""
Problem: Subarray Sum Equals K (LeetCode 560)
Chapter: Hashing / counting
Regime: cold revisit — no notes, no solution file

Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals k.

Example:
  Input: nums = [1,1,1], k = 2
  Output: 2
"""

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            curr += num
            
            counts[curr - k]



if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1, 1, 1], 2))
    # expected: 2
