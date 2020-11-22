
class State():
    def __init__(self,boxes,keeper):
        self.boxes = boxes
        self.keeper = keeper

    def __str__(self):
        return f"Caixas: {self.boxes} | keeper: {self.keeper}"