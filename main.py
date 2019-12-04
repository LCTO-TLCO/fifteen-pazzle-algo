from units import pazzle, Node, child_node
from define import prob_num
import copy
"""
node <- a node with state=prob.initstate,path-cost = 0
fromtier <- a priority queue ordered by path-cost, with node as the only element
explored <- an empty set
while(True):
    if not any(fronteer):
        return False
    node <- pop(frontier) # chooses the lowest-cost node in frontier
    if node.state is goal:
        return solution(node)
    add node.state to explored
    for action in prob.acton(node.state):
        child <- child_node(prob,node,action)
        if child.state is not in explored or frontier:
            frontier <- insert(child,frontier)  
        elif child.state is frontier with higher-path-cost:
            replace that frontier node with child
"""


def uniform_cost_search():
    probrem = pazzle()
    # node with initial-state
    node = Node(probrem.state)
    frontier = [node]
    explored = []
    while True:
        if not any(frontier):
            return False
        # choose the lowest-cost node in frontier
        min_cost = min([fr.cost for fr in frontier])
        node = frontier.pop([min_cost == fr.cost for fr in frontier].index(True))
        # goal test
        if probrem.goal_test(node.state):
            return node.movement_log()[::-1]
        explored.append(copy.deepcopy(node.state))
        for act in probrem.actions(node.state):
            child = child_node(probrem, node, act)
            if not (child.state in [fr.state for fr in frontier]) and not (child.state in explored):
                frontier.insert(0, child)
            elif any([child.state == fr.state for fr in frontier]):
                frontier_state = [child.state == fr.state for fr in frontier].index(True)
                if frontier[frontier_state].cost > child.cost:
                    # replace frontier with child
                    frontier[frontier_state] = child


def depth_first_tree_search():
    """
    node <- a node(initstate,cost=0)
    fronteer <- a stack with node as the only element
    loop do
        if Empty(fronteer)return False
        node <- pop(fronteer)
        if probrem.goal_test(node.state)
            return solution(node)
        for action in probrem.actions(node.state):
            child <- child_node(prob,node,action)
            fronteer <- push(child,fronteer)
    """
    probrem = pazzle()
    node = Node(probrem.state)
    fronteer = [node]
    while True:
        if not any(fronteer):
            return False
        node = fronteer.pop(-1)
        if probrem.goal_test(node.state):
            return node.movement_log().reverse()
        for act in probrem.actions(node.state):
            child = child_node(probrem, node, act)
            fronteer.append(child)


if __name__ == "__main__":
    solution = uniform_cost_search()
    solution = solution if not solution else " -> ".join(solution)
    print("prob{}".format(prob_num) + " solution:\n")
    print(solution)
    with open("./data/prob{}.txt".format(prob_num), "w") as f:
        f.writelines(solution)
