import unittest

from ospacial.officegraph import OfficeGraph


class TestOfficeGraph(unittest.TestCase):

    def setUp(self):
        # rank = 10
        self.og10 = OfficeGraph(10)
        # rank = 5
        self.og5 = OfficeGraph(5)

    # id of node representing food truck
    def test_target_id(self):
        # target = rank ** 2
        self.assertEqual(100, self.og10.target)
        self.assertEqual(25, self.og5.target)

    # Grid of 100 desks and 1 food truck
    def test_num_nodes(self):
        # num = rank ** 2 + 1
        self.assertEqual(101, len(self.og10.graph.nodes()))
        self.assertEqual(26, len(self.og5.graph.nodes()))

    def test_back_row(self):
        # range(0, rank)
        self.assertEqual(set(range(10)), self.og10.back_row())
        self.assertEqual(set(range(5)), self.og5.back_row())

    def test_all_desks(self):
        # range (0, rank ** 2)
        self.assertEqual(set(range(100)), self.og10.all_desks())
        self.assertEqual(set(range(25)), self.og5.all_desks())

    # all desks in the front row can reach the food truck
    def test_front_row_can_reach_target(self):
        # front row is range(rank * (rank - 1), rank ** 2)
        for n in range(90, 100):
            self.assertTrue(100 in self.og10.graph.neighbors(n))
        for n in range(20, 25):
            self.assertTrue(25 in self.og5.graph.neighbors(n))

    # no other desk can reach food truck directly
    def test_other_rows_cant_reach_target(self):
        # other rows are range(0, rank * (rank - 1))
        for n in range(0, 90):
            self.assertFalse(100 in self.og10.graph.neighbors(n))
        for n in range(0, 20):
            self.assertFalse(25 in self.og5.graph.neighbors(n))

    # can go between rows
    def test_can_move_front_back(self):
        # n - rank and n + rank
        self.assertTrue(32 in self.og10.graph.neighbors(42))
        self.assertTrue(52 in self.og10.graph.neighbors(42))

    # can go between columns
    def test_can_move_left_right(self):
        # n - 1 and n + 1
        self.assertTrue(41 in self.og10.graph.neighbors(42))
        self.assertTrue(43 in self.og10.graph.neighbors(42))

    # can't go diagonally
    def test_cant_move_diagonally(self):
        # n +/- rank +/- 1
        self.assertFalse(31 in self.og10.graph.neighbors(42))
        self.assertFalse(33 in self.og10.graph.neighbors(42))
        self.assertFalse(51 in self.og10.graph.neighbors(42))
        self.assertFalse(53 in self.og10.graph.neighbors(42))

    def assertNeighboursOf(self, og, node_list, neighbours_of):
        self.assertEqual(set(node_list), set(og.graph.neighbors(neighbours_of)))

    # you can move between desks in the same row or column, but not diagonally
    # here we check a set of neighbours is exactly as expected for different areas
    def test_valid_move_scenarios(self):
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

    # if a desk is occupied, you can no longer move to that desk
    # here we check a set of neighbours is exactly as expected in region of occupied desk
    def test_valid_move_scenarios_when_apply_occupancy(self):
        self.og10.apply_occupancy([53, 98])
        self.assertNeighboursOf(self.og10, [62, 64, 73], 63)
        self.assertNeighboursOf(self.og10, [42, 51, 62], 52)
        self.assertNeighboursOf(self.og10, [78, 87, 89], 88)
        self.assertNeighboursOf(self.og10, [89, 100], 99)


if __name__ == '__main__':
    unittest.main()
