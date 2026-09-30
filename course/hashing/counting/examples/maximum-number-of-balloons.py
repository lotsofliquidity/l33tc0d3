from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = defaultdict(int)
        for ch in text:
            freq[ch] += 1

        return min(
            freq["b"],
            freq["a"],
            freq["l"] // 2,
            freq["o"] // 2,
            freq["n"],
        )
