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

# required array and dictionary
color = {}
parent = {}
path = []
count = 0
# White = not visited
# Green = first explored
# Black = all the adjacent vertex of a given vertex explored
# Color keep track vertexes which are visited or not

# initialization
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

    # recursvely run ids algorithm
    # travel all the adjacent vertex of u
    for v in adj_list[u]:
        if color[v] == "White":
            color[v] = "Green"
            parent[v] = u

            if v != goal:
                IDS(v, goal)

            if v == goal:
                while v is not None:
                    path.append(v)
                    # print(path)
                    v = parent[v]
                path.reverse()

    # after explored all of the vertex of u, we change its color
    color[u] = 'Black'
    return path

print(IDS("S", "G"))
print(count)
