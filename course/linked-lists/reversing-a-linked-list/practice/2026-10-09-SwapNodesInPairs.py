"""
Problem: Swap Nodes in Pairs (LeetCode 24)
Chapter: Linked Lists / reversing a linked list
Source: course practice (stub)

Given the head of a linked list, swap every pair of adjacent nodes and return
the head of the modified list. You must not modify the values in the nodes
(only the nodes themselves may be changed).

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

Constraints:
  0 <= number of nodes <= 100
  0 <= Node.val <= 100
"""

from __future__ import annotations

import sys
from pathlib import Path

_CHAPTER = next(p for p in Path(__file__).resolve().parents if (p / "linked_list.py").exists())
sys.path.append(str(_CHAPTER))

from linked_list import ListNode, build, to_list


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        pass


if __name__ == "__main__":
    print(to_list(Solution().swapPairs(build([1, 2, 3, 4]))))
    # expected: [2, 1, 4, 3]
