"""
Problem: Previous Warmer Day (variant of Daily Temperatures, LeetCode 739)
Chapter: Monotonic
Move: soon — same pattern, recall-proof (answer comes off the container, not out
of a pop), ~15 min. Notes open only after your attempt.

Given an array of integers temperatures that represents the daily temperatures,
return an array answer such that answer[i] is the number of days since the most
recent day before i that was strictly warmer than day i. If no earlier day was
warmer, answer[i] = 0.

Strictly warmer: an equal temperature does not count.

Example 1:
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [0,0,0,1,1,3,0,1]

Example 2:
    Input: temperatures = [30,40,50,60]
    Output: [0,0,0,0]

Example 3:
    Input: temperatures = [60,50,40,30]
    Output: [0,1,1,1]

Example 4:
    Input: temperatures = [50,50,50]
    Output: [0,0,0]
"""

from typing import List


class Solution:
    def previousWarmerDays(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] > temperatures[i]:
                j = stack.pop
                answer[j] = j - i
            stack.append(i)

        return answer


if __name__ == "__main__":                           #1
    print(Solution().previousWarmerDays([73, 74, 75, 71, 69, 72, 76, 73]))
    # expected: [0, 0, 0, 1, 1, 3, 0, 1]
    print(Solution().previousWarmerDays([30, 40, 50, 60]))
    # expected: [0, 0, 0, 0]
    print(Solution().previousWarmerDays([60, 50, 40, 30]))
    # expected: [0, 1, 1, 1]
    print(Solution().previousWarmerDays([50, 50, 50]))
    # expected: [0, 0, 0]
