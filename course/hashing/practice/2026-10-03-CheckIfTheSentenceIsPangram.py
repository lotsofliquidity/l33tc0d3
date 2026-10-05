"""
Problem: Check if the Sentence Is Pangram (LeetCode 1832)
Chapter: Hashing
Source: cold revisit — no notes/hints

A pangram is a sentence where every letter of the English alphabet appears at
least once. Given a string sentence containing only lowercase English letters,
return true if sentence is a pangram, or false otherwise.

Example 1:
  Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
  Output: True

Example 2:
  Input: sentence = "leetcode"
  Output: False

Constraints:
  1 <= sentence.length <= 1000
  sentence consists of lowercase English letters.
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        pangramSet = set(sentence)
        return len(pangramSet) == 26
