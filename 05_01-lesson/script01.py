"""
Graph as an adjacency list
"""

# Classes

class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        self.add_edge(edges)

    def add_edge(self, edges):
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def remove_edge(self, edges):
        for n1, n2 in edges:
            self.data[n1].remove(n2)
            self.data[n2].remove(n1)

    def __repr__(self):
        return "\n".join(["{}: {}".format(n, neighbors) for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()


# Main

if __name__ == '__main__':
    num_nodes = 5
    edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4)]

    graph = Graph(num_nodes, edges)
    print(graph)

    graph.add_edge([(2, 3), (3, 4)])
    print('\n', graph)

    graph.remove_edge([(2, 3), (3, 4)])
    print('\n', graph)
