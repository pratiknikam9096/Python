# Dictionaries

Mappings of key → value. Created with `{}` or `dict()`.

```python
person = {"name": "Alice", "age": 30}
```

Common ops: `person[key]`, `get()`, `keys()`, `values()`, `items()`, `pop()`

Use cases:

- Counting occurrences: `counts = {}` then increment.
- Fast lookups by key.

Best practices:

- Use `defaultdict` or `Counter` from `collections` for counting patterns.

Common mistakes:

- Modifying dict during iteration — iterate over a copy or use comprehension.
