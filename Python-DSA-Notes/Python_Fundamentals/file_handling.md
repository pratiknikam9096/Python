# File Handling

Open and read files using `with` to ensure proper closing:

```python
with open('data.txt', 'r', encoding='utf-8') as f:
    text = f.read()

with open('out.txt', 'w') as f:
    f.write('hello')
```

Binary vs text mode: use `rb`/`wb` for binary data.

Best practices:

- Always use `with` for safety.
- Handle file not found errors with exceptions.
