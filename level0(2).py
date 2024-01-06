import pandas as pd
import networkx as nx
import json

with open('level0.json') as f:
    data = json.load(f)
# Extract relevant information
n_neighbourhoods = data["n_neighbourhoods"]
neighbourhoods_data = data["neighbourhoods"]
restaurants_data = data["restaurants"]
vehicles_data = data["vehicles"]

# Create DataFrame for neighbourhood distances
df_neighbourhoods = pd.DataFrame(index=range(n_neighbourhoods), columns=range(n_neighbourhoods))

# Fill DataFrame with neighbourhood distances
for n, data in neighbourhoods_data.items():
    distances = data["distances"]
    df_neighbourhoods.loc[int(n[1:]), :] = distances

# Convert to numeric values
df_neighbourhoods = df_neighbourhoods.apply(pd.to_numeric, errors='coerce')

# Replace INF with infinity
df_neighbourhoods.replace("INF", float("inf"), inplace=True)

# Create graph from neighbourhood distances DataFrame
G_neighbourhoods = nx.from_pandas_adjacency(df_neighbourhoods)

# Create DataFrame for restaurant distances
df_restaurants = pd.DataFrame(index=range(1), columns=range(n_neighbourhoods))  # Assuming one restaurant

# Fill DataFrame with restaurant distances
for r, data in restaurants_data.items():
    restaurant_distances = data["neighbourhood_distance"]
    df_restaurants.loc[0, :] = restaurant_distances

# Convert to numeric values
df_restaurants = df_restaurants.apply(pd.to_numeric, errors='coerce')

# Replace INF with infinity
df_restaurants.replace("INF", float("inf"), inplace=True)

# Create graph from restaurant distances DataFrame
G_restaurants = nx.from_pandas_adjacency(df_restaurants)

# Combine both graphs
G_combined = nx.compose(G_neighbourhoods, G_restaurants)


# Function to perform DFS
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph.neighbors(node):
            dfs(graph, neighbor, visited)

# Starting node for DFS
start_node = 19

# Perform DFS on the combined graph
print("DFS Traversal:")
dfs(G_combined, start_node, set())