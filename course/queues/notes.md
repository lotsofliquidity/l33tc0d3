# Queues

## In one sentence
An ordered collection where you add at one end and remove from the other — first in, first out (FIFO).

## When to use it
- The oldest pending item is the next one resolved: printer jobs, ticket lines, "process arrivals in order".
- An **expiring window**: "how many calls in the last 3000 ms" — drop the front as items age out.
- You only ever need the two ends — push at the back, look at / remove from the front.
- **BFS** (trees & graphs chapter) is the big one: a queue is what makes BFS level-by-level.

## Core idea / invariant
Add at the **back**, remove from the **front**; the front element is the one that has waited longest. FIFO holds at every step.

The same point as with stacks: a queue is an **interface**, not a data structure. Whatever gives O(1) add-at-back / remove-at-front is a queue.

Implementation choices the article covers:
- **Dynamic array** — works, but `pop(0)` / `insert(0, x)` are O(n), so front operations drag the whole thing to O(n).
- **Doubly linked list with head + tail** (usually sentinel nodes) — O(1) at both ends.
- **Deque** ("deck", double-ended queue) — add or delete at *either* end; a plain queue is the restricted case (add one end, delete the other).

In Python: `collections.deque` is the queue, not `list`.

## Pattern / template
Python interface:

```python
from collections import deque

queue = deque()
queue.append(x)      # enqueue — back
queue.popleft()      # dequeue — front, O(1)
queue[0]             # peek at the front
not queue            # empty check
```

Expiring-window shape (the article's `RecentCounter`):

1. Receive the new item / timestamp.
2. While the front is out of range, `popleft` it — expired items are gone for good, no future call can need them.
3. Enqueue the new item.
4. The queue now holds exactly the live set — often the answer is just `len(queue)`.

## Complexity
- Enqueue / dequeue / peek with `deque`: **O(1)**.
- `list.pop(0)` or `list.insert(0, x)`: **O(n)** — the trap above.
- Space: O(n) overall; O(window) for the expiring-window pattern, since expired items are discarded.

## Pitfalls
- Using a `list` as a queue — correct, but `pop(0)` makes every dequeue O(n), so the whole loop goes quadratic.
- Removing from the same end you add to — that's a stack, and the FIFO promise is silently broken.
- Expiring **after** measuring, or using `<=` instead of `<`: the boundary value `t - 3000` is still inside the window, so drop only `< t - 3000`.
- Reaching for a queue when the thing that resolves next is the *most recent* one — that's LIFO, take a stack.
- Indexing into the middle of the queue — the contract is the two ends only.

## Tiny example
`RecentCounter`, window 3000, pings at `1, 100, 3001, 3002`:

| ping | threshold `t - 3000` | dropped | queue | return |
|---|---|---|---|---|
| 1 | — | — | `[1]` | 1 |
| 100 | — | — | `[1, 100]` | 2 |
| 3001 | 1 | nothing (`1` is not `< 1`) | `[1, 100, 3001]` | 3 |
| 3002 | 2 | `1` | `[100, 3001, 3002]` | 3 |

Each ping is enqueued once and dequeued at most once → O(1) amortised per call.

Plain FIFO: `append(1), append(2), append(3)` → `popleft()` gives `1, 2, 3`.

## Related
- Stacks: [../stacks/notes.md](../stacks/notes.md) — same "collection of pending work", opposite end rule (LIFO vs FIFO).
- BFS in trees & graphs — queues exist mostly to power it.
- Monotonic (next chapter) — applies to both stacks and queues.
