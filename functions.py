from classes.graph import Graph
def create_graph(num_vertices, edges):
    G = Graph(num_vertices)
    
    # Add edges with weights
    for source, target, cost in edges:
        G.add_edge(source, target, weight=cost)
    
    return G