# Contiguous Array — plain-language walkthrough

Interactive: Cursor canvas **`contiguous-array`** (Play / Step).

## Forget code for a minute

You walk left to right keeping a **score**:

- see `1` → score goes up by 1  
- see `0` → score goes down by 1  

Whenever the score comes back to a value it had earlier, the numbers *between* those two moments cancel. Cancel = same number of ups and downs = equal 0s and 1s.

So the question becomes: **when I see this score again, how far is it from the first time I saw it?**

That distance is the length.

## What the map is

A notebook:

> “Score S was first seen at index I.”

Not a count. Just the earliest index for each score.

## The scary line: `first[0] = -1`

Before you read anything, the score is already `0`.

There is no array index for “before the start,” so we invent index `-1`.

That way, when the score returns to `0` at the end of `[0, 1]`:

```text
length = 1 - (-1) = 2
```

which is the whole array. Without the seed, you would not know where that first `0` “was.”

## The if / else

```python
if balance in first:
    best = max(best, i - first[balance])  # seen before → measure length
else:
    first[balance] = i                    # first time → write it down
```

- **Seen before:** do not change the notebook; only update the best length.  
- **New score:** write this index down (and never overwrite it later — earlier is better).

## Tiny trace: `[0, 1, 0]`

| step | score after | notebook | length found |
|---|---|---|---|
| seed | 0 | `0 → -1` | — |
| index 0, value 0 | -1 | add `-1 → 0` | — |
| index 1, value 1 | 0 | already have `0 → -1` | `1 - (-1) = 2` |
| index 2, value 0 | -1 | already have `-1 → 0` | `2 - 0 = 2` |

Answer: `2`.

## Related
- Solution: [examples/contiguous-array.py](examples/contiguous-array.py)
- Chapter notes: [notes.md](notes.md) (section “Longest length, not a count”)
