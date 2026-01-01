# Array Problems (10)

Problem 1: Reverse an Array

Approach: Two-pointer swap.

Code:

```python
def reverse_array(a):
    i, j = 0, len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1; j -= 1
    return a
```

Time Complexity: O(n)
Space Complexity: O(1)

Problem 2: Remove duplicates from sorted array (in-place)

Approach: Two-pointer unique overwrite.

Code:

```python
def remove_duplicates_sorted(a):
    if not a: return 0
    write = 1
    for i in range(1, len(a)):
        if a[i] != a[write-1]:
            a[write] = a[i]
            write += 1
    return write  # new length
```

Time: O(n), Space: O(1)

Problem 3: Rotate array by k

Approach: Reverse parts.

Code:

```python
def rotate(a, k):
    n = len(a); k%=n
    a[:] = a[-k:]+a[:-k]
    return a
```

Time: O(n), Space: O(n) (slice) or O(1) with in-place reversals

Problem 4: Majority element (Boyer-Moore)

Code:

```python
def majority(a):
    cand = None; count = 0
    for x in a:
        if count==0: cand=x
        count += 1 if x==cand else -1
    return cand
```

Time: O(n), Space: O(1)

Problem 5: Two-sum (indices)

Code: see fundamentals two_sum (hashmap)

Problem 6: Move zeros (stable)

Code:

```python
def move_zeros(a):
    j = 0
    for i in range(len(a)):
        if a[i] != 0:
            a[j] = a[i]; j+=1
    for k in range(j, len(a)): a[k] = 0
    return a
```

Time: O(n), Space: O(1)

Problem 7: Find peak in mountain array (binary search)

Code:

```python
def peak_index(a):
    lo, hi = 1, len(a)-2
    while lo<=hi:
        mid=(lo+hi)//2
        if a[mid]>a[mid-1] and a[mid]>a[mid+1]: return mid
        if a[mid]>a[mid-1]: lo = mid+1
        else: hi = mid-1
    return -1
```

Problem 8: Maximum subarray (Kadane) — see fundamentals

Problem 9: Product of array except self

Approach: Prefix & suffix products.

Code:

```python
def product_except_self(nums):
    n=len(nums)
    out=[1]*n
    prefix=1
    for i in range(n):
        out[i]=prefix; prefix*=nums[i]
    suffix=1
    for i in range(n-1,-1,-1):
        out[i]*=suffix; suffix*=nums[i]
    return out
```

Time: O(n), Space: O(n)

Problem 10: Find duplicates (return any duplicate)

Code:

```python
def find_duplicate(a):
    seen=set()
    for x in a:
        if x in seen: return x
        seen.add(x)
    return None
```
