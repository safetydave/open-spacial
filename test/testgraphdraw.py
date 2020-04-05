import numpy as np
import os
import sys
import unittest

sys.path.append(os.path.abspath('..'))
from src.graphdraw import grid_layout_pos


class TestGraphDraw(unittest.TestCase):

    def test_grid_layout_pos(self):
        pos = grid_layout_pos(10)
        expect = {0: np.array([-1, -1]),
                  9: np.array([1, -1]),
                  90: np.array([-1, 0.6]),
                  99: np.array([1, 0.6])}
        for e in expect:
            self.assertAlmostEqual(np.linalg.norm(pos[e] - expect[e]), 0)