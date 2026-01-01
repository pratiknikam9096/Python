# String Problems (10)

Problem 1: Reverse words in a sentence

Approach: Split, reverse list, join.

Code:

```python
def reverse_words(s):
    return ' '.join(s.split()[::-1])
```

Time: O(n), Space: O(n)

Problem 2: Check anagram

Code:

```python
from collections import Counter
def is_anagram(s,t):
    return Counter(s)==Counter(t)
```

Problem 3: Longest palindrome substring (center expand)

Code (simplified):

```python
def longest_palindrome(s):
    def expand(l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1; r+=1
        return s[l+1:r]
    best=''
    for i in range(len(s)):
        for cand in (expand(i,i), expand(i,i+1)):
            if len(cand)>len(best): best=cand
    return best
```

Problem 4: First non-repeating character

Code:

```python
from collections import Counter
def first_unique(s):
    cnt=Counter(s)
    for i,ch in enumerate(s):
        if cnt[ch]==1: return i
    return -1
```

Problem 5: Longest common prefix — see fundamentals

Problem 6: Implement `strStr()` (needle in haystack)

Code (simple):

```python
def str_str(hay, needle):
    if not needle: return 0
    n,m=len(hay),len(needle)
    for i in range(n-m+1):
        if hay[i:i+m]==needle: return i
    return -1
```

Problem 7: Count and say (sequence generator)

Problem 8: Check palindrome with preprocessing — see fundamentals

Problem 9: Valid palindrome after deleting at most one char

Approach: Two-pointer with one skip.

Code:

```python
def valid_pal_after_del(s):
    def check(l,r):
        while l<r:
            if s[l]!=s[r]: return False
            l+=1; r-=1
        return True
    l,r=0,len(s)-1
    while l<r:
        if s[l]!=s[r]:
            return check(l+1,r) or check(l, r-1)
        l+=1; r-=1
    return True
```

Problem 10: Group anagrams — see fundamentals
