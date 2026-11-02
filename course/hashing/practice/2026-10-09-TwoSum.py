"""
Problem: Two Sum (LeetCode 1)
Chapter: Hashing
Source: course practice

Given an array of integers nums and an integer target, return the indices i and
j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that
satisfy the condition.

Return the answer with the smaller index first.

Example 1:
  Input: nums = [3,4,5,6], target = 7
  Output: [0,1]

Example 2:
  Input: nums = [4,5,6], target = 10
  Output: [0,2]

Example 3:
  Input: nums = [5,5], target = 10
  Output: [0,1]

Constraints:
  2 <= nums.length <= 1000
  -10,000,000 <= nums[i] <= 10,000,000
  -10,000,000 <= target <= 10,000,000
  Only one valid answer exists.
"""

from collections import defaultdict

#Example 2:
#  Input: nums = [4,5,6], target = 10
#  Output: [0,2]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # for left in range(len(nums)):
        #     # 4
        #     for right in range(left + 1, len(nums)):
        #         # 5
        #         # 6 
        #         if nums[left] + nums[right] == target:
        #             return [left, right]

        dic = defaultdict(int)
        for i in range(len(nums)):
            # 7 - 3
            complement = target - nums[i]
            # 4
            if complement in dic:
                return[dic[complement], i]

            dic[nums[i]] = i
            #{number: index}
 

if __name__ == "__main__":
    print(Solution().twoSum([3, 4, 5, 6], 7))
    # expected: [0, 1]
