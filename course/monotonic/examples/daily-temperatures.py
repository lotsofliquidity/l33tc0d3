"""
Problem: Daily Temperatures (LeetCode 739)
Chapter: Monotonic
Source: course article (monotonic — keep a stack of indices in non-increasing
temperature order; a warmer day pops everything it beats, and the distance is
the answer for each popped day).

Companion file: none yet — there is no practice attempt for this problem.
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        
        return answer
