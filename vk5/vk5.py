from graafi3 import Graph


def ReadNodes(filename):
    ff = open(filename, 'r')
    x = ff.readlines()[0].split()
    S = []
    for i in x:
        S.append(int(i))
    return S


def bfs(graph, source, sink, parent,laskuri):

    #visited pitää kirjaa solmuista joissa on käyty
    visited = []
    #queue tarvitaan BFS suorittamiseksi
    queue = [source]
    visited.append(source)

    #normaali BFS looppi, jossa tarkastetaan kaarien jäljellä oleva
    #kapasiteetti ja loopissa pidetään kirjaa myös parent suhteista, joilla
    #itse suorat virtauspolut pidetään kartalla
    while queue:
        u = queue.pop(0)
        for v in graph.adj(u):
            laskuri[0] += 1
            if v not in visited and graph.W[(u,v)] > 0:
                queue.append(v)
                visited.append(v)
                parent[v] = u

    #True niin pitkään kuin queuessa on solmuja käymättä
    #(loppusolmu)
    return True if sink in visited else False


def ford_fulkerson(graph, source, sink):

    #parent kuvaa nodejen suhdetta toisiinsa
    #käytännöllisellä listalla, jonka pituus on
    #tällainen työarvo
    parent = [-1] * len(graph.V)*100000

    #flow kuvaa graafin maksimaalista virtausta
    flow = 0

    #laskuri pitää kirjaa selatuista kaarista
    #tyyppiä lista, että bfs voi muokata arvoa
    laskuri=[0]

    #while loop jossa virtauksia käydään läpi
    while bfs(graph, source, sink, parent,laskuri):

        #reitin virtauksen oletusarvo on inf
        path_flow = float("Inf")

        #käydään läpi pullonkaula reitissä
        s = sink
        while s != source:
            path_flow = min(path_flow, graph.W[(parent[s],s)])
            s = parent[s]

        #lisätään reitin flow maximi virtaukseen
        flow += path_flow

        #lasketaan ja asetetaan reitin kaarille äsken laskettua virtausta
        #vastaavat arvot potentiaaliselle virralle, eli jäljellä oleva
        #kapasiteetti
        v = sink
        while v != source:
            u = parent[v]
            graph.W[(u,v)] -= path_flow

            #try-except hakee tilanteet, joissa graafissa ei ole vielä olemassa
            #kaaren vastakaarta ja tarvittaessa luo sen
            try:
                graph.W[(v,u)] += path_flow
            except KeyError:
                graph.W[(v, u)] = path_flow

            v = parent[v]

    return (flow,laskuri[0])


if __name__ == "__main__":
    G = Graph("testflow_100")
    S = ReadNodes("testset_100")
    s = S[0]
    t = S[1]
    f = ford_fulkerson(G, s, t)
    print(f"max flow on {f[0]}")
    print(f"laskuri sanoo {f[1]}")
