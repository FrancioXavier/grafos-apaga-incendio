
import read_data as read_data
import classes.graph as graph
import classes.Truck as truck
from collections import deque
import classes.VertexState as VS

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
    truck_id = 0
    
    for i in range(len(firefighter_stations)):
        initial_position = firefighter_stations[i]

        #3 trucks per station
        for j in range (3):
            new_truck = truck.Truck(truck_capacity, initial_position, truck_id)
            trucks.append(new_truck)
            truck_id += 1
            
            print(f"Truck {new_truck.id} in position {new_truck.position} created with capacity {new_truck.capacity}.")

    for i in range(9):
        print(trucks[i].dijkstra(graph_obj, water_collection_points))
        
    
        
    # queue = deque()
    # queue.append(fire_start)
    # visited = set()
    
    # while queue:
    #     current = queue.popleft()
    #     vertex = graph.vertices[current]

    #     if vertex.state == VS.VertexState.BURNED:
    #         continue

    #     visited.add(current)
    #     queue = graph_obj.propagate_fire(current)
    
    # while True:
        
        
    #     break