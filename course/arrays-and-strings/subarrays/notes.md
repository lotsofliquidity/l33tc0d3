# Subarrays and substrings: the basics

## In one sentence
A subarray (or substring) is a continuous piece of an array (or string), chosen
by a start and an end position.

## When to use it
- The problem says **subarray** or **substring**: elements/characters must stay
  next to each other.
- The problem asks about a slice's sum, length, contents, or number of valid
  slices.

## Core idea / invariant
For each start index, the end can move only to the right. A subarray never skips
an element. A subsequence may skip elements while keeping their order.

For an array of length `n`, there are `n * (n + 1) // 2` non-empty subarrays:
choose one of `n` starts, then choose an end at or after it.

## Pattern / template

### List the slices

```text
for start in 0..n-1:
    for end in start..n-1:
        inspect nums[start..end]
```

### Sum every slice without re-summing it

```text
for start in 0..n-1:
    running_sum = 0
    for end in start..n-1:
        running_sum += nums[end]
        inspect running_sum
```

The second loop reuses the previous sum: extending `[start..end-1]` by one
element only adds `nums[end]`.

### Prefix-sum range query

Let `prefix[x]` be the sum of the first `x` elements, with `prefix[0] = 0`.
Then the sum from index `start` through `end` is:

```text
prefix[end + 1] - prefix[start]
```

The extra prefix slot represents the total before the array begins, so a slice
starting at index 0 needs no special case.

## Complexity
- Listing/inspecting all subarrays: **O(n²)** slices; explicitly summing each
  slice from scratch can take **O(n³)** total.
- Running sum per start: **O(n²)** time, **O(1)** extra space.
- Prefix build: **O(n)** time and space; each range sum: **O(1)**.

## Pitfalls
- `[1, 3]` is not a subarray of `[1, 2, 3]`: it skips `2`.
- Subarray means **contiguous**; subsequence means ordered but gaps are allowed.
- Prefix conventions vary. With `prefix[0] = 0` and `prefix[x]` covering the
  first `x` elements, use `prefix[end + 1] - prefix[start]`.
- A prefix sum gives a way to compute a slice sum; it does not by itself tell
  you which algorithm answers the problem.
- Sliding-window shrinking based on sum is not generally safe with negative
  values: adding an item can lower the sum, and removing one can raise it.

## Tiny example

For `nums = [1, 2, 3]`:

| Start | Slices as the end moves right |
|---|---|
| 0 | `[1]`, `[1, 2]`, `[1, 2, 3]` |
| 1 | `[2]`, `[2, 3]` |
| 2 | `[3]` |

With `prefix = [0, 1, 3, 6]`, the sum of `[2, 3]` (indices 1 through 2) is
`prefix[3] - prefix[1] = 6 - 1 = 5`.

## Related
- Fixed-size and variable-size windows: [sliding-window notes](../sliding-window/notes.md)
- Range sums: [prefix-sum notes](../prefix-sum/notes.md)
- Exact target-sum counts: [Subarray Sum Equals K](../../hashing/counting/examples/subarray-sum-equals-k.py)
