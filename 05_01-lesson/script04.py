"""
Deph-First Search
"""

# Imports

from script01 import Graph


# Functions

def dfs(graph, root):
    stack = []
    discovered = [False] * len(graph.data)
    result = []

    stack.append(root)

    while len(stack) > 0:
        current = stack.pop()

        if not discovered[current]:
            discovered[current] = True
            result.append(current)

            for node in graph.data[current]:
                if not discovered[node]:
                    stack.append(node)

    return result


# Main

if __name__ == '__main__':
    num_nodes = 5
    edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

    graph = Graph(num_nodes, edges)
    print('The Graph:')
    print(graph)

    result = dfs(graph, 3)
    print(f'\nThe DFS: {result}')
