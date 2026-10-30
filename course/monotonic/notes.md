# Monotonic stacks & queues

## In one sentence
A stack or deque that is **always sorted**: before you push, you pop everything that would break the order — so the answer to "next greater / next smaller" or "current window max/min" is always sitting at a known end, in O(n).

## When to use it
- "For each element, find the **next** (or previous) greater / smaller element."
- You need the **max or min of a sliding window** that keeps moving.
- "Longest subarray where `max - min <= limit`" → two monotonic deques at once.
- Signal that you need it: the brute force is "scan forward (or backward) from each element until you find something better", i.e. O(n²) with a lot of repeated work.

## Core idea / invariant
**After every push, the container is sorted** (non-increasing or non-decreasing).

The invariant is load-bearing because of *why* popping is safe: if a newer element is at least as good as an older one, the older one can never be the answer for anything that comes later. It is blocked forever, so delete it now.

The course's transitivity argument (Daily Temperatures): if `32` is not warmer than `33`, and `33` is not warmer than `34`, then `32` is not warmer than `34`. So there is no point resolving `34` before you have resolved `33` — resolve the **most recent unresolved** thing first. That is LIFO → a stack.

### "Decreasing" actually means *non-increasing* — log this

The article's terminology note, worth keeping because it changes the pop condition:

> Technically the correct term is **monotonically non-increasing**, not "monotonically decreasing". "Decreasing" implies the elements are *always* decreasing, so `[5, 3, 3, 2]` would be invalid since `3, 3` is not decreasing. In Daily Temperatures we can have equal temperatures in the stack.

So when the article says "monotonic decreasing", read **non-increasing**; "monotonic increasing" means **non-decreasing**. The test is "never increases" / "never decreases", not "always strictly rises/falls".

That's why the operator is a decision, not a style choice:

| Operator | Keeps equal elements? | Order |
|---|---|---|
| `stack[-1] > num` (article's Daily Temperatures) | yes | non-increasing |
| `stack[-1] >= num` | no | strictly decreasing |
| `stack[-1] < num` | yes | non-decreasing |
| `stack[-1] <= num` | no | strictly increasing |

The article's follow-on, verbatim, because it's the part that tells you *when to care*:

> For simplicity, we have used the term "decreasing" because the important part is that the stack is always sorted. However, it's good to understand the difference. If you wanted to implement a monotonic stack that cannot have equal elements, you would simply need to change the less-than/greater-than operator to a less-than or equal to/greater-than or equal to operator, i.e. `>` becomes `>=` and `<` becomes `<=`.

So: **sorted is the requirement; strict vs non-strict is a knob.** Need strict monotonicity (no duplicates in the container)? Flip `>` → `>=` and `<` → `<=` — one character each. Default to non-strict, since duplicate values are common and `[5, 3, 3, 2]` still satisfies "pops happen only when a strictly better element arrives".

## Pattern / template
Base template — pop first, then do the problem logic, then push:

```python
stack = []
for num in nums:
    while stack and stack[-1] > num:   # direction depends on the problem
        stack.pop()
    # logic goes between pop and push
    stack.append(num)
```

Sliding-window (deque of **indices**), three steps per `i`:
1. **Expire** the front if it left the window: `while dq and dq[0] <= i - k: dq.popleft()`
2. **Evict** useless back entries: for a window max, `while dq and nums[dq[-1]] <= nums[i]: dq.pop()`
3. **Push** `i`, then read the answer off the front: `nums[dq[0]]`.

Indices not values, because you must know *when* the extreme falls out of the window. The article writes the expiry as `if dq[0] + k == i` (equivalently `dq[0] == i - k`) — an `if`, not a `while`, because only one index can age out per step. `while dq[0] <= i - k` is the same guard written defensively.

## Complexity
- Time: **O(n) amortised** — the nested `while` looks quadratic, but each element is pushed once and popped at most once.
- Space: **O(n)** for a plain stack; **O(k)** for a monotonic deque over a window of size `k`.

## Pitfalls
- **Storing values instead of indices.** Fine for "next greater value", fatal for "how many days until" and for any window problem — you lose the position, so you can't compute a distance or know what expired.
- **Inverted direction.** Keep a *decreasing* stack when hunting for the next *greater* element (the top is the smallest unresolved value, waiting for something bigger). Get it backwards and nothing ever pops.
- **Reading the front before expiring.** Evict out-of-window indices first, otherwise the stale max/front is returned.
- **Using one deque for both max and min.** Example 3 needs *two* — one non-increasing, one non-decreasing.
- **Reaching for a stack when the window moves.** A window removes from the left and adds to the right, so you need a **deque**; a stack only has one working end.
- Ambiguous `>` / `>=` — decide whether equals survive, on purpose.

## Tiny example
Daily Temperatures, `temps = [40, 35, 32, 37, 50]`, stack holds indices, kept non-increasing by temperature:

| i | temp | pop while `temps[top] < temp` | answer | stack after |
|---|---|---|---|---|
| 0 | 40 | — | | `[0]` |
| 1 | 35 | — | | `[0, 1]` |
| 2 | 32 | — | | `[0, 1, 2]` |
| 3 | 37 | `2`, `1` | `ans[2] = 1`, `ans[1] = 2` | `[0, 3]` |
| 4 | 50 | `3`, `0` | `ans[3] = 1`, `ans[0] = 4` | `[4]` |

`ans = [4, 2, 1, 1, 0]`. Note `32` and `35` both exit on day 3 — one pass resolved two elements, which is why it beats brute force.

Sliding window maximum, `nums = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`, deque holds indices of a non-increasing run of values; the front is the window max:

| i | num | deque after expire + evict + push | window max |
|---|---|---|---|
| 0 | 1 | `[0]` | |
| 1 | 3 | `[1]` | |
| 2 | -1 | `[1, 2]` | 3 |
| 3 | -3 | `[1, 2, 3]` | 3 |
| 4 | 5 | `[4]` | 5 |
| 5 | 3 | `[4, 5]` | 5 |
| 6 | 6 | `[6]` | 6 |
| 7 | 7 | `[7]` | 7 |

`[3, 3, 5, 5, 6, 7]`. At `i = 4`, `5` evicted `3, -1, -3` from the back — they came earlier *and* are smaller, so they can never be a max again.

## Related
- [../stacks/notes.md](../stacks/notes.md) and [../queues/notes.md](../queues/notes.md) — monotonic is a *discipline* on top of those two, not a new structure.
- [../arrays-and-strings/sliding-window/notes.md](../arrays-and-strings/sliding-window/notes.md) — monotonic deque is the "max/min per window" upgrade to the plain window.
- **Not** for: k-th largest (use a heap), or anything needing the middle of the sorted order.
