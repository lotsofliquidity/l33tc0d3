"""
Problem: Remove Duplicates from Sorted List (LeetCode 83)
Chapter: Linked Lists

Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.

Example 1:
  Input: head = [1,1,2]
  Output: [1,2]

Example 2:
  Input: head = [1,1,2,3,3]
  Output: [1,2,3]

Constraints:
  0 <= number of nodes <= 300
  -100 <= Node.val <= 100
  The list is guaranteed to be sorted in ascending order.
"""

from __future__ import annotations

import sys
from pathlib import Path

_CHAPTER = next(p for p in Path(__file__).resolve().parents if (p / "linked_list.py").exists())
sys.path.append(str(_CHAPTER))

from linked_list import ListNode, build, to_list


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        
        dummy = head
        
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else: 
                head = head.next
                
        return dummy
        


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.deleteDuplicates(build([1, 1, 2]))))            # [1, 2]
    print(to_list(sol.deleteDuplicates(build([1, 1, 2, 3, 3]))))      # [1, 2, 3]
    print(to_list(sol.deleteDuplicates(build([]))))                   # []
