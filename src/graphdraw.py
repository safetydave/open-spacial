import matplotlib.pyplot as plt
import networkx as nx
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
    pos[rank ** 2] = np.array([0, 1.0])
    return pos


def draw_graph_styled(graph, pos, nodelist, colour):
    nx.draw(graph, pos=pos, nodelist=nodelist, node_color=colour, with_labels=True)


def draw_graph(og, fname, source=None):
    gl_pos = grid_layout_pos(og.rank)
    draw_graph_styled(og.graph, gl_pos, og.graph.nodes(), 'cornflowerblue')
    draw_graph_styled(og.graph, gl_pos, [og.target], 'tomato')
    if source is not None:
        draw_graph_styled(og.graph, gl_pos, [source], 'hotpink')
    # todo limegreen for path
    plt.savefig(fname)