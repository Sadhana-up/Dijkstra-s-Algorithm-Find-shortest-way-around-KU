import matplotlib.pyplot as plt
import networkx as nx
from src import Graph

class GraphVisualizer:
    """
    A class to visualize a graph, including the shortest path,
    using NetworkX and Matplotlib.

    Attributes:
        G (nx.Graph): A NetworkX graph object.
    """

    def __init__(self, graph: Graph) -> None:
        """
        Initializes the GraphVisualizer with a graph.

        This constructor converts the custom `Graph` object into a `networkx.Graph`
        object, which can be used for visualization.

        Args:
            graph (Graph): The graph to be visualized.
        """
        self.G = nx.Graph()
        # Iterate through the nodes and their neighbors in the input graph
        # to build the NetworkX graph.
        for node in graph.graph:
            for neighbor, weight in graph.graph[node].items():
                self.G.add_edge(node, neighbor, weight=weight)

    def draw(
        self, path: list[str], total_distance: float, start: str, end: str
    ) -> None:
        """
        Draws the graph and highlights the shortest path.

        This method uses Matplotlib to render the graph, showing all nodes, edges,
        and their weights. The shortest path is highlighted with a thicker,
        differently colored edge.

        Args:
            path (list[str]): The shortest path, represented as a list of nodes.
            total_distance (float): The total distance of the shortest path.
            start (str): The starting node of the path.
            end (str): The ending node of the path.
        """
        pos = nx.spring_layout(self.G, seed=42)

        plt.figure(figsize=(12, 8))

        nx.draw_networkx_nodes(self.G, pos, node_size=700, node_color="skyblue")

        nx.draw_networkx_edges(self.G, pos, width=1, edge_color="gray")

        nx.draw_networkx_labels(self.G, pos, font_size=9, font_weight="bold")

        edge_labels = nx.get_edge_attributes(self.G, "weight")
        nx.draw_networkx_edge_labels(
            self.G, pos, edge_labels=edge_labels, font_color="green"
        )

        path_edges = list(zip(path, path[1:]))

        nx.draw_networkx_edges(
            self.G, pos, edgelist=path_edges, width=3, edge_color="red"
        )

        plt.title(f"Shortest Path from {start} to {end} (Distance: {total_distance})")

        plt.axis("off")

        plt.show()
