#! /usr/bin/env python
from graafi3 import Graph
from CountShortest_dum import CountShortest

def ReadSet(filename):
    ff = open(filename,'r')
    x = ff.readlines()[0].split()
    S =set([])
    for i in x:
        S.add(int(i))
    return S

if __name__ == "__main__":
    G = Graph('testgraph_5')
    B = ReadSet('testset_1')
    x = CountShortest(G, B, 6,4)
    print(x)
