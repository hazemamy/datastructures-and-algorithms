# Uniform Cost Search #

from queue import PriorityQueue

def uniformCostSearch(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start, [start])) 
    while not queue.empty():
        cost, node, path = queue.get()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor, neighborCost in graph[node].items():
                newCost = cost + neighborCost
                newPath = path + [neighbor]
                queue.put((newCost, neighbor, newPath))
    return None

graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'D': 4, 'E': 2},
    'C': {'F': 1},
    'D': {'G': 5},
    'E': {'G': 2},
    'F': {'G': 3},
    'G': {},
    }

startNode = 'A'
goalNode = 'G'

result = uniformCostSearch(graph, startNode, goalNode) 

print("Uniform Cost Search")
if result:
    print("Path Found : ", result)
else:
    print("Path Not Found")