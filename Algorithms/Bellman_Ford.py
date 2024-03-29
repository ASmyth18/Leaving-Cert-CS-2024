"""
A simple implementation of the bellman-ford algorithm, accounting for negative edge weights.
"""

def bellman_ford(graph, source):
    n = len(graph)
    dist = [float('inf')] * n  # Initialize distances to infinity
    dist[source] = 0  # Distance from source to itself is 0

    # Relax edges repeatedly
    for _ in range(n - 1):
        for u in range(n):
            for v, weight in graph[u]:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

    # Check for negative-weight cycles
    for u in range(n):
        for v, weight in graph[u]:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                raise ValueError("Graph contains a negative-weight cycle")

    return dist

# Graph represented as an adjacency list, where each vertex is associated with a tuple.
graph = [
    [(1, 6), (2, 5), (3, 5)],  # Edges from vertex 0
    [(4, -1)],                 # Edges from vertex 1
    [(1, -2), (4, 1)],         # Edges from vertex 2
    [(2, -2), (5, -1)],        # Edges from vertex 3
    [(6, 3)],                  # Edges from vertex 4
    [(6, 3)],                  # Edges from vertex 5
    []                         # No edges from vertex 6
]

source = 0
distances = bellman_ford(graph, source)
print(distances)