# Lists, Tuples & Sets

Lists:

- Mutable ordered sequences. `lst = [1,2,3]`
- Common ops: `append`, `extend`, `insert`, `pop`, `remove`, slicing

Tuples:

- Immutable ordered sequences. `t = (1,2)`
- Use for fixed collections or when immutability matters.

Sets:

- Unordered collections of unique items. `s = {1,2,3}`
- Fast membership checks; good for deduplication.

Best practices:

- Use list comprehensions for concise construction: `[x*x for x in nums]`
- Use tuples for heterogeneous records (like coordinates) when immutability helps.

Common mistakes:

- Assuming set preserves order (it doesn't — use `dict`/`OrderedDict` or `list` if order matters).
