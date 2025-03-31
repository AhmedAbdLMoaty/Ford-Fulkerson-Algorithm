from src.graph.edge import Edge

class Graph:
    def __init__(self):
        self.adj = {}
        self.edges = []

    def add_edge(self, u, v, capacity):
        forward = Edge(u, v, capacity)
        backward = Edge(v, u, 0)

        forward.reverse = backward
        backward.reverse = forward

        self.adj.setdefault(u, []).append(forward)
        self.adj.setdefault(v, []).append(backward)
        self.edges.append(forward)