from mapa import *
from tree_search import SearchNode


def translate(self,solution):#translates the movements of the keeper to a wasd list
    res = []
    for x in solution:
        for i in range(len(solution)-1):
            parent = x[i+1]
            state = x[i]
            m =  parent - state
            if m == (0,1):
                res.append('w')
            elif m == (0,-1):
               res.append('s')
            elif m == (1,0):
                res.append('d')
            elif m == (-1,0):
                res.append('a')
    
    return res