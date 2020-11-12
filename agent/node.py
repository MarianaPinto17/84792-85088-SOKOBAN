class Node:
    def __init__(self,position,parent,heuristic,cost):
        self.position = position #tuple
        self.parent = None
        self.heuristic = heuristic
        self.cost = cost
        self.evalfunc = heuristic + cost
        