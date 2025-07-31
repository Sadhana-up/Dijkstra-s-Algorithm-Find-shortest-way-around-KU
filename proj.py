import heapq
import networkx as nx
import matplotlib.pyplot as plt


graph = {
    'KU_Gate': {'Block_9': 2, 'Civil_Arch_Block': 4},
    'Block_9': {'KU_Gate': 2, 'Block_8': 2},
    'Block_8': {'Block_9': 2, 'Block_7': 2, 'Library': 3},
    'Block_7': {'Block_8': 2, 'Block_6': 2},
    'Block_6': {'Block_7': 2, 'Slope_1': 2},
    'Slope_1': {'Block_6': 2, 'KU_Cafe': 2},

    'Civil_Arch_Block': {'KU_Gate': 4, 'Pharmacy_Block': 2, 'Library': 3},  # changed
    'Pharmacy_Block': {'Civil_Arch_Block': 2, 'KU_Cafe': 3},

    'Library': {'Civil_Arch_Block': 3, 'Canteen_2': 2, 'Block_8': 3, 'KU_Cafe': 2},  # changed
    'Canteen_2': {'Library': 2},  # changed

    'KU_Cafe': {'Slope_1': 2, 'Pharmacy_Block': 3, 'Library': 2}
}

def dijkstra(graph, start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))


    path = []
    current = end
    while current:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    return path, distances[end]


start = 'KU_Gate'
end = 'KU_Cafe'
path, total_distance = dijkstra(graph, start, end)

print("Shortest Path:", " -> ".join(path))
print("Total Distance:", total_distance)


G = nx.Graph()
for node in graph:
    for neighbor, weight in graph[node].items():
        G.add_edge(node, neighbor, weight=weight)

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')
nx.draw_networkx_edges(G, pos, width=1, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='green')


path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='grey')

plt.title(f"Shortest Path from {start} to {end} (Distance: {total_distance})")
plt.axis('off')
plt.show()