#    Example 3: 713. Subarray Product Less Than K.
#    Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.
#    For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:
#    [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

# --- This is a different kind of sliding window from what we've done before. ---
#hehe

def numSubarrayProductLessThanK_v1(nums, k):
    if k <= 1: # if value 1 then would loop forever because curr >= k would never be false
        return 0

    ans = left = 0
    curr = 1 # because you can't times by zero

    for right in range(len(nums)):
        curr *= nums[right]

        while  curr >= k:
            curr //= nums[left]
            left += 1

        ans += right - left + 1

    return ans

result = numSubarrayProductLessThanK_v1([10, 5, 2, 6], 100)
print(result)
