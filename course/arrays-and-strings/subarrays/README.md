# Subarrays and substrings

A gentle path from recognizing a contiguous slice to choosing the right
algorithm. Go in order; the later prefix-sum counting problems build on the
early ideas.

## Course path

| Step | Learn | Try / revisit | Ready to move on when… |
|---|---|---|---|
| 1 | A subarray is a continuous slice; choose start and end positions | Tiny hand-traces in [notes.md](notes.md) | You can list every subarray of a short array and explain why a skipped element makes a subsequence, not a subarray |
| 2 | Extend one start at a time and maintain a running sum | The brute-force warm-up in [notes.md](notes.md) | You can count subarrays with a target sum by checking each continuous slice |
| 3 | Prefix sums: later total minus earlier total gives a slice sum | [Prefix-sum notes](../prefix-sum/notes.md); [K Radius Subarray Averages practice](../prefix-sum/practice/2026-10-08-KRadiusSubarrayAverages.py) | You can find a slice sum by subtracting two prefix totals |
| 4 | Fixed-size sliding window: add one item, remove one item | [Maximum Average Subarray I practice](../sliding-window/practice/2026-10-14-MaximumAverageSubarrayI.py) | You can update a length-`k` sum without rebuilding it |
| 5 | Variable-size sliding window and when shrinking is safe | [Sliding-window notes](../sliding-window/notes.md); [Longest subarray with sum at most k example](../sliding-window/examples/find-max-length-of-subarray-equal-to-k.py) | You can state the window rule and why the values/constraint make the left edge safe to advance |
| 6 | Count target-sum subarrays with prefix-sum frequencies | [Subarray Sum Equals K practice](../../hashing/counting/practice/2026-10-26-SubarraySumEqualsK.py); [course example](../../hashing/counting/examples/subarray-sum-equals-k.py) | You can explain what `curr - k` means and why prefix sums are counted before the next lookup |
| 7 | Turn other questions into prefix-frequency or balance questions | [Contiguous Array example](../../hashing/counting/examples/contiguous-array.py); [Count Number of Nice Subarrays example](../../hashing/counting/examples/count-number-of-nice-subarrays.py) | You can describe the running state that repeats when a useful slice exists |
| 8 | Substrings use the same contiguous-slice idea; track what is in the window | [Longest Substring Without Repeating Characters practice](../sliding-window/practice/2026-10-03-LongestSubstringWithoutRepeatingCharacters.py) | You can distinguish substring from subsequence and maintain the required window condition |

## How to work through it

- Do one step per session. Start with the tiny hand-traces; no code is needed
  until the slice boundaries make sense.
- Before choosing a pattern, say what the problem asks for: a slice sum, a
  fixed-length best slice, a longest valid slice, or a count of slices.
- Keep the current problem's attempt in its existing `practice/` file. Problems
  linked from another chapter stay in that chapter; this page is only the
  learning path.
- For cold revisits, follow the regime and due dates in [`MISTAKES.md`](../../../MISTAKES.md).

## Quick pattern choice

- **Known length?** Usually fixed-size sliding window.
- **Many range-sum queries?** Prefix sums.
- **Longest/shortest valid window with a safe grow/shrink rule?** Variable-size
  sliding window.
- **Count subarrays with an exact sum, especially when values can be negative?**
  Prefix-sum frequency map.

These patterns all talk about contiguous slices, but they are not interchangeable.
In particular, a usual sum-based sliding window cannot safely shrink based on
the sum when negative numbers are allowed.
