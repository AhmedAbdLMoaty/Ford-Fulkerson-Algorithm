# Max Flow Algorithm Project

This project implements the Ford-Fulkerson algorithm for computing the maximum flow in a flow network. It includes functionalities for generating random graphs, running experiments, and visualizing results.

## Project Structure

```
max-flow-algorithm
├── src
│   ├── graph
│   │   ├── __init__.py
│   │   ├── edge.py
│   │   └── graph.py
│   ├── generators
│   │   ├── __init__.py
│   │   ├── random_graph.py
│   │   └── worst_case_graph.py
│   ├── algorithms
│   │   ├── __init__.py
│   │   └── ford_fulkerson.py
│   ├── experiments
│   │   ├── __init__.py
│   │   └── runner.py
│   └── utils
│       ├── __init__.py
│       ├── data_handler.py
│       └── visualization.py
├── main.py
├── requirements.txt
└── README.md
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the experiments and visualize the results, execute the `main.py` file:

```bash
python main.py
```

## Experimentation

The project includes functions to run experiments on both random and worst-case graphs. You can modify the parameters in `main.py` to adjust the size and characteristics of the graphs generated for experimentation.

## Visualization

Results from the experiments are visualized using Matplotlib. The project provides basic plots as well as detailed statistical plots with error bars and percentile ranges.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.