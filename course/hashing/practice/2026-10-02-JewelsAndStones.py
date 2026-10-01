"""
Problem: Jewels and Stones (LeetCode 771)
Chapter: Hashing
Source: course practice

You're given strings jewels representing the types of stones that are jewels, and
stones representing the stones you have. Each character in stones is a type of
stone you have. Return how many of the stones you have are also jewels.

Letters are case sensitive ("a" != "A").

Example 1:
  Input: jewels = "aA", stones = "aAAbbbb"
  Output: 3

Example 2:
  Input: jewels = "z", stones = "ZZ"
  Output: 0

Constraints:
  1 <= jewels.length, stones.length <= 50
  jewels and stones consist of only English letters.
  All the characters of jewels are unique.
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
      jewel_set = set(jewels)

      jewelsFound = 0
      for stone in stones:
        if stone in jewel_set:
          jewelsFound += 1

      return jewelsFound



if __name__ == "__main__":
    sol = Solution()
    # print(sol.numJewelsInStones("aA", "aAAbbbb"))
    # print(sol.numJewelsInStones("z", "ZZ"))
