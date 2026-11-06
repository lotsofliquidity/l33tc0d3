"""
Problem: Two Sum (LeetCode 1)
Difficulty: Easy
Chapter: Hashing
Session: interview companion (DS&A Interview AI)

Given a list of integers and a target, return the indices of the two numbers that add up to the target. Each input has exactly one answer and you may not use the same index twice. Return the pair with the smaller index first.

Example:
  Input: nums = [2,7,11,15], target = 9
  Output: [0,1]
  nums[0] + nums[1] = 9.

Constraints:
  2 <= len(nums) <= 10^4
  -10^9 <= nums[i] <= 10^9
  exactly one valid answer exists
"""

from typing import List, Optional

from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	dic = defaultdict(int)
		
		for i in range(len(nums)):
			complement = target - nums[i]
			# 7
			if complement in dic:
				return [dic[complement], i]
		
			# val: integer
			dic[nums[i]] = i
		


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
