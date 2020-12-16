
# Module: tree_search
# 
# This module provides a set o classes for automated
# problem solving through tree search:
#    SearchDomain  - problem domains
#    SearchProblem - concrete problems to be solved
#    SearchNode    - search tree nodes
#    SearchTree    - search tree with the necessary methods for searhing
#
#  (c) Luis Seabra Lopes
#  Introducao a Inteligencia Artificial, 2012-2019,
#  Inteligência Artificial, 2014-2019



from abc import ABC, abstractmethod
import asyncio
from deadlock import *
# Dominios de pesquisa
# Permitem calcular
# as accoes possiveis em cada estado, etc
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
        self.acumulate = set()
        self.cost = cost
        #self.depth = self.parent.depth + 1 if self.parent != None else 0
    def __str__(self):
        return "no(" + str(self.state) + "," + str(self.parent) + ")"
    def __repr__(self):
        return str(self)
        
    def in_parent(self,state):
        if self.state == state:
            return True
        if self.parent == None:
            return False
        return self.parent.in_parent(state)

# Arvores de pesquisa
class SearchTree:

    # construtor
    def __init__(self,problem, strategy='greedy'): 
        self.problem = problem
        root = SearchNode(problem.initial, None)
        self.open_nodes = [root]
        self.strategy = strategy
        

    # obter o caminho (sequencia de estados) da raiz ate um no

    def get_path(self,node):
        #if node.parent == None:
        #    return {node.state}
        #path = self.get_path(node.parent)
        #path.add(node.state) 
        if node.parent == None:
            return [node.state]
        path = self.get_path(node.parent)
        path += [node.state]

        return path
    
    def length(self):
        return self.solution.depth
    # procurar a solucao
    async def search(self,limit=None):
        while self.open_nodes != []:
            await asyncio.sleep(0)
            node = self.open_nodes.pop(0)
            if node.parent != None:
                node.acumulate = (node.parent.acumulate)
                node.acumulate.add(node.state)
            else:
                node.acumulate.add(node.state)
            if self.problem.goal_test(node.state): #solution detected
                self.solution = node
                print("==================WE HAVE A SOLUTION==================")
                todos_cantos.clear()
                return self.get_path(node)
            lnewnodes = []
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state,a)
                #print(newstate)
                if newstate != None:
                    if newstate not in node.acumulate: #set que acumula estados
                        newnode = SearchNode(newstate,node)
                        newnode.heuristic = self.problem.domain.heuristic(newnode.state,self.problem.goal)
                        lnewnodes.append(newnode)
            self.add_to_open(lnewnodes)
        print("!!!NO SOLUTION!!!")
        return None #no solution deteced

    # juntar novos nos a lista de nos abertos de acordo com a estrategia
    def add_to_open(self,lnewnodes):
        if self.strategy == 'breadth':
            self.open_nodes.extend(lnewnodes)
        elif self.strategy == 'depth':
            self.open_nodes[:0] = lnewnodes
        elif self.strategy == 'uniform':
            self.open_nodes += lnewnodes
            self.open_nodes.sort(key = (lambda x: x.cost))
        elif self.strategy == 'greedy':
            self.open_nodes += lnewnodes
            self.open_nodes.sort(key = (lambda x: x.heuristic))
        elif self.strategy == 'astar':
            self.open_nodes = sorted(self.open_nodes + lnewnodes, key = lambda node: node.heuristic + node.cost)

