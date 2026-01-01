# Control Flow

Conditionals:

```python
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")
```

Loops:

- `for` loop:

```python
for i in range(5):
    print(i)
```

- `while` loop:

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

Loop control:

- `break`, `continue`, and `else` on loops.

Real-world analogy: loops are like repeating a set of steps until a goal is reached (e.g., checking items on a checklist).

Best practices:

- Prefer `for` when iterating collections.
- Avoid complex nested loops if possible; extract into functions.
