import pandas as pd
import networkx as nx
import json
#df = pd.read_json('level0.json')
#d = pd.DataFrame(df)
#print(d)

with open('level0.json') as f:
    data = json.load(f)

n_neighbourhoods = data["n_neighbourhoods"]
neighbourhoods_data = data["neighbourhoods"]

# Create DataFrame
df = pd.DataFrame(index=range(n_neighbourhoods), columns=range(n_neighbourhoods))

# Fill DataFrame with distances
for n, data in neighbourhoods_data.items():
    distances = data["distances"]
    df.loc[int(n[1:]), :] = distances

# Convert to numeric values
df = df.apply(pd.to_numeric, errors='coerce')

# Replace INF with infinity
df.replace("INF", float("inf"), inplace=True)

print(df)

G = nx.from_pandas_adjacency(df)

# Compute Dijkstra's algorithm
source_node = 0  # You can change this to the desired source node
shortest_paths = nx.single_source_dijkstra_path_length(G, source=source_node)

# Display the results
print("Shortest Paths from Node {}:".format(source_node))
for node, distance in shortest_paths.items():
    print("Node {}: Distance {}".format(node, distance))