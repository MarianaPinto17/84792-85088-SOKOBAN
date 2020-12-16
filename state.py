
class State():
    def __init__(self,boxes,keeper):
        self.boxes = boxes
        self.keeper = keeper

    def __str__(self):
        return f"Caixas: {self.boxes} | keeper: {self.keeper}"

    def __repr__ (self):
        return str(self)

    def __eq__(self,other):
        if not isinstance(other,State):
            return NotImplemented
        return self.boxes == other.boxes and self.keeper == other.keeper

    def __hash__(self):
        aux = tuple(self.boxes)
        return hash((aux, self.keeper))