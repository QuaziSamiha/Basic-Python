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
path = []
count = 0

for node in adj_list.keys():
    # print(node)
    color[node] = "White"
    parent[node] = None

# print(parent, "\n", color)


def IDS(u, goal):
    color[u] = "Green"
    # print(goal)
    global count
    count += 1

    for v in adj_list[u]:
        if color[v] == "White":
            color[v] = "Green"
            parent[v] = u

            if v != goal:
                IDS(v,goal)

            if v == goal:
                while v is not None:
                    path.append(v)
                    # print(path)
                    v = parent[v]
                path.reverse()
        
    color[u] = 'Black'
    return path


print(IDS("S", "G"))
print(count)