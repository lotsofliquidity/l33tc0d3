"""
Problem: Squares of a Sorted Array
Difficulty: Easy
Session: interview companion
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        index = len(nums) - 1
        arr = [0] * len(nums)

        while left <= right:
            leftVal = nums[left] ** 2
            rightVal = nums[right] ** 2

            if leftVal < rightVal:
                # Back filling
                arr[index] = rightVal
                right -= 1
            else:
                arr[index] = leftVal
                left += 1
            index -= 1
        return arr


# Quick manual checks (optional)
if __name__ == "__main__":
    s = Solution()
    print(s.sortedSquares([-4, -1, 0, 3, 10]))
    print(s.sortedSquares([-7, -3, 2, 3, 11]))
