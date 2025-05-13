import classes.Vertex as V
import classes.graph as g


class Truck:
    def __init__(self, capacity: int, id: int):
        self.id = id
        self.capacity = capacity
        self.position = id
        self.current_capacity = capacity
        
    def emptying_tank(self, water_needed: int) -> int:
        if water_needed >= self.capacity:
            self.capacity = 0
            return water_needed - self.capacity
        
        self.capacity -= water_needed
        return 0
    
    def dijkstra(self, graph: g.Graph, vertices: list[int]) -> list[V.Vertex]:
        visited = [False] * graph.num_vertices
        distances = [float('inf')] * graph.num_vertices
        previous = [None] * graph.num_vertices

        distances[self.position] = 0
        
        lower_cost = [0, 0]

        for _ in range(graph.num_vertices):
            min_distance = float('inf')
            min_vertex = -1
            
            for vertex in range(graph.num_vertices):
                if not visited[vertex] and distances[vertex] < min_distance:
                    min_distance = distances[vertex]
                    min_vertex = vertex

            if min_vertex == -1:
                break

            visited[min_vertex] = True

            for neighbor, weight in graph.adjacency_list[min_vertex]:
                if not visited[neighbor]:
                    new_distance = distances[min_vertex] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous[neighbor] = min_vertex

                        if neighbor in vertices:
                            lower_cost[0] = neighbor
                            lower_cost[1] = new_distance

        return lower_cost

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
