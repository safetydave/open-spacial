import os
import sys
import unittest

sys.path.append(os.path.abspath('..'))
from src.officegraph import OfficeGraph


class TestOfficeGraph(unittest.TestCase):

    def test_target(self):
        og = OfficeGraph(10)
        self.assertEqual(100, og.target)
        og = OfficeGraph(5)
        self.assertEqual(25, og.target)

    # Grid of 100 desks and 1 food truck
    def test_num_nodes(self):
        og = OfficeGraph(10)
        self.assertEqual(101, len(og.graph.nodes))
        og = OfficeGraph(5)
        self.assertEqual(26, len(og.graph.nodes))


if __name__ == '__main__':
    unittest.main()
