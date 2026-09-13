# Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. 
# This problem is similar to Two Sum. (In Two Sum, the input is not sorted).
# For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
# Note: a similar version of this problem can be found on LeetCode: 167. Two Sum II - Input Array Is Sorted

def check_for_target_v1(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        # curr is the current sum
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1
    
    return False

result = check_for_target_v1([1, 2, 4, 6, 8, 9, 14, 15], 13)
print(result)

# 14/12/2025
# Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. 
# This problem is similar to Two Sum. (In Two Sum, the input is not sorted).
# For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
# Note: a similar version of this problem can be found on LeetCode: 167. Two Sum II - Input Array Is Sorted

# since it's sorted, we can assume if the right is larger than k, we can move the right down.
### First Attempt ### - cooked it
# def check_for_target(nums, k):
#     left = 0
#     right = len(nums) - 1

#     while left <= right:

        

#         if nums[right] > k:
#             right -= 1
        
#         else:
#             left += 1

### Second Attempt ###
def check_for_target_v2(nums, k):
    left = 0
    right = len(nums) - 1
    curr = 0

    while left < right:
        curr = nums[left] + nums[right]

        if curr == k:
            return True

        if curr > k:
            right -= 1

        else:
            left += 1

    return False

result = check_for_target_v2([1, 2, 4, 6, 8, 9, 14, 15], 13)
print(result)

# <='s not allowed because the problem requires a pair of distinct numbers.

# 17/12/2025
# Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. 
# This problem is similar to Two Sum. (In Two Sum, the input is not sorted).
# For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
# Note: a similar version of this problem can be found on LeetCode: 167. Two Sum II - Input Array Is Sorted

### First Attempt ###
def check_for_target_v3(nums, target):
    # two pointers
    # sorted means we know that if the right most element is > target then we can move it left

    left = 0
    right = len(nums) - 1
    
    while left < right:
        if nums[left] + nums[right] == target:
            return True
        
        if nums[right] > target:
            right -= 1
        else:
            left += 1
    
    return False


# Compare to the first with internet #
result = check_for_target_v3([1, 2, 4, 6, 8, 9, 14, 15], 0)
print(result)

def check_for_target_v4(nums, target):
    left = 0
    right = len(nums) - 1
    curr = 0

    while left < right:
        curr = nums[left] + nums[right]

        if curr == target:
            return True
        
        if curr > target:
            right -= 1
        else:
            left += 1

    return False

result = check_for_target_v4([1, 2, 4, 6, 8, 9, 14, 15], 21)
print(result)