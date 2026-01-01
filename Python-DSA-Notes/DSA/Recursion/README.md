# Recursion

Definition: A function calling itself with smaller inputs.

Why used: Natural fit for divide-and-conquer and backtracking.

Complexity: Depends on branching factor and depth; often exponential for naive recursion, linear for tail recursion.

Real-world: Russian nesting dolls or fractals.

Diagram: recursion tree text representation for fib:

fib(4)
├─ fib(3)
│  ├─ fib(2)
│  └─ fib(1)
└─ fib(2)

Advantages: Clear code for recursive patterns.
Disadvantages: Stack depth limits; may need memoization.
