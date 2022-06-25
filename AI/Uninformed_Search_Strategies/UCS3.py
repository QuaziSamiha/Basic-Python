graph = {
    'S': [('A', 2), ('B', 3), ('D', 5)],
    'A': [('C', 4)],
    'B': [('D', 4)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 5)],
    'G': []
}

# graph = {
#     'S': [('A', 5), ('B', 2), ('C', 4)],
#     'A': [('D', 9), ('E', 4)],
#     'B': [('G', 6)],
#     'C': [('F', 2)],
#     'D': [('H', 7)],
#     'E': [('G', 6)],
#     'F': [('G', 1)],
#     'G': [],
#     'H': []
# }


def path_cost(path):
    total_cost = 0
    for(node, cost) in path:
        total_cost = total_cost + cost

    return total_cost, path[-1][0]


def ucs(graph, start, goal):
    visited = []
    # queue = [[(start, 0)]]
    queue = [[(start, 0)]]
    print(type(queue))
    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)


solution = ucs(graph, 'S', 'G')
print('Solution is ', solution)
print('Cost of solution is ', path_cost(solution))

# Solution is  [('S', 0), ('A', 2), ('C', 4), ('G', 2)]
# Cost of solution is  (8, 'G')
