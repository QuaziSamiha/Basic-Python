# from queue import Queue
import queue

adj_list = {
    "S":["A", "B", "C"],
    "A":["S", "D", "E"],
    "B":["S", "G"],
    "C":["S", "F"],
    "D":["A", "H"],
    "E":["A", "G"],
    "G":["E", "B", "F"],
    "F":["C", "G"],
    "H":["D"]
}

def ucs(G, v):
    visited = set()                  # set of visited nodes
    visited.add(v)                   # mark the starting vertex as visited
    # we store vertices in the (priority) queue as tuples with cumulative cost
    q = queue.PriorityQueue()
    # add the starting node, this has zero *cumulative* cost
    q.put((0, v))
    goal_node = None                 # this will be set as the goal node if one is found
    # this dictionary contains the parent of each node, necessary for path construction
    parents = {v: None}

    while not q.empty():             # while the queue is nonempty
        dequeued_item = q.get()
        current_node = dequeued_item[1]             # get node at top of queue
        # get the cumulative priority for later
        current_node_priority = dequeued_item[0]

        if current_node.is_goal:                    # if the current node is the goal
            # the path to the goal ends with the current node (obviously)
            path_to_goal = [current_node]
            # set the previous node to be the current node (this will changed with each iteration)
            prev_node = current_node

            while prev_node != v:                   # go back up the path using parents, and add to path
                parent = parents[prev_node]
                path_to_goal.append(parent)
                prev_node = parent

            path_to_goal.reverse()                  # reverse the path
            return path_to_goal                     # return it

        else:
            for edge in current_node.out_edges:     # otherwise, for each adjacent node
                child = edge.to()                   # (avoid calling .to() in future)

                if child not in visited:            # if it is not visited
                    visited.add(child)              # mark it as visited
                    # set the current node as the parent of child
                    parents[child] = current_node
                    # and enqueue it with *cumulative* priority
                    q.put((current_node_priority + edge.weight, child))
