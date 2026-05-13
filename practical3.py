import heapq

# Input number of vertices and edges
vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

# Create graph
graph = {}

for i in range(vertices):
    graph[i] = []

# Input edges
print("Enter edges with weight (u v w):")

for i in range(edges):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))
    graph[v].append((u, w))   # Undirected graph

# Dijkstra Algorithm
def dijkstra(start):

    distance = [float('inf')] * vertices
    distance[start] = 0

    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbour, weight in graph[current_node]:

            new_distance = current_distance + weight

            if new_distance < distance[neighbour]:

                distance[neighbour] = new_distance

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbour)
                )

    return distance

# Main
start_node = int(input("Enter source node: "))

result = dijkstra(start_node)

print("\nShortest distances from source node:")

for i in range(vertices):
    print(f"Node {i} : {result[i]}")