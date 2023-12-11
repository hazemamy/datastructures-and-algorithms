# Depth First Search #

def dfs(graph, start):
    visited= set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end =" ")
            if node in graph:
                neighbors = graph[node]
                stack.extend(neighbors)

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: [],
}

startNode = 1
print("Depth First Traversal (DFS): ")

dfs(graph, startNode)