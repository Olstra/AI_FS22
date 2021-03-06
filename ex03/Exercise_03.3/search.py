#
# Introduction to Artificial Intelligence, Spring 2022, Sheet 3
# Oliver Strassmann, Julia Kostadinova, Alessio Brazerol
#
# Exercise 3.3 - Informed Search Algorithms: Programming
#

import search_problem
import time


class SearchNode:
    def __init__(self, state, parent, g, f=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.f = f

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def __eq__(self, other):
        return self.f == other.f


class Search:
    def __init__(self, search_problem, print_statistics=False):
        self.search_problem = search_problem
        self.expanded = 0
        self.generated = 0
        self.print_statistics = print_statistics
        self.max_generations = 1000000

    def search(self):
        raise NotImplementedError

    def run(self):
        self.expanded = 0
        self.generated = 0

        begin_time = time.time()
        print(f"Starting {self.name} search...")

        plan, cost = self.search()
        if plan is not None:
            print(f"Found solution of cost {cost}.")

        total_time = time.time() - begin_time
        print(f"Search time: {total_time:.3f}")

        if self.print_statistics:
            print(f"Expanded states: {self.expanded}")
            print(f"Generated states: {self.generated}")
            # if plan is not None:
            # print(f"State sequence: {plan}")

    def extract_path(self, node):
        path = [node.state]
        while node.parent:
            node = node.parent
            path.append(node.state)

        path.reverse()
        return path
