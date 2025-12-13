# Example 1: Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k. 
# This is the problem we have been talking about above. We will now formally solve it.

# nums = [3, 1, 2, 7, 4, 2, 1, 1, 5] and k = 8.

def find_length(nums, k):
    leftBound = curr = ans = 0
    for rightBound in range(len(nums)):
        curr += nums[rightBound]
        # [3, 1, 2, 7, 4, 2, 1, 1, 5]
        # [3, 1, 2] - longest so far
        # curr = 6

        # [3, 1, 2, 7]
        # curr = 13
        # proceeds to while loop 

        while curr > k:
            # [3, 1, 2, 7] > 8
            # Move the left bound up and decrease the curr by the value
            curr -= nums[leftBound]
            leftBound += 1

        # for each loop of the for loop, the answer of the longest substring is captured in this ans var
        ans = max(ans, rightBound - leftBound + 1)
    return ans

result = find_length([3, 1, 2, 7, 4, 2, 1, 1, 5], 8)
print(result)