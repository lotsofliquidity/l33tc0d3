# Arrays and strings

Course chapter folders:

- [`two-pointers/`](two-pointers/)
- [`sliding-window/`](sliding-window/)
- [`prefix-sum/`](prefix-sum/)
- [`more-patterns/`](more-patterns/)

Use this page as a **menu**, not a textbook. Pick the pattern, then open that folder’s `notes.md` only if you need more.

---

## Which pattern? (plain English)

Ask yourself what the problem is really about:

| If the problem is about… | Use… | You’ve seen it in… |
|--------------------------|------|---------------------|
| Two positions moving on a **sorted** array, or walking **two strings** together | **Two pointers** | Squares of a Sorted Array, Is Subsequence |
| A **contiguous** chunk that grows/shrinks under a rule (“sum ≤ k”, “at most k zeros”) | **Sliding window** | Max Average (fixed length), Max Consecutive Ones III |
| “What’s the sum from index L to R?” many times, or left-half vs right-half sums | **Prefix sum** | Running Sum, Ways to Split Array, K-Radius Averages |

**Subarray / substring** = must be next to each other (window or prefix).  
**Subsequence** = order matters, gaps allowed (often two pointers — like Is Subsequence).

---

## Before you code — Sliding window

**Picture:** a box around part of the array. `left` = left edge, `right` = right edge.

1. **What am I tracking inside the box?**  
   Sum? Number of zeros? Product? Call that `curr`.

2. **Is the box always the same size?**  
   - **Yes** (length always `k`) → build first `k` elements, then slide: add the new right, drop the old left (`curr += nums[i] - nums[i-k]`).  
   - **No** → grow `right`; if the box breaks the rule, move `left` until it’s OK again.

3. **What should I return?**  
   - Longest good box → keep `max(right - left + 1)`  
   - How many good boxes → often `ans += (right - left + 1)`  
   - Best average of length `k` → track best **sum**, divide by `k` at the end  

4. **Length of the box** is always `right - left + 1`.  
   On binary arrays use `0`, not `'0'`.

---

## Before you code — Two pointers

1. **One array or two?**  
   One sorted array (squares) vs two sequences (`s` and `t` for subsequence).

2. **When does each pointer move?**  
   Say it in a sentence before typing (e.g. “move `i` only on match; always move `j`”).

3. **Building a new array?**  
   Make it size `n` first. If you discover **biggest first**, write from the **end** (backward fill).

4. Sorted-squares trick only works because the input is **already sorted**.

---

## Before you code — Prefix sum

1. Build a running total list: each spot = “sum of everything up to here.”
2. Sum from `x` to `y` = (total through `y`) minus (total before `x`).
3. “Left half vs the rest” → left = running total so far; right = `total - left`.
4. Don’t re-add the same range in a nested loop — that’s what prefix avoids.

---

## If the notes still feel opaque

That’s a signal to **relearn with one tiny problem**, not to re-read jargon:

1. Open the matching folder’s `notes.md` → read **In one sentence** + **Tiny example** only.  
2. Re-solve one logged mistake with notes OK.  
3. Come back to this README tomorrow and see if the table clicks.

Want me to rewrite `sliding-window/notes.md` the same way (much plainer, fewer jargon words)?
