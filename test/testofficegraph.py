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

    def test_back_row(self):
        self.assertEqual(set(range(10)), self.og10.back_row())
        self.assertEqual(set(range(5)), self.og5.back_row())

    def test_all_desks(self):
        self.assertEqual(set(range(100)), self.og10.all_desks())
        self.assertEqual(set(range(25)), self.og5.all_desks())

    def test_apply_occupancy(self):
        self.og10.apply_occupancy([53, 98])
        self.assertNeighboursOf(self.og10, [62, 64, 73], 63)
        self.assertNeighboursOf(self.og10, [42, 51, 62], 52)
        self.assertNeighboursOf(self.og10, [78, 87, 89], 88)
        self.assertNeighboursOf(self.og10, [89, 100], 99)


if __name__ == '__main__':
    unittest.main()
