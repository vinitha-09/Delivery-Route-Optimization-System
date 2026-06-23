# Delivery Route Optimization using Dijkstra's Algorithm

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = []

    while len(visited) < len(graph):
        current = min(
            (node for node in graph if node not in visited),
            key=lambda node: distances[node]
        )

        visited.append(current)

        for neighbor, weight in graph[current].items():
            distance = distances[current] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances

start_node = 'A'
result = dijkstra(graph, start_node)

print("Delivery Route Optimization System")
print("Shortest distances from", start_node)

for node, distance in result.items():
    print(f"{node}: {distance}")
