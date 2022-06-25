# present a graph using a dictionary
adj_list = {
    'S': ["A", 'B', 'C'],
    'A': ['D', 'E'],
    'B': ['G'],
    'C': ['F'],
    'D': ['H'],
    'E': ['G'],
    'G': [],
    'F': ['G'],
    'H': []
}

color = {}
parent = {}
output = []

for node in adj_list.keys():
    # print(node)
    color[node] = "White"
    parent[node] = None

# print(parent, "\n", color)


def dfs(u):
    color[u] = "Green"
    output.append(u)

    for v in adj_list[u]:
        if color[v] == "White":
            color[v] = "Green"
            parent[v] = u
            dfs(v)

    color[u] = "Black"

    return output


print(dfs("S"))
