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

    def assertNeighboursOf(self, og, node_list, neighbours_of):
        self.assertEqual(set(node_list), set(og.graph.neighbors(neighbours_of)))

    # you can move between desks in the same row or column, but not diagonally
    # all desks in the last row can reach the food truck
    def test_neighbours(self):
        # start corner
        self.assertNeighboursOf(self.og10, [1, 10], 0)
        # start row and col
        self.assertNeighboursOf(self.og10, [0, 11, 20], 10)
        self.assertNeighboursOf(self.og10, [0, 2, 11], 1)
        # middle
        self.assertNeighboursOf(self.og10, [5, 14, 16, 25], 15)
        self.assertNeighboursOf(self.og10, [53, 62, 64, 73], 63)
        # other corner
        self.assertNeighboursOf(self.og10, [8, 19], 9)
        # last row
        self.assertNeighboursOf(self.og10, [80, 91, 100], 90)
        self.assertNeighboursOf(self.og10, [88, 97, 99, 100], 98)


if __name__ == '__main__':
    unittest.main()
