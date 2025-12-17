# Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

def combine_two_sorted_arrays(arr1, arr2):
    # ans is the answer
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
    
    return ans


# 14/12/2025
# Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

### First Attempt ###
def combine_two_sorted_arrays_v2(arr1, arr2):
    i = j = 0
    arr = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1


    while i < len(arr1):
        arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        arr.append(arr2[j])
        j += 1

    return arr


result = combine_two_sorted_arrays_v2([1, 2, 3, 4, 5, 6], [4, 6, 8])
print(result)


# 17/12/2025
# Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

def combine_two_sorted_arrays_v3(arr1, arr2):
    # need two iterables, one for each array
    i = j = 0
    arr = []
    while i < len(arr1) and j < len(arr2): # means one or both of the arrays have been exhausted

        # arr1 = [1, 8]
        # arr2 = [8, 3]
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1

        
    
    while i < len(arr1):
        arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        arr.append(arr2[j])
        j += 1

    return arr

# Notes during implementation
    # If working with while loops ensure you have incremented or decremented when required
    # ensure the syntax for appending is correct 
result = combine_two_sorted_arrays_v3([1, 2, 3, 4, 5, 6], [4, 6, 8])
print(result)
