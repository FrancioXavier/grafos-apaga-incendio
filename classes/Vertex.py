import classes.VertexType as VT
import classes.VertexState as VS

class Vertex:
    def __init__(self, id, type: VT):
        self.id = id
        self.type = type
        self.neighbors = []      # se o fogo foi apagado
        self.state = VS.VertexState.STABLE
        self.water_needed = 0

    def can_burn(self) -> bool:
        return (self.type == VT.VertexType.FOREST or self.type == VT.VertexType.LAKE) and self.state == VS.VertexState.STABLE
    
    def is_water_source(self) -> bool:
        return self.type in {VT.VertexType.LAKE, VT.VertexType.FIRE_STATION}
    
    def trying_to_extinguish(self, truck_capacity: int) -> bool:
        total_water = truck_capacity
        if(self.state == VS.VertexState.FIRE and self.water_needed <= total_water):
            self.state = VS.VertexState.STABILIZED
            return True

        self.request_additional_water(total_water)
        return False

    def request_additional_water(self, total_water: int): # O(1)
        if (self.water_needed <= total_water):
            self.water_needed -= total_water

        return