"""
Problem: Next Greater Element I (LeetCode 496)
Chapter: Monotonic

For each value in nums1, find the first greater value to its right in nums2.
Return -1 when no greater value exists.
"""


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        for num in stack:
            next_greater[num] = -1

        return [next_greater[num] for num in nums1]


if __name__ == "__main__":
    print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
    # expected: [-1, 3, -1]
    print(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]))
    # expected: [3, -1]
