# Hashing (hash maps & sets)

## In one sentence
Hash maps give O(1) key → value lookup by turning any (immutable) key into an array index via a hash function; sets are the same idea with keys only (existence, no values).

## When to use it
- Need fast "have I seen this before?" / "what's stored for this key?"
- Counting frequencies, grouping by a property, or trading O(n) search for O(1) lookup
- Keys aren't convenient as array indices (unknown range, non-integers, sparse)

## Pre-coding check
If your algorithm would do `if x in some_list` (or keep scanning a collection for membership), store those elements in a **hash map or set** so those ops are average **O(1)** instead of O(n).

## Core idea / invariant
A **hash function** maps a key → integer in `[0, size)`, deterministically. Pair that with an array → **hash map**: keys to values, not indices to values.

- **Interface** (how you use it) matters for interviews; **implementation** (how hashing works inside) is completeness only.
- Keys should be **immutable** (Python: `int`, `str`, `tuple` — not `list`).
- Map ops are O(1) *relative to map size* `n`. Hashing a string of length `m` is O(m).

## Pattern / template
Python dict / set:

```python
d = {}                    # or {k: v, ...}
d[key] = value            # insert or update
key in d                  # exists?
val = d[key]              # access (KeyError if missing)
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

## Related
- Array when keys are dense integers in a known range (less overhead)
- Sorted map / tree map (e.g. C++ `std::map`) when you need order — not a hash map
- **Counting** (frequencies, multi-key windows, exact subarrays): `course/hashing/counting/notes.md`
- Next: checking complements (Two Sum-style), grouping
