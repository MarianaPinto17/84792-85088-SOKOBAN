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

    def actions(self, state):

        #keeper neighborhood
        up = (state.keeper[0] ,state.keeper[1] - 1)
        down = (state.keeper[0], state.keeper[1] + 1)
        left = (state.keeper[0] - 1 , state.keeper[1])
        right = (state.keeper[0] + 1, state.keeper[1])
        neighbor = [up,down,left,right]

        pstate = [] #possible states
        
        for x in neighbor:
            #se não é parede o keeper não vai para lá
            if x not in self.walls:
                pstate.append(x)
        
        #print(f"Next states: {pstate}")

        return pstate
    
    # resultado de uma accao num estado, ou seja, o estado seguinte
    def result(self, state, action):

        new_state = State(state.boxes,action)
        # if action is go to box I push the box
        if action in state.boxes: #se a açao está em state.boxes
            #keeper coordinates
            (x1,y1) = state.keeper
            #action coordinates
            (x2,y2) = action
            #calculate the new coordinates of the box
            xres = x2 + (x2 - x1)
            yres = y2 + (y2 - y1)
            
            if (xres,yres) not in self.walls and (xres,yres) not in self.boxes:#prevents pushing into walls and boxes
                if deadlock_corner((xres,yres),self.walls) or (xres,yres) in self.goals: #prevents corner deadlocks
                    auxlist = state.boxes[:]
                    index = auxlist.index(action)
                    auxlist[index] = (xres,yres)
                    new_state = State(auxlist,action)
                else:
                    return None
            else:
                return None
        
        return new_state

    # custo de uma accao num estado
    def cost(self, state, action):
        return 1

    # custo estimado de chegar de um estado a outro
    def heuristic(self, state, goal):
        pass

    # test if the given "goal" is satisfied in "state"
    def satisfies(self, state, goal):
        return set(state.boxes)== set(goal)
