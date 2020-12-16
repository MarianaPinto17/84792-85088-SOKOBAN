from tree_search import *
from mapa import Map
from consts import Tiles 
from state import State
from translation import translate
from deadlock import deadlock_corner
import copy
class Sokosolver(SearchDomain):
    
    def __init__ (self,mapa):
        self.goals = mapa.filter_tiles([Tiles.GOAL]) + mapa.filter_tiles([Tiles.BOX_ON_GOAL]) + mapa.filter_tiles([Tiles.MAN_ON_GOAL])
        self.boxes = mapa.filter_tiles([Tiles.BOX]) + mapa.filter_tiles([Tiles.BOX_ON_GOAL])
        self.keeper = mapa.keeper
        self.walls = mapa.filter_tiles([Tiles.WALL])
        self.pairs = list()
        self.deadlock = []#hardcoded deadlocks

    def pair(self):
        all_pairs = list()
        valid_pairs = list()
        valid_goals = list()
        valid_boxes = list()
        result = list()
        for goal in self.goals:
            for box in self.boxes:
                dist = abs(box[0] - goal[0]) + abs(box[1] - goal[1])
                all_pairs.append((goal,box,dist))
            all_pairs.sort(key = lambda tup: tup[2])
        
        for x in all_pairs:
            if x[0] not in valid_goals and x[1] not in valid_boxes:
                valid_pairs.append(x)
                valid_boxes.append(x[1])
                valid_goals.append(x[0])
        
        for x in self.boxes:
            for y in valid_pairs:
                if x == y[1]:
                    result.append(y)
        self.pairs = result
    def actions(self, state):

        #keeper neighborhood
        up = (state.keeper[0] ,state.keeper[1] - 1)
        down = (state.keeper[0], state.keeper[1] + 1)
        left = (state.keeper[0] - 1 , state.keeper[1])
        right = (state.keeper[0] + 1, state.keeper[1])
        neighbor = {up,down,left,right}

        pstate = set() #possible states
        
        for x in neighbor: #check if keeper is going into a wall
            if x not in self.walls:
                pstate.add(x)
        return pstate
    
    # resultado de uma accao num estado, ou seja, o estado seguinte
    def result(self, state, next_move):
        new_state = State(state.boxes,next_move)
        # if action is go to box I push the box
        
        if next_move in state.boxes: #se a açao está em state.boxes
            #keeper coordinates
            (x1,y1) = state.keeper
            #action coordinates
            (x2,y2) = next_move
            #calculate the new coordinates of the box
            xres = x2 + (x2 - x1)
            yres = y2 + (y2 - y1)
            if (xres,yres) in self.goals or not deadlock_corner((xres,yres),self.walls): #prevents corner deadlocks
                if (xres,yres) not in self.walls and (xres,yres) not in state.boxes:#prevents pushing into walls and boxes
                    if (xres,yres) not in self.deadlock:
                        auxlist = state.boxes[:]
                        index = auxlist.index(next_move)
                        auxlist[index] = (xres,yres)
                        new_state = State(auxlist,next_move)
                    else:
                        return None    
                else:
                    return None
            else:
                return None
        return new_state

    # custo de uma accao num estado
    def cost(self, state, next_move):
        #distanca do keeper 
        return 1

    # custo estimado de chegar de um estado a outro
    def heuristic(self, state, goal):
        
        #i = 0
        #for s in state.boxes:
        #    if s in self.goals:
        #        i += 1
        #return i

        #Simple lower bound
        #é a soma das dsitancias entre as caixas até ao goal mais proximo
        
        # result = 0
        # for box in state.boxes:
        #     aux = set()
        #     for goal in self.goals:
        #         dist = abs(box[0] - goal[0]) + abs(box[1] - goal[1])
        #         aux.add(dist)
        #     result += min(aux) 
        # return result

        #Minimum Matching Lower Bound(GREEDY)
        
        result = 0
        for i in range(len(state.boxes)):
            result += abs(state.boxes[i][0]-self.pairs[i][0][0]) + abs(state.boxes[i][1]-self.pairs[i][0][1])        
        return result
            

    # test if the given "goal" is satisfied in "state"
    def satisfies(self, state, goal):
        return set(state.boxes)== set(goal)
