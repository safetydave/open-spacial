class OfficeGraph:

    rank = 10

    def __init__(self, rank):
        self.rank = rank

    def target(self):
        return self.rank ** 2
