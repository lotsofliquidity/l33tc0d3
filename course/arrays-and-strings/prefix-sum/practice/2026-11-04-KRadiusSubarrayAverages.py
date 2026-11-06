"""
For each index i, compute the average of the subarray centered at i with
radius k (from i - k through i + k), using integer division. If this subarray
extends beyond the array, set the result at i to -1.

Constraints:
    1 <= len(nums) <= 10**5
    0 <= nums[i] <= 10**5
    0 <= k <= 10**5
"""

from typing import List

#    print(Solution().getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))
#    # expected: [-1, -1, -1, 5, 4, 4, -1, -1, -1]

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n

        if k == 0:
            return nums[:]

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        window = k * 2 + 1
        for i in range(k, n - k):
            # we are at 






        


if __name__ == "__main__":
    print(Solution().getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))
    # expected: [-1, -1, -1, 5, 4, 4, -1, -1, -1]
    print(Solution().getAverages([100000], 0))
    # expected: [100000]
    print(Solution().getAverages([8], 1))
    # expected: [-1]
