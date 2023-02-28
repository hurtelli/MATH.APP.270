#! /usr/bin/env python
""" Monte carlo simulator for Juorukello game """
""" Number of rounds is n """

from graafi3 import Graph
from PQ import PQ
from random import random 
from copy import copy

""" Pelaa_weight(g,n) pelaa n kierrosta painotetussa graafissa g"""
def Pelaa_Weight(g, n):
    Nodes = [u for u in g.V]
    Points = {u:0 for u in g.V}
    i = 0
    while i < n:
        i += 1
        j = 0
        s = Nodes[int(random()*len(Nodes))]
        t = Nodes[int(random()*len(Nodes))]
        Messages = {s:[[]]}
        Q = PQ()
        Q.push((0,s))
        D = {s:0}
        while not Q.empty():
            u_pair = Q.pop()
            u = u_pair[1]
            d = u_pair[0]
            assert(d == D[u])
            if u == t:
                break
            # Pick a random message
            M = Messages[u][int(random()*len(Messages[u]))]
            for v in g.adj(u):
                w = g.W[(u,v)]
                if v not in D or D[v] > d + w:
                    D[v] = d + w
                    Messages[v] = []
                    Q.push((d+w,v))           
                if D[v] == d + w:
                    mm = copy(M)
                    mm.append(v)
                    Messages[v].append(mm)
        if not t in Messages:
            continue
        M = Messages[t][int(random()*len(Messages[t]))]
        for u in M:
            if u != t and u != s:
                Points[u] += 1
                u[0]

    a=[]
    for u in sorted(Points.items(), key=lambda x: x[1],
                    reverse=True):
        a.append(u)

    return a[:10]




""" Pelaa_uw(g,n) pelauttaa n kierrosta painottamattomassa graafissa g """
def Pelaa_uw(g, n):
    Nodes = [u for u in g.V]
    Points = {u:0 for u in g.V}
    i = 0
    while i < n:
        i += 1
        j = 0
        s = Nodes[int(random()*len(Nodes))]
        t = Nodes[int(random()*len(Nodes))]
        Messages = {s:[[]]}
        Q = [s]
        D = {s:0}
        while Q:
            u = Q.pop(0)
            d = D[u]
            if u == t:
                break
            # Pick a random message
            M = Messages[u][int(random()*len(Messages[u]))]
            for v in g.adj(u):
                if v not in D:
                    D[v] = d+1
                    Messages[v] = []
                    Q.append(v)
                # Send the random message forward
                if D[v] == d+1:
                    mm = copy(M)
                    mm.append(v)
                    Messages[v].append(mm)
        if not t in Messages:
            continue
        M = Messages[t][int(random()*len(Messages[t]))]
        for u in M:
            if u != t and u != s:
                Points[u] += 1
    a=[]
    for u in sorted(Points.items(), key=lambda x: x[1],
                    reverse=True):
        a.append(u[0])

    return a[:10]


if __name__ == "__main__":
    g = Graph('simply_random_101_1053')
    u = Pelaa_uw(g,10000)
    print(u[:10])
