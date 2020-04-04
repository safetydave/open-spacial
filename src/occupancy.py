import random


class Occupancy:

    def __init__(self, og, seed=None):
        self.og = og

        if seed:
            random.seed(seed)
        self.source = self.generate_source()

    def generate_source(self):
        return random.choice(range(self.og.rank))