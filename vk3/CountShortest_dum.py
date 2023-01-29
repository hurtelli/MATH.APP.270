#! /usr/bin/env python
"""
This py program will iterate through a graph
to find all the paths between nodes u and v

The twist is that from these paths, this sw will find the
shortest one and return the maximum amount of nodes from a set B
that are on a path as short as the shortest path.

::There can be multiple shortest paths from u to v
::This program finds one of these paths with the most
::amount of nodes that belong in a set of nodes S
"""

#importing a given solution for a graph class
from graafi3 import Graph


def ReadSet(filename):
    ff = open(filename,'r')
    x = ff.readlines()[0].split()
    S =set([])
    for i in x:
        S.add(int(i))
    return S


#Fatherfunction for holding data and for starting the
#recursive node iterating function CS
#g is the graph
#S is the set which nodes we are interested in
#s is the node were starting from
#t is the node we'd like to get to
def CountShortest(g,S,s,t):

    #data holds all the different paths as:
        #Tuple ('Pathlength','Amount of S nodes in this path')
    data = []

    #visited keeps count of wether a node has been visited already
    visited=[]

    #path holds the current path traversed
    #indexes are the nodes in the path
    path=[]

    #call for the iterating function
    CS(g,S,s,t,visited,path,data)


    #sorting the paths to get the shortest paths
    #to be more easily comparable
    data.sort()
    print(data)

    #Value to hold the most amount of S nodes in the shortest path
    Smax=0

    if len(data) != 0:
        #Iterating through the shortest paths to find the greatest
        #amount of S nodes in the path
        i = 0
        while data[i][0]==data[0][0]:
            if data[i][1] > Smax:
                Smax =data[i][1]
            i+=1

    #after the iterations Smax has the correct value that we were after
    return Smax


#recursive function to traverse the nodes to find paths from the first node
#to the node we're after (t)
#in this function s is the node currently being checked
#otherwise the variables are familiar from the Fatherfunction
def CS(g,S,s,t,visited,path,data):

    #adding the current node to visited and to the path
    visited.append(s)
    path.append(s)

    #check for reaching the goal
    if s==t:

        #a holds the amount of S nodes in the path
        a=0

        #checking the amount of S nodes in the path
        for b in path:
            if b in S:
                a+=1

        #adding the Tuple ('Path length', 'Amount of S nodes in path')
        #to the main data structure
        data.append((len(path),a))

    else:
        #as this node is not the goal
        #we'll check the next nodes (neighbours of node s)
        #that are not visited
        for i in g.adj(s):
            if i not in visited:
                CS(g,S,i,t,visited,path,data)


    #When a path has been completed
    #We'll need to remove them from the structure to find a new path
    path.pop()
    visited.remove(s)


if __name__ == "__main__":
    G = Graph('testgraph_1')
    B = ReadSet('testset_1')
    x = CountShortest(G, B, 1,10)
    print(x)