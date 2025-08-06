import heapq
from src import Graph


class Dijkstra:
    """
    A class to find the shortest path in a graph using Dijkstra's algorithm.

    Attributes:
        graph (Graph): An instance of the Graph class representing the graph.
    """

    def __init__(self, graph: Graph):
        """
        Initializes the Dijkstra class with a graph.

        Args:
            graph (Graph): The graph on which to perform the algorithm.
        """
        self.graph = graph

    def find_shortest_path(self, start: str, end: str) -> tuple[list[str], float]:
        """
        Finds the shortest path from a start node to an end node using Dijkstra's algorithm.

        The algorithm works by maintaining a set of visited nodes and a priority queue of nodes
        to visit, prioritized by their distance from the start node. It iteratively selects the
        node with the smallest distance, updates the distances of its neighbors, and adds them
        to the priority queue.

        Args:
            start (str): The starting node.
            end (str): The ending node.

        Returns:
            tuple[list[str], float]: A tuple containing the shortest path as a list of nodes
                                     and the total distance of the path.
        """
        # Priority queue to store nodes to visit, with priority as the distance.

        queue = [(0, start)]

        distances = {node: float("inf") for node in self.graph.get_nodes()}

        previous_nodes = {node: None for node in self.graph.get_nodes()}

        distances[start] = 0

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            # If the current node is the end node, we have found the shortest path.
            if current_node == end:
                break

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph.get_neighbors(current_node).items():
                distance = current_distance + weight

                # If a shorter path to the neighbor is found, update the distance and predecessor.
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))

        # Reconstruct the shortest path from the end node to the start node.
        path = []
        current = end
        while current:
            path.append(current)
            current = previous_nodes[current]
        path.reverse()  # Reverse the path to get it from start to end.

        return path, distances[end]
