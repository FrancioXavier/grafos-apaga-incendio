class Edge:
    def __init__(self, start, end, weight=1):
        self.start = start
        self.end = end
        self.weight = weight
        
    def __str__(self):
        return f"Edge from {self.start} to {self.end} with weight {self.weight}"
