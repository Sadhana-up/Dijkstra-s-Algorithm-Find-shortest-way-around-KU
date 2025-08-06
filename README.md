# Dijkstra's Algorithm: Finding the Shortest Way Around KU

This project implements Dijkstra's algorithm to find the shortest path between two locations on the Kathmandu University (KU) campus. It also includes a visualization of the campus map and the calculated shortest path.

## 🚀 Quickstart

### Prerequisites

- Python 3.11+
- `uv` (a fast Python package installer)

### Installation

1.  **Install `uv`** (if you haven't already):

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2.  **Create a virtual environment and install dependencies:**

    ```bash
    uv venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    uv sync pyproject.toml
    ```

    Alternatively, you can install the dependencies using `pip`:

    ```bash
    uv pip install -r pyproject.toml
    ```

### Running the Project

To run the main application, which calculates the shortest path and displays the visualization, execute the following command:

```bash
uv run python main.py
```

You can also run the simplified, single-file version:

```bash
python proj.py
```

## Project Structure

```
Dijkstra-s-Algorithm-Find-shortest-way-around-KU/
│
├── .gitignore
├── main.py                 # Main entry point of the application
├── proj.py                 # A simplified, single-file version of the project
├── pyproject.toml          # Project metadata and dependencies
├── README.md               # This file
├── uv.lock                 # Lockfile for reproducible builds
│
├── constants/
│   ├── __init__.py
│   └── nodes.py            # Defines the graph data (nodes and edges)
│
└── src/
    ├── __init__.py
    ├── algorithim.py       # Implements Dijkstra's algorithm
    ├── graph_plots.py      # Defines the Graph class
    └── visiualizer.py      # Visualizes the graph and the shortest path
```

## Dependencies

This project uses the following external libraries:

-   **`icecream`**: A debugging tool used for printing variables and data structures in a more readable format.
-   **`matplotlib`**: A plotting library used to create the graph visualization.
-   **`networkx`**: A library for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
-   **`ruff`**: A fast Python linter and code formatter, used to maintain code quality and consistency.
