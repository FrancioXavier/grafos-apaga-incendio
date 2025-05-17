
import read_data as read_data
import classes.graph as graph
import classes.Truck as truck

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
        fire_start,
        water_collection_points
    )
    
    trucks = []
    
    for i in range(len(firefighter_stations)):
        truck_id = firefighter_stations[i]

        #3 trucks per station
        for j in range (3):
            new_truck = truck.Truck(truck_capacity, truck_id)
            trucks.append(new_truck)

    print("Trucks created:")
    for i in range(len(trucks)):
        print(f"Truck {i}: ID {trucks[i].id}, Capacity {trucks[i].capacity}")

    for i in range(9):
        print(trucks[i].dijkstra(graph_obj, water_collection_points))