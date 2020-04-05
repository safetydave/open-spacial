from officegraph import OfficeGraph
from occupancy import Occupancy
from solver import Solver
from graphdraw import draw_graph


class ExampleDraw:
    pos_count = 0
    neg_count = 0
    limit = 10
    fname_str = '../out/trial_{:.1f}_graph_{:s}_{:d}.png'

    def draw_example(self, p, pos, og, solver, source):
        if pos:
            if self.pos_count < self.limit:
                path = solver.path_to_food(source)
                draw_graph(og, self.fname_str.format(p, 'pos', self.pos_count), source=source, path=path)
                self.pos_count = self.pos_count + 1
        else:
            if self.neg_count < self.limit:
                draw_graph(og, self.fname_str.format(p, 'neg', self.neg_count), source=source)
                self.neg_count = self.neg_count + 1

    def reset(self):
        self.pos_count = 0
        self.neg_count = 0


def main():
    trials = 10000
    print(f"Number of samples for each p: {trials}")
    # occupancy proportions to test
    ps = [x / 10.0 for x in range(11)]
    ps.reverse()

    ed = ExampleDraw()

    for p in ps:
        s = 0
        pos_drawn = 0
        neg_drawn = 0
        for i in range(trials):
            # set up office and scenario
            og = OfficeGraph()
            occupancy = Occupancy(og.back_row(), og.all_desks(), p)
            og.apply_occupancy(occupancy.seating)
            # solve and tally result
            solver = Solver(og)
            pos = solver.can_haz_food(occupancy.source)
            s = s + pos
            # draw some examples
            ed.draw_example(p, pos, og, solver, occupancy.source)

        rate = s / trials
        print("{:.1f} {:.3f}".format(p, rate))
        ed.reset()


if __name__ == "__main__":
    main()
