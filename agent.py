from mapa import *
from tree_search import SearchNode


def translate(solution):#translates the movements of the keeper to a wasd list
    res = []
    #print(solution)
    for x in range(1,len(solution)):
        print(f"new:{solution[x].keeper}old:{solution[x-1].keeper}")
        yaxis = solution[x].keeper[1] - solution[x-1].keeper[1]
        xaxis = solution[x].keeper[0] - solution[x-1].keeper[0]
        
        if xaxis == -1:
            res += 'a'
        if xaxis == 1:
            res += 'd'
        if yaxis == 1:
            res += 's'
        if yaxis == -1:
            res += 'w'
    return res




    
