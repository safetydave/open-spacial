from ospacial.officegraph import OfficeGraph
from ospacial.occupancy import Occupancy
from ospacial.solver import Solver
from ospacial.graphdraw import draw_graph


class TrialRunner:
    case_limit = 10
    pos_count = 0
    neg_count = 0
    fname_str = '../out/trial_{:.1f}_graph_{:s}_{:d}.png'

    def __init__(self, trials, ps, draw_cases=False):
        self.trials = trials
        self.ps = ps
        self.results = []
        self.draw_cases = draw_cases

    def run(self):
        for p in self.ps:
            s = 0
            for i in range(self.trials):
                # set up office and scenario
                og = OfficeGraph()
                occupancy = Occupancy(og.back_row(), og.all_desks(), p)
                og.apply_occupancy(occupancy.seating)
                # solve and tally result
                solver = Solver(og)
                pos = solver.can_haz_food(occupancy.source)
                s = s + pos
                # draw some examples
                if self.draw_cases:
                    self.draw_case(p, pos, og, solver, occupancy.source)

            self.results.append(s / self.trials)
            if self.draw_cases:
                self.reset_draw()

    def summary(self):
        s = "Number of samples for each p: {}\n".format(self.trials)
        for i, p in enumerate(self.ps):
            s += ("{:.1f} {:.3f}\n".format(p, self.results[i]))
        return s

    def draw_case(self, p, pos, og, solver, source):
        if pos:
            if self.pos_count < self.case_limit:
                path = solver.path_to_food(source)
                draw_graph(og, self.fname_str.format(p, 'pos', self.pos_count), source=source, path=path)
                self.pos_count = self.pos_count + 1
        else:
            if self.neg_count < self.case_limit:
                draw_graph(og, self.fname_str.format(p, 'neg', self.neg_count), source=source)
                self.neg_count = self.neg_count + 1

    def reset_draw(self):
        self.pos_count = 0
        self.neg_count = 0
