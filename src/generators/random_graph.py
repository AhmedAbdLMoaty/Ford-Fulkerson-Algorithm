import random
from src.graph.graph import Graph

def generate_graph(num_nodes, edge_probability, min_capacity, max_capacity):
    """
    Creates a random directed graph with a single source 'S' and sink 'T'.
    - 'num_nodes' internal nodes named N0..N(num_nodes-1).
    - Each edge capacity is random within [min_capacity, max_capacity].
    - 'edge_probability' controls how likely any two nodes are connected.
    """
    g = Graph()
    nodes = [f"N{i}" for i in range(num_nodes)]
    source = "S"
    sink = "T"
    added_edges = set()

    for node in nodes:
        if random.random() < 0.8:
            cap = random.randint(min_capacity, max_capacity)
            g.add_edge(source, node, cap)
            added_edges.add((source, node))

    for u in nodes:
        for v in nodes:
            if u != v and (u, v) not in added_edges:
                if random.random() < edge_probability:
                    cap = random.randint(min_capacity, max_capacity)
                    g.add_edge(u, v, cap)
                    added_edges.add((u, v))

    for node in nodes:
        if random.random() < 0.8:
            cap = random.randint(min_capacity, max_capacity)
            g.add_edge(node, sink, cap)
            added_edges.add((node, sink))

    return g