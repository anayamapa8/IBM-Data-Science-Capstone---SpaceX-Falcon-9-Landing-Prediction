#--- HEADER: GENERATE API CALL FLOWCHART
#--- Creating a simple visual flowchart of the SpaceX API data collection process.

import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes (steps in the process)
steps = [
    "Start",
    "Send GET Request\nto SpaceX API",
    "Receive JSON\nResponse",
    "Extract Launch\nRecords",
    "Filter:\nSingle Core & Payload",
    "Build Lookup\nDictionaries",
    "Extract Features\nwith Functions",
    "Create Final\nDataFrame",
    "End"
]

# Add edges (flow connections)
edges = [
    ("Start", "Send GET Request\nto SpaceX API"),
    ("Send GET Request\nto SpaceX API", "Receive JSON\nResponse"),
    ("Receive JSON\nResponse", "Extract Launch\nRecords"),
    ("Extract Launch\nRecords", "Filter:\nSingle Core & Payload"),
    ("Filter:\nSingle Core & Payload", "Build Lookup\nDictionaries"),
    ("Build Lookup\nDictionaries", "Extract Features\nwith Functions"),
    ("Extract Features\nwith Functions", "Create Final\nDataFrame"),
    ("Create Final\nDataFrame", "End")
]

# Add nodes and edges to the graph
G.add_nodes_from(steps)
G.add_edges_from(edges)

# Set up the plot
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G, seed=42, k=0.8)

# Draw nodes, edges, and labels
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightblue', edgecolors='black')
nx.draw_networkx_edges(G, pos, width=2, arrows=True, arrowsize=18) # * cambiado
nx.draw_networkx_labels(G, pos, font_size=8, font_weight='normal') # * cambiado

# Remove axes and display
plt.axis('off')
plt.title("SpaceX API Data Collection Flowchart", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()