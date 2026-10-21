# Reverse Linked List — visual walkthrough

Interactive play-through (Cursor canvas): open **`reverse-linked-list`** from the
canvases panel (file lives with the project canvases, not under `course/`).

This page is the same model in git, so it stays even when the canvas is closed.

## The picture to keep

Every loop pass moves **one** node from the OLD chain onto the front of the NEW chain.

| name | job |
|---|---|
| `prev` | front of the **NEW** (already reversed) chain |
| `curr` | front of the **OLD** (still to reverse) chain |
| `next_node` | temporary save of the rest of the OLD chain |

Only one line changes the list: `curr.next = prev` (the flip).
Everything else only moves the three names.

```
next_node = curr.next   # save rest of OLD
curr.next = prev        # FLIP — only arrow that changes
prev = curr             # this node is now front of NEW
curr = next_node        # walk to remaining OLD
```

When `curr` is `None`, return `prev`.

## Trace: `[1, 2, 3]`

### Start
- NEW: empty (`prev = None`)
- OLD: `1 → 2 → 3` (`curr = 1`)

### Pass 1
1. `next_node = 2` — save OLD remainder  
2. **Flip:** `1.next` was `2` → now `None`  
3. `prev = 1` — NEW front is `1`  
4. `curr = 2`  
   - NEW: `1 → None`  
   - OLD: `2 → 3`

### Pass 2
1. `next_node = 3`  
2. **Flip:** `2.next` was `3` → now `1`  
3. `prev = 2`  
4. `curr = 3`  
   - NEW: `2 → 1`  
   - OLD: `3`

### Pass 3
1. `next_node = None`  
2. **Flip:** `3.next` was `None` → now `2`  
3. `prev = 3`  
4. `curr = None` → stop  
   - NEW: `3 → 2 → 1`  
   - OLD: empty  

Return `prev` → `[3, 2, 1]`.

## Common mix-up

Do not keep reading `head.next` after the first flip. `head` is only the starting
value for `curr`. After that, the walker is `curr` alone.

## Related files
- Notes: [notes.md](notes.md)
- Article copy: [examples/reverse-linked-list.py](examples/reverse-linked-list.py)
- Soon rebuild with comments: [practice/2026-10-22-ReverseLinkedList-soon.py](practice/2026-10-22-ReverseLinkedList-soon.py)
- Cold due: entry #16 in `MISTAKES.md` (2026-10-29)
