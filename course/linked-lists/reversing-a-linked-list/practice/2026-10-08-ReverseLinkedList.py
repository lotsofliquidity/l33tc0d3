"""
Problem: Reverse Linked List (LeetCode 206)
Chapter: Linked Lists / reversing a linked list

Solution written after the 10-minute stop on 2026-10-08. Cold revisit due
2026-10-15 — re-solve before opening this file.

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

Constraints:
  0 <= number of nodes <= 5000
  -5000 <= Node.val <= 5000
"""

from __future__ import annotations

import sys
from pathlib import Path

_CHAPTER = next(p for p in Path(__file__).resolve().parents if (p / "linked_list.py").exists())
sys.path.append(str(_CHAPTER))

from linked_list import ListNode, build, to_list


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head

        # 1 -> 2 -> 3 -> 4
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.reverseList(build([1, 2, 3, 4, 5]))))  # [5, 4, 3, 2, 1]
    print(to_list(sol.reverseList(build([1, 2]))))            # [2, 1]
    print(to_list(sol.reverseList(build([]))))                 # []



