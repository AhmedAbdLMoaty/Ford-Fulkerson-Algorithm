import pandas as pd
import matplotlib.pyplot as plt
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