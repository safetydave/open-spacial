import os
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

    # source is always in the first row
    def test_source(self):
        self.assertGreaterEqual(self.occ_rnd_min.source, 0)
        self.assertLessEqual(self.occ_rnd_min.source, 9)
        self.assertEqual(self.occ_42.source, 1)

    # p = 0.0 is empty office except you
    # p = 1.0 is all office full including you
    def test_seating(self):
        self.assertEqual(0, len(self.occ_rnd_min.seating))
        self.assertTrue(set(self.occ_rnd_min.seating).issubset(self.all_desks))
        self.assertEqual(50, len(self.occ_rnd_mid.seating))
        self.assertTrue(set(self.occ_rnd_mid.seating).issubset(self.all_desks))
        self.assertEqual(99, len(self.occ_rnd_max.seating))
        self.assertTrue(set(self.occ_rnd_max.seating).issubset(self.all_desks))

    # todo test distributions
