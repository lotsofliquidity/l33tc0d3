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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        
        dummy = head
        
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else: 
                head = head.next
                
        return dummy
        


def build(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head):
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.deleteDuplicates(build([1, 1, 2]))))            # [1, 2]
    print(to_list(sol.deleteDuplicates(build([1, 1, 2, 3, 3]))))      # [1, 2, 3]
    print(to_list(sol.deleteDuplicates(build([]))))                   # []
