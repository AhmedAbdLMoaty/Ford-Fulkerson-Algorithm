def dfs(graph, current, sink, visited, flow):
    if current == sink:
        return [], flow

    visited.add(current)

    for edge in graph.adj.get(current, []):
        residual = edge.residual_capacity()
        if edge.to_node not in visited and residual > 0:
            path, min_cap = dfs(graph, edge.to_node, sink, visited, min(flow, residual))
            if min_cap > 0:
                return [edge] + path, min_cap

    return None, 0

def ford_fulkerson(graph, source, sink):
    max_flow = 0

    while True:
        visited = set()
        path, flow = dfs(graph, source, sink, visited, float('inf'))
        if flow == 0:
            break

        max_flow += flow
        for edge in path:
            edge.flow += flow
            edge.reverse.flow -= flow

    return max_flow