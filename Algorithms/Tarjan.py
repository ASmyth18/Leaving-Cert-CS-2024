"""
That one leet code problem that required this was stupid. 
"""

def tarjan(graph):
    n = len(graph)
    stack = []
    on_stack = [False] * n
    index = [None] * n
    low_link = [None] * n
    scc = []
    idx = 0

    def dfs(v):
        nonlocal idx
        index[v] = idx
        low_link[v] = idx
        idx += 1
        stack.append(v)
        on_stack[v] = True

        for neighbor in graph[v]:
            if index[neighbor] is None:
                dfs(neighbor)
                low_link[v] = min(low_link[v], low_link[neighbor])
            elif on_stack[neighbor]:
                low_link[v] = min(low_link[v], index[neighbor])

        if low_link[v] == index[v]:
            component = []
            while True:
                u = stack.pop()
                on_stack[u] = False
                component.append(u)
                if u == v:
                    break
            scc.append(component)

    for v in range(n):
        if index[v] is None:
            dfs(v)

    return scc

graph = [
    [1],        # Edges from vertex 0
    [2],        # Edges from vertex 1
    [0],        # Edges from vertex 2
    [1, 4, 5],  # Edges from vertex 3
    [5],        # Edges from vertex 4
    [3]         # Edges from vertex 5
]

components = tarjan(graph)
for component in components:
    print(component)