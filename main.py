
import read_data as read_data
import functions as f
if __name__ == "__main__":
    data = read_data.read_data("data.txt")

    num_vertices = data['num_vertices']
    num_edges = data['num_edges']
    fire_start = data['fire_start']
    water_needed = data['water_needed']

    graph = f.create_graph(num_vertices, data['edges'])
    
    for vertex, water in water_needed.items(): # O(N)
        graph.set_water_needed(vertex, water)
    
    flame = graph.set_state(fire_start, "fire")
    
    neighbors = f.fire_propagation(graph, fire_start)
