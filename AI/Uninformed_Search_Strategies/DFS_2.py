# present a graph using a dictionary
adj_list = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['B', 'F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# adj_list = {
#     'S': ["A", 'B', 'C'],
#     'A': ['D', 'E'],
#     'B': ['G'],
#     'C': ['F'],
#     'D': ['H'],
#     'E': ['G'],
#     'G': [],
#     'F': ['G'],
#     'H': []
# }

# required array and dictionary
color = {}
# W = not visited
# G = first explored
# B = all the adjacent vertex of a given vertex explored
# Color keep track vertexes which are visited or not
parent = {}
trav_time = {}
''' keep track when a node is first (G color) 
visited and when a node is fully visited (B color)'''
dfs_traversat_output = []

# initialization
for node in adj_list.keys():
    color[node] = 'W'
    parent[node] = None
    trav_time[node] = [-1, -1]

# print(color)
# print(parent)
# print(trav_time)

# use this variable for all recursive call
time = 0  # global variable


def dfs_util(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time  # assign start time
    dfs_traversat_output.append(u)

    # recursvely run dfs algorithm
    # travel all the adjacent vertex of u
    for v in adj_list[u]:
        if color[v] == 'W':  # it means v is not visited
            parent[v] = u
            dfs_util(v)
    # after explored all of the vertex of u, we change its color
    color[u] = "B"  # means this vertex is fully explored
    trav_time[u][1] = time
    time += 1


dfs_util("A")
print(dfs_traversat_output)
print(parent)
print(parent["E"])
print(trav_time)

# for node in adj_list.keys():
#     print(node, " ->", trav_time[node])
