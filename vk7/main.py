import heapq
from graafi3 import Graph
from MCJuorukello import Pelaa_uw

"""
JUORUKELLO GRAAFIANALYYSI

ohjelma toimii painottomilla kaarilla täysin oikein, aseta painottoman graafin
nimi vain riville 84 ("xxx")   xxx:n tilalle

Tehtävänä on analysoida graafi sen perusteella kuinka usein
solmu on lyhimmällä polulla jostain solmusta toiseen

Tehtävä on toteutettu analysoimalla kaikki lyhimmät polut graafissa jokaisesta
solmusta jokaiseen solmuun

Näin on yksinkertaista pitää kirjaa siitä kuinka monta kertaa solmu esiintyy
lyhimmällä polulla
"""
#bfs toimii tilanteessa kun ei tarvi ottaa kaarien hintaa huomioon
def bfs(graph, start, end):

    #parents pitää vanhemmuussuhteista kirjaa
    parents = {start: None}

    #perinteinen bfs looppi
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node == end:
            break
        for neighbor in graph.adj(node):
            if neighbor not in parents:
                parents[neighbor] = node
                queue.append(neighbor)

    #virhetilanne jossa viimeisellä solmulla ei ole
    #vanhemmuusuhdetta = kytkemätön graafi/solmu.
    #paluuarvona none
    if end not in parents:
        return None

    #reitin järjestäminen vanhemmuuksista
    path = [end]
    while path[-1] != start:
        path.append(parents[path[-1]])
    path.reverse()

    #palauttaa reitin
    return path


#funktion tehtävänä on analysoida graafista, kuinka usein solmu on millä tahansa
#lyhimmällä (bfs) polulla
def analyze_shortest_path(graph):
    #shortestcounter pitää kirjaa kuinka montaa kertaa solmu on lyhimmällä polulla
    shortestcounter={}

    #dict arvojen alustaminen
    for i in graph.V:
        shortestcounter[i]=0

    #looppi käy läpi reitit jokaisesta solmusta jokaiseen solmuun etsien
    #lyhimmän polun bfs:llä
    for u in graph.V:
        for v in graph.V:
            if u == v:
                continue

            #bfs etsitty polku on shortestpath
            shortestpath = bfs(graph, u, v)

            if shortestpath is not None:
                #looppi lisää solmun laskuriin yhden jos se on käydyllä polulla
                for node in shortestpath:
                    shortestcounter[node] += 1

    #paluuarvona tulee laskurin avaimet listana järjestettynä avaimen arvon
    #perusteella(=kuinka monta kertaa esiintynyt lyhimmällä polulla)
    a = sorted(shortestcounter.keys(),
            key=lambda x: shortestcounter[x], reverse=True)
    return a[:10]


if __name__ == "__main__":
    G=Graph("preferential_random_weighted_102_817")
    x=analyze_shortest_path(G)
    y=Pelaa_uw(G,10000)
    print(f"{len(set(x) & set(y))}")
