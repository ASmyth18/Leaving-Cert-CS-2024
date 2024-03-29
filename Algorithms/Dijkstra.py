"""
Dijkstra was a cool character in the Witcher, shame his algorithm doesn't account for negative edge weights.
"""

import heapq

def dijkstra(graph, source):
    n = len(graph)
    dist = [float('inf')] * n  # Initialize distances to infinity
    dist[source] = 0  # Distance from source to itself is 0
    pq = [(0, source)]  # Priority queue to store vertices and their distances
    visited = set()  # Set to keep track of visited vertices

    while pq:
        curr_dist, curr_vertex = heapq.heappop(pq)
        if curr_vertex in visited:
            continue
        visited.add(curr_vertex)

        for neighbor, weight in graph[curr_vertex]:
            if neighbor not in visited:
                new_dist = curr_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

    return dist

graph = [
    [(1, 4), (2, 1)],  # Edges from vertex 0
    [(3, 1)],          # Edges from vertex 1
    [(1, 2), (3, 5)],  # Edges from vertex 2
    [(4, 3)],          # Edges from vertex 3
    []                 # No edges from vertex 4
]

source = 0
distances = dijkstra(graph, source)
print(distances)