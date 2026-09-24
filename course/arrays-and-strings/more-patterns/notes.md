# More common patterns (arrays & strings wrap-up)

## In one sentence
A few cross-cutting tricks: build strings in O(n), and don’t confuse subarray / subsequence / subset when picking a pattern.

## Before you code
1. Building a result **string** in Python? Use a **list** + `"".join` — don’t `+=` in a loop.
2. Word in the prompt: **subarray/substring** (contiguous) vs **subsequence** (order, gaps OK) vs **subset** (order doesn’t matter).
3. Contiguous + constraint / best length / count → think **sliding window**.
4. Many subarray **sums** → think **prefix**.
5. Subsequence with two inputs → often **two pointers**; harder subsequence → later (DP). Subsets → later (backtracking).

## When to use it
- Any problem that builds a long string character by character
- Prompt wording that mixes “subarray / subsequence / subset”
- Choosing among patterns you’ve already learned this chapter

## Core idea / invariant

### O(n) string building (Python)
Strings are immutable → `s += c` copies the whole string → loop of concatenations is **O(n²)**.

```python
arr = []
for c in s:
    arr.append(c)      # O(1) amortized each
return "".join(arr)    # O(n) once
```

Total **O(n)**. (JS: array + `join`; Java: `StringBuilder`; C++ `+=` is OK — mutable.)

### Terminology

| Term | Contiguous? | Order matters? | Example from `[1,2,3,4]` |
|------|-------------|----------------|---------------------------|
| **Subarray / substring** | Yes | Yes (as in array) | `[2,3]` |
| **Subsequence** | No | Yes (relative order) | `[1,3]`, not `[3,1]` |
| **Subset** | No | No (same elements = same subset) | `[3,2]` same as `[2,3]` |

- Window / prefix → **subarrays** only.
- If a “subsequence” problem doesn’t care about order (e.g. sum only), you can treat it like a **subset** (sorting input is OK).

## Pattern / template

**String build**

```
arr = []
# ... append pieces ...
return "".join(arr)
```

**Size / count reminder (subarrays)**  
Length `i..j` inclusive = `j - i + 1`  
(= also: number of subarrays ending at `j` that start at `i` or later, in the count trick).

## Complexity
- Naive string `+=` in a loop: **O(n²)**
- List + join: **O(n)**

## Pitfalls
- Building the answer with `result += char` in Python/Java-style immutable strings
- Hearing “subsequence” and reaching for sliding window / prefix (those need contiguous)
- Assuming every “subarray + constraint” problem is a window (guideline, not a law)

## Tiny example
Build `"abc"` badly vs well:

```text
"" + "a" → "a"
"a" + "b" → copy both → "ab"
"ab" + "c" → copy all → "abc"   # cost 1+2+3 = O(n²) pattern
```

Well: `["a","b","c"]` then `"".join` once.

## Related
- This chapter: [`two-pointers/`](../two-pointers/), [`sliding-window/`](../sliding-window/), [`prefix-sum/`](../prefix-sum/)
- Later: hash maps unlock more windows; DP → many subsequences; backtracking → subsets
- Next in course: chapter quiz, then hashing
