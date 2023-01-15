"""
Shortest Path (Dijkstra's Algorithm)
"""

# Imports

from script05 import Graph


# Functions

def update_distances(graph, current, distance, parent=None):
    """
    Update the distances of the current node's neighbors.
    """
    neighbors = graph.data[current]
    weights = graph.weight[current]

    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current


def pick_next_node(distance, visited):
    """
    Pick the next unvisited node at the smallest distance.
    """
    min_distance = float('inf')
    min_node = None

    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_distance = distance[node]
            min_node = node

    return min_node


def shortest_path(graph, source, target):
    visited = [False] * graph.num_nodes
    distance = [float('inf')] * graph.num_nodes
    queue = []

    distance[source] = 0
    queue.append(source)
    idx = 0

    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        visited[current] = True
        idx += 1

        update_distances(graph, current, distance)
        next_node = pick_next_node(distance, visited)

        if next_node:
            queue.append(next_node)

    return distance[target]


# Main

if __name__ == '__main__':
    num_nodes = 6
    edges = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]
    graph = Graph(num_nodes, edges, weighted=True, directed=True)

    print(shortest_path(graph, 0, 5))
