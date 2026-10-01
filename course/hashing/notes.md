# Hashing (hash maps & sets)

## In one sentence
Hash maps give O(1) key → value lookup by turning any (immutable) key into an array index via a hash function; sets are the same idea with keys only (existence, no values).

## When to use it
- Need fast "have I seen this before?" / "what's stored for this key?"
- Counting frequencies, grouping by a property, or trading O(n) search for O(1) lookup
- Keys aren't convenient as array indices (unknown range, non-integers, sparse)

## Pre-coding check
If your algorithm would do `if x in some_list` (or keep scanning a collection for membership), store those elements in a **hash map or set** so those ops are average **O(1)** instead of O(n).

On a hashing problem, the container is `defaultdict` or `set`:
- Need a value for each key (count, index, list of items) → `defaultdict`
- Only “have I seen this?” → `set`

Do not start from a plain `{}`. A missing key then raises `KeyError` on `d[k] += 1` or `d[k]`.

## Core idea / invariant
A **hash function** maps a key → integer in `[0, size)`, deterministically. Pair that with an array → **hash map**: keys to values, not indices to values.

- **Interface** (how you use it) matters for interviews; **implementation** (how hashing works inside) is completeness only.
- Keys should be **immutable** (Python: `int`, `str`, `tuple` — not `list`).
- Map ops are O(1) *relative to map size* `n`. Hashing a string of length `m` is O(m).

## Pattern / template
`defaultdict` or `set` — not a plain dict:

```python
from collections import defaultdict

d = defaultdict(int)      # or defaultdict(list)
d[key] += 1               # missing key starts at 0
key in d                  # exists?
val = d[key]
del d[key]                # remove (must exist)
len(d)
for k, v in d.items(): ...

s = set()
s.add(x)
x in s
s.remove(x)               # or discard
```

Need a list as a key → `tuple(arr)` (or a delimiter string if elements can't contain the delimiter).

## Complexity
- Time: add / remove / lookup / update → average **O(1)** (per map size); iterate → O(n)
- Space: O(n) stored entries; tables often over-allocate → more memory than a tight array

## Pitfalls
- Starting from `{}` instead of `defaultdict` or `set`
- Treating O(1) as "free" on tiny inputs — hash overhead can lose to a simple array/scan
- Using a **set** when you need **counts** (sets ignore duplicates; use a dict/Counter)
- Mutating a list and expecting it to stay a valid key — convert to `tuple` first
- `del d[k]` / `d[k]` when `k` may be missing → use `in` or `.get(k, default)`
- Saying map ops are O(1) without noting string-key hashing is O(m)

## Tiny example
`d = {}` then `d["ab"] = 1`, `d["c"] = 2`:
- `"ab" in d` → True (hash → bucket → find key)
- `d["ab"] = 3` → update, still one entry for `"ab"`
- `s = {"ab"}`; `s.add("ab")` again → still size 1 (no frequency)

## More hashing examples (meta-patterns)

Hash maps show up everywhere; these four problems repeat the same moves with different “group IDs.”

### 1. Use a **group identifier** as the key
Anything that is equal for all members of a group can key the map:
- Anagrams → sorted string (`"".join(sorted(s))`) — [group-anagrams.py](examples/group-anagrams.py)
- Same digit sum → `sum(int(d) for d in str(x))`
- Equal row/column as 1D arrays → hashable form (`tuple(row)`, not `list`)

Values hold the group (`list` of strings) or a count of how many times that pattern appeared.

**Alt key (anagrams):** length-26 frequency `tuple(counts)` → O(n·m) vs sort O(n·m log m); fixed alphabet only; often slower on short strings due to constants.

### 2. Store **only what you still need** in the value
First draft: map key → *all* indices or *all* numbers in the group, then scan/sort values.

Better when the question asks for a **minimum gap** or **maximum pair**:
- Shortest subarray with a duplicate → key → **last index seen**; on repeat, `dist = i - last`, update min, then `last = i`
- Max sum with equal digit sum → key → **largest number seen** for that sum; on each `x`, try `x + best[sum]` before updating `best[sum] = max(...)`

Same O(n) time often, but less space on average and no per-group sort.

### 3. Nested loops can still be **O(n) total**
Mapping every element to a list of indices, then pairing consecutive indices in each list: inner work across all keys touches each index a bounded number of times → linear in array length, not O(n²) from the nesting shape alone.

### 4. **Hashable keys** for sequences
Rows/columns: build `tuple(row)` (or a string encoding). Count row patterns and column patterns in two maps (or one pass + multiply counts when keys match).

| Problem idea | Key | Value (minimal) |
|---|---|---|
| Group anagrams | sorted string | list of originals |
| Min cards w/ duplicate | card value | last index |
| Max pair, equal digit sum | digit sum | max num in group |
| Equal row/column pairs | tuple(row/col) | count of occurrences |

## Related
- Array when keys are dense integers in a known range (less overhead)
- Sorted map / tree map (e.g. C++ `std::map`) when you need order — not a hash map
- **Counting** (frequencies, multi-key windows, exact subarrays): `course/hashing/counting/notes.md`
- Article copies: [two-sum.py](examples/two-sum.py), [find-players-with-zero-or-one-losses.py](examples/find-players-with-zero-or-one-losses.py), [group-anagrams.py](examples/group-anagrams.py)
