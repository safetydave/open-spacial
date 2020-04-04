import random


class Occupancy:

    def __init__(self, og, p, seed=None):
        self.og = og
        self.p = p

        if seed:
            random.seed(seed)
        self.source = self.generate_source()
        self.seating = self.generate_seating()

    def generate_source(self):
        return random.choice(range(self.og.rank))

    def generate_seating(self):
        excluded_nodes = set([self.source, self.og.target])
        open_seats = set(self.og.graph.nodes).difference(excluded_nodes)
        num_seats = int(round(self.p * len(open_seats)))
        return random.sample(open_seats, num_seats)