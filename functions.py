from classes.graph import Graph

def create_graph(num_vertices, edges): # O(E) beeing E the number of edges
    G = Graph(num_vertices)
    
    # Add edges with weights
    for source, target, cost in edges:
        G.add_edge(source, target, weight=cost)
    
    return G

def fire_propagation(graph: Graph, fire_start): # O(1)
    neighbors =  graph.get_neighbors(fire_start)
    
    return neighbors
    