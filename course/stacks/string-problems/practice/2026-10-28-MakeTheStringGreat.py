"""
Problem: Make The String Great (LeetCode 1544)
Chapter: Stacks / string problems

Given a string s of lower and upper case English letters, a string is good if
no two adjacent characters are the same letter in different case. Repeatedly
remove any such adjacent pair until the string is good, and return it. The
answer is guaranteed to be unique. An empty string is good.
"""


class Solution:
    def makeGood(self, s: str) -> str:
        # Invariant: the stack already holds the cleaned prefix, so a new
        # character can only clash with the top — one pass is enough.
        stack = []
        for char in s:
            if stack and char != stack[-1] and char.lower() == stack[-1].lower():
                stack.pop()
                continue
            else: 
                stack.append(char) # l e E

        return "".join(stack)

        
        
                




if __name__ == "__main__":
    print(Solution().makeGood("leEeetcode"))
    # expected: leetcode
    print(Solution().makeGood("abBAcC"))
    # expected: (empty string)
    print(Solution().makeGood("s"))
    # expected: s
    print(Solution().makeGood("Aa"))
    # expected: (empty string)
    print(Solution().makeGood("abBcC"))
    # expected: a
