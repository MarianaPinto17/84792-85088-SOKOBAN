
class State():
    def __init__(self,boxes,keeper):
        self.boxes = boxes
        self.keeper = keeper

    def __str__(self):
        return f"Caixas: {self.boxes} | keeper: {self.keeper}"

        def __repr__ (self):
            return str(self)