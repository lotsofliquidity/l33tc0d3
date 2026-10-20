"""
Problem: Reverse Linked List II (LeetCode 92) — recursive alternate
Chapter: Linked Lists / reversing a linked list
Source: LeetCode editorial (recursive). Kept as a second approach; the
        pointer-rewiring solution for this problem is reverse-linked-list-ii.py.

This is a recursive solution. It does not rewire `next` pointers. Two walks
share the same nodes: `right_node` advances to position `right` by recursion,
and on the way back `left_node` and `right_node` meet in the middle while
swapping `.val`. The nodes stay in place; only the numbers move. O(n)
call-stack space.

The chapter's preferred shape is still the iterative reverse of the stretch
(prev / curr / next_node). Keep this file for contrast, not as the first
thing to re-derive cold.

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
    def reverseBetween(
        self, head: ListNode | None, left: int, right: int
    ) -> ListNode | None:
        if not head:
            return None

        left_node, right_node = head, head
        stop = False

        def recurseAndReverse(right_node: ListNode | None, left: int, right: int) -> None:
            nonlocal left_node, stop

            # base case. Don't proceed any further
            if right == 1:
                return

            # Keep moving the right pointer one step forward until (right == 1)
            right_node = right_node.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if left > 1:
                left_node = left_node.next

            # Recurse with left and right reduced.
            recurseAndReverse(right_node, left - 1, right - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left_node == right_node or right_node.next == left_node:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers
            if not stop:
                left_node.val, right_node.val = right_node.val, left_node.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left_node = left_node.next

        recurseAndReverse(right_node, left, right)
        return head


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.reverseBetween(build([1, 2, 3, 4, 5]), 2, 4)))  # [1, 4, 3, 2, 5]
    print(to_list(sol.reverseBetween(build([5]), 1, 1)))              # [5]
    print(to_list(sol.reverseBetween(build([5, 6, 7]), 1, 2)))        # [6, 5, 7]
    print(to_list(sol.reverseBetween(build([1, 2, 3, 4, 5]), 1, 5)))  # [5, 4, 3, 2, 1]
