"""
Problem: Maximum Average Subarray I
Chapter: Sliding window (fixed size)
Source: practice

Idea: Fixed window of length k — track max sum, return max_sum / k.
"""

# --- Your attempt (bugs noted below) ---
# class Solution:
#     def findMaxAverage(self, nums: list[int], k: int) -> float:
#         curr = 0
#         for i in range(k):
#             curr += nums[k]          # BUG: always nums[k], should be nums[i]
#         ans = curr / k
#         for right in range(k, len(nums)):
#             curr += nums[i] - nums[i - k]  # BUG: i is stale (k-1); use right
#             ans = max(ans, curr)     # BUG: curr is a sum, ans is an average
#         # missing return


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr = 0
        for i in range(k):
            curr += nums[i]

        best = curr  # track max sum (same k → max sum == max average)

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            best = max(best, curr)

        return best / k


if __name__ == "__main__":
    print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # 12.75
