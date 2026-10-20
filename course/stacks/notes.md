# Stacks

## In one sentence
An ordered collection where you only add and remove from the **same end** — last in, first out (LIFO).

## When to use it
- The problem has a LIFO shape: the most recent unmatched thing is the next one that gets resolved.
- Elements in the input **interact** with each other — matching pairs, querying “how far is the next larger element”, evaluating a math expression given as a string, comparing elements against each other, or any similar abstract interaction.
- Browser-history style undo: push on each step forward, pop to go back.
- Recursion is already a stack of calls — an explicit stack can replace or explain that.
- The LIFO property is sometimes hard to see at first; if the thing that resolves next is always the one you saw most recently, try a stack.

## Core idea / invariant
Push and pop share one end (the “top”). Whatever was pushed last is the only thing you can remove next.

A stack is the **abstract interface**, not a specific data structure. The defining rule is only “add and remove from the same end.” A dynamic array, a linked list with a tail pointer, or anything else that respects that rule is a stack.

**Stacks and recursion are the same shape.** Function calls are pushed on a call stack; the call at the top is the active one; a `return` (or end of function) pops it. An explicit stack in an algorithm often mirrors that.

## Pattern / template
Terminology: **push** = insert at the top, **pop** = remove the top, **peek** = look at the top without removing.

In Python the usual implementation is a dynamic array:

```python
stack = []
stack.append(x)   # push
x = stack.pop()   # pop (raises if empty)
top = stack[-1]   # peek
```

Typical algorithm shape:

1. Walk the input left to right.
2. When you see something that “opens” or is unresolved, push it.
3. When you see something that “closes” or resolves against the most recent open item, pop and handle the pair.
4. Whatever is left on the stack is still unresolved.

## Complexity
Depends on the implementation. With a dynamic array (most common / easiest):

- Push / pop / peek (and random access of the array): O(1)
- Search for an arbitrary element: O(n)
- Space: O(n) for the elements stored

A linked list with a tail pointer is another valid implementation; same LIFO interface, complexity follows the list.

## Pitfalls
- Treating it like a queue (FIFO) — wrong end, wrong order of resolution.
- Calling `pop()` on an empty stack — guard with `if stack:` or check length first.
- Forcing a stack when the interaction is not LIFO (e.g. you need the oldest unmatched item first).
- Confusing “stack as a list” with “I can index wherever I want” — the *algorithm* should only touch the top; random access is an implementation accident, not the pattern.

## Tiny example
Physical world: a stack of plates — you only add or remove from the top of the pile.

Browser history: start on `A`, click to `B`, click to `C`.

| action | stack |
|---|---|
| visit A | `[A]` |
| visit B | `[A, B]` |
| visit C | `[A, B, C]` |
| back | `[A, B]` |
| back | `[A]` |

Last page visited is the first one the back button undoes.

## Related
- Recursion: each call is pushed; return pops. An explicit stack often mirrors a recursive DFS.
- Queues: same “collection of pending work”, opposite end rule (FIFO).
- String problems: [string-problems/notes.md](string-problems/notes.md) — brackets, cascading adjacent deletes, backspace typing.
