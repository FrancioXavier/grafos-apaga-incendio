import classes.Vertex as V
import classes.graph as g


class Truck:
    def __init__(self, capacity: int, id: int):
        self.id = id
        self.capacity = capacity
        
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

        distances[self.id] = 0
        
        distances_list_vertices = [float('inf')] * len(vertices)

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
                            pass
                        
            

        return self.get_path(previous, vertices)

    def get_path(self, previous: list[int], vertices: list[int]) -> list[V.Vertex]:
        path = []
        for vertex in vertices:
            if previous[vertex] is not None:
                path.append(vertex)
                
        print(f"Truck {self.id} path: {path}")

        return path
