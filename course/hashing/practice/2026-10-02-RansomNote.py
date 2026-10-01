"""
Problem: Ransom Note (LeetCode 383)
Chapter: Hashing
Source: course practice

Given two strings ransomNote and magazine, return true if ransomNote can be
constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
  Input: ransomNote = "a", magazine = "b"
  Output: false

Example 2:
  Input: ransomNote = "aa", magazine = "ab"
  Output: false

Example 3:
  Input: ransomNote = "aa", magazine = "aab"
  Output: true

Constraints:
  1 <= ransomNote.length, magazine.length <= 10^5
  ransomNote and magazine consist of lowercase English letters.
"""

from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineLetters = defaultdict(int)
        for ch in magazine:
            magazineLetters[ch] += 1
            
        for ch in ransomNote:
            if ch in magazineLetters:
                magazineLetters[ch] -= 1
                
                if magazineLetters[ch] == 0:
                    del magazineLetters[ch]
            else: 
                return False
        return True
            
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct("a", "b"))
    print(sol.canConstruct("aa", "ab"))
    print(sol.canConstruct("aa", "aab"))
