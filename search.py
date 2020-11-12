from math import sqrt
from node import *
from consts import *

#distance tfrom start to goal
def heuristic(start,goal):
    #return(round(sqrt(pow((goal[0]-start[0]),2) + (pow((goal[1]-start[1]),2))))) #euclidiana
    return(abs(start.position[0] - goal.position[0])+ abs(start.position[1] - goal.position[1])) #manhattan

#A* algorithm
def astar(map,start,goal):

    #list of open and closed nodes (closed ones are the one that already have been visited)
    open_nodes = []
    closed_nodes = []

    start_node = Node(start,None,0,0)
    goal_node = Node(goal,None,0,0)
    
    open_nodes.append(start_node)

    while open_nodes != []:
        #sort the open_node list from lowest to highest cost
        open_nodes.sort()
        current_node = open_nodes.pop(0)
        closed_nodes.append(current_node)

        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
            #return reversed path
            return path [::-1]

        (x,y) = current_node.position

        #get neighbors position
        neighbors = [(x-1,y), (x+1, y), (x, y-1), (x, y+1)]

        for a in neighbors:
            #get value from map
            map_value = map.get(a)

            #if node is a wall finds another one
            if(map_value == Tiles.WALL):
                continue

            neighbor = Node(a,current_node,heuristic(start,neighbor),heuristic(neighbor,goal))
            neighbor.evalfunc = neighbor.cost + neighbor.heuristic

            if(add_to_open(open_nodes,neighbor) == True):
                open_nodes.append(neighbor)

    #NO PATH FOUND :(
    return None

#Check if a neighbor should be added to open_nodes list
def add_to_open(open_nodes,neighbor):
    for node in open_nodes:
        if(neighbor == node and neighbor.evalfunc >= node.evalfunc):
            return False
    return True