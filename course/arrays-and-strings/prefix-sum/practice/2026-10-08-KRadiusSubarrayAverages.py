"""
Problem: K Radius Subarray Averages (LeetCode 2090)
Chapter: Prefix sum
Source: cold revisit #4 (first logged 2026-09-20) — no notes/hints

You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray centered at index i is the average of all
elements in nums between indices i - k and i + k (inclusive). If there are fewer
than k elements before or after index i, the k-radius average is -1.

Return an array avgs of length n where avgs[i] is the k-radius average for the
subarray centered at index i.

The average of x elements is their sum divided by x, using integer division.
The division rounds toward zero.

Example 1:
  Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
  Output: [-1,-1,-1,5,4,4,-1,-1,-1]
  Explanation:
    i = 0, 1, 2 and i = 6, 7, 8 do not have k elements on both sides.
    i = 3: (7+4+3+9+1+8+5) / 7 = 5
    i = 4: (4+3+9+1+8+5+2) / 7 = 4
    i = 5: (3+9+1+8+5+2+6) / 7 = 4

Example 2:
  Input: nums = [100000], k = 0
  Output: [100000]

Example 3:
  Input: nums = [8], k = 100000
  Output: [-1]

Constraints:
  n == nums.length
  1 <= n <= 10^5
  0 <= nums[i], k <= 10^5
"""


class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        curr = 0
        prefix_arr = [-1] * len(nums)

        if len(nums) <= k:
            return 0

        for i in range(k, len(nums) - k):
            curr += nums[i] / k
            prefix_arr.append(curr)

        return prefix_arr
        


if __name__ == "__main__":
    s = Solution()
    print(s.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))
    print(s.getAverages([100000], 0))
    print(s.getAverages([8], 100000))
