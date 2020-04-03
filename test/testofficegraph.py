import os
import sys
import unittest

sys.path.append(os.path.abspath('..'))
from src.officegraph import OfficeGraph


class TestOfficeGraph(unittest.TestCase):

    def test_target(self):
        og = OfficeGraph(5)
        self.assertEqual(og.target(), 25)


if __name__ == '__main__':
    unittest.main()
