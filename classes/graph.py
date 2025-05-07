import classes.VertexState as VS

class Graph:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adjacency_list = {vertex: [] for vertex in range(num_vertices)}
        self.state = {state: VS.VertexState.STABLE for state in range(num_vertices)}
        self.water_needed = {water_needed: 0 for water_needed in range(num_vertices)}
        self.firefighters_quant = {firefighters_quant: 0 for firefighters_quant in range(num_vertices)}
    
    def add_edge(self, start: int, end: int, weight=1):  # O(1)
        self.adjacency_list[start].append((end, weight))
        self.adjacency_list[end].append((start, weight))
        
    def assemble_graph(
        self, 
        edges: list[tuple[int, int, int]],
        water_needed: dict[int, int], 
        firefighter_stations: list, 
        fire_start: int
    ): # O(E) beeing E the number of edges
        
        for vertex, water in water_needed.items(): # O(N)
            self.water_needed[vertex] = water
            if(vertex in firefighter_stations):
                new_quant = self.firefighters_quant[vertex] + 1
                self.firefighters_quant[vertex] = new_quant
        
        self.state[fire_start] = VS.VertexState.FIRE
        
        # Add edges with weights
        for source, target, cost in edges:
            self.add_edge(source, target, weight=cost)

    def propagate_fire(self, fire_start: int): # O(1)
        neighbors =  self.adjacency_list[fire_start]
        
        self.state[fire_start] =VS.VertexState.BURNED
        
        for neighbor, _ in neighbors:
            if self.state[neighbor] == VS.VertexState.STABLE:
                self.state[neighbor] = VS.VertexState.FIRE

    def attempt_to_extinguish_fire(self, vertex_fire: int, truck_capacity: int): # O(1)
        total_water = self.firefighters_quant[vertex_fire] * truck_capacity
        if(self.state[vertex_fire] == VS.VertexState.FIRE and self.water_needed[vertex_fire] <= total_water):
            self.state[vertex_fire] = VS.VertexState.STABILIZED
            self.report_fire_extinguished(vertex_fire)
            return

        self.request_additional_water(vertex_fire, total_water)
        return
    
    def report_fire_extinguished(self, vertex_fire: int): # O(1)
        if(self.state[vertex_fire] == VS.VertexState.STABILIZED):
            print(f"Fire at vertex {vertex_fire} extinguished.")
            return
            
    def request_additional_water(self, vertex_fire: int, total_water: int): # O(1)
        self.water_needed[vertex_fire] -= total_water
        if(self.state[vertex_fire] == VS.VertexState.FIRE):
            print(f"Need {self.water_needed[vertex_fire]} additional water for vertex {vertex_fire}.")
            return
    
    def __str__(self):
        result = f"Graph with {self.num_vertices} vertices\n"
        for vertex, neighbors in self.adjacency_list.items():
            result += f"  Vertex {vertex} -> {neighbors}\n"
        return result
