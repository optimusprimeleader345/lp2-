from collections import deque

# Input number of vertices and edges
vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

# Create empty graph
graph = {}

for i in range(vertices):
    graph[i] = []

# Input edges
print("Enter edges (u v):")

for i in range(edges):
    u, v = map(int, input().split())

    # Undirected graph
    graph[u].append(v)
    graph[v].append(u)

# -------- DFS --------
visited_dfs = set()

def DFS(node):
    if node not in visited_dfs:
        print(node, end=" ")
        visited_dfs.add(node)

        for neighbour in graph[node]:
            DFS(neighbour)

# -------- BFS --------
def BFS(start):
    visited_bfs = set()
    queue = deque()

    visited_bfs.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited_bfs:
                visited_bfs.add(neighbour)
                queue.append(neighbour)

# -------- Main --------
start_node = int(input("Enter starting node: "))

print("\nDFS Traversal:")
DFS(start_node)

print("\nBFS Traversal:")
BFS(start_node)