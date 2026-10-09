"""
Shared linked-list plumbing for this chapter.

Paste this header into a practice file instead of re-declaring ListNode and
the build/to_list harness. It finds `linked_list.py` from any depth under
course/linked-lists/ (regular practice/ folders and article subfolders alike):

    from __future__ import annotations

    import sys
    from pathlib import Path

    _CHAPTER = next(p for p in Path(__file__).resolve().parents if (p / "linked_list.py").exists())
    sys.path.append(str(_CHAPTER))

    from linked_list import ListNode, build, to_list

    print(to_list(build([1, 2, 3])))   # [1, 2, 3]

The `annotations` import matters on this machine (Python 3.9): without it,
`ListNode | None` in a signature is evaluated when the class is created.

Your `Solution` class stays exactly as it would be on LeetCode — this module
only supplies the node type and the testing plumbing around it.
"""

from __future__ import annotations

from collections.abc import Iterable


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


# There is deliberately no __eq__: cycle detection compares nodes, and
# structural equality would make `slow == fast` true for distinct nodes.


def build(values: Iterable[int]) -> ListNode | None:
    """Return the head of a list holding `values` (None for an empty input)."""
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head: ListNode | None, max_nodes: int = 10_000) -> list[int]:
    """Return the values as a Python list.

    Raises ValueError past `max_nodes` so a mis-wired pointer shows up as an
    error instead of hanging the test.
    """
    out: list[int] = []
    curr = head
    while curr is not None:
        out.append(curr.val)
        if len(out) > max_nodes:
            raise ValueError(f"stopped after {max_nodes} nodes — the list looks cyclic")
        curr = curr.next
    return out


def clone(head: ListNode | None) -> ListNode | None:
    """Copy the nodes, so a case can be re-run after a solution mutates them."""
    return build(to_list(head))


def build_cycle(values: Iterable[int], pos: int) -> ListNode | None:
    """Build the list and point its tail at index `pos` (-1 for no cycle)."""
    head = build(values)
    if pos < 0 or head is None:
        return head

    seen: list[ListNode] = []
    curr: ListNode | None = head
    while curr is not None:
        seen.append(curr)
        curr = curr.next

    if pos >= len(seen):
        raise ValueError(f"pos={pos} is past the end of a {len(seen)}-node list")

    seen[-1].next = seen[pos]
    return head


if __name__ == "__main__":
    head = build([1, 2, 3, 4])
    print(to_list(head))                      # [1, 2, 3, 4]
    print(to_list(clone(head)))               # [1, 2, 3, 4]

    cycled = build_cycle([1, 2, 3], 1)
    print(cycled.val, cycled.next.next.next.val)   # 1 2  -> tail points back at index 1
    try:
        to_list(cycled)
    except ValueError as exc:
        print("guard works:", exc)
