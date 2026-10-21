"""
Problem: Reverse Linked List (LeetCode 206)
Chapter: Linked Lists / reversing a linked list

Given the head of a singly linked list, reverse the list, and return the
reversed list.

Example 1:
  Input: head = [1,2,3,4,5]
  Output: [5,4,3,2,1]

Example 2:
  Input: head = [1,2]
  Output: [2,1]

Example 3:
  Input: head = []
  Output: []

Cold revisit: 2026-10-22 (logged #16, due today). No notes, no lookups.
"""

from __future__ import annotations

import sys
from pathlib import Path

_CHAPTER = next(p for p in Path(__file__).resolve().parents if (p / "linked_list.py").exists())
sys.path.append(str(_CHAPTER))

from linked_list import ListNode, build, to_list


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr = head
        prev = None
        
        while curr:
          next_node = head.next
          # next_node = 2
          head.next = prev
          # prev = 2
          prev = curr
          curr = next_node

        return prev



if __name__ == "__main__":
    print(to_list(Solution().reverseList(build([1, 2, 3, 4, 5]))))
    # expected: [5, 4, 3, 2, 1]
    print(to_list(Solution().reverseList(build([1, 2]))))
    # expected: [2, 1]
    print(to_list(Solution().reverseList(build([]))))
    # expected: []
