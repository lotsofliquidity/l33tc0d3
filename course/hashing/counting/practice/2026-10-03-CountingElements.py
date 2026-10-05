"""
Problem: Counting Elements (LeetCode 1426)
Chapter: Hashing
Source: cold revisit — no notes/hints

Given an integer array arr, count the number of elements x where x + 1 is also
present in arr.

Example 1:
  Input: arr = [1, 2, 3]
  Output: 2
  Explanation: 1 and 2 are counted because 2 and 3 are present.

Example 2:
  Input: arr = [1, 1, 3, 3, 5, 5, 7, 7]
  Output: 0

Example 3:
  Input: arr = [1, 3, 2, 3, 5, 0]
  Output: 3
  Explanation: 0, 1, and 2 are counted because 1, 2, and 3 are present.

Constraints:
  1 <= arr.length <= 1000
  0 <= arr[i] <= 1000
"""


class Solution:
    def countElements(self, arr: list[int]) -> int:
        element_set = set(arr)
        count = 0
        for element in arr:
            if element + 1 in element_set:
                count += 1

        return count