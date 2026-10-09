# Reversing a linked list

## In one sentence
Flip every `next` pointer so the chain runs backwards, using a small fixed set of pointers (`prev`, `curr`, `next_node`) and no extra memory.

## When to use it
- The problem is literally "return the list reversed" (206).
- You need the second half backwards — e.g. twin sums, palindrome checks — so you reverse half and walk both ends inward.
- You need to rewire a small neighbourhood of nodes (swap pairs, reverse in groups of `k`), which is the same three-pointer dance on a local segment.
- You need O(1) extra space; turning the list into an array is the easy way out and usually not the intended answer.

## Core idea / invariant
At the top of each iteration, everything up to and including `curr` is already reversed, `prev` is the new head of that reversed part, and `curr`'s original `next` chain is untouched and still reachable. The single step `curr.next = prev` is what advances that invariant; `next_node` exists purely so you can still get to the untouched part after the pointer flips.

## Pattern / template
```python
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev, curr = None, head
        while curr:
            next_node = curr.next   # save before rewiring
            curr.next = prev
            prev = curr
            curr = next_node
        return prev                 # prev is the new head
```
Same move, local to one pair `A -> B` (swap nodes in pairs):
1. `next_node = A.next.next` — save `C`, else the rest of the list is lost.
2. `A.next.next = A` — makes `B` point back at `A`.
3. `prev = A` — remember `A` so it can be attached to the next pair later.
4. `head = next_node` — move to `C`.
5. `prev.next = head.next` — connect `A` to the node after the next pair (this is what overrides the temporary `A.next = C`).

## Complexity
- Time: O(n) — the loop runs n times, O(1) work per iteration.
- Space: O(1) — a few pointers, no new list and no array.

## Pitfalls
- Setting `curr.next = prev` before saving `curr.next` → the rest of the list is unreachable.
- Flipping without advancing (no `prev = curr; curr = next_node`) → the next pass re-flips the same node and never terminates. This is where 206 stalled.
- Returning `curr` instead of `prev` — after the loop `curr` is `None`; `prev` is the new head.
- Forgetting `head is None` / single node (the loop handles it, but the return value must still be `prev`, which is `None`/the node).
- Loop guard too loose: any body using `head.next.next` needs `while head and head.next`, or you crash on a 1-node tail.
- Keeping `A.next -> B` after a pair swap — `A` must point to the node *after* the pair, or you keep a two-node cycle.
- Losing the answer when it is not the original head: save it in a `dummy` node up front.

## Tiny example
`1 -> 2 -> 3 -> 4`, reverse it. `curr` and `next_node` are read at the top of the body; `list` is the state right after the flip.

| # | `curr` | `next_node` | after `curr.next = prev` | then `prev` | then `curr` |
|---|---|---|---|---|---|
| 1 | 1 | 2 | `1 -> None` | 1 | 2 |
| 2 | 2 | 3 | `2 -> 1 -> None` | 2 | 3 |
| 3 | 3 | 4 | `3 -> 2 -> 1 -> None` | 3 | 4 |
| 4 | 4 | None | `4 -> 3 -> 2 -> 1` | 4 | None → loop ends |

Return `prev` → `4 -> 3 -> 2 -> 1`.

The list is always split in two lanes, and both move right every iteration:

```
None <- 1 <- 2   |   3 -> 4 -> None
        prev      curr/next_node

reversed prefix   |   untouched suffix  (reachable only via next_node)
```

## Related
- Fast and slow pointers (`fast-and-slow-pointers/notes.md`) — used to *find* the middle before reversing half of it.
- Dummy head — the standard trick when the node you must return is no longer `head` (e.g. swap pairs returns the old second node).
- Not the same as arrays: this is the one place pointers beat indexing, because reversal needs no extra storage.
- Reversal in groups of `k` / reverse between positions is the same loop with a saved "tail of the previous segment".
