"""
Problem: Swap Nodes in Pairs (LeetCode 24)
Chapter: Linked Lists / reversing a linked list
Source: **reference copy — NOT an attempt.** The solution was walked through in
        session 2026-10-09 and typed in here to study from; the failure trace
        (the two-node cycle, the missing return) is in the comments below the
        imports. The same code is indexed in SOLUTIONS.md via
        ../examples/swap-nodes-in-pairs.py, so this file is the duplicate.

Do not open this file for the cold revisit on 2026-10-20 — that check only
measures what you can rebuild from scratch.

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

# start                     list=2 -> 3 -> 4            prev=None head=1
# head.next.next = head     list=2 -> 1 -> *CYCLE*      prev=1  head=1
# head.next = next_node     list=2 -> 1 -> 3 -> 4       prev=1  head=1
# ...
# prev.next = head.next     list=2 -> 1 -> 4            prev=1  head=3      ← 3 detached
# head.next.next = head     list=2 -> 1 -> 4 -> 3 -> *CYCLE*  prev=3  head=3
# head.next = next_node     list=2 -> 1 -> 4 -> 3       prev=3  head=3

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 0 or 1 nodes: nothing to pair up
        if not head or not head.next:
            return head

        # A -> B -> C -> D
        # `dummy` holds the node to return. After the first swap the front of the
        # list is B, not A, so this is the only handle on the answer.
        dummy = head.next               # B - this become the new head because A and B will be swapped
        prev = None                     # tail of the swapped part; nothing swapped yet

        # a full pair A -> B has to exist
        while head and head.next:
            # from the 2nd pass on: the previous pair's A must point at B
            if prev:
                prev.next = head.next

            prev = head                 # A becomes the tail of the finished part

            next_node = head.next.next  # C — save it, or the rest is unreachable

            # flip the pair: B -> A. A still points at B, so A <-> B is a
            # two-node cycle until the next line breaks it.
            head.next.next = head
            head.next = next_node       # A -> C — rest of the list reachable again

            head = next_node            # move to C, front of the next pair

        return dummy





        


if __name__ == "__main__":
    print(to_list(Solution().swapPairs(build([1, 2, 3, 4]))))
    # expected: [2, 1, 4, 3]
