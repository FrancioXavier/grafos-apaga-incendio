import networkx as nx
def create_graph(num_vertices, edges):
    G = nx.Graph()
    
    # Add vertices
    G.add_nodes_from(range(num_vertices))
    
    # Add edges with weights
    for source, target, cost in edges:
        G.add_edge(source, target, weight=cost)
    
    return G