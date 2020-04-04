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
