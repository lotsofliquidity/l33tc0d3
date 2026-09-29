# Two pointers

## In one sentence
Use two index variables that walk an iterable (or two) so you scan once instead of nesting loops.

## Before you code
1. One array or two? Ends → middle, or both moving forward?
2. What’s the **decision rule** (when does left move vs right)?
3. Loop condition: `<` (skip middle OK) or `<=` (must visit every index)?
4. Building a new sorted array? Pre-size it; fill forward or backward to match discovery order.
5. Target: O(n) time, usually O(1) extra space.

## When to use it
- Array/string problem where pairs of positions matter (ends → center, or two sequences in lockstep)
- Input is sorted and you need a pair / merge / ordered scan
- Subsequence / “consume both inputs” style problems
- You can decide which pointer(s) to move from local comparison alone

## Core idea / invariant
Two integers advance along one or more sequences; each step moves at least one pointer closer to “done,” so the loop is linear if the body is O(1). The **decision rule** (which pointer moves) is the problem-specific invariant — e.g. for sorted two-sum: if sum is too big, shrink from the right forever (left can only grow); if too small, grow from the left.

## Pattern / template

### 1. Opposite ends (converge)

```
left, right = 0, n - 1
while left < right:
    # compare / check arr[left], arr[right]
    # then: left++, or right--, or both
```

Classic uses: palindrome check, sorted two-sum / pair with target.

### 2. Two sequences (same direction)

```
i = j = 0
while i < n and j < m:
    # compare arr1[i], arr2[j]
    # then: i++, or j++, or both
# optionally exhaust the remaining array
while i < n: ...
while j < m: ...
```

Classic uses: merge two sorted arrays, is-subsequence (`s` pointer advances only on match; `t` always advances).

### Variations
- Both pointers can start at 0 on **one** array and both move forward
- Sometimes three pointers; “two pointers” is the idea, not a fixed layout

### 3. Forward fill vs backward fill (write index)

Not an official course name — just a useful label. When you **build a new array** and each step you already know the *next* value to place:

1. Pre-size: `out = [0] * n` (don’t use empty `[]` if you need random writes)
2. Keep a **write index**
3. Point it the same direction as the order you’re producing

| Fill | Write cursor | When |
|------|--------------|------|
| **Forward** | `index = 0`, then `index += 1` | You’re emitting values in the same order the answer wants (e.g. merge two sorted arrays ascending; or sorted-squares if the answer wanted largest first) |
| **Backward** | `index = n - 1`, then `index -= 1` | You’re emitting values in the *opposite* order the answer wants (classic sorted squares: pick larger end-square each time → big→small stream, but answer needs small→big) |

Rule of thumb: **match write direction to discovery order.** Same two-pointer reads; only `index` flips.

```
# backward fill sketch (sorted squares — ascending output)
left, right = 0, n - 1
index = n - 1
out = [0] * n
while left <= right:          # <= so the middle element is placed
    # take larger of nums[left]**2 and nums[right]**2
    out[index] = chosen
    index -= 1
    # move left++ or right--
```

### Why sorted squares needs non-decreasing input

The O(n) two-pointer solution **only** works because `nums` is already sorted non-decreasing.

On a sorted line, the **largest squares** live at the **far left** (big negative → big square) and **far right** (big positive → big square). The middle (near 0) has the smallest squares. That’s why comparing `left` and `right` and taking the **larger** square each time is correct — the next biggest square is always at one of the two ends of the remaining range.

If the array were unsorted, those ends wouldn’t mean “largest magnitudes,” and this trick breaks. Unsorted → square everything, then sort (O(n log n)), or use another approach.

Same idea for the less common forward-fill merge (find the first non-negative, walk outward taking the **smaller** square): that also depends on negatives left / non-negatives right, which only holds when the input is sorted.

## Length vs last index

`len(s)` is a count. The last valid index is `len(s) - 1`. Subtract 1 only when the number has to name a position.

`for i in range(len(s))` already visits `0` through `len(s) - 1`. Inside that loop the last character is `i == len(s) - 1`. The test `i == len(s)` never fires.

Two different ends:

| Kind | Value | Use |
|------|--------|-----|
| Inclusive last character | an index | two-pointer reverse: `l, r = start, end`, `while l < r` |
| Exclusive end (a slice) | one past the last character | `s[left:right]` — a space at `i` means the word is `s[left:i]`; the last word is `s[left:len(s)]` |

On a space at `i`, the last letter of the word is `i - 1` and the next word starts at `i + 1`. After the scan, the last word runs through `len(s) - 1`.

Keep `n = len(s)` meaning the length. If you instead store `n = len(s) - 1` and then write `range(n)`, the last character is skipped.

A new list of length `right - left` only has indexes `0` through `right - left - 1`. Those indexes are not positions in the original string. `arr[left]` or `arr[right]` on that list raises `IndexError` — this is what broke Reverse Words III on 2026-09-29 (`reverseString(0, 2)` built a list of length 2 and wrote index `2`, the space).

```python
def reverse_words(s: str) -> str:
    chars = list(s)  # a Python str cannot be swapped in place
    n = len(chars)

    def reverse(l, r):  # inclusive ends
        while l < r:
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1

    start = 0
    for i in range(n):
        if chars[i] == " ":
            reverse(start, i - 1)
            start = i + 1
    reverse(start, n - 1)
    return "".join(chars)
```

`"Mr Ding"`: space at `2` → `reverse(0, 1)` makes `"rM Ding"`, `start = 3`. After the loop, `reverse(3, 6)` makes `"rM gniD"`.

Time is `O(n)`. In Python the character list is `O(n)` extra. The swaps on that list use a handful of indexes.

## Complexity
- Time: O(n) for one array; O(n + m) for two — if each iteration is O(1)
- Space: O(1) extra (ignore output array when building a merge)

## Pitfalls
- Nested pair scan when the array is sorted → O(n²) instead of converge/merge
- Forgetting to exhaust the leftover array after a two-array merge loop
- Moving the wrong pointer on sorted two-sum (breaks the “x only increases / y only decreases” argument)
- Assuming pointers must start at 0 and n−1 — some problems need different starts
- **Building a new sorted array from ends (sorted squares):** pre-size `arr = [0] * n` and fill from `index = n - 1` (largest square first). An empty `[]` + append, or fill from index 0, puts big values in the wrong place.
- **`left < right` vs `left <= right`:** palindrome can stop at the middle; sorted-squares must place *every* element → use `<=` or you leave a hole (often a leftover `0` from init that looks “fine” on lucky cases).
- **`len(s)` vs `len(s) - 1`:** length is the count and the exclusive end; last index is `len(s) - 1`. Inside `range(len(s))`, `i == len(s)` never happens. A word-sized list cannot be indexed with positions from the original string. See **Length vs last index**.

## Tiny example
Sorted two-sum: `nums = [1, 2, 4, 6, 8, 9, 14, 15]`, `target = 13`

| left | right | sum | action |
|------|-------|-----|--------|
| 1 | 15 | 16 > 13 | right-- |
| 1 | 14 | 15 > 13 | right-- |
| 1 | 9 | 10 < 13 | left++ |
| 2 | 9 | 11 < 13 | left++ |
| 4 | 9 | 13 = 13 | found |

## Related
- Sibling: sliding window (also two indices, but a contiguous window with grow/shrink rules)
- Not for: unsorted Two Sum needing arbitrary pairs → hashing is usually better
- Course examples in this folder: palindrome, check-for-target, combine-two-sorted-arrays, is-subsequence
