# Counting (hash maps)

## In one sentence
Use a hash map to track **how often** keys appear — frequencies unlock sliding-window constraints on many elements, “appears in all lists,” equal-frequency checks, and **exact** subarray metrics via prefix counts.

## When to use it
- “Count / frequency / how many times” of anything
- Sliding window where the constraint involves **multiple** distinct keys (not one `curr` int)
- Exact subarray constraint (sum == k, exactly k odds, …) — not “at most / less than”

## Core idea / invariant
**Map key → integer count.** `len(counts)` = number of distinct keys still present (delete when count hits 0).

### Exact subarrays (prefix + map)
Any subarray sum (or other additive metric) = difference of two prefixes.  
Lock right end at `i` with prefix `curr`. A valid left end exists for each earlier prefix equal to **`curr - k`**.  
So: `ans += counts[curr - k]`, then `counts[curr] += 1`.  
Initialize **`counts[0] = 1`** (empty prefix) so subarrays starting at index 0 are counted.

Same code shape for “exactly k odds”: let `curr` count odds (`x % 2`) instead of sum.

## Pattern / template

**Frequency build**
```python
from collections import defaultdict, Counter
counts = defaultdict(int)  # or Counter(s)
for x in items:
    counts[x] += 1
```

**Window: at most k distinct**
```python
counts = defaultdict(int)
left = ans = 0
for right in range(len(s)):
    counts[s[right]] += 1
    while len(counts) > k:
        counts[s[left]] -= 1
        if counts[s[left]] == 0:
            del counts[s[left]]
        left += 1
    ans = max(ans, right - left + 1)
```

**Exact metric == k (prefix frequencies)**
```python
counts = defaultdict(int)
counts[0] = 1
curr = ans = 0
for x in nums:
    curr += x          # or curr += x % 2 for “odd count”
    ans += counts[curr - k]
    counts[curr] += 1
```

## Complexity
- Window + map: time **O(n)** if map ops amortized O(1); space **O(k)** distinct in window
- Intersection of n lists × m avg: time **O(m·(n + log m))** with sort of answer; space up to **O(n·m)** if all unique
  - Walk every element once: O(n·m). Second pass over unique keys is also ≤ O(n·m), so it does not raise the bound.
  - Answer ⊆ one list, so ≤ m values; sorting them is O(m log m). Factor: O(n·m + m log m) = O(m·(n + log m)).
  - Array counts need length `max(value)+1` even for unused slots. A map stores only numbers that appeared, so a huge key (1000, or 10^11) is one entry.
- Equal frequencies / subarray sum = k: time & space **O(n)** (or O(alphabet) if keys bounded)

## Pitfalls
- One-element window constraint → a single `curr` int is enough; map when many keys matter
- Array-as-count for integer keys wastes space if range is huge/sparse — prefer a map
- Exact (== k) ≠ at-most: don’t use plain “expand while valid” window counting for exact
- Forgetting `counts[0] = 1` drops subarrays that start at index 0
- With negatives/zeros, the same prefix can appear many times — need a **map**, not a set
- When shrinking a window, **delete** keys at count 0 or `len(counts)` is wrong
- "Zero losses" is still a count you must store. With `defaultdict(int)`, `losses[winner] += 0` records a new winner and leaves an existing loss count unchanged. `losses[winner] = 0` on every win erases earlier losses.

## Tiny example
`nums = [1, 2, 1, 2, 1]`, `k = 3` (subarray sum = k):

| i | x | curr | curr−k | counts before add | ans |
|---|---|------|--------|-------------------|-----|
| — | — | 0 | — | {0:1} | 0 |
| 0 | 1 | 1 | −2 | … | +0 → 0; then counts[1]=1 |
| 1 | 2 | 3 | 0 | 0 seen once | +1 → 1 |
| 2 | 1 | 4 | 1 | 1 seen once | +1 → 2 |
| 3 | 2 | 6 | 3 | 3 seen once | +1 → 3 |
| 4 | 1 | 7 | 4 | 4 seen once | +1 → 4 |

Four subarrays; empty-prefix init is why the first `[1,2]` is found.

## Related
- Chapter intro: `course/hashing/notes.md` (maps/sets basics)
- Sliding window “at most / less than” (positive metrics) — chapter 1; here for **exact** use prefix+count
- Two Sum: lock `num`, seek `target - num` → here lock `curr`, seek `curr - k`
