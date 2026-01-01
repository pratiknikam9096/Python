# Strings

Strings are sequences of characters. They are immutable.

Common operations:

- Concatenation: `"a" + "b"`
- Repetition: `"a" * 3`
- Slicing: `s[1:4]`
- Methods: `s.lower()`, `s.upper()`, `s.strip()`, `s.split()`, `s.replace()`

f-strings (recommended):

```python
name = "Alice"
age = 30
print(f"{name} is {age}")
```

Real-world analogy: a string is like a sentence written on paper — you can read and copy it, but not change a character in place.

Common mistakes:

- Using `+` repeatedly for many concatenations (use `str.join` for lists).

Examples:

```python
words = ["hello", "world"]
sentence = " ".join(words)
```
