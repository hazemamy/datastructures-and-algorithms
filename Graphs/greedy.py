from queue import PriorityQueue
def greedy_search(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))
    while not queue.empty():
        cost, node = queue.get()
        if node == goal: 
            print("Goal reached!")
            break
        if node not in visited:
            visited.add(node)
            print("Visiting node:", node)
        for neighbor, neighbor_cost in graph[node].items():
            if neighbor not in visited:
                priority = heuristic(neighbor, goal)
                queue.put((priority, neighbor))
def heuristic(node, goal):
    return abs(ord(node) - ord(goal))
graph = {
    's': {'b': 4, 'a': 2},
    'b': {'c': 1, 'd': 3, 'a': 3},
    'c': {'d': 2},
    'a': {'c': 5, 'd': 3},
    'd': {},}
start_node = 'a'
goal_node = 'd'
greedy_search(graph, start_node, goal_node)

print("  حازم احمد محمد علي  ::  شعبة رياضة وحاسب  ")