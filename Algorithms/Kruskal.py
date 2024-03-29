"""
Implementation of Kruskals algorithm. I wish he died before discovering this.
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

def kruskal(graph):
    n = len(graph)
    edges = []
    for u in range(n):
        for v, weight in graph[u]:
            edges.append((weight, u, v))
    edges.sort()  # Sort edges by weight in ascending order

    uf = UnionFind(n)
    mst = []
    total_weight = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

graph = [
    [(1, 4), (2, 3)],  # Edges from vertex 0
    [(0, 4), (2, 1), (3, 2)],  # Edges from vertex 1
    [(0, 3), (1, 1), (3, 5)],  # Edges from vertex 2
    [(1, 2), (2, 5)]   # Edges from vertex 3
]

mst, total_weight = kruskal(graph)
print("Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} (weight: {weight})")