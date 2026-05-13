import heapq

# Graph with heuristic values
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 1,
    'F': 2,
    'G': 0
}

# A* Algorithm
def astar(start, goal):

    priority_queue = []
    
    # (f_cost, current_node, path, g_cost)
    heapq.heappush(priority_queue, (0, start, [start], 0))

    visited = set()

    while priority_queue:

        f_cost, current, path, g_cost = heapq.heappop(priority_queue)

        if current == goal:
            print("Path found:", path)
            print("Total Cost:", g_cost)
            return

        if current not in visited:

            visited.add(current)

            for neighbour, cost in graph[current]:

                new_g_cost = g_cost + cost
                h_cost = heuristic[neighbour]

                new_f_cost = new_g_cost + h_cost

                heapq.heappush(
                    priority_queue,
                    (new_f_cost, neighbour, path + [neighbour], new_g_cost)
                )

    print("Path not found")


# Main
start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")

astar(start_node, goal_node)