class Node:
    def __init__(self,position,symbol):
        self.position = position #tuple
        self.symbol = symbol #char
        self.parent = None
        self.g = 0
        self.h = 0

    def f(self):
        return self.g + self.h
        