"""
Problem: Previous Warmer Day (variant of Daily Temperatures, LeetCode 739)
Chapter: Monotonic
Source: written with you in a session, 2026-11-02.

For each day, the distance back to the most recent strictly warmer day.

Idea: sweep left to right and keep a stack of indices whose temperatures are
strictly decreasing from bottom to top. Before pushing day i, pop every day
that is not strictly warmer than day i (temps[top] <= temps[i]) — day i is
nearer to every future day and at least as warm, so those days can never be
anybody's answer again. Whatever is left on top is now the nearest strictly
warmer day, and the answer is read off it. Unlike 739, the pops do not write
answers; they only clear dead days.
"""

from typing import List


class Solution:
    def previousWarmerDays(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                answer[i] = i - stack[-1]
            stack.append(i)

        return answer


if __name__ == "__main__":
    print(Solution().previousWarmerDays([73, 74, 75, 71, 69, 72, 76, 73]))
    # expected: [0, 0, 0, 1, 1, 3, 0, 1]
    print(Solution().previousWarmerDays([30, 40, 50, 60]))
    # expected: [0, 0, 0, 0]
    print(Solution().previousWarmerDays([60, 50, 40, 30]))
    # expected: [0, 1, 1, 1]
    print(Solution().previousWarmerDays([50, 50, 50]))
    # expected: [0, 0, 0]
