# Fast and slow pointers

## In one sentence
Use two pointers moving at different speeds to find a midpoint, detect a cycle, or find a node by offset without converting the list to an array.

## When to use it
- The problem is about a linked list but the length is unknown
- You need to detect whether the list loops back on itself
- You need the middle node, the kth-from-end node, or a “meet-in-the-middle” condition
- You want O(n) time and O(1) extra space

## Core idea / invariant
The fast pointer moves farther each step, so it reaches the end or completes a cycle before the slow pointer. The invariant is that, after each iteration, the fast pointer is always either at least as far along the list as the slow pointer or it is one step behind in a cycle. That lets you reason about the relative gap instead of the absolute index.

## Pattern / template
```python
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    # check the condition you care about
```

Common uses:
- Middle node: once `fast` hits the end, `slow` is in the middle
- Cycle detection: if `slow == fast`, there is a cycle
- Kth from end: advance `fast` by `k`, then move both together until `fast` reaches the end

## Complexity
- Time: O(n)
- Space: O(1)

## Pitfalls
- Forgetting the `fast and fast.next` guard before doing `fast.next.next`
- Using `slow == fast` to mean “found the middle” in a non-cycle list — only a cycle gives a true meeting point
- Mixing absolute position logic with relative-gap logic
- For kth-from-end, forgetting that the fast pointer must get the gap first, then both move together

## Tiny example
List: `1 -> 2 -> 3 -> 4 -> 5 -> None`

- `slow = 1`, `fast = 1`
- after one step: `slow = 2`, `fast = 3`
- after two steps: `slow = 3`, `fast = 5`
- fast reaches end, so slow is the middle node (`3`)

The key is not “count nodes,” but “the fast pointer covers two steps for every one step the slow pointer takes.”

## Related
- Sibling pattern: two pointers in arrays/strings
- Related to dummy pointers for edge-case handling, but not the same idea
- Useful in cycle detection, palindrome checking, and kth-from-end problems
