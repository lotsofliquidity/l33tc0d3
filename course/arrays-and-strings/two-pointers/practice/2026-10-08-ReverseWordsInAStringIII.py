# Cold revisit 2026-10-08 — no notes, no hints.
# 557. Reverse Words in a String III
# Given a string s, reverse the order of characters in each word (words are
# separated by single spaces, order of words stays the same). Return the string.

class Solution:

    def reverseWords(self, s: str) -> str:

        def reverseString(leftIndex, rightIndex):
            while leftIndex < rightIndex:
                temp = s_list[leftIndex]
                s_list[leftIndex] = s_list[rightIndex]
                s_list[rightIndex] = temp
                rightIndex -= 1
                leftIndex += 1

        s_list = list(s)
        left = 0
        for right in range(len(s_list)):
            if s_list[right] == ' ':
                reverseString(left, right - 1)
                left = right + 1
        reverseString(left, len(s) - 1)

        return "".join(s_list)






if __name__ == "__main__":
    print(Solution().reverseWords("Let's take LeetCode contest"))
    # expected: "s'teL ekat edoCteeL tsetnoc"

