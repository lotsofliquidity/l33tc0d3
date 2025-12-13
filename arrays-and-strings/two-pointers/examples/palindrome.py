# output should be "True" if the input string is a palindrome, "False" otherwise
# time complexity: O(n)
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

result = is_palindrome("racecar")
print(result)