# Object-Oriented Programming (OOP)

Core concepts:

- Class and instance
- **Encapsulation**, **Abstraction**, **Inheritance**, **Polymorphism**

---

## The Four Pillars of OOP

### 1) Encapsulation ✅
- Encapsulation groups data (attributes) and the operations on that data (methods) together inside a class and restricts direct access to some of the object's components.
- In Python, use naming conventions (`_protected`, `__private`) and properties to control access.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # "private"

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    @property
    def balance(self):
        return self.__balance

acct = BankAccount('Alex', 100)
acct.deposit(50)
print(acct.balance)  # 150
```

### 2) Abstraction 🧩
- Abstraction hides complex implementation details and exposes a simple interface.
- Use abstract base classes or simply provide well-defined public methods.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        from math import pi
        return pi * self.r * self.r

c = Circle(2)
print(c.area())
```

### 3) Inheritance 🌳
- Inheritance lets a class (child) inherit attributes and methods from another class (parent), enabling code reuse and specialization.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I'm {self.name}"

class Student(Person):
    def __init__(self, name, sid):
        super().__init__(name)
        self.sid = sid

s = Student('Maya', 123)
print(s.greet())  # Hi, I'm Maya
```

### 4) Polymorphism 🔁
- Polymorphism allows objects of different classes to be treated via the same interface (method names) — either by overriding methods or via duck typing.

```python
class Dog:
    def speak(self):
        return 'woof'

class Cat:
    def speak(self):
        return 'meow'

animals = [Dog(), Cat()]
for a in animals:
    print(a.speak())  # works for all 'speak' implementations
```

---

## Quick Tips
- Prefer composition over deep inheritance when possible. 🔧
- Keep methods small and focused; expose only what's necessary. 💡

## Practice Exercises ✅
1. Implement a `Vehicle` base class and `Car` / `Bike` subclasses; give each a `max_speed` method and demonstrate polymorphism.
2. Create a `Library` class that encapsulates a list of books and exposes methods to add/remove/search books.
3. Use `abc.ABC` to define an abstract `Exporter` with a `export()` method and implement `CSVExporter` and `JSONExporter`.

---

**Summary:** This file now contains concise definitions and short Python examples for **encapsulation**, **abstraction**, **inheritance**, and **polymorphism** to illustrate the core OOP principles.

