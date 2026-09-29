"""
Problem: Largest Unique Number (LeetCode 1133)
Chapter: Hashing / counting
Source: course practice

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

# Given an integer array nums, return the largest integer that occurs once.
# If no integer occurs once, return -1.
class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        counts = defaultdict(int)

        for num in nums:
          counts[num] += 1

        best = -1
        for num, count in counts.items():
          if count == 1 and num > best:
            best = num

        return best

        

        




if __name__ == "__main__":
    s = Solution()
    print(s.largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]))
    print(s.largestUniqueNumber([9, 9, 8, 8]))
