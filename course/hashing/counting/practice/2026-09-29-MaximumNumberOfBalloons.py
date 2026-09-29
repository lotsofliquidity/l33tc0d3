"""
Problem: Maximum Number of Balloons (LeetCode 1189)
Chapter: Hashing / counting
Source: course practice

Given a string text, use the characters of text to form as many instances of
the word "balloon" as possible. Each character in text may be used at most
once. Return the maximum number of instances that can be formed.

Example 1:
  Input: text = "nlaebolko"
  Output: 1

Example 2:
  Input: text = "loonbalxballpoon"
  Output: 2

Example 3:
  Input: text = "leetcode"
  Output: 0

Constraints:
  1 <= text.length <= 10^4
  text consists of lowercase English letters only.
"""

from collections import defaultdict

# {b: 1, a: 1, l: 2, o: 2, n: 1 }
from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = defaultdict(int)

        for ch in text:
            freq[ch] += 1

        # balloon requires: b:1, a:1, l:2, o:2, n:1
        return min(
            freq['b'],
            freq['a'],
            freq['l'] // 2,
            freq['o'] // 2,
            freq['n']
        )

          


if __name__ == "__main__":
    s = Solution()
    print(s.maxNumberOfBalloons("nlaebolko"))
    print(s.maxNumberOfBalloons("loonbalxballpoon"))
    print(s.maxNumberOfBalloons("leetcode"))
