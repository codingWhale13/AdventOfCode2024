def is_clique(g, proposed_clique):
    for i in range(len(proposed_clique)):
        for j in range(i + 1, len(proposed_clique)):
            if proposed_clique[j] not in g[proposed_clique[i]]:
                return False
    return True


def get_biggest_clique(g: dict[str:list]):
    # Peculiarity of the LAN party: everyone is connected to 13 people
    for k in g.keys():
        assert len(g[k]) == 13
    l = 13

    # Visualizing the graph shows it's connected so there are a few links going outside of cliques.
    # Assumption: Mr. Wastl is nice to me, so there will exist exactly one 13-clique.
    no_gos = []
    for k in g.keys():
        if k in no_gos:
            continue
        neighbors = g[k]
        for blind_eye in range(l):
            proposed_clique = [k] + neighbors[:blind_eye] + neighbors[blind_eye + 1 :]
            if is_clique(g, proposed_clique):
                return proposed_clique
        no_gos.extend(neighbors + [k])


with open("input.txt", "r") as input_file:
    g = {}
    for line in input_file.readlines():
        a, b = line.rstrip().split("-")
        if a not in g:
            g[a] = []
        if b not in g:
            g[b] = []
        g[a].append(b)
        g[b].append(a)

    biggest_clique = get_biggest_clique(g)
    res = ",".join(sorted(biggest_clique))

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(res))
