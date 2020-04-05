import numpy as np
import os
import sys
import unittest

sys.path.append(os.path.abspath('..'))
from src.graphdraw import grid_layout_pos, draw_graph
from src.officegraph import OfficeGraph


class TestGraphDraw(unittest.TestCase):

    def test_grid_layout_pos(self):
        pos = grid_layout_pos(10)
        expect = {0: np.array([-1, -1]),
                  9: np.array([1, -1]),
                  90: np.array([-1, 0.6]),
                  99: np.array([1, 0.6])}
        for e in expect:
            self.assertAlmostEqual(np.linalg.norm(pos[e] - expect[e]), 0)

    def test_draw_graph(self):
        og = OfficeGraph()
        draw_graph(og, '../out/test_graph1.png')
        draw_graph(og, '../out/test_graph2.png', source=5)
        og.apply_occupancy([50, 51, 52, 53, 54])
        path = [2, 12, 22, 32, 42, 43, 44, 45, 55, 65, 75, 85, 95, 100]
        draw_graph(og, '../out/test_graph3.png', source=2, path=path)