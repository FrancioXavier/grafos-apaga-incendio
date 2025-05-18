import classes.Vertex as V
import classes.graph as g
from classes.BinaryHeap import BinaryHeap

class Truck:
    def __init__(self, capacity: int, position: int, id: int):
        self.id = id
        self.capacity = capacity
        self.position = position
        self.current_capacity = capacity
        self.path = []
        
    def emptying_tank(self, water_needed: int) -> int:
        if water_needed >= self.capacity:
            self.capacity = 0
            return water_needed - self.capacity
        
        self.capacity -= water_needed
        return 0
    
    def dijkstra(self, graph: g.Graph, vertices: list[int]) -> list[V.Vertex]:
        distances = [float('inf')] * graph.num_vertices
        previous = [None] * graph.num_vertices
        distances[self.position] = 0

        min_heap = BinaryHeap(is_min_heap=True)
        min_heap.push((0, self.position))
        
        closest_target = None
        min_target_distance = float('inf')
        
        target_set = set(vertices)
        
        while min_heap.heap:
            current_distance, current_vertex = min_heap.pop()
            
            if current_distance > distances[current_vertex]:
                continue
            
            if current_vertex in target_set and current_distance < min_target_distance:
                closest_target = current_vertex
                min_target_distance = current_distance
            
            for neighbor, weight in graph.adjacency_list[current_vertex]:
                new_distance = distances[current_vertex] + weight
                
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_vertex
                    min_heap.push((new_distance, neighbor))
        
        if closest_target is None:
            return [0, []]
        path = self.get_path(closest_target, previous)
 
        return [closest_target, path]

    def get_path(self, target: int, previous: list[int]) -> list[int]:
        path = []
        current = target

        while current is not None:
            path.append(current)
            current = previous[current]
        
        return path[::-1]
    
    def refueling_water(self, water_collections: list[int]) -> int:
        if (self.position in water_collections):
            self.current_capacity = self.capacity
            print(f"Truck refueled at vertex {self.position}.")
            return 0
        
        print(f"Position {self.position} is not at a water collection point.")
        return 0
