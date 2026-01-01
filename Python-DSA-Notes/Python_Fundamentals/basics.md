# Basics

Introduction to Python syntax, variables, and built-in types.

Syntax:

- To run a script: `python script.py`
- Indentation defines blocks (use 4 spaces)

Variables and types:

- Integers: `x = 10`
- Floats: `f = 3.14`
- Strings: `s = "hello"`
- Booleans: `b = True`
- None: `n = None`

Type conversion:

- `int("5")`, `float("3.2")`, `str(10)`

Built-in functions:

- `print()`, `len()`, `type()`, `range()`

Example:

```python
name = "Alice"
age = 25
print(f"{name} is {age} years old")
```

Best practices:

- Use descriptive variable names.
- Keep functions small and single-purpose.
- Avoid shadowing built-ins (don't name variables `list` or `str`).

Common mistakes:

- Mixing tabs and spaces — configure editor to use spaces.
- Mutable default arguments in functions.
