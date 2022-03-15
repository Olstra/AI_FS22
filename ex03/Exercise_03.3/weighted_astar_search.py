#
# Introduction to Artificial Intelligence, Spring 2022, Sheet 3
# Oliver Strassmann, Julia Kostadinova, Alessio Brazerol
#
# Exercise 3.3 - Informed Search Algorithms: Programming
#

import pancake_problem

from pancake_problem import PancakeProblem
from queue import PriorityQueue
from search import Search, SearchNode


class WeightedAStarSearch(Search):
    name = "weighted-astar"

    def __init__(self, search_problem, weight, **kwargs):
        super().__init__(search_problem, **kwargs)
        self.w = weight
        if weight == 0:
            self.name = "uniform-cost"
        elif weight == 1:
            self.name = "astar"

    def search(self):
        # initialize variables
        prob = self.search_problem
        current_node = prob.initial_state

        # early goal testing for first node
        if prob.is_goal(current_node):
            return [prob.initial_state], 0

        # add initial state to queue and to dictionary
        frontier = [SearchNode(current_node, None, 0)]

        reached = {current_node}

        # loop for children
        prev_cost = current_node
        while frontier:
            # remove from frontier because it was already reached.

            current_node = frontier.pop()

            self.expanded += 1
            reached.add(current_node.state)
            if prob.is_goal(current_node.state):
                return self.extract_path(current_node), current_node.g

            # add potential successors to frontier
            for action in prob.actions(current_node.state):
                pot_successor_state, pot_cost = prob.result(current_node.state, action)

                # calculate the g(n') = g(n) + c(n,a,n')
                g = current_node.g + pot_cost
                # calculate the f(n') = g(n') + h(n')
                f = g + self.w * prob.h(pot_successor_state)

                successor_node = SearchNode(pot_successor_state, current_node, g, f)
                # only add if node was not already reached
                if successor_node.state not in reached:
                    frontier.append(successor_node)
                    self.generated += 1

            frontier.sort(key=lambda x: x.g, reverse=True)

        return None, None


if __name__ == "__main__":
    problem = pancake_problem.generate_random_problem(5)
    problem = PancakeProblem((1, 5, 6, 2, 4, 3))
    problem.dump()
    astar = WeightedAStarSearch(problem, 1, print_statistics=True)
    astar.run()
