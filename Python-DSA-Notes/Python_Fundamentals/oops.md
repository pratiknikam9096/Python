# Object-Oriented Programming (OOP)

Core concepts:

- Class and instance
- Encapsulation, Inheritance, Polymorphism, Abstraction

Example:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}"

class Student(Person):
    def __init__(self, name, age, sid):
        super().__init__(name, age)
        self.sid = sid
```

Best practices:

- Keep classes small and cohesive.
- Prefer composition over deep inheritance hierarchy.

Common mistakes:

- Overusing inheritance for code reuse instead of composition.
