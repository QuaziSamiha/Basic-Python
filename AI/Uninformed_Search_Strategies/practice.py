from queue import Queue

adj_list = {
    "S": ["A", "B", "C"],
    "A": ["D", "E"],
    "B": ["S", "G"],
    "C": ["S", "F"],
    "D": ["A", "H"],
    "E": ["A", "G"],
    "F": ["C", "G"],
    "G": ["B", "E", "F"],
    "H": ["D"]
}

visited = {}
parent = {}
queue = Queue()
output = []

# print(visited)
# print(parent)


def bfs(source):

    for node in adj_list.keys():
        # print(node)
        visited[node] = False
        parent[node] = None

    visited[source] = True
    queue.put(source)

    while not queue.empty():
        u = queue.get()
        output.append(u)

        for v in adj_list[u]:
            # print(v)
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.put(v)
    return output

print(bfs("S"))
