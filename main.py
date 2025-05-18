
import read_data as read_data
import classes.graph as graph
import classes.Truck as truck
import classes.VertexState as VS
import classes.VertexType as VT
from collections import deque

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

    total_water_used = 0
    total_time = 0
     
    trucks = []
    truck_id = 0
    for i in range(len(firefighter_stations)):
        initial_position = firefighter_stations[i]

        #3 trucks per station
        for j in range (3):
            new_truck = truck.Truck(truck_capacity, initial_position, truck_id)
            trucks.append(new_truck)
            truck_id += 1
        
        
    # queue = deque()
    # queue.append(fire_start)
    # visited = set()
    
    # while queue:
    #     current = queue.popleft()
    #     vertex = graph_obj.vertices[current]

    #     if vertex.state == VS.VertexState.BURNED:
    #         continue

    #     visited.add(current)
    #     queue = graph_obj.propagate_fire(current, queue, visited)
        
    #     print(queue)
    
    # Inicialização - Execute uma vez antes do loop
    fire_vertices = set(v.id for v in graph_obj.vertices if v.state == VS.VertexState.FIRE)

    round_number = 0
    while fire_vertices:  # Continua enquanto houver fogo
        print(f"\n--- Rodada {round_number} ---")
        
        next_fire_vertices = set()
        
        # Processa apenas os vértices em chamas (não todos os vértices)
        next_fire_vertices = graph_obj.propagate_fire(fire_vertices, next_fire_vertices)
        
        # Atualiza conjunto de vértices em chamas para próxima rodada
        if not next_fire_vertices:
            print("O fogo não pode mais se espalhar.")
        else:
            print(f"Vértices que pegaram fogo: {next_fire_vertices}")
            
        fire_vertices = next_fire_vertices
        round_number += 1
        
        # Imprime apenas se necessário (reduzimos para O(1) relevantes em vez de O(V))
        if len(fire_vertices) < 10:  # Só imprime quando há poucos vértices
            print("Estado atual dos vértices em chamas:")
        else:
            print(f"Total de {len(fire_vertices)} vértices em chamas")

    print(f"Simulação encerrada após {round_number} rodadas.")