class Node:
    def __init__(self,position,parent,depth,cost,heuristic):
        self.position = position
        self.parent = parent
        self.depth = depth 
        self.cost = cost
        self.heuristic = heuristic
        
    def __str__(self):
        return "node(" + str(self.state) + "," + str(self.parent) + ")"
    
    def __repr__(self):
        return str(self)
