# Sliding window

## In one sentence
Maintain a contiguous “window” (`left`…`right`) that slides rightward, growing until invalid and shrinking until valid, so you scan the array once instead of checking every subarray.

## Before you code
1. What’s the **constraint metric**? (sum, product, count of zeros, …)
2. Fixed size `k`, or grow/shrink until valid?
3. Dynamic: `for right` → add → `while` invalid shrink left → update answer.
4. Answer type: `max(length)`, or `ans += length` (count), or max sum then `/k`?
5. Length formula: `right - left + 1`. Types: `0` vs `'0'`.

## When to use it
- Problem talks about **subarrays/substrings** (contiguous) that are **“valid”** under a constraint
- Asks for **best** valid window (longest / shortest / max sum of fixed size) or **count** of valid windows
- Constraint metric can be updated in O(1) when you add/remove one end (sum, product, count of zeros, etc.)
- Same idea works for arrays and strings (both are iterables)

## Core idea / invariant
A **subarray** = contiguous slice; defined by bounds `left` and `right`. A **window** is just that subarray.

**Valid** = constraint metric obeys a numeric rule (e.g. `sum <= k`, `zeros <= 1`, `product < k`).

**Invariant:** after each `right` advance (and any shrinks), the window `[left, right]` is valid (or empty / handled specially). You never re-check every possible left for that right from scratch — you only move `left` forward when the metric breaks.

Why forgetting an element on the left is safe (classic **positive** nums + sum/product constraints): once `[left…right]` is too big, any longer window that still includes that left end stays invalid; and you can’t skip the middle, so that left element is dead for the rest of the scan.

## Pattern / template

### Dynamic window (variable size)

```
left = 0
curr = 0          # constraint metric
answer = 0

for right in range(n):
    # ADD nums[right] into curr
    while WINDOW_INVALID:
        # REMOVE nums[left] from curr
        left += 1
    # window is valid → update answer
    answer = max(answer, right - left + 1)   # length formula
```

- `right` always moves forward (for-loop).
- `left` only moves when invalid (while-loop).
- Length of window: **`right - left + 1`** (memorize).

### Number of valid subarrays (math trick)

When the current window `[left, right]` is valid under a monotone “longer → worse” constraint (e.g. product of positives), **every** subarray ending at `right` with start in `[left, right]` is also valid.

Add **`right - left + 1`** to the answer each time (not just the one longest window).

### Fixed window size `k`

Adjacent windows differ by **two** elements: add `arr[i]`, remove `arr[i - k]`.

```
# build first window [0 .. k-1]
# ans = that window’s metric
for i in range(k, n):
    add arr[i]
    remove arr[i - k]
    update ans
```

## Complexity
- Time: **O(n)** — `right` moves ≤ n times, `left` moves ≤ n times total (**amortized** O(1) per for-iteration even with an inner while)
- Space: **O(1)** for metric as a few ints (later chapters: hashmaps → more space)
- Brute “every subarray”: there are `n(n+1)/2` of them → at least **O(n²)**

## Pitfalls
- Storing the window as a real array and re-summing → O(n) per step; keep **`curr`** and `+=` / `-=` (or × / ÷) instead
- Thinking inner `while` makes O(n²) — left never goes backward, so total shrinks are O(n)
- Forgetting **`right - left + 1`** when updating length or counting
- Fixed-size: forget to remove `arr[i - k]` when adding `arr[i]`
- Fixed-size **max average**: you don’t need to compare `curr/k` every step. Same `k` for every window ⇒ **max sum ↔ max average**; track `best` sum, return `best / k` once
- Binary array / string windows: compare to `0` / `1` (ints) or `"0"` / `"1"` (chars) — **match the type**. `nums[i] == '0'` on `[1,0,1]` never fires
- Count-of-subarrays problems: updating only `max(length)` instead of adding `right - left + 1`
- Product `< k`: if `k <= 1`, no valid window of positives → return 0 early
- Positive-integer assumptions matter for “shrink and forget left” correctness on sum/product

## Tiny example
Longest subarray with sum `<= k`: `nums = [3, 2, 1, 3, 1, 1]`, `k = 5`

| right | window after add | curr | action | length |
|------:|------------------|------|--------|-------:|
| 0 | [3] | 3 | ok | 1 |
| 1 | [3,2] | 5 | ok | 2 |
| 2 | [3,2,1] | 6 | shrink → drop 3 → [2,1] | 2 |
| … | keep grow/shrink | … | track max length | … |

After `[3,2,1]` breaks, the leading `3` can never return — any extension including it only increases the sum.

### Counting trick — product `< k`
`nums = [10, 5, 2, 6]`, `k = 100`. After each `right`, add **how many valid subarrays end at `right`** = current window length.

| right | after shrink | window | product | add to ans | new subarrays ending here |
|------:|--------------|--------|--------:|-----------:|---------------------------|
| 0 | — | [10] | 10 | **1** | [10] |
| 1 | — | [10,5] | 50 | **2** | [5], [10,5] |
| 2 | drop 10 | [5,2] | 10 | **2** | [2], [5,2] |
| 3 | — | [5,2,6] | 60 | **3** | [6], [2,6], [5,2,6] |

Total `1+2+2+3 = 8`. You never list them all in code — the length *is* the count for that ending index.


## Related
- Sibling: two pointers (window *is* two pointers with a grow/shrink rule)
- Later: sliding window + **hashmap** (frequencies / unique counts)
- Course examples in this folder: longest sum ≤ k, flip one zero, product < k, fixed-size max sum
- Not for: non-contiguous subsequences, or unsorted pair search (often hashing / other patterns)
