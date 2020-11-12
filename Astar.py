from math import sqrt
from agent.node import *

def heuristic(start,goal):
    #return(round(sqrt(pow((goal[0]-start[0]),2) + (pow((goal[1]-start[1]),2))))) #euclidiana
    return(abs(start.position[0] - goal.position[0])+ abs(start.position[1] - goal.position[1])) #manhattan

#finds path from start to goal
def find_path(mapa,start,goal):
    root = Node(start,None,0,0)

# Reconstruct path to a given node (using Node class prev field)
def reconstruct_path(target):
    pass



