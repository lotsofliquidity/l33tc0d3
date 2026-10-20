"""
Problem: Reverse Linked List II (LeetCode 92)
Chapter: Linked Lists / reversing a linked list
Source: session solution 2026-10-20. The course has no copy of this problem.

Companion file: ../practice/2026-10-20-ReverseLinkedListII.py is the attempt.
Recursive alternate (LeetCode editorial, value-swaps): reverse-linked-list-ii-recursive.py.

Idea: the full-list reverse, limited to the stretch from position left through
      right. Walk to the real node just before the stretch (there is none when
      left is 1), reverse only (right - left + 1) nodes with the usual
      prev / curr / next_node dance, then stitch both ends back on. `dummy`
      is the existing node to return: the original head, or the front of the
      stretch when left is 1.

Example 1:
  Input: head = [1,2,3,4,5], left = 2, right = 4
  Output: [1,4,3,2,5]
Example 2:
  Input: head = [5], left = 1, right = 1
  Output: [5]
"""

from __future__ import annotations

import sys
from pathlib import Path

_CHAPTER = next(p for p in Path(__file__).resolve().parents if (p / "linked_list.py").exists())
sys.path.append(str(_CHAPTER))

from linked_list import ListNode, build, to_list


class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = head  # existing front; still the answer unless left is 1
        # before is the real node just left of the stretch. None when left is 1,
        # because the original head is inside the stretch and will not be returned.
        before = None
        if left == 1:
            curr = head
        else:
            before = head
            for _ in range(left - 2):
                before = before.next
            curr = before.next

        tail = curr  # old front of the stretch, becomes its new end
        prev = None
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        tail.next = curr  # node that followed the stretch
        if before is None:
            dummy = prev
        else:
            before.next = prev
        return dummy


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.reverseBetween(build([1, 2, 3, 4, 5]), 2, 4)))  # [1, 4, 3, 2, 5]
    print(to_list(sol.reverseBetween(build([5]), 1, 1)))              # [5]
    print(to_list(sol.reverseBetween(build([5, 6, 7]), 1, 2)))        # [6, 5, 7]
    print(to_list(sol.reverseBetween(build([1, 2, 3, 4, 5]), 1, 5)))  # [5, 4, 3, 2, 1]
