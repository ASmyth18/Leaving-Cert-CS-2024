"""
Warshall is a stupid name.
"""

def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]

    # Initialize distances with the weight of direct edges
    for u in range(n):
        dist[u][u] = 0  # Distance from a vertex to itself is 0
        for v, weight in graph[u]:
            dist[u][v] = weight

    # Update distances by considering intermediate vertices
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Check for negative-weight cycles
    for u in range(n):
        if dist[u][u] < 0:
            raise ValueError("Graph contains a negative-weight cycle")

    return dist

graph = [
    [(1, 3), (2, 8), (4, -4)],  # Edges from vertex 0
    [(4, 7), (3, 1)],           # Edges from vertex 1
    [(1, 4)],                   # Edges from vertex 2
    [(0, 2), (2, -5)],          # Edges from vertex 3
    [(3, 6)]                    # Edges from vertex 4
]

distances = floyd_warshall(graph)
for row in distances:
    print(row)