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

Constraints:
  The number of nodes in the list is the range [0, 5000].
  -5000 <= Node.val <= 5000

Cold revisit: 2026-10-15 (logged #16, due today). No notes, no lookups.
"""

from __future__ import annotations

import sys
from pathlib import Path

_CHAPTER = next(p for p in Path(__file__).resolve().parents if (p / "linked_list.py").exists())
sys.path.append(str(_CHAPTER))

from linked_list import ListNode, build, to_list



# variable	what it is
# prev	front of the new chain (None while empty — and None is exactly "the front of an empty chain")
# curr	first node still on the old chain — the next one to move
# next_node	second node of the old chain, noted before you lift curr off, because lifting severs the link
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head

        while curr:
            # A -> B -> C -> D
            next_node = head.next
            # next_node is B
            head.next = prev
            # head.next is none
            # A -> B -> D -> D
            prev = curr
            # prev is A - swapping is completed

            curr = next_node
            # curr is B
            

            


            


            
            


if __name__ == "__main__":
    print(to_list(Solution().reverseList(build([1, 2, 3, 4, 5]))))
    # expected: [5, 4, 3, 2, 1]
    print(to_list(Solution().reverseList(build([1, 2]))))
    # expected: [2, 1]
    print(to_list(Solution().reverseList(build([]))))
    # expected: []
