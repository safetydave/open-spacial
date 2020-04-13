import os
from scipy.stats import chisquare
import sys
import unittest

sys.path.append(os.path.abspath('..'))
from src.occupancy import Occupancy


class TestOccupancy(unittest.TestCase):

    def setUp(self):
        self.back_row = set(range(10))
        self.all_desks = set(range(100))
        self.occ_rnd_min = Occupancy(self.back_row, self.all_desks, 0.0)
        self.occ_rnd_mid = Occupancy(self.back_row, self.all_desks, 0.5)
        self.occ_rnd_max = Occupancy(self.back_row, self.all_desks, 1.0)
        self.occ_42 = Occupancy(self.back_row, self.all_desks, 0.5, seed=42)

    # source is always in the back row
    def test_source_back_row(self):
        self.assertGreaterEqual(self.occ_rnd_min.source, 0)
        self.assertLessEqual(self.occ_rnd_min.source, 9)

    # source is repeatable with specified seed
    def test_source_repeatable_with_seed(self):
        self.assertEqual(self.occ_42.source, 1)

    # p = 0.0 is empty office except you
    def test_seating_empty(self):
        self.assertEqual(0, len(self.occ_rnd_min.seating))
        self.assertTrue(set(self.occ_rnd_min.seating).issubset(self.all_desks))

    # p = 0.5 office is half full (rounded to nearest full seat)
    def test_seating_half_full(self):
        self.assertEqual(50, len(self.occ_rnd_mid.seating))
        self.assertTrue(set(self.occ_rnd_mid.seating).issubset(self.all_desks))

    # p = 1.0 is all office full including you
    def test_seating_full(self):
        self.assertEqual(99, len(self.occ_rnd_max.seating))
        self.assertTrue(set(self.occ_rnd_max.seating).issubset(self.all_desks))

    # source is at a random position (uniform distribution) in the back row
    def test_source_distribution(self):
        trials = 1000
        counts = [0] * 10
        for t in range(trials):
            occ = Occupancy(self.back_row, self.all_desks, 0.0)
            counts[occ.source] = counts[occ.source] + 1

        _, p = chisquare(counts)
        # reject null hypothesis of same distribution if p <= 0.05
        # this will fail for instance if generate_source() were to
        # return 5
        self.assertGreater(p, 0.05)

    # seating is random (uniform distribution) excluding source
    def test_seating_distribution(self):
        trials = 1000
        p = 0.5

        rank = len(self.back_row)
        open_desks = len(self.all_desks) - 1
        counts = [0] * len(self.all_desks)
        for t in range(trials):
            occ = Occupancy(self.back_row, self.all_desks, p)
            for s in occ.seating:
                counts[s] = counts[s] + 1

        # expected distribution of desk occupancy
        # given one random source seat is occupied in back row
        seats_per_trail = int(round(p * open_desks))
        seats = trials * seats_per_trail
        e_back_row_seat = seats * (rank - 1) / rank / open_desks
        e_other_row_seat = seats / open_desks
        e_counts = ([e_back_row_seat] * rank)
        e_counts.extend([e_other_row_seat] * (len(self.all_desks) - rank))

        _, pc = chisquare(counts, e_counts)
        # reject null hypothesis of same distribution if p <= 0.05
        # this will fail for instance if generate_seating() were to
        # return [list(open_desks)[i] for i, _ in enumerate(open_desks)]
        self.assertGreater(pc, 0.05)


if __name__ == '__main__':
    unittest.main()
