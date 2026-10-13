"""
Problem: Missing Number (LeetCode 268)
Chapter: Hashing
Source: cold revisit — entry #8, Revisit due 2026-10-10

Given an array nums containing n distinct numbers in the range [0, n], return
the only number in the range that is missing from the array.

Example 1:
  Input: nums = [3, 0, 1]
  Output: 2

Example 2:
  Input: nums = [0, 1]
  Output: 2

Example 3:
  Input: nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
  Output: 8

Constraints:
  n == nums.length
  1 <= n <= 10^4
  0 <= nums[i] <= n
  All the numbers of nums are unique.
"""

from collections import defaultdict

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        missing_set = set(nums)

        for num in range(len(nums) + 1):
            if num not in missing_set:
                return num


if __name__ == "__main__":
    sol = Solution()
    print(sol.missingNumber([3, 0, 1]))                    # expected: 2
    print(sol.missingNumber([0, 1]))                       # expected: 2
    print(sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # expected: 8
    print(sol.missingNumber([1, 2, 3]))                    # expected: 0
