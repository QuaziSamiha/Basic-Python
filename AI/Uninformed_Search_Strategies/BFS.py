# shortest path of any node from source node
from queue import Queue

adj_list = {
    "S":["A", "B", "C"],
    "A":["S", "D", "E"],
    "B":["S", "G"],
    "C":["S", "F"],
    "D":["A", "H"],
    "E":["A", "G"],
    "G":["E", "B", "F"],
    "F":["C", "G"],
    "H":["D"]
}

# bfs code
visited = {} # a dictionary for visited nodes
level = {} # distance dictionary
parent = {}
bfs_traversal_output = [] # list for output
queue = Queue()

for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1
    
# mark the source node as A
s = "S"
# visited["S"] = True
visited[s] = True
level[s] = 0
queue.put(s)

while not queue.empty():
    u = queue.get()
    bfs_traversal_output.append(u)
    
    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u]+1
            queue.put(v)
# print(bfs_traversal_output)

v = "G"
path = []
while v is not None:
    path.append(v)
    v = parent[v]
path.reverse()
print(path)