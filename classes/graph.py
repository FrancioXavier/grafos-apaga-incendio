import classes.VertexState as VS
import classes.Vertex as V
import classes.VertexType as VT

class Graph:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.vertices = [i for i in range(num_vertices)]
        self.adjacency_list = {vertex: [] for vertex in range(num_vertices)}
    
    def add_edge(self, start: int, end: int, weight=1):  # O(1)
        self.adjacency_list[start].append((end, weight))
        self.adjacency_list[end].append((start, weight))
        
    def assemble_graph(
        self, 
        edges: list[tuple[int, int, int]],
        water_needed: dict[int, int], 
        firefighter_stations: list, 
        fire_start: int,
        water_collect_points:list
    ): # O(E) beeing E the number of edges
        
        for vertex in self.vertices: # O(N)
            if vertex in [fs for fs in firefighter_stations]:
                vertex = V.Vertex(vertex, VT.VertexType.FIRE_STATION)
            elif vertex in [wcp for wcp in water_collect_points]:
                vertex = V.Vertex(vertex, VT.VertexType.LAKE)
            else:
                vertex = V.Vertex(vertex, VT.VertexType.FOREST)
            
            if vertex.id == fire_start and vertex.type == VT.VertexType.FOREST:
                vertex.state = VS.VertexState.FIRE
            
            vertex.water_needed = water_needed[vertex.id]

            if(vertex in firefighter_stations):
                vertex.firefighters_quant += 1
                
            self.vertices[vertex.id] = vertex

        for source, target, cost in edges:
            self.add_edge(source, target, weight=cost)


    def propagate_fire(self, fire_vertices: set, next_fire_vertices: set): # O(v) sendo v o numero de vizinhos ao redor do vertice
        for v_id in fire_vertices:
            vertex = self.vertices[v_id]
            vertex.state = VS.VertexState.BURNED
            
            # Verifica apenas vizinhos que são estáveis e tipo floresta
            for neighbor_id, _ in self.adjacency_list[v_id]:
                neighbor_vertex = self.vertices[neighbor_id]
                if neighbor_vertex.can_burn():
                    neighbor_vertex.state = VS.VertexState.FIRE
                    next_fire_vertices.add(neighbor_id)
        return next_fire_vertices
    

    def attempt_to_extinguish_fire(self, vertex_fire: int, truck_capacity: int): # O(1)
        vertex = self.vertices[vertex_fire]
        return vertex.trying_to_extinguish(truck_capacity)
    
    def compare_costs(self, vertex_id: int, destiny_id: int, current_cost: int):
        for id_value, weight_edge in self.adjacency_list[vertex_id]:
            if id_value == destiny_id:
                weight = weight_edge
                break
        
        if current_cost >= weight:
            return (True, current_cost - weight)

        return (False, current_cost)
        
    
    def __str__(self):
        result = f"Graph with {self.num_vertices} vertices\n"
        for vertex, neighbors in self.adjacency_list.items():
            result += f"  Vertex {vertex} -> {neighbors}\n"
        result += "\n"
        for vertex in self.vertices:
            result += f"  Vertex {vertex.id}: Type: {vertex.type}, State: {vertex.state}, Water Needed: {vertex.water_needed}\n"
        return result
