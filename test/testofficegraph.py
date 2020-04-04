import os
import sys
import unittest

sys.path.append(os.path.abspath('..'))
from src.officegraph import OfficeGraph


class TestOfficeGraph(unittest.TestCase):

    def setUp(self):
        self.og10 = OfficeGraph(10)
        self.og5 = OfficeGraph(5)

    def test_target(self):
        self.assertEqual(100, self.og10.target)
        self.assertEqual(25, self.og5.target)

    # Grid of 100 desks and 1 food truck
    def test_num_nodes(self):
        self.assertEqual(101, len(self.og10.graph.nodes))
        self.assertEqual(26, len(self.og5.graph.nodes))

    def test_col_neighbours(self):
        self.assertEqual(tuple([10]), tuple(self.og10.graph.neighbors(0)))
        self.assertEqual(tuple([0, 20]), tuple(self.og10.graph.neighbors(10)))


if __name__ == '__main__':
    unittest.main()
