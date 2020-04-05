import networkx as nx


class Solver:

    def __init__(self, og):
        self.og = og

    def can_haz_food(self, source):
        return nx.has_path(self.og.graph, source, self.og.target)

    def path_to_food(self, source):
        return nx.shortest_path(self.og.graph, source, self.og.target)