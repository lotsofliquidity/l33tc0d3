"""
Problem: Largest Unique Number (LeetCode 1133)
Chapter: Hashing / counting
Source: cold revisit 2026-10-09 (first logged 2026-09-29)

Given an integer array nums, return the largest integer that occurs once.
If no integer occurs once, return -1.

Example 1:
  Input: nums = [5,7,3,9,4,9,8,3,1]
  Output: 8
  Explanation: 9 is larger but repeated. 8 occurs once.

Example 2:
  Input: nums = [9,9,8,8]
  Output: -1
  Explanation: No number occurs once.

Constraints:
  1 <= nums.length <= 2000
  0 <= nums[i] <= 1000
"""

from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        best = -1
        for num, freq in count.items():
            if freq == 1:
                best = max(best, num)

        return best

        

if __name__ == "__main__":
    print(Solution().largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]))
    # expected: 8
