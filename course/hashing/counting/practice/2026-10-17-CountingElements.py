"""
Problem: Counting Elements (LeetCode 1426)
Chapter: Hashing / counting
Source: cold revisit — no notes/hints

Given an integer array arr, count how many elements x there are such that x + 1
is also in arr. If there are duplicates in arr, count them separately.

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
  Explanation: 0, 1 and 2 are counted because 1, 2 and 3 are present.

Constraints:
  1 <= arr.length <= 1000
  0 <= arr[i] <= 1000
"""


class Solution:
    def countElements(self, arr: list[int]) -> int:
        count = 0
        seen = set()

        for num in arr:
            seen.add(num)
            if num in seen:
                count += 1
            else:
                count -= 1
                seen.remove(num)


        return count


if __name__ == "__main__":
    s = Solution()
    print(s.countElements([1, 2, 3]))
    # expected: 2
    print(s.countElements([1, 1, 3, 3, 5, 5, 7, 7]))
    # expected: 0
    print(s.countElements([1, 3, 2, 3, 5, 0]))
    # expected: 3
