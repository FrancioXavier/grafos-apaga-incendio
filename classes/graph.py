class Graph:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adjacency_list = {vertex: [] for vertex in range(num_vertices)}
        self.state = {state: "stable" for state in range(num_vertices)}
        self.water_needed = {water_needed: 0 for water_needed in range(num_vertices)}
    
    def add_edge(self, start: int, end: int, weight=1):  # O(1)
        self.adjacency_list[start].append((end, weight))
        self.adjacency_list[end].append((start, weight))
    
    def get_neighbors(self, vertex: int):  # O(1)
        return self.adjacency_list[vertex]
    
    def get_state(self, vertex: int):  # O(1)
        return self.state[vertex]
    
    def set_state(self, vertex: int, state: str):  # O(1)
        self.state[vertex] = state
        
    def set_water_needed(self, vertex: int, water: int):  # O(1)
        self.water_needed[vertex] = water
    
    def change_state(self, state: str):  # O(1) 
         self.state = state
    
    def __str__(self):
        result = f"Graph with {self.num_vertices} vertices\n"
        for vertex, neighbors in self.adjacency_list.items():
            result += f"  Vertex {vertex} -> {neighbors}\n"
        return result
