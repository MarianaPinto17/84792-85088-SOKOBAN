class Node:
    def __init__(self,position,parent,cost,heuristic):
        self.position = position
        self.parent = parent
        self.depth = self.parent.depth + 1 if self.parent != None else 0
        self.cost = cost
        self.heuristic = heuristic
        
    def __str__(self):
        return "node(" + str(self.state) + "," + str(self.parent) + ")"
    
    def __repr__(self):
        return str(self)
