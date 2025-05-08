
import read_data as read_data
import classes.graph as graph
if __name__ == "__main__":
    data = read_data.read_data("data.txt")

    num_vertices = data['num_vertices']
    num_edges = data['num_edges']
    fire_start = data['fire_start']
    water_needed = data['water_needed']
    firefighter_stations = data['firefighter_stations']
    edges = data['edges']
    truck_capacity = data['truck_capacity']
    water_collection_points = data['water_collection_points']
    
    graph_obj = graph.Graph(num_vertices)


    graph = graph_obj.assemble_graph(
        edges, 
        water_needed, 
        firefighter_stations, 
        fire_start
    )
    
    graph_obj.propagate_fire(fire_start)

