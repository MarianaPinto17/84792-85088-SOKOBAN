from mapa import *
from node import *


def deadlock_corner(self,box):
    (x,y) = box.position
    #filter tiles devolve uma lista de todas as tiles de um tipo, percorro a lista ate encotrar as coordenadas ?
    up = get_tile((x,y+1))
    down = get_tile((x,y-1))
    left = get_tile((x-1,y))
    right = get_tile((x+1,y))
    
