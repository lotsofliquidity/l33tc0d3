"""
Problem: Counting Elements (LeetCode 1426)
Chapter: Hashing / counting
Regime: cold revisit — no notes, no solution file

Given an integer array arr, count how many elements x there are such that x + 1
is also in arr. If there are duplicates in arr, count them separately.

Example 1:
  Input: arr = [1, 2, 3]
  Output: 2

Example 2:
  Input: arr = [1, 1, 3, 3, 5, 5, 7, 7]
  Output: 0

Example 3:
  Input: arr = [1, 3, 2, 3, 5, 0]
  Output: 3
"""


class Solution:
    def countElements(self, arr: list[int]) -> int:
        seen = set(arr)
        counter = 0

        for el in arr:
            if el + 1 in seen:
                counter += 1

        return counter
                


if __name__ == "__main__":
    s = Solution()
    print(s.countElements([1, 2, 3]))
    # expected: 2
    print(s.countElements([1, 1, 3, 3, 5, 5, 7, 7]))
    # expected: 0
    print(s.countElements([1, 3, 2, 3, 5, 0]))
    # expected: 3
