import search_problem
from search import Search, SearchNode


class UniformCostSearch(Search):
    name = "uniform-cost"

    def search(self):
        # initialize variables
        prob = self.search_problem
        current_node = prob.initial_state
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
                new_g = current_node.g + pot_cost
                successor_node = SearchNode(pot_successor_state, current_node, new_g)
                # only add if node was not already reached
                if successor_node.state not in reached:
                    frontier.append(successor_node)
                    self.generated += 1
            frontier.sort(key=lambda x: x.g, reverse=True)
        return None, None


if __name__ == "__main__":
    problem = search_problem.generate_random_problem(8, 2, 3, max_cost=10)
    problem.dump()
    ucs = UniformCostSearch(problem, True)
    ucs.run()
