"""
Problem: Swap Nodes in Pairs (LeetCode 24)
Chapter: Linked Lists / reversing a linked list
Source: course article walkthrough (swap one pair at a time with prev/head/
        dummy), written up as runnable code in session 2026-10-09.

Companion file: ../practice/2026-10-09-SwapNodesInPairs.py is the attempt.

Idea: relink each pair A -> B into B -> A while keeping the rest of the list
      reachable. `dummy` holds the node to return (the old second node, which
      is no longer the list head); `prev` is the last node of the already
      finished part, so it can attach to B while A points at whatever follows
      the pair. The loop needs two nodes, so an odd tail is left in place.

Example 1:
  Input: head = [1,2,3,4]
  Output: [2,1,4,3]
Example 2:
  Input: head = []
  Output: []
Example 3:
  Input: head = [1]
  Output: [1]
Example 4:
  Input: head = [1,2,3,4,5,6]
  Output: [2,1,4,3,6,5]
"""

from __future__ import annotations

import sys
from pathlib import Path

_CHAPTER = next(p for p in Path(__file__).resolve().parents if (p / "linked_list.py").exists())
sys.path.append(str(_CHAPTER))

from linked_list import ListNode, build, to_list


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)  # keeps the node we must return
        prev = dummy               # tail of the already-swapped part
        while prev.next and prev.next.next:
            first = prev.next          # A
            second = first.next        # B
            first.next = second.next   # A -> C, so the rest stays reachable
            second.next = first        # B -> A
            prev.next = second         # finished part -> B
            prev = first               # A is now the tail of the finished part
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.swapPairs(build([1, 2, 3, 4]))))        # [2, 1, 4, 3]
    print(to_list(sol.swapPairs(build([]))))                  # []
    print(to_list(sol.swapPairs(build([1]))))                 # [1]
    print(to_list(sol.swapPairs(build([1, 2, 3, 4, 5, 6]))))  # [2, 1, 4, 3, 6, 5]
