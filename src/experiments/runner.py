from src.generators.random_graph import generate_graph
from src.generators.worst_case_graph import generate_worst_case_graph
from src.algorithms.ford_fulkerson import ford_fulkerson
from src.utils.data_handler import save_results_to_csv
from src.utils.visualization import plot_results, plot_detailed_stats
import time

def run_experiments(instance_sizes, repetitions, edge_probability, min_capacity, max_capacity):
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