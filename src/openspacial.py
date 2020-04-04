from officegraph import OfficeGraph
from occupancy import Occupancy
from solver import Solver


def main():
    trials = 10000
    print(f"Number of samples for each p: {trials}")
    # occupancy proportions to test
    ps = [x / 10.0 for x in range(11)]
    ps.reverse()

    for p in ps:
        s = 0
        for i in range(trials):
            # set up office and scenario
            og = OfficeGraph()
            occupancy = Occupancy(og.back_row(), og.all_desks(), p)
            og.apply_occupancy(occupancy.seating)
            # solve and tally result
            solver = Solver(og)
            s = s + solver.can_haz_food(occupancy.source)
        rate = s / trials
        print("{:.1f} {:.3f}".format(p, rate))


if __name__ == "__main__":
    main()
