from src.graph.graph import Graph

def generate_worst_case_graph(num_layers, capacity_per_edge):
    """
    Creates a linear chain from S -> N0 -> N1 -> ... -> N(num_layers-1) -> T.
    Each edge has capacity 'capacity_per_edge'.
    This often forces Ford-Fulkerson to run in many iterations (worst-case).
    """
    g = Graph()
    source = "S"
    sink = "T"

    previous = source
    for i in range(num_layers):
        node = f"N{i}"
        g.add_edge(previous, node, capacity_per_edge)
        previous = node

    g.add_edge(previous, sink, capacity_per_edge)
    return g