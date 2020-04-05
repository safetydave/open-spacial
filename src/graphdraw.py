import numpy as np


def grid_layout_pos(rank):
    pos = {}
    h_scale = 2 / (rank - 1)
    v_scale = 1.6 / (rank - 1)
    offs = 1
    for i in range(rank):
        for j in range(rank):
            n = i * rank + j
            pos[n] = np.array([(j * h_scale - offs), (i * v_scale - offs)])
    pos[rank ** 2] = np.array([1.0, 0])
    return pos
