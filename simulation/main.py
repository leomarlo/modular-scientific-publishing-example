import utils.graph as graph

VERBOSE = True
# check if main then execute the code

if __name__ == "__main__":
    gr = graph.generateGraph(10, 0.5, verbose=VERBOSE)
    graph.generateFigure(gr, save=True, verbose=VERBOSE)
    graph.dumpGraph(gr, asEdgeList=True, verbose=VERBOSE)
    # print(gr.edges)

