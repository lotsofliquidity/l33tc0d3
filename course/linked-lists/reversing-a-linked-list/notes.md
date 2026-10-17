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
Read the reverse body as moving the first node of the *old* chain onto the front of a
*new* chain: `curr.next = prev` performs the move, `prev = curr` says the moved node is
the new chain's front, `curr = next_node` steps to the first node still on the old chain.
When the old chain runs out (`curr is None`), `prev` is the entire new chain — which is
why the answer is `prev` and not `curr`.

The order of those four lines is forced by data flow, not taste: line 1 exists only
because line 2 destroys `curr.next`; line 2 is the only line that changes the list;
line 3 must follow it (the other order makes `curr.next = curr`, a self-loop); line 4 must
be last because it is the only line that still needs the old `curr`.

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
- **Why the four lines can't be reordered** — each swap breaks it a different way:
  - flip before saving → the untouched part becomes unreachable
  - `prev = curr` before the flip → `curr.next = curr`, a one-node cycle
  - `curr = next_node` before `prev = curr` → `prev` lands on the *unprocessed* node, so the return value is wrong
- **The guard belongs to the pattern.** Plain reversal walks with `while curr:` — a 1-node list still qualifies. `while head and head.next` is the *pair-swap* guard; writing it into a reversal means the loop never starts (2026-10-15).
- **The names are positional, not role-based.** `prev`/`curr` say *where you are in the walk*; the jobs they do are "front of the list I'm building" (`prev` = `new_head`) and "front of the list I'm consuming" (`curr`). That mismatch is part of why reversal reads as bookkeeping. Positional names also collapse once a problem needs three or four live pointers (swap pairs) — that's the signal to name by role. Minor Python point: `next` is a builtin, so the temp is `next_node`/`nxt`.
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

## Self-test (before the cold revisit)
Answer out loud, no code open:
1. Why is `next_node` saved *before* the flip, and not after?
2. What is `prev` on the first pass, and why is that the correct value?
3. When the loop ends, where does `curr` point — and why must you return `prev`?
4. Move `prev = curr` above `curr.next = prev`. What breaks?

## Related
- Fast and slow pointers (`fast-and-slow-pointers/notes.md`) — used to *find* the middle before reversing half of it.
- Dummy head — the standard trick when the node you must return is no longer `head` (e.g. swap pairs returns the old second node).
- Not the same as arrays: this is the one place pointers beat indexing, because reversal needs no extra storage.
- Reversal in groups of `k` / reverse between positions is the same loop with a saved "tail of the previous segment".
