import heapq

def dijkstra(graph, start):
    # Initialization
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        # Check if current path is shorter than the known distance
        if current_distance > distances[current_node]:
            continue
        # Explore nieghbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Update distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

if __name__ == '__main__':
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_node ='A'
    result = dijkstra(graph, start_node)
    print(f"Shorter distance from {start_node}: {result}")