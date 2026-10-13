"""
Problem: Maximum Average Subarray I (LeetCode 643)
Chapter: Sliding window
Source: cold revisit — entry #2, Revisit due 2026-10-10

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum
average value and return this value. Any answer with a calculation error less
than 1e-5 will be accepted.

Example 1:
  Input: nums = [1, 12, -5, -6, 50, 3], k = 4
  Output: 12.75000

Example 2:
  Input: nums = [5], k = 1
  Output: 5.00000
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:        
        curr = 0

        for i in range(k):
            curr += nums[i]

        # store the best already found in the current window
        best = curr

        # 1, 12, -5, -6 = 13 - 11 = 2
        for i in range(k, len(nums)):
            curr -= nums[i - k] # removes the first val from the sub arry
            curr += nums[i] # adds the new value to the subarray
            best = max(best, curr)
        # 12, -5, -6, 50 = 62 - 11 = 51

        return best / k


        


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # expected: 12.75
    print(s.findMaxAverage([5], 1))  # expected: 5.0
