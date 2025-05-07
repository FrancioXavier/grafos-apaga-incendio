
import read_data as read_data
import functions as f
if __name__ == "__main__":
    data = read_data.read_data("data.txt")

    num_vertices = data['num_vertices']
    num_edges = data['num_edges']
    fire_start = data['fire_start']
    water_needed = data['water_needed']
    firefighter_stations = data['firefighter_stations']
    edges = data['edges']
    truck_capacity = data['truck_capacity']

    graph = f.create_graph(
        num_vertices, 
        edges, 
        water_needed, 
        firefighter_stations, 
        fire_start
    )
    
    neighbors = f.put_out_fire(graph, fire_start, truck_capacity)
    
    print(neighbors)
