"""
This file defines the graph structure for the KU campus map.
The graph is represented as a list of tuples, where each tuple defines an edge
in the format: (start_node, end_node, weight).
- start_node: The starting point of the edge.
- end_node: The ending point of the edge.
- weight: The distance or cost to travel between the two nodes.

For example, the tuple ("KU_Gate", "Block_9", 2) represents an edge between
"KU_Gate" and "Block_9" with a weight of 2.
"""

graph = [
    # Edges starting from KU_Gate
    ("KU_Gate", "Block_9", 2),
    ("KU_Gate", "Civil_Arch_Block", 4),
    # Edges starting from Block_9
    ("Block_9", "Block_8", 2),
    ("Block_8", "Block_7", 2),

    ("Block_8", "Library", 3),
    ("Block_7", "Block_6", 2),

    ("Block_6", "Slope_1", 2),

    ("Slope_1", "KU_Cafe", 2),

    ("Civil_Arch_Block", "Pharmacy_Block",2),
    ("Civil_Arch_Block", "Library", 3),
    ("Pharmacy_Block", "KU_Cafe", 3),

    ("Library", "Canteen_2", 2),

    ("Library", "KU_Cafe", 2),
]
