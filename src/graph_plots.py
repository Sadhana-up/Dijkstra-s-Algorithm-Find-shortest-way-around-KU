from typing import List, Dict

class Graph:
    """
    A class to represent a graph using an adjacency list.

    The graph is stored as a dictionary where keys are node identifiers (e.g., 'KU_Gate')
    and values are dictionaries of their neighbors with corresponding edge weights.

    Example of the internal graph structure:
    {
        'KU_Gate': {'Block_9': 2, 'Civil_Arch_Block': 4},
        'Block_9': {'KU_Gate': 2, 'Block_8': 2}
    }
    """

    def __init__(self) -> None:
        """
        Initializes an empty graph.
        """
        self.graph: Dict[str, Dict[str, int]] = {}

    def add_edge(self, u: str, v: str, weight: int) -> None:
        """
        Adds an undirected edge between two nodes with a given weight.

        If the nodes `u` or `v` do not exist in the graph, they are created.
        The edge is added in both directions, from `u` to `v` and from `v` to `u`.

        Args:
            u (str): The first node.
            v (str): The second node.
            weight (int): The weight of the edge between the nodes.
        """
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}
        
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def get_nodes(self) -> List[str]:
        """
        Returns a list of all nodes in the graph.

        Returns:
            List[str]: A list containing all the node identifiers.
        """
        return list(self.graph.keys())

    def get_neighbors(self, node: str) -> Dict[str, int]:
        """
        Returns the neighbors of a given node and the weights of the edges to them.

        Args:
            node (str): The node for which to get the neighbors.

        Returns:
            Dict[str, int]: A dictionary of neighbors, where keys are the neighbor nodes
                            and values are the edge weights. Returns an empty dictionary
                            if the node is not found.
        """
        return self.graph.get(node, {})
