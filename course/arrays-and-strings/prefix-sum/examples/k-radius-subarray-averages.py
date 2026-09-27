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
        # One answer per index. -1 means "this center cannot see k spots on both sides."
        avgs = [-1] * n
        if k == 0:
            return nums[:]

        # prefix[i] = sum of everything BEFORE index i. prefix[0] = 0 so a
        # window that starts at 0 still subtracts something.
        # nums    [7, 4,  3,  9,  1,  8,  5,  2,  6]
        # prefix  [0, 7, 11, 14, 23, 24, 32, 37, 39, 45]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        window = 2 * k + 1  # k=3 → 7 numbers: left side, center, right side
        # range(k, n-k) skips the edges. For k=3 and n=9 that is centers 3, 4, 5.
        for i in range(k, n - k):
            left, right = i - k, i + k
            total = prefix[right + 1] - prefix[left]
            avgs[i] = total // window

        return avgs


if __name__ == "__main__":
    print(Solution().getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))
