# Try to solve 392. Is Subsequence without looking at the answer.
# Return True if s is a subsequence of t, otherwise False.


def isSubsequence(s, t):
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


# Quick checks
print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
print(isSubsequence("", "abc"))
