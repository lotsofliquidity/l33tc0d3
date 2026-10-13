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

Read every line with these roles in your head — the body's only job is to make
`prev.next = B`, `B.next = A` and `A.next = C` true, in an order that never loses `C`:

| pointer | role |
|---|---|
| `prev` | last node of the already-swapped part (the boundary) |
| `A` (`head` in the article) | first node of the pair being swapped |
| `B` (`head.next`) | second node of the pair — becomes the front of this pair |
| `C` (`next_node`) | first node not yet touched |

Same habit for the reverse loop: `prev` = new head of the reversed part, `curr` = first
unprocessed node. If you can't say what each pointer is *for* in words, the body is noise.

1. `next_node = A.next.next` — save `C`, else the rest of the list is lost.
2. `A.next.next = A` — makes `B` point back at `A`.
3. `prev = A` — remember `A` so it can be attached to the next pair later.
4. `head = next_node` — move to `C`.
5. `prev.next = head.next` — connect `A` to the node after the next pair (this is what overrides the temporary `A.next = C`).

Why the join needs *two* fixes: `prev.next = head.next` points the last node of the
finished part at the pair's **second** node (`B`), and the flip `head.next.next = head`
is what closes the pair by pointing `B` back at `A`. In between, the pair's first node
is briefly detached — `head.next = next_node` is what breaks the `A <-> B` cycle that
`A.next.next = A` just created.

```
finished + swapped   |  current pair  |  untouched
2 -> 1               |  3 -> 4        |  None
     prev               head
```

A real dummy node (`ListNode(0, head)`, `prev = dummy`, `while prev.next and prev.next.next`)
removes the first-pair special case entirely — this is the **sentinel shape**; the shape
with `prev = None` and a step 5 (`prev.next = head.next`) is the **front-handle shape**,
and its join lands one iteration later. Only one of the two at a time.

```python
first, second = prev.next, prev.next.next
first.next = second.next   # A -> C
second.next = first        # B -> A
prev.next = second         # finished part -> B   (same iteration)
prev = first               # A is now the last node of the finished part
```

Trace `1 -> 2 -> 3 -> 4` (sentinel), one row per pass:

| pass | `first`,`second` | writes | list | `prev` after |
|---|---|---|---|---|
| start | — | — | `dummy -> 1 -> 2 -> 3 -> 4` | `dummy` |
| 1 | 1, 2 | `1->3`, `2->1`, `dummy->2` | `dummy -> 2 -> 1 -> 3 -> 4` | `1` |
| 2 | 3, 4 | `3->None`, `4->3`, `1->4` | `dummy -> 2 -> 1 -> 4 -> 3` | `3` |
| end | guard fails (`3.next` is `None`) | — | `2 -> 1 -> 4 -> 3` | |

Note pass 2's third write: `1` is re-pointed from `3` to `4`. That is not a bug and it is
not "the join happening twice" — pass 1 pointed `1` at `C` (the pair's *successor*, `3`),
and pass 2 then reveals that `3` was itself the front of the next pair, so the finished
tail has to move to `4`. Both shapes do this; the sentinel shape just does it every pass,
uniformly, instead of only from pass 2 on.

Odd tail, `1 -> 2 -> 3`:

| after | list | `prev` |
|---|---|---|
| start | `dummy -> 1 -> 2 -> 3` | `dummy` |
| iter 1 | `dummy -> 2 -> 1 -> 3` | `1` |
| guard | `prev.next.next` is `3.next` = `None` → stop | `1` |

Return `dummy.next` → `2 -> 1 -> 3`. The odd tail is never entered or repaired: `first.next = second.next` already wired `1 -> 3` in the pass that swapped the pair, and `prev` ends on the last *swapped* node.

## Complexity
- Time: O(n) — the loop runs n times, O(1) work per iteration.
- Space: O(1) — a few pointers, no new list and no array.

## Pitfalls
- Setting `curr.next = prev` before saving `curr.next` → the rest of the list is unreachable.
- Flipping without advancing (no `prev = curr; curr = next_node`) → the next pass re-flips the same node and never terminates. This is where 206 stalled.
- Returning `curr` instead of `prev` — after the loop `curr` is `None`; `prev` is the new head.
- Forgetting `head is None` / single node (the loop handles it, but the return value must still be `prev`, which is `None`/the node).
- Loop guard too loose: any body using `head.next.next` needs `while head and head.next`, or you crash on a 1-node tail.
- After a pair swap `A` must point at the node *after* the pair (`A.next = C`), or you keep a two-node cycle `A <-> B`.
- **Two shapes for pair swapping — pick one and never mix lines between them.** They differ in one place only: *when* the finished part gets attached to the new front `B`.
  - **Sentinel shape** (recommended): `dummy = ListNode(0, head)`, `prev = dummy`, guard `while prev.next and prev.next.next`. Join happens **inside the same iteration** via `prev.next = second`, and every iteration is identical — no first-pair special case.
  - **Front-handle shape** (`practice/2026-10-09-SwapNodesInPairs.py`): `dummy = head.next`, `prev = None`, guard `while head and head.next`, join is the conditional `if prev: prev.next = head.next` **at the top of the next iteration** — one pass late. The first pass has no predecessor, so the loop carries a special case. It's correct (exhaustively checked), just harder to reason about.
- Losing the answer when it is not the original head: save it in a `dummy` node up front.
- In the article's shape the `# Step N` comments are **not** execution order (`# Step 5` runs first, `# Step 6` last) — follow the code, not the numbers.

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
