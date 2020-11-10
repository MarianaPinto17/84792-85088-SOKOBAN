
from math import *
from agent import Node
from agent import const
from abc import ABC, abstractmethod

#returns the distance between two points
def distance(orig,dest):
    return dist(orig,dest)


class SearchDomain(ABC):

    # construtor
    @abstractmethod
    def __init__(self):
        pass

    # lista de accoes possiveis num estado
    @abstractmethod
    def actions(self, state):
        pass

    # resultado de uma accao num estado, ou seja, o estado seguinte
    @abstractmethod
    def result(self, state, action):
        pass

    # custo de uma accao num estado
    @abstractmethod
    def cost(self, state, action):
        pass

    # custo estimado de chegar de um estado a outro
    @abstractmethod
    def heuristic(self, state, goal):
        pass

    # test if the given "goal" is satisfied in "state"
    @abstractmethod
    def satisfies(self, state, goal):
        pass


# Problemas concretos a resolver
# dentro de um determinado dominio
class SearchProblem:
    def __init__(self, domain, initial, goal):
        self.domain = domain
        self.initial = initial
        self.goal = goal
    def goal_test(self, state):
        return self.domain.satisfies(state,self.goal)

# Nos de uma arvore de pesquisa
class SearchNode:
    def __init__(self,state,parent,cost=0): 
        self.state = state
        self.parent = parent
        self.cost = cost
        self.depth = self.parent.depth + 1 if self.parent != None else 0
    def __str__(self):
        return "no(" + str(self.state) + "," + str(self.parent) + ")"
    def __repr__(self):
        return str(self)

# Arvores de pesquisa
class SearchTree:

    # construtor
    def __init__(self,problem, strategy='astar'): 
        self.problem = problem
        root = SearchNode(problem.initial, None)
        self.open_nodes = [root]
        self.strategy = strategy
        self.terminals = 0
        self.non_terminals = 0

    # obter o caminho (sequencia de estados) da raiz ate um no
    def get_path(self,node):
        if node.parent == None:
            return [node.state]
        path = self.get_path(node.parent)
        path += [node.state]
        return(path)
    
    def length(self):
        return self.solution.depth

    @property
    def avg_ramification(self):
        return (self.terminals + self.non_terminals - 1) / self.non_terminals

    # procurar a solucao
    def search(self,limit=None):
        while self.open_nodes != []:
            node = self.open_nodes.pop(0)
            self.non_terminals += 1
            self.terminals = len(self.open_nodes)
            if self.problem.goal_test(node.state): #check if solution
                self.solution = node
                self.cost = self.solution.cost
                return self.get_path(node)
            lnewnodes = [] #list of children nodes to expand
            if limit != None and node.depth > limit: #check if node has correct depth
                continue
            for a in self.problem.domain.actions(node.state): #  a = action
                newstate = self.problem.domain.result(node.state,a)
                if newstate not in self.get_path(node): #prevents loops
                    newnode = SearchNode(newstate,node)
                    newnode.cost = self.problem.domain.cost(node.state,a) + node.cost
                    newnode.heuristic = self.problem.domain.heuristic(newstate, self.problem.goal)
                    lnewnodes.append(newnode)
            self.add_to_open(lnewnodes)
            
        return None

    # juntar novos nos a lista de nos abertos de acordo com a estrategia
    def add_to_open(self,lnewnodes):
        if self.strategy == 'astar':
            self.open_nodes = sorted(self.open_nodes + lnewnodes, key = lambda node: node.heuristic + node.cost)



