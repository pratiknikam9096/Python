# Functions

Defining functions:

```python
def greet(name):
    return f"Hello, {name}"

print(greet("Bob"))
```

Parameters and returns, default args, keyword args:

```python
def add(a, b=0):
    return a + b

add(1, b=2)
```

Lambda (anonymous) functions:

```python
square = lambda x: x*x
print(square(5))
```

Scope:

- Local vs global variables. Prefer returning values instead of using globals.

Common pitfall:

- Mutable default arguments (use None and initialize inside).

Best practices:

- Keep functions short and focused.
- Use type hints for clarity: `def add(a: int, b: int) -> int:`
