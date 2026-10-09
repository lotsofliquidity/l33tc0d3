# Linked Lists

## In one sentence
Linked lists are node-based chains where each node stores a value and a pointer to the next node, which makes insertion and deletion at known positions cheap without reindexing the whole structure.

## When to use it
- You need to insert or delete at the front or in the middle without shifting a whole array
- The problem is naturally expressed as “follow next pointers” rather than “access by index”
- You need to merge, reverse, or detect cycles in a chain of nodes
- You want to preserve order while changing the structure around a specific node

## Core idea / invariant
A valid linked list is a sequence of nodes where each node except the last points to the next node, and the tail points to `None` (or some sentinel). The pattern is to keep a few pointers (`prev`, `curr`, `next_node`, `slow`, `fast`) and carefully rewire `curr.next` so the chain stays connected while you move through it. If a pointer is lost, the rest of the list can become unreachable.

## Pattern / template
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# common traversal pattern
prev = None
curr = head
while curr is not None:
    next_node = curr.next
    # mutate / rewire here
    prev = curr
    curr = next_node
```

Typical linked-list patterns:
- Reverse: keep `prev`, move `curr`, and redirect `curr.next = prev`
- Remove node: keep `prev`, then skip `curr` by setting `prev.next = curr.next`
- Insert at front: create a new node and point it to `head`, then set `head = new_node`
- Fast/slow: `slow` moves 1 step, `fast` moves 2; useful for cycle detection and middle-finding
- Dummy head: a fake node before the real head makes front insertion and edge cases easier

## Complexity
- Time: O(n) for scanning, reversing, merging, or detecting a cycle
- Space: O(1) extra for pointer-based algorithms, unless you build a separate structure
- Arrays are better for random access; lists are better for pointer rewiring and order-preserving edits

## Pitfalls
- Losing the head by overwriting `head` before saving the old node
- Rewiring `curr.next` before copying `curr.next` to a temp variable
- Forgetting to handle `head is None` or a single-node list
- Accidentally creating a cycle by pointing a node back into the list
- Using index-based reasoning on a list that has no random access

## Tiny example
Start with `1 -> 2 -> 3 -> None` and remove `2`:

- `prev = 1`, `curr = 2`
- Save `next_node = curr.next` (which is `3`)
- Set `prev.next = next_node`
- Result: `1 -> 3 -> None`

The important part is that `2` is removed by changing the pointer before it, not by shifting values.

## Shared helpers
[`linked_list.py`](linked_list.py) holds the node type and the test plumbing, so practice files don't re-declare it:

| Helper | Does |
|---|---|
| `build(values)` | `[1, 2, 3]` → head |
| `to_list(head)` | head → `[1, 2, 3]` (raises instead of hanging on a cycle) |
| `clone(head)` | fresh copy, so a case can be re-run after a solution mutates it |
| `build_cycle(values, pos)` | tail links back to index `pos` — for 141 / 142 |

Header for a practice file (the `annotations` line is needed on Python 3.9):

```python
from __future__ import annotations

import sys
from pathlib import Path

_CHAPTER = next(p for p in Path(__file__).resolve().parents if (p / "linked_list.py").exists())
sys.path.append(str(_CHAPTER))

from linked_list import ListNode, build, to_list
```

`examples/` copies stay standalone on purpose — they keep their own `ListNode` like the course wrote it.

## Related
- Sibling pattern: two pointers / fast-slow pointers are often used with linked lists
- Not the same as arrays: arrays support O(1) index access, but linked lists are better for structural edits
- Often paired with stacks, queues, and trees when you need careful pointer manipulation
