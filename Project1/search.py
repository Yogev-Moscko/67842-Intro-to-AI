"""
In search.py, you will implement generic search algorithms
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def is_goal_state(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def depth_first_search(problem):
    """
    :param search.SearchProblem problem: The problem

    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    # initialize the stack with the start state
    start = problem.get_start_state()
    stack = util.Stack()
    stack.push((start, []))
    visited = set()

    while not stack.isEmpty():
        state, actions = stack.pop()
        if problem.is_goal_state(state):  # check if the state is the goal state
            return actions
        if state not in visited:
            visited.add(state)
            for successor, action, _ in problem.get_successors(state):  # run of the successors of the state
                stack.push((successor, actions + [action]))


def breadth_first_search(problem):
    """
    Search the shallowest nodes in the search tree first.
    """

    # initialize the queue with the start state
    start = problem.get_start_state()
    queue = util.Queue()
    queue.push((start, []))
    visited = set()

    while not queue.isEmpty():
        state, actions = queue.pop()
        if problem.is_goal_state(state):  # check if the state is the goal state
            return actions
        if state not in visited:
            visited.add(state)
            for successor, action, _ in problem.get_successors(state):  # run of the successors of the state
                queue.push((successor, actions + [action]))


def uniform_cost_search(problem):
    """
    Search the node of the least total cost first.
    """

    # initialize the queue with the start state
    start = problem.get_start_state()
    queue = util.PriorityQueue()
    queue.push(Node(start, []), 0)
    visited = set()

    while not queue.isEmpty():
        state, actions = queue.pop().get_state_actions__()
        if problem.is_goal_state(state):  # check if the state is the goal state
            return actions
        if state not in visited:
            visited.add(state)
            for successor, action, _ in problem.get_successors(state):  # run of the successors of the state
                queue.push(Node(successor, actions + [action]), problem.get_cost_of_actions(actions + [action]))



def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """

    # initialize the queue with the start state
    start = problem.get_start_state()
    queue = util.PriorityQueue()
    queue.push(Node(start, []), heuristic(start, problem))
    visited = set()

    while not queue.isEmpty():
        state, actions = queue.pop().get_state_actions__()
        if problem.is_goal_state(state):  # check if the state is the goal state
            return actions
        if state not in visited:
            visited.add(state)
            for successor, action, _ in problem.get_successors(state):  # run of the successors of the state
                queue.push(Node(successor, actions + [action]),
                           problem.get_cost_of_actions(actions + [action]) + heuristic(successor, problem))


# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search


class Node:
    def __init__(self, state, actions):
        self.state = state
        self.actions = actions

    def get_state__(self):
        return self.state

    def get_actions__(self):
        return self.actions

    def get_state_actions__(self):
        return self.state, self.actions
