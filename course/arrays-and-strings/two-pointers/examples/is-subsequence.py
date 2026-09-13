#  Example 4: 392. Is Subsequence.
#  Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#  A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, 
#  while maintaining the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.

def isSubsequence(s, t):
    i = j = 0
    while i < len(s) and j < len(t):
        # s = "ace"
        # t = "abcde"
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)


# 14/12/2025
#  Example 4: 392. Is Subsequence.
#  Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#  A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, 
#  while maintaining the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.

## First Attempt ###
def isSubsequence_v2(s, t):
    left = 0

    for right in range(len(t)):
        # s = "ace"
        # t = "abcde"
        if t[right] == s[left]:
            left += 1

    return left == len(s)
    

result = isSubsequence_v2("ace", "abcde")
print(result)

# left is used as an index into s.
# If all characters of s are matched, then left == len(s).
# But Python strings are 0‑indexed. The last valid index is len(s) - 1.
# So if left == len(s), then s[left] is out of bounds → IndexError.


# 14/12/2025
#  Example 4: 392. Is Subsequence.
#  Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#  A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, 
#  while maintaining the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.

### Second Attempt ###
def isSubsequence_v3(s, t):
    i = j = 0
    # s = 'ace'
    # t = 'abcde'
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1

        j += 1

    return i == len(s)

result = isSubsequence_v3("ace", "abcde")
print(result)


# 17/12/2025
# Example 4: 392. Is Subsequence.
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, 
# while maintaining the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.

def isSubsequence_a4(s, t):
    # s = 'ace'
    # t = 'abcde'

    # We will need to iterate over all elements in t.
        # unless all elements in s have been found in t.

    i = j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        
        j += 1

    return i == len(s)

result = isSubsequence_a4("ace", "abcde")
print("a4", result)