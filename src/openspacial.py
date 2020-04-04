from src.officegraph import OfficeGraph
from src.occupancy import Occupancy
from src.solver import Solver


def main():
    trials = 10000
    print(f"Number of samples for each p: {trials}")

    ps = [x / 10.0 for x in range(11)]
    ps.reverse()

    for p in ps:
        s = 0
        for i in range(trials):
            og = OfficeGraph()
            solver = Solver(og)
            occupancy = Occupancy(og.back_row(), og.all_desks(), p)
            og.apply_occupancy(occupancy.seating)
            s = s + solver.can_haz_food(occupancy.source)
        rate = s / trials
        print("{:.1f} {:.3f}".format(p, rate))


if __name__ == "__main__":
    main()
