import networkx as nx


class OfficeGraph:

    def __init__(self, rank=10):
        self.rank = rank
        self.target = rank ** 2
        self.graph = nx.Graph()

        self.graph.add_node(self.target)

        for i in range(rank):
            for j in range(rank):
                n = i * rank + j
                self.graph.add_node(n)
                self.add_edges(n, i, j)

    def add_edges(self, n, i, j):
        if i > 0:
            self.graph.add_edge(n - self.rank, n)
        if j > 0:
            self.graph.add_edge(n - 1, n)
        if i == self.rank - 1:
            self.graph.add_edge(n, self.target)

    def all_desks(self):
        return set(range(self.target))

    def back_row(self):
        return set(range(self.rank))

    def apply_occupancy(self, seating):
        #todo this might be nicer as just removing edges
        self.graph.remove_nodes_from(seating)
