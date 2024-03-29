"""
Implements the Edmonds Karp alogrithm to solve the following problem:

Implement the Edmonds-Karp algorithm for finding the maximum flow in a flow network.
Given a flow network with a source vertex and a sink vertex,
find the maximum flow from the source to the sink.
"""

from collections import deque

def edmonds_karp(graph, source, sink):
    n = len(graph)
    residual_graph = [[graph[u][v] for v in range(n)] for u in range(n)]
    max_flow = 0

    while True:
        # Find an augmenting path using BFS
        parent = [-1] * n
        parent[source] = source
        queue = deque([source])

        while queue:
            u = queue.popleft()
            for v in range(n):
                if parent[v] == -1 and residual_graph[u][v] > 0:
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        break

        if parent[sink] == -1:
            break

        # Find the minimum residual capacity along the augmenting path
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = u

        # Update the residual graph and the maximum flow
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow

graph = [
    [0, 16, 13, 0, 0, 0],   # Capacities from vertex 0
    [0, 0, 10, 12, 0, 0],   # Capacities from vertex 1
    [0, 4, 0, 0, 14, 0],    # Capacities from vertex 2
    [0, 0, 9, 0, 0, 20],    # Capacities from vertex 3
    [0, 0, 0, 7, 0, 4],     # Capacities from vertex 4
    [0, 0, 0, 0, 0, 0]      # Capacities from vertex 5
]

source = 0
sink = 5

max_flow = edmonds_karp(graph, source, sink)
print("Maximum flow:", max_flow)