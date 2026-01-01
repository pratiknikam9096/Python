# Graphs

Definition: Nodes (vertices) connected by edges. Can be directed/undirected, weighted/unweighted.

Why used: Model networks, dependencies, routes.

Complexity:

- DFS/BFS: O(V+E)
- Dijkstra: O(E + V log V) with heap

Real-world: Road maps, social networks.

Diagram (text adjacency):

0: 1,2
1: 0,3
2: 0
3: 1

Advantages: Expressive, models many problems.
Disadvantages: Can be complex; memory for adjacency matrix O(V^2).
