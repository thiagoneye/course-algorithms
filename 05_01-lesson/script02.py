"""
Graph as an adjacency matrix
"""

# Classes

class Graph:
    def __init__(self, num_nodes):
        self.data = [num_nodes*[0] for _ in range(num_nodes)]

    def add_edges(self, edges):
        for n1, n2 in edges:
            self.data[n1][n2] = 1
            self.data[n2][n1] = 1

    def remove_edges(self, edges):
        for n1, n2 in edges:
            self.data[n1][n2] = 0
            self.data[n2][n1] = 0


# Main

if __name__ == '__main__':
    num_nodes = 5
    edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

    graph = Graph(num_nodes)
    graph.add_edges(edges)

    print(graph.data)
