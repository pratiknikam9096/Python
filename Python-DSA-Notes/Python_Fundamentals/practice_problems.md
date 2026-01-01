# Practice Problems (20)

Each problem includes solution and complexity.

1. Sum of list

Problem: Given a list of numbers, return their sum.

Approach: Iterate and accumulate.

Code:

```python
def sum_list(nums):
    total = 0
    for x in nums:
        total += x
    return total
```

Time: O(n), Space: O(1)

2. Reverse a string

Problem: Return reversed copy of a string.

Code:

```python
def reverse_str(s):
    return s[::-1]
```

Time: O(n), Space: O(n)

3. Palindrome check

Code:

```python
def is_palindrome(s):
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]
```

4. Count vowels

Code:

```python
def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in 'aeiou')
```

5. FizzBuzz (1..n)

Code:

```python
def fizzbuzz(n):
    res = []
    for i in range(1, n+1):
        if i%15==0:
            res.append('FizzBuzz')
        elif i%3==0:
            res.append('Fizz')
        elif i%5==0:
            res.append('Buzz')
        else:
            res.append(str(i))
    return res
```

6. Two-sum (hash map)

Problem: Given array and target, return indices of two numbers that add to target.

Code:

```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        diff = target - x
        if diff in seen:
            return (seen[diff], i)
        seen[x] = i
    return None
```

Time: O(n), Space: O(n)

7. Merge two sorted lists

Code:

```python
def merge(a, b):
    i=j=0
    res=[]
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            res.append(a[i]); i+=1
        else:
            res.append(b[j]); j+=1
    res.extend(a[i:]); res.extend(b[j:])
    return res
```

8. Remove duplicates from list (preserve order)

Code:

```python
def dedup(lst):
    seen=set(); out=[]
    for x in lst:
        if x not in seen:
            seen.add(x); out.append(x)
    return out
```

9. Rotate list right by k

Code:

```python
def rotate_right(a, k):
    n=len(a); k%=n
    return a[-k:]+a[:-k]
```

10. Flatten nested list (one level)

Code:

```python
def flatten_once(lst):
    out=[]
    for x in lst:
        if isinstance(x, list):
            out.extend(x)
        else:
            out.append(x)
    return out
```

11. Valid parentheses

Code:

```python
def valid_parentheses(s):
    pairs = {')':'(', ']':'[', '}':'{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop()!=pairs[ch]:
                return False
    return not stack
```

12. Find max subarray (Kadane)

Code:

```python
def max_subarray(nums):
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
```

13. Binary search

Code:

```python
def binary_search(a, x):
    lo, hi = 0, len(a)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if a[mid]==x: return mid
        if a[mid]<x: lo=mid+1
        else: hi=mid-1
    return -1
```

14. Power function (fast exp)

Code:

```python
def fast_pow(x, n):
    res=1
    while n>0:
        if n&1: res*=x
        x*=x; n>>=1
    return res
```

15. Check prime (trial division)

Code:

```python
def is_prime(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True
```

16. Count set bits

Code:

```python
def count_bits(n):
    cnt=0
    while n:
        cnt += n&1
        n >>= 1
    return cnt
```

17. Merge intervals (simple)

Code:

```python
def merge_intervals(intervals):
    intervals.sort()
    out=[]
    for s,e in intervals:
        if not out or s>out[-1][1]: out.append([s,e])
        else: out[-1][1]=max(out[-1][1], e)
    return out
```

18. Longest common prefix

Code:

```python
def lcp(strs):
    if not strs: return ''
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix: return ''
    return prefix
```

19. Move zeros to end

Code:

```python
def move_zeros(a):
    res=[x for x in a if x!=0]
    res += [0]*(len(a)-len(res))
    return res
```

20. Group anagrams

Code:

```python
from collections import defaultdict
def group_anagrams(strs):
    d=defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        d[key].append(s)
    return list(d.values())
```
