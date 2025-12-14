# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# 
# Example 1:
# 
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# 
# Example 2:
# 
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# 
# Constraints:
# 
#     1 <= nums.length <= 104
#     -104 <= nums[i] <= 104
#     nums is sorted in non-decreasing order.


# Comments:
# sorted! in non-decreasing

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
def sortedSquares(nums):
    left = 0
    right = len(nums) - 1

    # since there's a new array, we need an array and index
    index = len(nums) - 1
    arr = len(nums) * [0]

    while left <= right:
        leftSquared = nums[left] ** 2
        rightSquared = nums[right] ** 2

        if leftSquared < rightSquared:
            arr[index] = rightSquared
            right -= 1
        else:
            arr[index] = leftSquared
            left += 1

        index -= 1

    return arr

result = sortedSquares([-7,-3,2,3,11])
print(result)

### First attempt ###
# def sortedSquares(nums):
#     left = 0
#     right = len(nums) - 1

#     # since there's a new array, we need an array and index
#     index = 0
#     arr = len(nums) - 1 * [0]

#     while left < right:
#         leftSquared = nums[left] ** 2
#         rightSquared = nums[right] ** 2

#         if leftSquared < rightSquared:
#             arr[index] = leftSquared
#             left += 1
#         else:
#             arr[index] = rightSquared
#             right -= 1

#         index += 1

#     return arr

# result = sortedSquares([-7,-3,2,3,11])
# print(result)

# Errored because array should be the length of the nums array, not -1.


### Second attempt ###
# def sortedSquares(nums):
#    left = 0
#    right = len(nums) - 1
# 
#    # since there's a new array, we need an array and index
#    index = 0 (change to len - 1)
#    arr = len(nums) * [0]
# 
#    while left < right:
#        leftSquared = nums[left] ** 2
#        rightSquared = nums[right] ** 2
# 
#        if leftSquared < rightSquared:
#            arr[index] = leftSquared
#            left += 1
#        else:
#            arr[index] = rightSquared
#            right -= 1
# 
#        index += 1
# 
#    return arr

# Since the sorted squares problem expects the result array to be sorted in non-decreasing order. 
# The largest squares come from the ends of the input array (negative large numbers and positive large numbers). 
# If you start filling from index 0, you’ll put the largest values at the beginning, which makes the array unsorted.

### Third attempt ###
# def sortedSquares(nums):
#     left = 0
#     right = len(nums) - 1
# 
#     # since there's a new array, we need an array and index
#     index = len(nums) - 1
#     arr = len(nums) * [0]
# 
#     while left < right:
#         leftSquared = nums[left] ** 2
#         rightSquared = nums[right] ** 2
# 
#         if leftSquared < rightSquared:
#             arr[index] = rightSquared
#             right -= 1
#         else:
#             arr[index] = leftSquared
#             left += 1
# 
#         index -= 1
# 
#     return arr

# Didn't add the first element to the array because my while conditional wasn't <=
# unlike in palindrome where when you get to the middle, you assume that it's equal to itself, you need to check ALL elements.

# 14/12/2025
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# 
# Example 1:
# 
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# 
# Example 2:
# 
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# 
# Constraints:
# 
#     1 <= nums.length <= 104
#     -104 <= nums[i] <= 104
#     nums is sorted in non-decreasing order.


# Comments:
# sorted! in non-decreasing

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
def sortedSquares_v2(nums):
    left = 0
    right = len(nums) - 1
    arr = len(nums) * [0]
    index = len(nums) - 1

    while left <= right:
        leftVal = nums[left] ** 2
        rightVal = nums[right] ** 2

        if leftVal < rightVal:
            arr[index] = rightVal
            right -= 1

        else:
            arr[index] = leftVal
            left += 1

        index -= 1

    return arr

result = sortedSquares_v2([-7,-3,2,3,11])
print(result)