from classes.graph import Graph

def create_graph(num_vertices, edges, water_needed, firefighter_stations, fire_start): # O(E) beeing E the number of edges
    G = Graph(num_vertices)
    
    for vertex, water in water_needed.items(): # O(N)
        G.set_water_needed(vertex, water)
        if(vertex in firefighter_stations):
            new_quant = G.get_firefighters_quant(vertex) + 1
            G.set_firefighters_quant(vertex, new_quant)
    
    G.set_state(fire_start, "fire")
    
    # Add edges with weights
    for source, target, cost in edges:
        G.add_edge(source, target, weight=cost)
    
    return G

def fire_propagation(graph: Graph, fire_start): # O(1)
    neighbors =  graph.get_neighbors(fire_start)
    
    graph.set_state(fire_start, "burned")
    
    for neighbor, _ in neighbors:
        if graph.get_state(neighbor) == "stable":
            graph.set_state(neighbor, "fire")
    
    return neighbors

def put_out_fire(graph: Graph, vertex_fire: int, truck_capacity: int): # O(1)
    total_water = graph.get_firefighters_quant(vertex_fire) * truck_capacity
    if(graph.get_state(vertex_fire) == "fire" and graph.get_water_needed(vertex_fire) <= total_water):
        graph.set_state(vertex_fire, "stabilized")
        return True
    return False