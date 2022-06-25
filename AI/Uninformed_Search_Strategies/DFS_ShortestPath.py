adj_list = {
    'S': ['A', 'B', 'C'],
    'A': ['D', 'E'],
    'B': ['G'],
    'C': ['F'],
    'D': ['H'],
    'E': ['G'],
    'F': ['G'],
    'G': [],
    'H': []
}

color = {}
parent = {}
output = []
path = []

for node in adj_list.keys():
    # print(node)
    color[node] = "White"
    parent[node] = None

# print(parent, "\n", color)


def dfs(u, goal):
    color[u] = "Green"
    output.append(u)
    # print(goal)

    for v in adj_list[u]:
        if color[v] == "White":
            color[v] = "Green"
            parent[v] = u
            dfs(v, "G")
            if v == goal:
                while v is not None:
                    path.append(v)
                    # print(path)
                    v = parent[v]
                path.reverse()
        
    color[u] = 'Black'
    # v = goal
    return path


print(dfs("S", "G"))
# print(parent)
