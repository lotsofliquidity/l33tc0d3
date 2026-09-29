"""
Problem: Reverse Words in a String III
Difficulty: Easy
Session: interview companion
"""

from typing import List, Optional


class Solution:

    def reverseWords(self, s: str) -> str:
        def reverseString(leftIndex, rightIndex):
            arr = [0] * (rightIndex - leftIndex)

            while leftIndex < rightIndex:
                temp = s[leftIndex]
                arr[leftIndex] = s[rightIndex]
                arr[rightIndex] = temp
                leftIndex += 1
                rightIndex -= 1

            return arr
            
        left = 0
        arr = []

        # Mr Ding
        # r
        # l
        # Mr Ding
        # lr
        # Mr Ding
        # l r
        # REVERSE STRING (leftIndex = 0, rightIndex = 2)
        #     []
        #     lr
        #     ['r', 'M']
        #     RETURN
        # Mr Ding
        #   rl
        #    l
        #    r

        for right in range(len(s)):
            if s[right] == ' ' and right < len(s):
                reversedString = reverseString(left, right)
                left = right + 1
                arr.append(reversedString)
                arr.append(' ')
            elif right == len(s) - 1:
                reversedString = reverseString(left, right)
                arr.append(reversedString)

        return "".join(arr)


# Quick manual checks (optional)
if __name__ == "__main__":
    sol = Solution()
    # print(sol.reverseWords("Let's take LeetCode contest"))
    # print(sol.reverseWords("Mr Ding"))
