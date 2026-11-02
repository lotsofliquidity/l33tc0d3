"""
Problem: Daily Temperatures (LeetCode 739)
Chapter: Monotonic

Given an array of integers temperatures that represents the daily
temperatures, return an array answer such that answer[i] is the number of days
you have to wait after the ith day to get a warmer temperature. If there is no
future day that is warmer, have answer[i] = 0 instead.

Example 1:
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]

Example 2:
    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]

Example 3:
    Input: temperatures = [30,60,90]
    Output: [1,1,0]
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


if __name__ == "__main__":
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    # expected: [1, 1, 4, 2, 1, 1, 0, 0]
    print(Solution().dailyTemperatures([30, 40, 50, 60]))
    # expected: [1, 1, 1, 0]
    print(Solution().dailyTemperatures([30, 60, 90]))
    # expected: [1, 1, 0]
