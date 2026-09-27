"""
Problem: K Radius Subarray Averages
Chapter: Prefix sum
Source: course example

Same answer as k-radius-subarray-averages.py.
prefix[i] is the sum through index i, the version from the practice file.
"""


class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        # prefix[i] = sum THROUGH index i.
        # nums   [7,  4,  3,  9,  1,  8,  5,  2,  6]
        # prefix [7, 11, 14, 23, 24, 32, 37, 39, 45]
        prefix = []
        curr = 0
        for num in nums:
            curr += num
            prefix.append(curr)

        n = len(nums)
        ans = [-1] * n  # edges stay -1 unless a later step fills them
        size = 2 * k + 1
        for i in range(n):
            left = i - k
            right = i + k
            if left < 0 or right >= n:
                print(f"center {i}: window {left}..{right} falls off the array → -1")
                continue
            # Sum through right, minus the sum before left.
            if left == 0:
                total = prefix[right]
            else:
                total = prefix[right] - prefix[left - 1]
            ans[i] = total // size
            print(
                f"center {i}: nums[{left}..{right}] = {nums[left:right + 1]} "
                f"sum={total} avg={ans[i]}"
            )
        return ans


if __name__ == "__main__":
    print(Solution().getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))
