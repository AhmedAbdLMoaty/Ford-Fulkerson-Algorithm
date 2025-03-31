from src.experiments.runner import run_experiments, run_worst_case_experiment
from src.generators.random_graph import generate_graph
from src.generators.worst_case_graph import generate_worst_case_graph
from src.utils.data_handler import save_results_to_csv
from src.utils.visualization import plot_results, plot_detailed_stats
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
