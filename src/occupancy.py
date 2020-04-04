import random


class Occupancy:

    def __init__(self, sources, all_desks, p, seed=None):
        self.sources = sources
        self.all_desks = all_desks
        self.p = p

        if seed:
            random.seed(seed)
        self.source = self.generate_source()
        self.seating = self.generate_seating()

    def generate_source(self):
        return random.choice(list(self.sources))

    def generate_seating(self):
        open_desks = self.all_desks.difference({self.source})
        num_desks = int(round(self.p * len(open_desks)))
        return random.sample(open_desks, num_desks)
