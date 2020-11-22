from tree_search import *
from mapa import Map
from consts import Tiles 
from state import State

class Sokosolver(SearchDomain):
    def __init__ (self,mapa):
        self.goals = mapa.filter_tiles([Tiles.GOAL]) + mapa.filter_tiles([Tiles.BOX_ON_GOAL]) + mapa.filter_tiles([Tiles.MAN_ON_GOAL])
        self.boxes = mapa.filter_tiles([Tiles.BOX]) + mapa.filter_tiles([Tiles.BOX_ON_GOAL])
        self.keeper = mapa.keeper
        self.walls = mapa.filter_tiles([Tiles.WALL])

    def actions(self, state):
        
        #keeper neighborhood
        up = (state.keeper[0] + 1 ,state.keeper[1])
        down = (state.keeper[0] - 1, state.keeper[1])
        left = (state.keeper[0], state.keeper[1] - 1)
        right = (state.keeper[0], state.keeper[1] + 1)
        neighbor = [up,down,left,right]

        pstate = [] #possible states

        for x in neighbor:
            if x not in self.walls:
                pstate.append(x)
        
        print(f"Next states: {pstate}")

        return pstate
            

    # resultado de uma accao num estado, ou seja, o estado seguinte
    def result(self, state, action):
        new_state = State(state.boxes,action)
        #new_state.keeper = action
        return new_state

    # custo de uma accao num estado
    def cost(self, state, action):
        return 1

    # custo estimado de chegar de um estado a outro
    def heuristic(self, state, goal):
        pass

    # test if the given "goal" is satisfied in "state"
    def satisfies(self, state, goal):
        if set(state.boxes).issubset(goal):
            return True
        else:
            return False