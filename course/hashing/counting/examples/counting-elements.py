from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        seen = set(arr)
        count = 0
        for x in arr:
            if x + 1 in seen:
                count += 1
        return count
