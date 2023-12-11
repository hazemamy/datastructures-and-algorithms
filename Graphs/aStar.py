from queue import PriorityQueue
graph={'S':{'A':2},'S': {'B':4},'A': {'C':5},'A':{'D':3},'C': {'D':3},'B': {'A':3},
       'A': {'D':3},'B': {'C':1},'C': {'D':3},'B': {'D':3}}

heuristic = {'S': 7,'A': 4, 'B':3, 'C': 2, 'D':0}

def astar (graph, start, goal):
    
    queue = PriorityQueue()
    visited = set()
    
    queue.put((0, start,[]))
   
    while not queue.empty():
       cost, node, path = queue.get()

       if node == goal:
           path =path +[node]
           return path

       if node not in visited:
          visited.add(node)
          print("visited node: ", node)

          for neighbor, neighbor_cost in graph[node].items():
             total_cost = cost + neighbor_cost+heuristic [neighbor]
             queue.put((total_cost, neighbor, path+[node]))

    return "path not found"

result =astar(graph, "S", "D")
print("result: ", result)