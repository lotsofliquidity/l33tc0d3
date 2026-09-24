# Prefix sum

## In one sentence
Precompute running totals so any subarray sum `nums[i..j]` can be answered in O(1) instead of re-adding the range.

## Before you code
1. Build running totals → `prefix[i]` = sum through index `i`.
2. Sum of `x..y` → sum through `y`, minus sum before `x`.
3. “Left vs rest” → left = `prefix[i]`, right = `total - left` (stop before empty right).
4. **K-radius average:** center `i` needs `i-k..i+k` (len `2k+1`) or `-1`; sum via prefix, `// (2k+1)`.
5. Cost: O(n) build, O(1) per range; array is O(n) space (running left can be O(1)).

## When to use it
- Problem asks for **sums of many subarrays / ranges** (queries, splits, “sum from L to R”)
- Brute force would re-sum the same elements over and over → O(n) per query
- Numbers array (usually); same idea later for other “range aggregates” with care

## Core idea / invariant
`prefix[i]` = sum of `nums[0] + nums[1] + … + nums[i]`.

Subarray sum from `i` to `j` (inclusive):

```text
prefix[j] - prefix[i - 1]     # when i > 0
prefix[j]                     # when i == 0
```

Why: green line (sum through `j`) minus red line (sum through `i-1`) leaves only `i..j`.

Alternate (avoids `i-1` bounds): `prefix[j] - prefix[i] + nums[i]`.

**Pre-processing:** spend O(n) once building `prefix`, then each range sum is O(1).

## Pattern / template

### Build

```
prefix = [nums[0]]
for i in range(1, n):
    prefix.append(nums[i] + prefix[-1])
```

### Query sum `i..j`

```
if i == 0:
    s = prefix[j]
else:
    s = prefix[j] - prefix[i - 1]
```

### Space trick (when you only need prefixes in order)

Sometimes you don’t need the full array:
- Keep `left = 0`, add `nums[i]` as you go (current prefix)
- Precompute `total = sum(nums)`
- Right section = `total - left`

Still a prefix-sum *idea*, just O(1) extra space (e.g. ways to split array).

## Complexity
- Build: **O(n)** time, **O(n)** space (or O(1) extra with the running-prefix trick)
- Each range sum after build: **O(1)**
- `m` queries: **O(n + m)** vs **O(n·m)** without prefix

## Pitfalls
- Off-by-one on `i - 1` when `i == 0` — handle the empty-left case
- Confusing `prefix[i]` (inclusive through `i`) with “sum before `i`”
- Building prefix but still looping `i..j` to sum — defeats the point
- Not every subarray problem needs a prefix array (sliding window may fit better for “best window under a constraint”)
- **Min start value so running sum ≥ 1:** deepest dip = `min(prefix)`; need `startValue ≥ 1 - min_prefix`, and at least 1 → `max(1, 1 - min_prefix)`

## Tiny example
`nums = [5, 2, 1, 6, 3, 8]`  
`prefix = [5, 7, 8, 14, 17, 25]`

Sum of `nums[2..4]` = `1+6+3 = 10`:
`prefix[4] - prefix[1] = 17 - 7 = 10`

## Related
- Sibling: sliding window (online grow/shrink); prefix sum (random range sums / many queries)
- Example patterns: answer range-sum queries vs limit; count ways to split array (left ≥ right)
- Next in course: more array/string tricks, then chapter quiz → hashing
