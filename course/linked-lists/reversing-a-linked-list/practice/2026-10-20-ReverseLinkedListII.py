"""
Problem: Reverse Linked List II (LeetCode 92)
Chapter: Linked Lists / reversing a linked list

Given the head of a singly linked list and two integers left and right where
left <= right, reverse the nodes of the list from position left to position
right, and return the reversed list.

Example 1:
  Input: head = [1,2,3,4,5], left = 2, right = 4
  Output: [1,4,3,2,5]

Example 2:
  Input: head = [5], left = 1, right = 1
  Output: [5]

Constraints:
  The number of nodes in the list is n.
  1 <= n <= 500
  -500 <= Node.val <= 500
  1 <= left <= right <= n

Follow up: Could you do it in one pass?
"""

from __future__ import annotations

import sys
from pathlib import Path

_CHAPTER = next(p for p in Path(__file__).resolve().parents if (p / "linked_list.py").exists())
sys.path.append(str(_CHAPTER))

from linked_list import ListNode, build, to_list


class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        
        # Linkedlist problem similar to reversing a singly linkedlist
        curr = head
        prev = None
        position = 1

        if not curr.next:
          return head

        while curr and curr.next:
          if position >= left and position <= right:
            # flip the nodes.
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
          position += 1
        return head





if __name__ == "__main__":
    print(to_list(Solution().reverseBetween(build([1, 2, 3, 4, 5]), 2, 4)))
    # expected: [1, 4, 3, 2, 5]
    print(to_list(Solution().reverseBetween(build([5]), 1, 1)))
    # expected: [5]
