from mapa import *
from tree_search import SearchNode


def translate(solution):#translates the movements of the keeper to a wasd list
    aux = list(solution)
    for a in aux:
        print(a.keeper)
    res = []
    for x in range(1,len(aux)):
        yaxis = aux[x].keeper[1] - aux[x-1].keeper[1]
        xaxis = aux[x].keeper[0] - aux[x-1].keeper[0]
        
        if xaxis == -1:
            res += 'a'
        if xaxis == 1:
            res += 'd'
        if yaxis == 1:
            res += 's'
        if yaxis == -1:
            res += 'w'
    return res




    
