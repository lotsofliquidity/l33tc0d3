"""
Problem: K Radius Subarray Averages
Chapter: Prefix sum
Source: course practice

Idea: For center i, average of nums[i-k .. i+k] if both ends in range;
      else -1. Window length always 2*k+1. Use prefix for O(1) range sums.
"""


class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        avgs = [-1] * n
        if k == 0:
            return nums[:]

        # prefix[i] = sum of nums[0 .. i-1]  (length n+1, prefix[0] = 0)
        # then sum nums[L .. R] = prefix[R+1] - prefix[L]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        window = 2 * k + 1
        for i in range(k, n - k):
            left, right = i - k, i + k
            total = prefix[right + 1] - prefix[left]
            avgs[i] = total // window

        return avgs
