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


def draw_graph(og, fname, source=None, path=None):
    gl_pos = grid_layout_pos(og.rank)
    plt.clf()
    draw_graph_styled(og.graph, gl_pos, og.graph.nodes(), 'tab:blue')
    draw_graph_styled(og.graph, gl_pos, [og.target], 'tab:orange')
    if source is not None:
        draw_graph_styled(og.graph, gl_pos, [source], 'tab:pink')
    if path is not None:
        draw_graph_styled(og.graph, gl_pos, path[1:-1], 'tab:green')
    plt.savefig(fname)
