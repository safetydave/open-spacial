import os
import sys
import unittest

sys.path.append(os.path.abspath('..'))
from src.occupancy import Occupancy
from src.officegraph import OfficeGraph


class TestOccupancy(unittest.TestCase):

    def setUp(self):
        self.og10 = OfficeGraph(10)
        self.occ_rnd = Occupancy(self.og10)
        self.occ_42 = Occupancy(self.og10, seed=42)

    def test_source(self):
        self.assertGreaterEqual(self.occ_rnd.source, 0)
        self.assertLessEqual(self.occ_rnd.source, 9)
        self.assertEqual(self.occ_42.source, 1)
