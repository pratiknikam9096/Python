# Linked List Problems (10)

Problem 1: Reverse linked list (iterative)

Approach: Prev, current iterate.

Code:

```python
class Node:
    def __init__(self, val, nxt=None):
        self.val = val; self.next = nxt

def reverse(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
```

Time: O(n), Space: O(1)

Problem 2: Detect cycle (Floyd's tortoise and hare)

Code:

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False
```

Problem 3: Merge two sorted lists

Problem 4: Remove nth node from end (two-pointer)

Problem 5: Find middle node (two-pointer)

Code snippets and approaches are standard interview patterns.

Problem 6: Palindrome linked list (reverse second half)

Problem 7: Intersection of two linked lists (two-pointer switch)

Problem 8: Add two numbers represented by linked lists

Problem 9: Copy list with random pointer (hash map)

Problem 10: Rotate list k places

For all above, time O(n) and space O(1) or O(n) depending on method.
