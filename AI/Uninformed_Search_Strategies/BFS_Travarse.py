from queue import Queue

adj_list = {
    "S": ["A", "B", "C"],
    "A": ["S", "D", "E"],
    "B": ["S", "G"],
    "C": ["S", "F"],
    "D": ["A", "H"],
    "E": ["A", "G"],
    "G": ["E", "B", "F"],
    "F": ["C", "G"],
    "H": ["D"]
}

visited = {}  # a dictionary for visited nodes
parent = {}
queue = Queue()
bfs_traversal_output = []


for node in adj_list.keys():
    # print(node)
    visited[node] = False
    parent[node] = None

# print(visited)
# print(parent)

s = "S"
visited[s] = True
# print(visited)
queue.put(s)

while not queue.empty():
    u = queue.get()
    # print(u)
    bfs_traversal_output.append(u)

    for v in adj_list[u]:
        # print(v)
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            queue.put(v)

print(bfs_traversal_output)

