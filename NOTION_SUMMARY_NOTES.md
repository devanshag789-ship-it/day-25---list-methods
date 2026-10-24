# Day 25 — Python List Methods

## Learning goals
- Insert an item at a chosen position with `insert()`.
- Find an item's position with `index()` and count occurrences with `count()`.
- Sort a list with `sort()` and reverse its current order with `reverse()`.
- Make a shallow copy with `copy()`.
- Add items from another iterable with `extend()`.
- Remove all items with `clear()`.

## Key ideas
- List methods such as `sort()`, `reverse()`, `extend()`, and `clear()` modify the list in place.
- `copy()` creates a separate shallow copy, so changing the copied list does not change the original list's top-level items.
- `extend()` adds each item from the second list; it does not append the second list as one nested item.
- `index()` raises `ValueError` if the requested value is not present.

## Try it
1. Add another fruit using `insert()`.
2. Add a repeated number and inspect the result of `count()`.
3. Compare `a.append(b)` with `a.extend(b)`.
