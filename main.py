# Import necessary classes and data
from src import Graph, Dijkstra, GraphVisualizer
from constants import graph
from icecream import ic

def main():
    """
    Main function to execute the Dijkstra's algorithm and visualize the graph.

    This function performs the following steps:
    1. Initializes a graph instance.
    2. Populates the graph with edges and weights from the `constants.graph` data.
    3. Runs Dijkstra's algorithm to find the shortest path between a specified start and end node.
    4. Prints the shortest path and total distance using the `icecream` library for debugging.
    5. Visualizes the entire graph, highlighting the shortest path.
    """
    # Create a new graph instance
    graph_instance = Graph()

    # Add all the edges to the graph from the `constants/nodes.py` file
    # The graph is represented as a list of tuples, where each tuple
    # contains the start node, end node, and the weight of the edge.
    for start_node, end_node, weight in graph:
        graph_instance.add_edge(start_node, end_node, weight)

    # Create an instance of the Dijkstra class with the graph
    dikstra_instance = Dijkstra(graph_instance)

    # Define the start and end nodes for which to find the shortest path
    start, end = "KU_Gate", "KU_Cafe"

    # Find the shortest path and total distance using Dijkstra's algorithm
    shortest_path, total_distance = dikstra_instance.find_shortest_path(start, end)

    # Use icecream to print the shortest path and total distance for easy debugging
    ic(shortest_path, total_distance)

    # Create an instance of the GraphVisualizer to draw the graph
    visiualizer = GraphVisualizer(graph_instance)

    # Draw the graph, highlighting the shortest path
    visiualizer.draw(shortest_path, total_distance, start, end)


if __name__ == "__main__":
    # This ensures that the main function is called only when the script is executed directly
    main()
