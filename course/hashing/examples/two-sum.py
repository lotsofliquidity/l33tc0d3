# Look through nums to see which two indexs will makeup the target number

def twoSum(nums, target):
    # target = 8
    # nums = [5, 2, 7, 19, 3, 9]
    seen = {}
    
    for i in range(len(nums)):
        num = nums[i] 
        # 5

        complement = target - num
        #   3     =    8   -   5        
        if complement in seen:
            return[i, seen[complement]]
        
        seen[num] = i

    return [-1, -1]



print(twoSum([5, 2, 7, 19, 3, 9], 5))