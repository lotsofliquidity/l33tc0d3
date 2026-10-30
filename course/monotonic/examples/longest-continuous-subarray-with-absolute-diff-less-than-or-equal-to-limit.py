"""
Problem: Longest Continuous Subarray With Absolute Diff Less Than or Equal to
Limit (LeetCode 1438)
Chapter: Monotonic
Source: course article (monotonic — two deques, one non-increasing for the
window max and one non-decreasing for the min, inside the standard sliding
window; shrink from the left while max - min > limit).

Companion file: none yet — there is no practice attempt for this problem.
"""

from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing = deque()
        decreasing = deque()
        left = ans = 0
        
        for right in range(len(nums)):
            # maintain the monotonic deques
            while increasing and increasing[-1] > nums[right]:
                increasing.pop()
            while decreasing and decreasing[-1] < nums[right]:
                decreasing.pop()
                
            increasing.append(nums[right])
            decreasing.append(nums[right])
            
            # maintain window property
            while decreasing[0] - increasing[0] > limit:
                if nums[left] == decreasing[0]:
                    decreasing.popleft()
                if nums[left] == increasing[0]:
                    increasing.popleft()
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans
