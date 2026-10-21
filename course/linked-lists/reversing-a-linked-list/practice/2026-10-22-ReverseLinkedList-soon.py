"""
Problem: Reverse Linked List (LeetCode 206)
Chapter: Linked Lists / reversing a linked list
Source: soon-move rebuild for entry #16 (cold revisit due 2026-10-29).

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

Soon move (~15 min): chapter notes OK. Attempt first — then you may open
examples/reverse-linked-list.py. After that, close everything and re-derive
closed-book into this file (or a fresh pass).

Visual aid (keep for later — understanding can lag the working code):
  - Cursor canvas: reverse-linked-list (Play / Step)
  - In-repo walkthrough: ../reverse-linked-list-walkthrough.md
"""

from __future__ import annotations

import sys
from pathlib import Path

_CHAPTER = next(p for p in Path(__file__).resolve().parents if (p / "linked_list.py").exists())
sys.path.append(str(_CHAPTER))

from linked_list import ListNode, build, to_list


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None   # front of the reversed chain (None = empty new chain)
        curr = head   # front of what is still left to reverse

        # Each loop iteration moves ONE node from the old chain onto the new chain.
        # Trace for [1, 2, 3]:
        #
        #   start:     prev = None          curr = 1 -> 2 -> 3
        #
        #   pass 1:    take 1
        #              next_node = 2 -> 3
        #              1.next = None        →  1
        #              prev = 1             →  1
        #              curr = 2 -> 3
        #
        #   pass 2:    take 2
        #              next_node = 3
        #              2.next = 1           →  2 -> 1
        #              prev = 2             →  2 -> 1
        #              curr = 3
        #
        #   pass 3:    take 3
        #              next_node = None
        #              3.next = 2           →  3 -> 2 -> 1
        #              prev = 3             →  3 -> 2 -> 1
        #              curr = None  → loop ends
        #
        while curr:
            next_node = curr.next  # save the old chain before we break the link
            curr.next = prev       # move this node onto the new chain
            prev = curr            # it is now the front of the new chain
            curr = next_node       # continue with whatever is still unreversed

        return prev  # when curr is None, prev is the whole answer







if __name__ == "__main__":
    print(to_list(Solution().reverseList(build([1, 2, 3, 4, 5]))))
    # expected: [5, 4, 3, 2, 1]
    print(to_list(Solution().reverseList(build([1, 2]))))
    # expected: [2, 1]
    print(to_list(Solution().reverseList(build([]))))
    # expected: []
