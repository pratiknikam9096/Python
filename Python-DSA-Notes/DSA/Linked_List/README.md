# Linked List

Definition: Collection of nodes where each node points to the next (singly) or both next and prev (doubly).

Why used: Dynamic size, efficient insert/delete when node reference known.

Time & Space Complexity:

- Access by index: O(n)
- Insert/Delete at head: O(1)
- Search: O(n)
- Space: O(n)

Real-world: a chain of train coaches where each coach links to the next.

Diagram (text):

Head -> [val|next] -> [val|next] -> None

Advantages: cheap insert/delete at known positions.
Disadvantages: no random access; uses extra memory for pointers.
