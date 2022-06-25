from queue import PriorityQueue
v = 7
graph = [[] for i in range(v)]


def best_first_search(actual_Src, target, n):
	visited = [False] * n
	pq = PriorityQueue()
	pq.put((0, actual_Src))
	visited[actual_Src] = True
	
	while pq.empty() == False:
		u = pq.get()[1]
		# Displaying the path having lowest cost
		print(u, end=" ")
		if u == target:
			break

		for v, c in graph[u]:
			if visited[v] == False:
				visited[v] = True
				pq.put((c, v))
	print()

# Function for adding edges to graph


def addedge(x, y, cost):
	graph[x].append((y, cost))
	graph[y].append((x, cost))


# The nodes shown in above example(by alphabets) are
# implemented using integers addedge(x,y,cost);
addedge(0, 1, 8)
addedge(0, 2, 4)
addedge(0, 3, 3)
addedge(1, 4, 1000)
addedge(1, 5, 1000)
addedge(1, 6, 0)
addedge(2, 4, 0)
addedge(3, 6, 0)

source = 0
target = 6
best_first_search(source, target, v)

# This code is contributed by Jyotheeswar Ganne
