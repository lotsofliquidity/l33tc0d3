"""
Problem: Maximum Twin Sum of a Linked List (LeetCode 2130)
Chapter: Linked Lists / reversing a linked list

In a linked list of size n, where n is even, the ith node (0-indexed) of the
linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
The twin sum is the sum of a node and its twin. Return the maximum twin sum.

Example 1:
  Input: head = [5,4,2,1]
  Output: 6
  (Twin sums: 5+1 = 6, 4+2 = 6)

Example 2:
  Input: head = [4,2,2,3]
  Output: 7
  (Twin sums: 4+3 = 7, 2+2 = 4)

Example 3:
  Input: head = [1,100000]
  Output: 100001

Constraints:
  2 <= number of nodes <= 10^5
  n is even
  1 <= Node.val <= 10^5
"""

from __future__ import annotations

import sys
from pathlib import Path

_CHAPTER = next(p for p in Path(__file__).resolve().parents if (p / "linked_list.py").exists())
sys.path.append(str(_CHAPTER))

from linked_list import ListNode, build, to_list


class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        pass
