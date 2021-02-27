# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    "*** YOUR CODE HERE ***"

    start = problem.getStartState()
    stack = util.Stack()
    visited = []

    visited.append(start)
    stack.push((start, []))

    if problem.isGoalState(start):
        return []

    while stack.isEmpty() == False:
        currNode, moves = stack.pop()
        visited.append(currNode)
        if problem.isGoalState(currNode) == True:
            return moves
        nodes = problem.getSuccessors(currNode)
        if nodes:
            for i in nodes:
                if i[0] not in visited:
                    moreMoves = moves + [i[1]]
                    stack.push((i[0], moreMoves))
    return []
    util.raiseNotDefined()



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    start = problem.getStartState()
    queue = util.Queue()
    visited = []
    visited.append(start)
    queue.push((start, []))
    if problem.isGoalState(start):
        return []

    while queue.isEmpty() == False:
        found = False
        currNode, moves = queue.pop()
        visited.append(currNode)

        if problem.isGoalState(currNode) == True:
            return moves
        if found == True:
            return moves
        nodes = problem.getSuccessors(currNode)
        queueList = [x[0] for x in queue.list]

        if nodes:
            for i in nodes:
                if i[0] not in visited and i[0] not in queueList:
                    if problem.isGoalState(i[0]) == True:
                        found = True
                        queue.push((i[0], moves + [i[1]]))
                    else:
                        queue.push((i[0], moves + [i[1]]))


    return []



    util.raiseNotDefined()



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    queue = util.PriorityQueue()
    visited = []
    visited.append(start)
    queue.push((start, []), 0)
    if problem.isGoalState(start):
        return []

    while queue.isEmpty() == False:

        currNode, moves = queue.pop()
        # print(f"currNode {currNode}")
        visited.append(currNode)


        if problem.isGoalState(currNode) == True:
            return moves

        nodes = problem.getSuccessors(currNode)
        pastList = [x[2][0] for x in queue.heap]
        if nodes:
            for i in nodes:
                if i[0] not in visited and i[0] not in pastList:
                    priority = problem.getCostOfActions(moves + [i[1]])
                    queue.push((i[0], moves + [i[1]]), priority)

                elif i[0] not in visited and i[0] in pastList:
                    for x in queue.heap:
                        if x[2][0] == i[0]:
                            oldPriority = problem.getCostOfActions(x[2][1])
                    newPriority = problem.getCostOfActions(moves + [i[1]])
                    if oldPriority > newPriority:
                        queue.update((i[0], moves + [i[1]]), newPriority)




def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    queue = util.PriorityQueue()
    start = problem.getStartState()
    visited = []
    if problem.isGoalState(start):
        return []

    queue.push((start, []), heuristic(problem.getStartState(), problem))
    while queue.isEmpty() == False:
        currNode, moves = queue.pop()
        if currNode not in visited:
            visited.append(currNode)
            if problem.isGoalState(currNode):
                return moves
            nodes = problem.getSuccessors(currNode)
            if nodes:
                for i in nodes:
                    if i[0] not in visited:
                        print(heuristic(i[0], problem))
                        h = problem.getCostOfActions(moves + [i[1]]) + heuristic(i[0], problem)
                        queue.push((i[0], moves + [i[1]]), h)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
