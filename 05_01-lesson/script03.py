"""
Breadth-First Search
"""

# Imports

from script01 import Graph


# Functions

def bfs(graph, root):
    queue = []
    discovered = [False] * len(graph.data)
    parent = [None] * len(graph.data)
    distance = [None] * len(graph.data)

    queue.append(root)
    discovered[root] = True
    distance[root] = 0
    idx = 0

    while idx < len(queue):
        # Dequeue
        current = queue[idx]
        idx += 1

        # Check all edges of current
        for node in graph.data[current]:
            if not discovered[node]:
                queue.append(node)
                discovered[node] = True
                parent[node] = current
                distance[node] = 1 + distance[current]

    return queue, parent, distance


# Main

if __name__ == '__main__':
    num_nodes = 5
    edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

    graph = Graph(num_nodes, edges)
    print('The Graph:')
    print(graph)

    queue, parent, distance = bfs(graph, 3)
    print(f'\nThe BFS: {queue}')
    print(f'The parent: {parent}')
    print(f'The distance: {distance}')
