from queue import Queue


adj_list = {
    'S': ['A', 'B', 'C'],
    'A': ['D', 'E'],
    'B': ['G'],
    'C': ['F'],
    'D': ['H'],
    'E': ['G'],
    'F': ['G'],
    'H': [],
    'G': []
}

visited = {}
parent = {}
queue = Queue()
travarse_path = []
shortest_path = []

for node in adj_list.keys():
    # print(node)
    visited[node] = False
    parent[node] = None


def bfs(source, goal):

    visited[source] = True
    queue.put(source)

    while not queue.empty():
        u = queue.get()
        # print(u)
        travarse_path.append(u)

        for v in adj_list[u]:
            # print(v)
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.put(v)

    g = goal
    while g is not None:
        shortest_path.append(g)
        g = parent[g]

    shortest_path.reverse()

    return print("Travarse Path using BFS: ", travarse_path, '\nShortest Path usign BFS: ', shortest_path)


bfs("S", "G")
# print(visited, "\n", parent)
