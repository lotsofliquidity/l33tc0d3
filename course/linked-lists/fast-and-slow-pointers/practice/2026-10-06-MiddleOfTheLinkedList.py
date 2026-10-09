"""
Problem: Middle of the Linked List (LeetCode 876)
Chapter: Linked Lists / fast and slow pointers

Given the head of a singly linked list, return its middle node. If there are
two middle nodes, return the second middle node.

Example 1:
  Input: head = [1, 2, 3, 4, 5]
  Output: [3, 4, 5]

Example 2:
  Input: head = [1, 2, 3, 4, 5, 6]
  Output: [4, 5, 6]

Constraints:
  1 <= number of nodes <= 100
  1 <= Node.val <= 100
"""

from __future__ import annotations

import sys
from pathlib import Path

_CHAPTER = next(p for p in Path(__file__).resolve().parents if (p / "linked_list.py").exists())
sys.path.append(str(_CHAPTER))

from linked_list import ListNode, build, to_list


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        pass
