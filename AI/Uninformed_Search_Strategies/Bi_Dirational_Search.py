graph = {
    'S': [('A', 1), ('B', 2)],
    'A': [('C', 5)],
    'B': [('C', 3)],
    'C': [('D', 2)],
    'D': [('G', 5)],
    'F': [('E', 1)],
    'H': [('E', 8)],
    'E': [('D', 1)],
    'G': [('F', 4), ('H', 2)]
}

def path_cost(path):
    total_cost = 0
    for(node, cost) in path:
        total_cost = total_cost + cost

    return total_cost, path[-1][0]


def ucs(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    # print(type(queue))
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


sol1 = ucs(graph, "S", 'D')
print("\nForword Path: ", sol1)
print('\nCost of solution is ', path_cost(sol1))
sol2 = ucs(graph, "G", 'D')
print("\nBackword Path: ", sol2)
print('\nCost of solution is ', path_cost(sol2))