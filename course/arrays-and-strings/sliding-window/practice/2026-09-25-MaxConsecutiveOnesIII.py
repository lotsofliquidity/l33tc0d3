"""
Problem: Max Consecutive Ones III (LeetCode 1004)
Chapter: Sliding window
Source: cold revisit — no notes/hints

Given a binary array nums and an integer k, return the maximum number of
consecutive 1's in the array if you can flip at most k 0's.

Example 1:
  Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
  Output: 6
  Explanation: Flip the two zeros in [0,1,1,1,1,0] (indices 5–10) to get six 1's.

Example 2:
  Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
  Output: 10

Constraints:
  1 <= nums.length <= 10^5
  nums[i] is either 0 or 1
  0 <= k <= nums.length
"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        curr = 0
        ans = 0
        left = 0

        # 0, 1, 1, 1, 0, 1
        # LR


        # 0, 1, 1, 1, 0, 1
        # L  R

        # 0, 1, 1, 1, 0, 0
        # L           R


        # 0, 1, 1, 1, 0, 0
        # L              R
        for right in range(len(nums)):
          if nums[right] == 0:
            curr += 1
            # CURR = 1
            # 0, 1, 1, 1, 0, 1
            # LR

            # CURR = 3
            # 0, 1, 1, 1, 0, 0
            # L              R
            while curr > k:
              if nums[left] == 0:

                # CURR = 3
                # 0, 1, 1, 1, 0, 0
                # L              R

                curr -= 1

                # CURR = 2
                # 0, 1, 1, 1, 0, 0
                #    L           R
              left += 1
          
          ans = max(ans, right - left + 1)
        return ans

              


