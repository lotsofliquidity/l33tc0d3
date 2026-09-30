"""
Problem: Group Anagrams (LeetCode 49)
Chapter: Hashing
Source: course practice

Given an array of strings strs, group the anagrams together. You can return
the answer in any order.

Example 1:
  Input: strs = ["eat","tea","tan","ate","nat","bat"]
  Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
  Input: strs = [""]
  Output: [[""]]

Example 3:
  Input: strs = ["a"]
  Output: [["a"]]

Constraints:
  1 <= strs.length <= 10^4
  0 <= strs[i].length <= 100
  strs[i] consists of lowercase English letters.
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # print(sol.groupAnagrams([""]))
    # print(sol.groupAnagrams(["a"]))
