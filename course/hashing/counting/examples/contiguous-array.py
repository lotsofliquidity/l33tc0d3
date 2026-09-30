from collections import defaultdict
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = defaultdict(int)
        first[0] = -1
        balance = 0
        best = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                balance += 1
            else:
                balance -= 1

            if balance in first:
                best = max(best, i - first[balance])
            else:
                first[balance] = i

        return best
