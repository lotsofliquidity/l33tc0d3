"""
Problem: Maximum Average Subarray I (LeetCode 643)
Chapter: Sliding window
Source: soon practice after failed cold revisit (2026-09-24)

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
        
        # This is a fixed window problem
        # create the window with the current count
        curr = 0
        
        # [1, 12, -5, -6]
        for i in range(k):
          print("Current element is ", i)
          curr += nums[i]
        
        print("Finished fixed window")

        # curr = 2

        # store the curr in an ans var to start
        ans = curr

        # ans = 2

        # Run sliding window from the end of the current fixed window
        for i in range(k, len(nums)):
          print("Current element is ", i)
          print(nums[i], nums[k], nums[i - k])
          curr += nums[i]
          curr -= nums[i - k]

          # keep track of the current max window number
          ans = max(ans, curr)

        return ans / k



if __name__ == "__main__":
    s = Solution()
    print(s.findMaxAverage([1, 12, -5, -6, 50, 3, 5, 22, 12, 5, -10, 2], 4))  # 12.75
    #print(s.findMaxAverage([5], 1))  # 5.0
