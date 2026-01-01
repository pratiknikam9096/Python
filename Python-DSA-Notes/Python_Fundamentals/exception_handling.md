# Exception Handling

Use `try/except/finally` to handle runtime errors.

```python
try:
    x = int(input())
except ValueError:
    print("Please enter an integer")
finally:
    print("Done")
```

Best practices:

- Catch specific exceptions, not a bare `except:`.
- Use `with` statements (context managers) for resources.

Common mistakes:

- Swallowing exceptions silently.
