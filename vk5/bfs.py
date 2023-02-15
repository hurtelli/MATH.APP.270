from collections import deque
from graafi3 import Graph

## Read set
def ReadNodes(filename):
    ff = open(filename, 'r')
    x = ff.readlines()[0].split()
    S = []
    for i in x:
        S.append(int(i))
    return S


def maxflow(graph, source, sink):

    # initialize residual graph
    residual = Graph()
    for vertex in graph.V:
        residual.addVertex(vertex)
    for u, v in graph.AL.items():
        for w in v:
            residual.addEdge(u, w, graph.W.get((u, w), 1))

    # initialize flow
    flow = 0
    while True:
        bfs(residual,source,sink)

    return flow

if __name__ == "__main__":
    G = Graph("testgraph_weighted")
    #print(G.W)
    S = ReadNodes("testset_flow")
    print(S)
    s = S[0]
    t = S[1]
    f = maxflow(G, s, t)
    print(f)
