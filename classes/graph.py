from classes.edge import Edge

class Graph:
    def __init__(self, num_vertices, edges = []):
        self.num_vertices = num_vertices
        self.edges = edges
        
    
    def add_edge(self, start, end, weight=1):
        edge = Edge(start, end, weight)
        self.edges.append(edge)
    
    def __str__(self):
        result = f"Graph with {self.num_vertices} vertices and {len(self.edges)} edges\n"
        for edge in self.edges:
            result += f"  {edge}\n"
        return result