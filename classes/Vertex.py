import classes.VertexType as VT
import classes.VertexState as VS

class Vertex:
    def __init__(self, id, type: VT):
        self.id = id
        self.type = type
        self.neighbors = []             # lista de vértices adjacentes
        self.burning = False            # apenas relevante para vertices FOREST
        self.estabilized = False        # se o fogo foi apagado
        self.state = VS.VertexState.STABLE
        self.water_needed = 0
        self.firefighters_quant = 0

    def can_burn(self) -> bool:
        return self.type == VT.VertexType.FOREST and not self.burning and not self.estabilized
    
    def is_water_source(self) -> bool:
        return self.type in {VT.VertexType.LAKE, VT.VertexType.FIRE_STATION}
    
    def trying_to_extinguish(self, truck_capacity: int) -> bool:
        total_water = self.firefighters_quant * truck_capacity
        if(self.state == VS.VertexState.FIRE and self.water_needed <= total_water):
            self.state = VS.VertexState.STABILIZED
            self.report_fire_extinguished()
            return

        self.request_additional_water(total_water)
        return

    def report_fire_extinguished(self): # O(1)
        if(self.state == VS.VertexState.STABILIZED):
            print(f"Fire at vertex {self.id} extinguished.")
            return

    def request_additional_water(self, total_water: int): # O(1)
        if (self.water_needed <= total_water):
            self.water_needed -= total_water

        if(self.state == VS.VertexState.FIRE):
            print(f"Need {self.water_needed} additional water for vertex {self.id}.")
            return