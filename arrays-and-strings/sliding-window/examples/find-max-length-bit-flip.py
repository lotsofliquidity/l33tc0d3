#   Example 2: You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". 
#   What is the length of the longest substring achievable that contains only "1"?
#
#   For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.

def find__max_length_bit_flip_v1(s):
    left  = curr = ans = 0

    for right in range(len(s)):
        # 110110
        if s[right] == '0':
            curr += 1
            # curr = 1
            # curr = 2

            while curr > 1:
                if s[left] == "0":
                    curr -= 1
                
                left += 1


        ans = max(ans, right - left + 1)
    
    return ans

result = find__max_length_bit_flip_v1("1101100111")
print(result)


#   Example 2: You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". 
#   What is the length of the longest substring achievable that contains only "1"?
#
#   For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.

### First attempt ###
# def find_length(s):
#     left  = curr = ans = 0

#     for right in range(len(s)):
#         # 110110
#         if s[right] == '0':
#             curr += 1
#             # curr = 1
#             # curr = 2

#         ans = (ans, right - left + 1)
    
#     return ans

# Misunderstood the conditions - missing the while loop for if curr > 1 and missed the max in ans.


# 14/12/2025
#   Example 2: You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". 
#   What is the length of the longest substring achievable that contains only "1"?
#
#   For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.

### First Attempt ###
def find__max_length_bit_flip_v2(s):
    left = curr = ans = 0

    for right in range(len(s)):
        # 110
        # 1100
        if s[right] == '0':
            curr += 1
            # Good! 1 bit if flipped.
            # Uh oh, 2 bits are now flipped! - proceed to next condition
        
        while curr > 1:
            # Left most bit if not a 0
            # 2nd element from left is not a 0
            if s[left] == '0':
                curr -= 1
            
            # if it's a 1 or 0
            left += 1
    
        ans = max(ans, right - left + 1)

    return ans


result = find__max_length_bit_flip_v2("1101100111")
print(result)


# 17/12/2025
#   Example 2: You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". 
#   What is the length of the longest substring achievable that contains only "1"?
#
#   For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.

def find__max_length_bit_flip_v3(s):
    left = curr = 0
    # forgot to store ans
    ans = 0

    for right in range(len(s)):

        if s[right] == '0':
            # s = "1001"
            curr += 1

        while curr > 1:
            if s[left] == '0':
                curr -= 1 # I can't see why we remove current (sad face) - write it out with pen and paper when home

            left += 1


        ans = max(ans, right - left + 1)

    return ans


# Notes
    # Find out when to use a forloop over while
        # ans - I think sliding windows use it 
    # I keep getting messed up in the while loop

result = find__max_length_bit_flip_v3("1101100111")
print(result)