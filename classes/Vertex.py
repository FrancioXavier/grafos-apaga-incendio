import VertexType as VT

class Vertex:
    def __init__(self, id, type: VT):
        self.id = id
        self.type = type
        self.neighbors = []             # lista de vértices adjacentes
        self.burning = False            # apenas relevante para vertices FOREST
        self.estabilized = False        # se o fogo foi apagado

    def can_burn(self) -> bool:
        return self.type == VT.VertexType.FOREST and not self.burning and not self.estabilized
    
    def is_water_source(self) -> bool:
        return self.type in {VT.VertexType.LAKE, VT.VertexType.FIRE_STATION}