class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        n = len(chars)

        def reverse(l, r):
            while l < r:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1

        start = 0
        for i in range(n):
            if chars[i] == " ":
                reverse(start, i - 1)
                start = i + 1
        reverse(start, n - 1)
        return "".join(chars)
