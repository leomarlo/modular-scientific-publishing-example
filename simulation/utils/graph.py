# This script handles graph creation and manipulation
import os
import networkx as nx
import matplotlib.pyplot as plt

ROOTFOLDER = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# create a function that generates a random graph with networkx
def generateGraph(N: int, m: float, verbose=False):
    graph = nx.gnm_random_graph(N, int(N * m), directed=True)
    if verbose:
        print('>>> Graph generated with {} nodes and {} edges'.format(N, int(N * m)))
    return graph


# visualize the graph and return the figure and axes object
def generateFigure(graph, save=False, verbose=False):
    fig, ax = plt.subplots(figsize=(10, 10))
    nx.draw(graph, ax=ax, with_labels=True)
    if save:
        path = os.path.join(ROOTFOLDER, "img", "graph.png")
        fig.savefig(path)
        if verbose:
            print('>>> Graph image saved to {}'.format(path))

    return fig, ax


def dumpGraph(graph, asEdgeList=True, verbose=False):
    filename = 'graph'
    fullfilename = filename + ('.edgelist' if asEdgeList else '.adjlist')
    
    path = os.path.join(ROOTFOLDER, "data", fullfilename)
    if asEdgeList:
        nx.write_edgelist(graph, path)
    else:
        nx.write_adjlist(graph, path)
    if verbose:
        print('>>> Graph data saved to {}'.format(path))





