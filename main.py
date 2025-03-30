import time
import random
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ---------- Core Algorithm ----------
class Edge:
    def __init__(self, from_node, to_node, capacity):
        self.from_node = from_node
        self.to_node = to_node
        self.capacity = capacity
        self.flow = 0
        self.reverse = None

    def residual_capacity(self):
        return self.capacity - self.flow

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

# ---------- Random Graph Generator ----------
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

    # Connect source to some nodes
    for node in nodes:
        if random.random() < 0.8:
            cap = random.randint(min_capacity, max_capacity)
            g.add_edge(source, node, cap)
            added_edges.add((source, node))

    # Connect internal nodes among themselves
    for u in nodes:
        for v in nodes:
            if u != v and (u, v) not in added_edges:
                if random.random() < edge_probability:
                    cap = random.randint(min_capacity, max_capacity)
                    g.add_edge(u, v, cap)
                    added_edges.add((u, v))

    # Connect some nodes to sink
    for node in nodes:
        if random.random() < 0.8:
            cap = random.randint(min_capacity, max_capacity)
            g.add_edge(node, sink, cap)
            added_edges.add((node, sink))

    return g

# ---------- Worst-Case Graph Generator ----------
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

# ---------- Experiment Runners ----------
def run_experiments(instance_sizes, repetitions, edge_probability, min_capacity, max_capacity):
    """
    Runs random graph experiments for each size in 'instance_sizes'.
    Generates a new random graph for each repetition, times the FF algorithm,
    and returns a list of dict results: {'nodes': size, 'run': i, 'time': runtime}.
    """
    results = []
    for size in instance_sizes:
        for i in range(repetitions):
            g = generate_graph(size, edge_probability, min_capacity, max_capacity)
            start_time = time.perf_counter()
            ford_fulkerson(g, "S", "T")
            end_time = time.perf_counter()
            runtime = end_time - start_time
            results.append({
                "nodes": size,
                "run": i + 1,
                "time": runtime
            })
    return results

def run_worst_case_experiment(sizes, repetitions, capacity_per_edge):
    """
    Runs worst-case linear-chain experiments for each size in 'sizes'.
    'size' here is how many N_i nodes we have, so actual total nodes = size + 2 (S + T).
    """
    results = []
    for size in sizes:
        for i in range(repetitions):
            g = generate_worst_case_graph(num_layers=size, capacity_per_edge=capacity_per_edge)
            start_time = time.perf_counter()
            ford_fulkerson(g, "S", "T")
            end_time = time.perf_counter()
            runtime = end_time - start_time
            results.append({
                "nodes": size + 2,
                "run": i + 1,
                "time": runtime
            })
    return results

# ---------- Save & Basic Plot ----------
def save_results_to_csv(results, filename):
    """
    Writes out the results list of dicts to a CSV file.
    """
    if not results:
        return  # no data
    keys = results[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)

def plot_results(results, title):
    """
    Simple average runtime vs. node count line plot.
    """
    df = pd.DataFrame(results)
    avg_times = df.groupby("nodes")["time"].mean()
    plt.figure()
    plt.plot(avg_times.index, avg_times.values, marker='o')
    plt.xlabel("Number of Nodes")
    plt.ylabel("Average Runtime (seconds)")
    plt.title(title)
    plt.grid(True)
    plt.show()

# ---------- Enhanced Statistical Plot ----------
def plot_detailed_stats(results, title):
    """
    Plots average runtime with standard deviation error bars
    and a shaded area showing the 25th–75th percentile range.
    """
    df = pd.DataFrame(results)
    grouped = df.groupby("nodes")["time"]

    avg = grouped.mean()
    std_dev = grouped.std()
    p25 = grouped.quantile(0.25)
    p75 = grouped.quantile(0.75)

    x = avg.index.values
    y = avg.values
    err = std_dev.values
    y1 = p25.values
    y2 = p75.values

    plt.figure()
    plt.errorbar(x, y, yerr=err, fmt='-o', label='Average ± Std Dev')
    plt.fill_between(x, y1, y2, alpha=0.2, label='25th–75th Percentile Range')
    plt.xlabel("Number of Nodes")
    plt.ylabel("Runtime (seconds)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# ---------- EXAMPLE USAGE: Random Graphs ----------
sizes = [2, 5, 10, 20, 50]
repetitions = 10
random_results = run_experiments(sizes, repetitions, edge_probability=0.3, min_capacity=1, max_capacity=20)
save_results_to_csv(random_results, "./ff_experiment_results.csv")

plot_results(random_results, "Ford-Fulkerson (Random Graphs) - Basic Plot")
plot_detailed_stats(random_results, "Ford-Fulkerson (Random Graphs) - Detailed Stats")

# ---------- EXAMPLE USAGE: Worst-Case Graphs ----------
worst_case_sizes = [5, 10, 20, 30, 40, 50]
worst_case_repetitions = 10
worst_case_results = run_worst_case_experiment(worst_case_sizes, worst_case_repetitions, capacity_per_edge=1)
save_results_to_csv(worst_case_results, "./ff_worst_case_results.csv")

plot_results(worst_case_results, "Ford-Fulkerson (Worst-Case Graphs) - Basic Plot")
plot_detailed_stats(worst_case_results, "Ford-Fulkerson (Worst-Case Graphs) - Detailed Stats")

# ---------- EXAMPLE USAGE: Dense Graphs ----------
dense_sizes = [2, 5, 10, 20, 30]
dense_repetitions = 10
dense_results = run_experiments(dense_sizes, dense_repetitions, edge_probability=0.9, min_capacity=1, max_capacity=20)
save_results_to_csv(dense_results, "./ff_dense_graph_results.csv")

plot_results(dense_results, "Ford-Fulkerson (Dense Graphs) - Basic Plot")
plot_detailed_stats(dense_results, "Ford-Fulkerson (Dense Graphs) - Detailed Stats")
