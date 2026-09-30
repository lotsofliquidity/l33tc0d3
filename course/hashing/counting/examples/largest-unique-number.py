from collections import defaultdict
from typing import List

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        best = -1
        for num, count in counts.items():
            if count == 1:
                best = max(best, num)
        return best
